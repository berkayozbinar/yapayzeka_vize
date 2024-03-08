import os
import pandas as pd

# Verilerin bulunduğu ana dizin
dizin = 'C:/Users/berka/OneDrive/Masaüstü/yapayzeka/haber/news/'

# Alt dizinleri temsil eden bir liste oluşturun
alt_dizinler = os.listdir(dizin)

# Boş listeler oluşturun
metin = []
kategori = []

# Her alt dizini dön
for alt_dizin in alt_dizinler:
    alt_dizin_yolu = os.path.join(dizin, alt_dizin)

    # Her TXT dosyasını dön
    for txt_dosyasi in os.listdir(alt_dizin_yolu):
        txt_dosya_yolu = os.path.join(alt_dizin_yolu, txt_dosyasi)

        try:
            # 'utf-8' formatında okuma
            with open(txt_dosya_yolu, 'r', encoding='utf-8') as dosya:
                metin_verisi = dosya.read().replace('\n', ' ')
                metin.append(metin_verisi)
                kategori.append(alt_dizin)
        except UnicodeDecodeError:
            try:
                # 'latin-1' formatında okuma
                with open(txt_dosya_yolu, 'r', encoding='latin-1') as dosya:
                    metin_verisi = dosya.read().replace('\n', ' ')
                    metin.append(metin_verisi)
                    kategori.append(alt_dizin)
            except UnicodeDecodeError:
                # 'ISO-8859-1' formatında okuma
                with open(txt_dosya_yolu, 'r', encoding='ISO-8859-1') as dosya:
                    metin_verisi = dosya.read().replace('\n', ' ')
                    metin.append(metin_verisi)
                    kategori.append(alt_dizin)

# Listeleri DataFrame'e çevirin
df = pd.DataFrame({'Metin': metin, 'Kategori': kategori})

# Türkçe karakter sorununu çöz
df['Metin'] = df['Metin'].str.replace('ð', 'ğ')
df['Metin'] = df['Metin'].str.replace('ý', 'ı')
df['Metin'] = df['Metin'].str.replace('þ', 'ş')
df['Metin'] = df['Metin'].str.replace('ý', 'i')
df['Metin'] = df['Metin'].str.replace('Ý', 'İ')
df['Metin'] = df['Metin'].str.replace('Þ', 'Ş')

# DataFrame'i CSV dosyasına yaz
df.to_csv('C:/Users/berka/OneDrive/Masaüstü/yapayzeka/haber/trainer/dataset.csv', index=False)

# İşlem bittiğinde mesaj yazdır
print("Yeni CSV dosyası başarıyla oluşturuldu.")
