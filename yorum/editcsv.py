import pandas as pd

# İlk formattaki CSV dosyasını oku (UTF-16 formatında olduğunu belirt)
df_first = pd.read_csv('C:/Users/berka/OneDrive/Masaüstü/yapayzeka/yorum/trainer/dataset.csv', encoding='utf-16')

# Yeni formattaki CSV dosyası için boş bir DataFrame oluştur
df_new = pd.DataFrame(columns=['Yorum', 'Durum'])

for index, row in df_first.iterrows():
    yorumlar = row['Yorum']
    review = row['Durum']

    # Eğer 'Yorum' sütunu içinde NaN değer varsa, bu durumu işleyin
    if pd.notna(yorumlar):
        yorumlar = '"' + yorumlar.strip("") + '"'  # Her yorumun başına ve sonuna birer tane çift tırnak ekleniyor
    else:
        yorumlar = '""'  # NaN ise çift tırnak içinde boş bir string yapısı

    # Yeni DataFrame'e ekle
    df_new = pd.concat([df_new, pd.DataFrame({'Yorum': [yorumlar], 'Durum': [review]})], ignore_index=True)

# Türkçe karakter sorununu çöz
df_new['Yorum'] = df_new['Yorum'].str.replace('ð', 'ğ')
df_new['Yorum'] = df_new['Yorum'].str.replace('ý', 'ı')
df_new['Yorum'] = df_new['Yorum'].str.replace('þ', 'ş')
df_new['Yorum'] = df_new['Yorum'].str.replace('ý', 'i')
df_new['Yorum'] = df_new['Yorum'].str.replace('Ý', 'İ')
df_new['Yorum'] = df_new['Yorum'].str.replace('Þ', 'Ş')

# Yeni DataFrame'i CSV dosyasına yaz (UTF-16 formatında yaz)
df_new.to_csv('C:/Users/berka/OneDrive/Masaüstü/yapayzeka/yorum/trainer/dataset2.csv', index=False, encoding='utf-8')

# İşlem bittiğinde mesaj yazdır
print("Yeni CSV dosyası başarıyla oluşturuldu.")
