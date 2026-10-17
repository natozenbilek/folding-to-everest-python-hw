# Introduction to Python, Ödev 3
# IEEE Hacettepe University Student Branch, Güz 2026
#
# Bu ödevin sonunda while ve for ile sayan ve toplayan, iç içe loop'larla
# satır satır şekil kuran ve str'leri index ve slicing ile parçalayan
# programlar yazabileceksiniz.
#
# Son teslim: 8 Kasım 2026 Pazar 23.59
# Teslim formu: https://forms.gle/2Ei4AbGpuuJNtN5w7
# Ödev reposu: https://github.com/natozenbilek/folding-to-everest-python-hw
#
# Ödevi nasıl yapacaksınız
# 1. Bu dosyayı python-kurs klasörünüze kaydedin ve PyCharm'da açın.
# 2. Her görevde "# TODO" satırının yerine kodunuzu yazın.
# 3. Dosyayı Run ile çalıştırın. Her görevin başlık satırından sonraki
#    çıktısı, o görevin "Beklenen çıktı" kısmıyla birebir aynı olmalı.
# 4. Bitince formda "İsim" alanına isminizi yazın, odev3.py'yi "Ödev dosyası"
#    alanına yükleyin ve "Kişisel verileriniz" sorusundaki onay kutusunu
#    işaretleyin. Söylemek istediğiniz bir şey varsa "Açıklama" alanına
#    yazabilirsiniz; bu alan isteğe bağlı.
#
# Dosya bu haliyle de hatasız çalışır ve yalnızca görev başlıklarını yazar.
# Yalnızca Ders 1, 2 ve 3'te gördüğümüz yapıları kullanın; list Ders 4'te
# gelecek.


print("=== 1. Basamaklar ===")
n = 2026
# n'nin basamaklarını while ile sağdan sola tek tek alın: n 0'dan büyük
# olduğu sürece son basamak n % 10, geri kalan sayı n // 10 olsun.
# Basamak sayısını bir counter ile, basamakların toplamını bir accumulator
# ile bulun. Sayıyı ters çevirmek için bir accumulator daha kullanın:
# reverse = reverse * 10 + digit
# TODO
#
# Beklenen çıktı:
# Basamak sayısı: 4
# Basamak toplamı: 10
# Ters çevrilmiş: 6202


print("=== 2. Kağıdı Everest'e katlamak ===")
# Derste kağıdı Ay'a kadar katladık. Şimdi hedef Everest.
# 0,1 mm kalınlığındaki bir kağıt her katlamada iki kat kalınlaşır.
# Everest yaklaşık 8849 metre, yani 8849 * 1000 milimetre.
# Kalınlık Everest'e ulaşana kadar kağıdı katlayın ve katlamaları sayın.
# Kalınlığı metre olarak, iki basamakla yazdırın.
# TODO
#
# Beklenen çıktı:
# 27 katlamada Everest'i geçer.
# Kalınlık: 13421.77 m


print("=== 3. Hacettepe FizzBuzz ===")
# for ve range() ile 1'den 15'e kadar her sayı için:
# - hem 3'ün hem 5'in katıysa "Hacettepe",
# - yalnızca 3'ün katıysa "Hacet",
# - yalnızca 5'in katıysa "tepe",
# - hiçbiri değilse sayının kendisi yazılsın.
# if, elif ve else kullanın. Hangi şartı önce yazdığınız önemli.
# TODO
#
# Beklenen çıktı:
# 1
# 2
# Hacet
# 4
# tepe
# Hacet
# 7
# 8
# Hacet
# tepe
# 11
# Hacet
# 13
# 14
# Hacettepe


print("=== 4. Sayı üçgeni ===")
n = 5
# Derste yıldız üçgenini iç içe iki loop ile satır satır kurduk. Şimdi
# yıldız yerine sayılar olsun: i. satırda 1'den i'ye kadar sayılar yan yana
# dursun. Her satırı row adlı bir str'de += ile kurun; sayıyı str() ile
# ekleyin.
# TODO
#
# Beklenen çıktı:
# 1
# 12
# 123
# 1234
# 12345


print("=== 5. Gizli mesaj ===")
message = "Phyatrhiokna"
# Bu mesajda iki kelimenin harfleri sırayla dizilmiş.
# a) Slicing ile çift index'teki harfleri ve tek index'teki harfleri ayırıp
#    iki kelimeyi yan yana yazdırın.
# b) Şimdi gizli mesajı siz kurun: first = "Salı" ve second = "ders" olsun.
#    for ve range(len(first)) ile index'leri dolaşın; her turda first[i] ve
#    second[i]'yi secret adlı bir str'ye += ile ekleyin. secret'ı
#    yazdırın, sonra (a)'daki gibi çözüp iki kelimeyi yazdırın.
# TODO
#
# Beklenen çıktı:
# Python harika
# Sdaelrıs
# Salı ders


print("=== Meraklısına ===")
# Zorunlu değil.
# Bir tarihin haftanın hangi gününe denk geldiğini Zeller'in 1882'de
# yayımladığı formül bulur.
# Gün, ay ve yılı int olarak sorun. Ay 3'ten küçükse (Ocak, Şubat) aya 12
# ekleyin ve yıldan 1 çıkarın. Sonra şunları hesaplayın:
#   k = year % 100
#   j = year // 100
#   h = (day + 13 * (month + 1) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
# h'yi elif ile güne çevirin: 0 Cumartesi, 1 Pazar, 2 Pazartesi, 3 Salı,
# 4 Çarşamba, 5 Perşembe, 6 Cuma.
# Çalıştırınca şunları yazın: 29, 10, 1923. Sonra kendi doğum gününüzü
# deneyin.
# TODO
#
# Beklenen çıktı:
# Gün: 29
# Ay: 10
# Yıl: 1923
# O gün Pazartesi.
