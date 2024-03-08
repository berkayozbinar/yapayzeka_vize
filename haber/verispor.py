import requests
from bs4 import BeautifulSoup
import pandas as pd

def tum_haberleri_cek(haber_sitesi_url):
    response = requests.get(haber_sitesi_url)
    soup = BeautifulSoup(response.content, "html.parser")


    # Tüm haber başlıklarını ve URL'lerini çekme
    haberler = []
    for haber in soup.find_all("div", class_="p12-col"):
        url_element = haber.find("a", class_="box boxStyle hbBoxMainText color-sport")
        if url_element:
            url = url_element["href"]
            haberler.append(url)
    return haberler

def haber_metni_cek(haber_url):
    response = requests.get(haber_url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Haber metnini çekme
    haber_metni = soup.find("main", class_="mtm-20 hbptContent haber_metni").text.strip()

    return haber_metni

# Haber URL'leri çekme
gecici_haber_sitesi = "https://www.haberler.com/"
haber_url_listesi = tum_haberleri_cek("https://www.haberler.com/spor/")

# CSV dosyasına yazmak üzere bir DataFrame oluşturun
veri = {"Metin": []}

# Her bir haber için haber metnini çekme
for haber_url in haber_url_listesi:
    haber_metni = haber_metni_cek(haber_url)
    
    # Veri DataFrame'e ekleme
    veri["Metin"].append(haber_metni)

# DataFrame'i CSV dosyasına kaydetme
csv_dosya_yolu = "C:/Users/berka/OneDrive/Masaüstü/yapayzeka/haber/datasets/dataset.csv"
veri_df = pd.DataFrame(veri)
veri_df.to_csv(csv_dosya_yolu, mode="a", index=False, encoding='utf-8')

print(f"Haber metinleri CSV dosyasına başarıyla kaydedildi: {csv_dosya_yolu}")
