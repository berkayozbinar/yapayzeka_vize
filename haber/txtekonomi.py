import os
import csv

def txt_to_csv(input_folder, output_file):
    # Kategorilerin ve verilerin saklanacağı liste
    data_list = []

    # Belirtilen klasördeki tüm .txt dosyalarını bul
    txt_files = [f for f in os.listdir(input_folder) if f.endswith('.txt')]

    # Her bir .txt dosyasını oku ve kategorisiyle birlikte listeye ekle
    for txt_file in txt_files:
        file_path = os.path.join(input_folder, txt_file)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            data_list.append({ 'Metin': content, 'Kategori': "Ekonomi",})

    # CSV dosyasına yaz
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Metin', 'Kategori']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_list)


# Kullanım örneği
input_folder_path = 'C:/Users/berka/OneDrive/Masaüstü/yapayzeka/haber/news/ekonomi'
output_csv_path = 'C:/Users/berka/OneDrive/Masaüstü/yapayzeka/haber/trainer/dataset.csv'
txt_to_csv(input_folder_path, output_csv_path)
