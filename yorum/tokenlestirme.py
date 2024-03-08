import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# nltk.download("punkt")
# nltk.download("stopwords")

veri = pd.read_csv("trainer/egitici_veri_yorum.csv")

stopWords = set(stopwords.words("turkish"))
stemmer = PorterStemmer()

tokenler = []

for metin in veri["Yorum"]: # Haberler için token alınacaksa veri["Metin"]

    metin = metin.lower()
    kelimeler = word_tokenize(metin)
    kelimeler = [kelime for kelime in kelimeler if kelime.isalnum() and kelime not in stopWords]
    kelimeler = [stemmer.stem(kelime) for kelime in kelimeler]
    
    tokenler.append(kelimeler)

tokenleştirilmişDf = pd.DataFrame({"Tokenler": tokenler})

csvDosyaYolu = "datasets/veri_tokenlestirilmis.csv"
tokenleştirilmişDf.to_csv(csvDosyaYolu, index=False)

print(f"Tokenleştirilmiş CSV dosyası başarıyla oluşturuldu: {csvDosyaYolu}")
