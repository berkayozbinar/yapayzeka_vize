import pandas as pd

# Metin dosyasını oku
with open('C:/Users/berka/OneDrive/Masaüstü/yapayzeka/yorum/datasets/yorum_metinleri.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Her satırı bir liste içinde topla
data = {'Yorum': lines}

# DataFrame oluştur
df = pd.DataFrame(data)

# CSV dosyasına yaz
df.to_csv('C:/Users/berka/OneDrive/Masaüstü/yapayzeka/yorum/datasets/dataset.csv', index=False, encoding='utf-8')

print("CSV dosyası başarıyla oluşturuldu.")
