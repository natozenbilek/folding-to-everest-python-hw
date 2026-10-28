# Introduction to Python, Ödev 3
# IEEE Hacettepe University Student Branch, Güz 2026
#
# Bu ödevin sonunda if, elif ve else ile karar veren, while ve for ile
# sayan, bir str'yi harf harf dolaşan, iç içe loop'larla satır satır şekil
# kuran ve break ile loop'tan çıkan programlar yazabileceksiniz.
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
#    5. görev sizden tahmin ister: Run penceresine yazıp Enter'a basın.
# 4. Bitince formda "İsim" alanına isminizi yazın, odev3.py'yi "Ödev dosyası"
#    alanına yükleyin ve "Kişisel verileriniz" sorusundaki onay kutusunu
#    işaretleyin. Söylemek istediğiniz bir şey varsa "Açıklama" alanına
#    yazabilirsiniz; bu alan isteğe bağlı.
#
# Dosya bu haliyle de hatasız çalışır ve yalnızca görev başlıklarını yazar.
# Yalnızca Ders 1, 2 ve 3'te gördüğümüz yapıları kullanın.


print("=== 1. Hacettepe FizzBuzz ===")
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


print("=== 2. Kağıdı Everest'e katlamak ===")
# Derste kağıdı Ay'a kadar katladık. Şimdi hedef Everest.
# 0,1 mm kalınlığındaki bir kağıt her katlamada iki kat kalınlaşır.
# Everest yaklaşık 8849 metre, yani 8849 * 1000 milimetre.
# Kalınlık Everest'e ulaşana kadar kağıdı while ile katlayın ve katlamaları
# bir counter ile sayın. Kalınlığı metre olarak, iki basamakla yazdırın.
# TODO
#
# Beklenen çıktı:
# 27 katlamada Everest'i geçer.
# Kalınlık: 13421.77 m


print("=== 3. Gizli mesaj ===")
message = "P1y2t3h4o5n h6a7r8i9k0a"
# Bu mesajın harflerinin arasına rakamlar saklanmış.
# for ile message'ı harf harf dolaşın. Karakter bir rakamsa ("0123456789"
# str'sinde varsa) atlanan rakamları bir counter ile sayın ve continue ile
# sıradaki karaktere geçin. Rakam değilse karakteri secret adlı bir str'ye
# += ile ekleyin. Loop bitince secret'ı ve atlanan rakam sayısını yazdırın.
# TODO
#
# Beklenen çıktı:
# Python harika
# Atlanan rakam: 10


print("=== 4. Sayı üçgeni ===")
n = 5
# Derste yıldızlarla satır kurduk. Şimdi yıldız yerine sayılar olsun:
# i. satırda 1'den i'ye kadar sayılar yan yana dursun. İç içe iki loop
# kullanın; her satırı row adlı bir str'de += ile kurun, sayıyı str() ile
# ekleyin.
# TODO
#
# Beklenen çıktı:
# 1
# 12
# 123
# 1234
# 12345


print("=== 5. Sayı tahmin oyunu ===")
secret = 37
# while True ile kullanıcıdan tahmin isteyin:
#     guess = int(input("Tahmin: "))
# Tahmin secret'tan küçükse "Daha büyük.", büyükse "Daha küçük." yazdırın.
# Doğru tahminde break ile loop'tan çıkın. Her tahmini bir counter ile
# sayın ve loop bittikten sonra kaç denemede bilindiğini yazdırın.
# Çalıştırınca sırayla 50, 25 ve 37 yazın.
# TODO
#
# Beklenen çıktı:
# Tahmin: 50
# Daha küçük.
# Tahmin: 25
# Daha büyük.
# Tahmin: 37
# 3 denemede bildiniz.


print("=== Meraklısına ===")
# Zorunlu değil.
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
