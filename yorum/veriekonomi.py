import requests
from bs4 import BeautifulSoup

def tum_haberleri_cek(haber_sitesi_url):
    response = requests.get(haber_sitesi_url)
    soup = BeautifulSoup(response.content, "html.parser")

    haberler = []
    for haber in soup.find_all("div", class_="p12-col"):
        url_element = haber.find("a", class_="boxStyle color-finance hbBoxMainText")
        if url_element:
            url = url_element["href"]
            haberler.append(url)
    return haberler

def haber_metni_cek(haber_url, file):
    response = requests.get(gecici_haber_sitesi + haber_url)
    soup = BeautifulSoup(response.content, "html.parser")

    haber_metni = soup.find("p", class_="hbcMsg")

    if haber_metni:
        titles_text = haber_metni.text.strip() + ","
        file.write(f'{titles_text}\n')
    else: print("")

    return haber_metni

gecici_haber_sitesi = "https://www.haberler.com/"
haber_url_listesi = tum_haberleri_cek("https://www.haberler.com/ekonomi/")

# Text dosyasına yazmak için bir dosya oluşturun
txt_dosya_yolu = "C:/Users/berka/OneDrive/Masaüstü/yapayzeka/yorum/datasets/haber_metinleri.txt"
with open(txt_dosya_yolu, 'w', encoding='utf-8') as file:
    # Her bir haber için haber metnini çekme
    for haber_url in haber_url_listesi:
        haber_metni = haber_metni_cek(haber_url, file)

print(f"Haber metinleri TXT dosyasına başarıyla kaydedildi: {txt_dosya_yolu}")
