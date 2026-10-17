# Ödev 3 kontrolü: odev3.py'yi çalıştırır, her görevin çıktısını beklenen çıktıyla karşılaştırır.
# PyCharm'da bu dosyayı açıp Run deyin. odev3.py ile aynı klasörde olmalı. Not vermez, yol gösterir.
import builtins
import os
import pathlib
import re
import runpy
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
ODEV = HERE / "odev3.py"
TIMEOUT = 10

# Meraklısına'daki input() satırlarına, odev3.py'nin söylediği gibi sırayla bunlar yazılır.
INPUTS = ["29", "10", "1923"]

EXPECTED = {
    "1. Basamaklar": ["Basamak sayısı: 4", "Basamak toplamı: 10", "Ters çevrilmiş: 6202"],
    "2. Kağıdı Everest'e katlamak": ["27 katlamada Everest'i geçer.", "Kalınlık: 13421.77 m"],
    "3. Hacettepe FizzBuzz": ["1", "2", "Hacet", "4", "tepe", "Hacet", "7", "8", "Hacet", "tepe",
                              "11", "Hacet", "13", "14", "Hacettepe"],
    "4. Sayı üçgeni": ["1", "12", "123", "1234", "12345"],
    "5. Gizli mesaj": ["Python harika", "Sdaelrıs", "Salı ders"],
}
OPTIONAL = {"Meraklısına": ["Gün: 29", "Ay: 10", "Yıl: 1923", "O gün Pazartesi."]}

# Görevin başındaki value değiştirilip dosya bir kez daha çalıştırılır. Sonuç o value'dan
# hesaplanıyorsa çıktı da değişir; elle yazılmışsa aynı kalır.
# (görev, aranan satır, yerine yazılan satır, beklenen çıktı, yalnızca ilk satırlara mı bakılır)
VARIANTS = [
    ("1. Basamaklar", r"^n\s*=\s*2026[ \t]*$", "n = 907",
     ["Basamak sayısı: 3", "Basamak toplamı: 16", "Ters çevrilmiş: 709"], False),
    ("4. Sayı üçgeni", r"^n\s*=\s*5[ \t]*$", "n = 3", ["1", "12", "123"], False),
    ("5. Gizli mesaj", r'^message\s*=\s*"Phyatrhiokna"[ \t]*$', 'message = "ksaillegmi"',
     ["kalem silgi"], True),
]

STEP2 = r"\[[^\[\]]*:[^\[\]]*:\s*2\s*\]"


def run_with_inputs(path):
    """kontrol.py'nin kendisi bu modda çalışır: input()'a INPUTS'u yazar, sonra odev3.py'yi çalıştırır."""
    answers = iter(INPUTS)

    def typed_input(prompt=""):
        print(prompt, end="")
        try:
            value = next(answers)
        except StopIteration:
            raise EOFError("EOF when reading a line") from None
        print(value)
        return value

    builtins.input = typed_input
    sys.argv = [path]
    runpy.run_path(path, run_name="__main__")


def last_title(text):
    titles = [m.group(1) for ln in text.splitlines() if (m := re.fullmatch(r"=== (.+) ===", ln.strip()))]
    return titles[-1] if titles else None


def run(path):
    """Dosyayı çalıştırır. Hata yoksa (çıktı, None), varsa (None, açıklama satırları) döndürür."""
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUNBUFFERED="1")
    try:
        done = subprocess.run([sys.executable, str(pathlib.Path(__file__).resolve()), "--calistir", str(path)],
                              capture_output=True, stdin=subprocess.DEVNULL, env=env, timeout=TIMEOUT)
    except subprocess.TimeoutExpired as e:
        partial = (e.stdout or b"").decode("utf-8", errors="replace")
        lines = [f"{TIMEOUT} saniyede bitmedi. Bir while loop'u hiç bitmiyor olabilir (infinite loop):",
                 "devam şartındaki variable loop'un içinde değişiyor mu, bakın."]
        title = last_title(partial)
        if title:
            lines.append(f"Çıktıdaki son görev başlığı: {title}")
        return None, lines
    out = done.stdout.decode("utf-8", errors="replace")
    if done.returncode != 0:
        err = [ln for ln in done.stderr.decode("utf-8", errors="replace").splitlines() if ln.strip()]
        lines = ["çalışırken hata verdi. Error message'ın son satırı:", "    " + (err[-1] if err else "(boş)")]
        title = last_title(out)
        if title:
            lines.append(f"Çıktıdaki son görev başlığı: {title}")
        return None, lines
    return out, None


def sections(text):
    """'=== başlık ===' satırlarına göre çıktıyı böler."""
    out, cur = {}, None
    for line in text.splitlines():
        m = re.fullmatch(r"=== (.+) ===", line.strip())
        if m:
            cur = m.group(1)
            out[cur] = []
        elif cur is not None:
            out[cur].append(line.rstrip())
    return out


def block(src, start, end):
    """odev3.py'de iki görev başlığı arasındaki kod (comment satırları hariç)."""
    a = src.find(start)
    b = src.find(end, a + 1) if end else len(src)
    lines = src[a:b if b != -1 else len(src)].splitlines()[1:]
    return [ln for ln in lines if ln.strip() and not ln.strip().startswith("#")]


