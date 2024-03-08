import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# NLTK kaynaklarını indir
# nltk.download("punkt")
# nltk.download("stopwords")

# Metin verisini yükle (bu kısmı CSV dosyasını okuyarak gerçekleştirebilirsiniz)
veri = pd.read_csv("trainer/egitici_veri_haber.csv")

# Metin verilerini tokenleştirme işlemi
stop_words = set(stopwords.words("turkish"))
stemmer = PorterStemmer()

tokenler = []

for metin in veri["Metin"]:
    # Küçük harfe çevirme
    metin = metin.lower()
    
    # Kelimeleri ayırma
    kelimeler = word_tokenize(metin)
    
    # Stop words'leri ve noktalama işaretlerini temizleme
    kelimeler = [kelime for kelime in kelimeler if kelime.isalnum() and kelime not in stop_words]
    
    # Kelimeleri köklerine ayırma
    kelimeler = [stemmer.stem(kelime) for kelime in kelimeler]
    
    tokenler.append(kelimeler)

# Tokenleştirilmiş veriyi yeni bir DataFrame'e ekleme
tokenleştirilmis_df = pd.DataFrame({"Tokenler": tokenler})

# Tokenleştirilmiş veriyi CSV dosyasına kaydetme
csv_dosya_yolu = "datasets/veri_haber_tokenlestirilmis.csv"
tokenleştirilmis_df.to_csv(csv_dosya_yolu, index=False)

print(f"Tokenleştirilmiş CSV dosyası başarıyla oluşturuldu: {csv_dosya_yolu}")
