import sqlite3

def metin_kaydet(metin1, metin2):
  """
  Metinleri sqlite veritabanına kaydet
  """
  conn = sqlite3.connect("metinler.db")
  cursor = conn.cursor()
  cursor.execute("CREATE TABLE IF NOT EXISTS metinler (id INTEGER PRIMARY KEY, metin TEXT)")
  cursor.execute("INSERT INTO metinler (metin) VALUES (?)", (metin1,))
  cursor.execute("INSERT INTO metinler (metin) VALUES (?)", (metin2,))
  conn.commit()
  conn.close()

def metin_oku():
  """
  Metinleri sqlite veritabanından oku
  """
  conn = sqlite3.connect("metinler.db")
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM metinler")
  metinler = cursor.fetchall()
  conn.close()
  return metinler[0][1], metinler[1][1]

def benzerlik_analizi(metin1, metin2):
  """
  Özgün bir algoritma kullanarak metinlerin benzerliğini analiz et
  """
  #Her iki metni de kelime listesine dönüştür
  kelimeler1 = metin1.lower().split()
  kelimeler2 = metin2.lower().split()

  #iki metinde de geçen kelimelerin kümesini bul
  ortak_kelimeler = set(kelimeler1) & set(kelimeler2)

  #Ortak kelimelerin sayısını ve toplam kelime sayısını kullanarak benzerlik oranı hesapla
  benzerlik_orani = len(ortak_kelimeler) / (len(kelimeler1) + len(kelimeler2) - len(ortak_kelimeler))

  #Benzerlik durumunu açıklayan bir metin oluştur
  benzerlik_durumu = f"Metinler %{benzerlik_orani * 100:.2f} oranında benzerdir. Ortak kelimeler: {', '.join(ortak_kelimeler)}"

  return benzerlik_durumu

def sonuclari_yazdir(benzerlik_durumu):
  """
  Benzerlik durumunu ekrana yazdır ve dosyaya kaydet
  """
  print(benzerlik_durumu)
  with open("benzerlik_durumu.txt", "w") as f:
    f.write(benzerlik_durumu)

#Kullanıcıdan metinleri al
metin1 = input("Birinci metni girin: ")
metin2 = input("İkinci metni girin: ")

#Metinleri kaydet ve veritabanından oku
metin_kaydet(metin1, metin2)
metin1, metin2 = metin_oku()

#Benzerlik analizini gerçekleştir
benzerlik_durumu = benzerlik_analizi(metin1, metin2)

#Sonuçları yazdır
sonuclari_yazdir(benzerlik_durumu)
