# Ödev 3: Kağıdı Everest'e katlamak

IEEE Hacettepe **Introduction to Python** dersinin 3. ödevi, Güz 2026.

<p align="center"><img src="img/kart.png" width="600" alt="Ödev 3 kartı: bu haftanın kodları, bir çizim, görevler ve teslim bilgisi"></p>

Yukarıdaki kart bu haftanın özeti. Aşağıda aynı konuların daha ayrıntılı tekrarı var.

**İndirmek için:** yeşil **Code** düğmesine basın, **Download ZIP** deyin, zip'i açın. Git bilmenize gerek yok.

**Son teslim:** 8 Kasım 2026 Pazar, 23.59\
**Teslim:** [Ödev 3 teslim formu](https://forms.gle/2Ei4AbGpuuJNtN5w7)

Bu ödevin sonunda while ve for loop'larıyla (döngüler) sayan ve toplayan, nested loops (iç içe döngüler) ile satır satır şekil kuran, str'leri (karakter dizileri) index (indis) ve slicing (dilimleme) ile parçalayan programlar yazabileceksiniz.

## Bu ödevde kullanacaklarımız

Hepsini Ders 3'te gördük. Görevlerde gereken birkaç Ders 2 konusunu da en sona ekledim.

### while loop
`while`, devam şartı True olduğu sürece altındaki block'u (blok) tekrar tekrar çalıştırır. Şart her turun başında yeniden sorulur. False olduğunda loop biter ve program loop'tan sonraki satırdan devam eder.

```text
while <devam şartı>:
    <tekrarlanan satırlar>
```

![while loop akış şeması](img/ders2-while-flow.png)

```python
i = 10
while i > 0:
    print(i)
    i = i - 3
print("Bitti")
```

```text
10
7
4
1
Bitti
```

Her while üç parçayla çalışır:

| Parça | Örnekte | Ne yapar |
|---|---|---|
| Başlangıç | `i = 10` | Loop başlamadan variable'a (değişken) ilk value'sunu (değer) verir |
| Devam şartı | `i > 0` | Her turun başında sorulur; True ise bir tur daha dönülür |
| Güncelleme | `i = i - 3` | Variable'ı değiştirir ve şartı eninde sonunda False yapar |

`if` de bir şart sorar ama yalnızca bir kez; `while` her turun başında yeniden sorar.

**Sık yapılan hata:** güncellemeyi unutmak. `i` hiç değişmezse şart hep True kalır ve loop bitmez. Buna infinite loop (sonsuz döngü) denir. Python hata vermez, aynı satırı durmadan yazar. Programı PyCharm'da Run penceresindeki kırmızı kare, **Stop** düğmesi durdurur.

### Counter (sayaç), accumulator ve +=
Counter her turda bir artar ve turları sayar. Accumulator ise loop boyunca bir toplamı biriktirir. İkisi de loop'tan önce 0'dan başlar.

![Ortalama: total / count](img/ders2-average.png)

`x += 1`, `x = x + 1`'in kısa yazılışıdır. str'de de çalışır:

| Yazılış | Uzun hali | Önce | Sonra |
|---|---|---|---|
| `x += 1` | `x = x + 1` | `5` | `6` |
| `total += 2.5` | `total = total + 2.5` | `0` | `2.5` |
| `word += "tepe"` | `word = word + "tepe"` | `"Bey"` | `"Beytepe"` |

Python'da `x++` yoktur; yazarsanız `SyntaxError: invalid syntax` alırsınız.

2'den 10'a kadar çift sayıları bir counter ile sayan ve bir accumulator ile toplayan loop:

```python
count = 0
total = 0
i = 2
while i <= 10:
    count += 1
    total += i
    i += 2
print(count, total, total / count)
```

```text
5 30 6.0
```

Son sayı ortalama: counter ile accumulator birlikte ortalamayı verir.

**Sık yapılan hata:** `total = 0`'ı loop'un içine yazmak. Toplam her turda sıfırlanır ve sonda yalnızca son tur kalır, tıpkı her üründen sonra toplamı sıfırlayan bir kasiyer gibi. Aşağıdaki kod 1 + 2 + 3 = 6 yerine 3 yazar:

```python
i = 1
while i <= 3:
    total = 0
    total += i
    i += 1
print(total)
```

```text
3
```

### for loop ve range()
`for`, bir sıranın elemanlarını sırayla tek tek alır. Şimdilik sıramız `range()`. Her turda sıradaki sayı `for`'dan sonraki isme atanır ve onu `for` kendisi ilerletir; `i += 1` yazmazsınız.

```text
for <isim> in <sıra>:
    <gövde>
```

![for loop'un akış şeması](img/ders3-for-flow.png)

```python
for week in range(1, 4):
    print(f"{week}. hafta")
```

```text
1. hafta
2. hafta
3. hafta
```

`range()` tam sayılar üretir. Bitiş hiçbir zaman dahil değildir:

| Yazılış | Verdiği sayılar | Not |
|---|---|---|
| `range(5)` | 0, 1, 2, 3, 4 | Tek sayı verilirse başla 0'dır |
| `range(1, 6)` | 1, 2, 3, 4, 5 | Bitiş, istediğiniz son sayının bir fazlası |
| `range(0, 10, 3)` | 0, 3, 6, 9 | Üçüncü sayı adımdır |
| `range(10, 0, -3)` | 10, 7, 4, 1 | Negatif adım geriye sayar |
| `range(10, 0)` | hiç sayı yok | Adım yazılmazsa +1'dir; 10'dan 0'a artarak varılmaz |

Kaç tur döneceği belliyse `for`, belli değilse `while` kullanın.

**Sık yapılan hata:** bitişi bir eksik yazmak. 1'den 10'a kadar saymak için `range(1, 11)` gerekir; `range(1, 10)` 9'da durur. `for i in 10:` gibi range olmadan bir sayı yazarsanız da `TypeError: 'int' object is not iterable` alırsınız.

### for içinde if, elif ve else
Ders 2'deki if, elif ve else loop'un gövdesinde de çalışır ve her turda yeniden sorulur. Bir sayının başka bir sayının katı olup olmadığını `%` operator'ı (işlemci) söyler: kalan 0 ise kattır.

![if ile saymak: 0'dan 29'a 3'ün katları](img/ders3-count-multiples.png)

```python
for n in range(1, 5):
    if n % 2 == 0:
        print(n, "çift")
    else:
        print(n, "tek")
```

```text
1 tek
2 çift
3 tek
4 çift
```

Şartlar yukarıdan aşağı sınanır. İlk True olanın block'u çalışır, gerisine bakılmaz bile. Bu yüzden sıra önemlidir:

```python
score = 95
if score >= 50:
    print("Geçti")
elif score >= 90:
    print("Yüksek onur")
```

```text
Geçti
```

95, 90'dan da büyük ama ilk True `score >= 50` olduğu için ikinci şart hiç sınanmadı. Daha dar olan `score >= 90` şartını üste yazınca çıktı `Yüksek onur` olur.

### Nested loops (iç içe döngüler)
Bir loop'un gövdesinde başka bir loop olabilir. İç loop, dış loop'un her turunda baştan sona çalışır. Her katta o katın bütün kapılarına ekmek bırakan kapıcıyı düşünün: katlar dış loop, kapılar iç loop.

![Nested loops: çalışma sırası](img/ders3-nested-grid.png)

```python
for floor in range(1, 3):
    for door in range(1, 4):
        print(floor, door)
```

```text
1 1
1 2
1 3
2 1
2 2
2 3
```

Dış loop 2, iç loop 3 tur döndüğü için iç gövde 2 × 3 = 6 kez çalıştı.

### Satır satır şekil kurmak
Ekrana bir şekli satır satır çizmek için her satırı önce bir str'de kurar, sonra tek bir `print()` ile yazarız. `row` boş str'den (`""`) başlar ve her turda `+=` ile büyür. Aşağıdaki dama tahtasında dolu kareler `#`, boş kareler `.`:

```python
for i in range(4):
    row = ""
    for j in range(6):
        if (i + j) % 2 == 0:
            row += "#"
        else:
            row += "."
    print(row)
```

```text
#.#.#.
.#.#.#
#.#.#.
.#.#.#
```

![Satır kurmak: row'un dört hali](img/ders3-one-row.png)

İki satırın yeri önemli: `row = ""` dış loop'un içinde, her satırın başında duruyor; `print(row)` ise iç loop bittikten sonra, yine dış loop'un içinde.

| Yanlış yer | Ne olur |
|---|---|
| `row = ""` dış loop'tan önce | `row` hiç boşalmaz, her satır bir öncekinin devamı olarak uzar |
| `print(row)` iç loop'un içinde | Satır her eklemeden sonra yeniden yazılır, yarım satırlar da çıkar |

İkisinde de Python hata vermez, yalnızca çıktı yanlış olur. Böyle bir durumda satırların indentation'ına (girinti) bakın.

Bir str'ye sayı eklemek için sayıyı önce `str()` ile str'ye çevirin, çünkü `+` bir str ile bir int'i birleştiremez:

```python
label = "Ders "
label += str(3)
print(label)
```

```text
Ders 3
```

`label += 3` yazarsanız şu error message'ı (hata mesajı) alırsınız:

```text
TypeError: can only concatenate str (not "int") to str
```

### Index (indis) ve len()
str de range gibi bir sequence'tir (dizi): karakterleri sırayla durur ve her karakterin bir index'i vardır. Index 0'dan başlar ve köşeli parantez içine yazılır. Negatif index sondan sayar, `-1` son karakterdir.

![Index cetveli: code = "BBM101"](img/ders3-index-ruler.png)

| Karakter | `B` | `e` | `y` | `t` | `e` | `p` | `e` |
|---|---|---|---|---|---|---|---|
| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| Negatif index | -7 | -6 | -5 | -4 | -3 | -2 | -1 |

`len()` bir str'nin length'ini (uzunluk), yani karakter sayısını verir. Son karakterin index'i `len - 1`'dir.

```python
word = "Beytepe"
print(word[0], word[3], word[-1])
print(len(word))
print(word[len(word) - 1])
```

```text
B t e
7
e
```

**Sık yapılan hata:** son index'ten sonrasını istemek. `"Beytepe"` için `word[7]` yoktur:

```text
IndexError: string index out of range
```

str immutable'dır (değişmez). `word[0] = "b"` yazarsanız `TypeError: 'str' object does not support item assignment` alırsınız. Bir str'yi değiştirmek yerine `+=` ile yeni bir str kurarız.

### Bir str'yi index ile dolaşmak
Index'i bir variable da verebilir. `range(len(month))`, `month`'un bütün index'lerini sırayla verir; `month[i]` de o turdaki karakterdir.

```python
month = "Ekim"
for i in range(len(month)):
    print(i, month[i])
```

```text
0 E
1 k
2 i
3 m
```

Bir counter ile birlikte, örneğin bir harfin kaç kez geçtiğini sayabilirsiniz:

```python
word = "Hacettepe"
count = 0
for i in range(len(word)):
    if word[i] == "e":
        count += 1
print(count)
```

```text
3
```

**Sık yapılan hata:** `range(len(word) + 1)` yazmak. Son turda `i` length'e eşit olur ve `IndexError` alırsınız. `range(len(word))` zaten son index'te durur.

### Slicing (dilimleme)
Slicing, iki sınır arasındaki karakterleri yeni bir str olarak verir. Tablet çikolatayı çizgisinden kırmaya benzer: parçalar ayrılır ama hiçbir kare kaybolmaz. Bitiş, range'de olduğu gibi dahil değildir. Üçüncü sayı adımdır.

```text
<str>[<başla>:<bitiş>:<adım>]
```

![Slicing: sınırlar 0'dan 6'ya](img/ders3-slice-ruler.png)

`word = "Beytepe"` için:

| Yazılış | Sonuç | Ne alır |
|---|---|---|
| `word[0:3]` | `"Bey"` | 0, 1 ve 2. index'i; 3 dahil değil |
| `word[3:]` | `"tepe"` | Bitiş yazılmazsa sona kadar |
| `word[:3]` | `"Bey"` | Başla yazılmazsa baştan |
| `word[-4:]` | `"tepe"` | Son dört karakter |
| `word[::2]` | `"Byee"` | 0'dan başlayıp ikişer atlayarak, yani çift index'ler |
| `word[1::2]` | `"etp"` | 1'den başlayıp ikişer atlayarak, yani tek index'ler |
| `word[::-1]` | `"epetyeB"` | Adım -1, yani tersten |
| `word[2:100]` | `"ytepe"` | Sınırı aşan slice hata vermez, olduğu kadarını alır |

Slicing yeni bir str yapar; `word` değişmez, hala `"Beytepe"`dir.

**Sık yapılan hata:** bitişi dahil sanmak. `word[0:3]`, 3. index'teki `t`'yi almaz. Bir de şunu karıştırmayın: sınırı aşan index `IndexError` verir, sınırı aşan slice vermez.

### Ders 2'den: f-string, :.2f ve input()
f-string'de `{}` içine yazılan expression'ın (ifade) value'su yazının içine yerleşir. `:.2f` value'yu noktadan sonra iki basamakla gösterir; variable'ın kendisi değişmez.

![{:.2f} ile iki basamak](img/ders2-format-2f.png)

```python
price = 100 / 3
print(f"Kişi başı: {price:.2f} TL")
print(price)
```

```text
Kişi başı: 33.33 TL
33.333333333333336
```

`input()` kullanıcının yazdığını her zaman str olarak verir. Sayı olarak kullanmak için `int()` ile çevirin:

```python
year = int(input("Yıl: "))
print(year + 1)
```

```text
Yıl: 2026
2027
```

## Görevler

Görevlerin ayrıntısı ve her birinin beklenen çıktısı `odev3.py` dosyasının içinde.

1. **Basamaklar:** 2026'nın basamaklarını while ile sağdan sola alacak, bir counter ile sayacak, bir accumulator ile toplayacak ve sayıyı ters çevireceksiniz.
2. **Kağıdı Everest'e katlamak:** 0,1 mm'lik bir kağıdı kalınlığı Everest'i geçene kadar katlayacak, katlamaları sayacak ve kalınlığı metre olarak yazdıracaksınız.
3. **Hacettepe FizzBuzz:** for ve range() ile 1'den 15'e kadar her sayı için 3'ün katına Hacet, 5'in katına tepe, ikisinin de katına Hacettepe yazdıracaksınız.
4. **Sayı üçgeni:** Derste kurduğumuz yıldız üçgeni gibi, iç içe iki loop ile 1, 12, 123, 1234 ve 12345 satırlarını kuracaksınız.
5. **Gizli mesaj:** Harfleri sırayla dizilmiş iki kelimeyi slicing ile ayıracak, sonra range(len()) ile kendi gizli mesajınızı kurup yeniden çözeceksiniz.

Zorunlu olmayan bir **Meraklısına** görevi de var: Zeller'in formülüyle bir tarihin haftanın hangi gününe denk geldiğini bulacaksınız.

Yalnızca Ders 1, 2 ve 3'te gördüğümüz yapıları kullanın; list Ders 4'te gelecek.

## Nasıl çalışılır

1. Zip'ten çıkan `odev3.py` ve `kontrol.py` dosyalarını aynı klasörde tutun ve `odev3.py`'yi PyCharm'da açın.
2. Her görevde `# TODO` satırının yerine kodunuzu yazın.
3. Dosyayı **Run** ile çalıştırın ve çıktıyı görevin "Beklenen çıktı" kısmıyla karşılaştırın.

Meraklısına'yı yaparsanız program sizden gün, ay ve yılı ister; Run penceresine yazıp Enter'a basın.

## Kendi kendinize kontrol

Bitirince `kontrol.py`'yi PyCharm'da açıp **Run** deyin. Her görev için geçti ya da kaldı yazar, kaldıysa beklenen satırı ve sizin satırınızı gösterir. Görevin istediği yapıyı, örneğin while'ı, `+=`'yi ya da slicing'i kullanıp kullanmadığınıza da bakar. 1, 4 ve 5. görevlerde baştaki value'yu değiştirip dosyayı bir kez daha çalıştırır; sonucu elle yazdıysanız bunu fark eder. Meraklısına'nın üç sorusuna 29, 10 ve 1923'ü kendisi yazar. Dosya 10 saniyede bitmezse durdurur ve hangi görevde takıldığını söyler. Kontrol not vermez, sadece size yol gösterir.

## Teslim

[Ödev 3 teslim formunda](https://forms.gle/2Ei4AbGpuuJNtN5w7) "İsim" alanına isminizi yazın, `odev3.py`'yi "Ödev dosyası" alanına yükleyin ve "Kişisel verileriniz" sorusundaki onay kutusunu işaretleyin. Söylemek istediğiniz bir şey varsa isteğe bağlı "Açıklama" alanına yazabilirsiniz.

Takıldığınız bir yer olursa dersin WhatsApp grubuna yazın.

Dersin sitesi: https://natozenbilek.github.io/ieee-hacettepe-python-course/
