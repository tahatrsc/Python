print("oyuncu kaydetme")

ad =input("oyuncunun adı giriniz:")
soyad =input("oyuncunun soyadını giriniz:")
takım =input("oyuncunun takımını giriniz:")

bilgiler = [ad,soyad,takım]

print("bilgiler kaydediliyor...")

print(" oyuncu adı: {}\n oyuncunun soyadı: {}\n oyuncunun takımı: {}\n" .format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("kaydedildi...")