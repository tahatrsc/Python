def hesap_makinesi(sayi1, operator, sayi2):
  if operator == "+":
    return sayi1 + sayi2
  elif operator == "-":
    return sayi1 - sayi2
  elif operator == "*":
    return sayi1 * sayi2
  elif operator == "/":
    return sayi1 / sayi2
  else:
    print("Geçersiz operatör")

while True:
  sayi1 = float(input("İlk sayıyı girin: "))
  operator = input("Operatörü girin (+, -, *, /): ")
  sayi2 = float(input("İkinci sayıyı girin: "))

  sonuc = hesap_makinesi(sayi1, operator, sayi2)
  print(f"Sonuç: {sonuc}")

  devam = input("Devam etmek istiyor musunuz? (e/h): ")
  if devam == "h":
    break