def first_difference(want, have):
    for i, w in enumerate(want):
        h = have[i] if i < len(have) else "(satır yok)"
        if h != w:
            return f"{i + 1}. satır beklenen: {w!r}, sizinki: {h!r}"
    return f"beklenenden fazla satır var: {have[len(want)]!r}"


def source_notes(title, src):
    """Görevin odev3.py'de yazan kurallarına uyulmuş mu."""
    titles = list(EXPECTED) + ["Meraklısına"]
    i = titles.index(title)
    code = "\n".join(block(src, f'print("=== {title.split(".")[0]}.', f'print("=== {titles[i + 1].split(".")[0]}'))
    notes = []
    if title.startswith("1."):
        if not re.search(r"\bwhile\b", code):
            notes.append("basamakları while ile alın")
        if not re.search(r"%\s*10\b", code) or not re.search(r"//\s*10\b", code):
            notes.append("son basamağı n % 10 ile, geri kalan sayıyı n // 10 ile bulun")
        if "6202" in code:
            notes.append("6202'yi elle yazmayın, reverse bir accumulator ile kurulsun")
    if title.startswith("2."):
        if not re.search(r"\bwhile\b", code):
            notes.append("kağıdı while ile, Everest'e ulaşana kadar katlayın")
        if re.search(r"\b27\b", code) or "13421" in code:
            notes.append("27'yi ya da kalınlığı elle yazmayın, loop katlayıp saysın")
    if title.startswith("3."):
        if not re.search(r"\bfor\b", code) or "range(" not in code:
            notes.append("sayıları for ve range() ile dolaşın")
        if not re.search(r"\belif\b", code) or not re.search(r"\belse\b", code):
            notes.append("if, elif ve else kullanın")
    if title.startswith("4."):
        if len(re.findall(r"\b(?:for|while)\b", code)) < 2:
            notes.append("satırları iç içe iki loop ile kurun")
        if not re.search(r"\brow\s*\+=", code):
            notes.append("her satırı row adlı str'de += ile kurun")
        if "str(" not in code:
            notes.append("sayıyı row'a str() ile ekleyin")
    if title.startswith("5."):
        if len(re.findall(r"\bmessage\s*" + STEP2, code)) < 2:
            notes.append("(a) message'ın çift ve tek index'teki harflerini slicing ile ayırın")
        if not re.search(r"range\(\s*len\(", code):
            notes.append("(b) index'leri for ve range(len(first)) ile dolaşın")
        if not re.search(r"\bsecret\s*\+=", code):
            notes.append("(b) harfleri secret'a += ile ekleyin")
        if len(re.findall(r"\bsecret\s*" + STEP2, code)) < 2:
            notes.append("(b) secret'ı da (a)'daki gibi slicing ile çözün")
        if "harika" in code or "Sdaelr" in code:
            notes.append("mesajı ya da sonucu elle yazmayın, slicing ve loop bulsun")
    return notes


def variant_note(title, src):
    """Görevin başındaki value'yu değiştirip dosyayı yeniden çalıştırır."""
    for name, pattern, new_line, want, head_only in VARIANTS:
        if name != title:
            continue
        changed, count = re.subn(pattern, new_line, src, count=1, flags=re.M)
        if count == 0:
            return []
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / "odev3.py"
            path.write_text(changed, encoding="utf-8")
            out, problem = run(path)
        if problem:
            return [f"{new_line} ile denedim, dosya " + problem[0]] + problem[1:]
        have = sections(out).get(title, [])
        if head_only:
            have = have[:len(want)]
        if have != want:
            return [f"{new_line} ile denedim: " + first_difference(want, have),
                    "Sonuç görevin başındaki value'dan hesaplanmalı, elle yazılmamalı."]
    return []


def main():
    try:
        sys.stdout.reconfigure(errors="replace")
    except AttributeError:
        pass
    if not ODEV.exists():
        print("odev3.py bulunamadı. kontrol.py ile aynı klasöre koyun.")
        return
    out, problem = run(ODEV)
    if problem:
        print("odev3.py " + problem[0])
        for ln in problem[1:]:
            print(ln)
        print("Önce bunu düzeltin, sonra kontrolü tekrar çalıştırın.")
        return
    got = sections(out)
    src = ODEV.read_text(encoding="utf-8")
    passed = 0
    for title, want in EXPECTED.items():
        have = got.get(title)
        if have is None:
            print(f"✗ {title}: başlık satırı çıktıda yok. Başlığı yazdıran print() satırını silmeyin.")
            continue
        if not have:
            print(f"✗ {title}: henüz çıktı yok. TODO'nun yerine kodunuzu yazın.")
            continue
        notes = []
        if have != want:
            notes.append(first_difference(want, have))
        notes += source_notes(title, src)
        if not notes:
            notes += variant_note(title, src)
        if notes:
            print(f"✗ {title}")
            for n in notes:
                print("    " + n)
        else:
            print(f"✓ {title}")
            passed += 1
    for title, want in OPTIONAL.items():
        have = got.get(title, [])
        if have:
            print(("✓ " if have == want else "· ") + title + " (zorunlu değil)")
            if have != want:
                print("    " + first_difference(want, have))
    print(f"\n{passed} / {len(EXPECTED)} görev geçti.")


if len(sys.argv) > 2 and sys.argv[1] == "--calistir":
    run_with_inputs(sys.argv[2])
else:
    main()
