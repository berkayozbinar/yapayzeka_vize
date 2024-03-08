import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense
import tensorflow as tf
from keras.utils import to_categorical

tf.compat.v1.disable_eager_execution()

df = pd.read_csv('C:/Users/berka/OneDrive/Masaüstü/yapayzeka/haber/trainer/egitici_veri_haber.csv')

encoder = LabelEncoder()
df['Etiket'] = encoder.fit_transform(df['Kategori'])
classes = len(encoder.classes_)

vectorizer = TfidfVectorizer(max_features=5000)  
x = vectorizer.fit_transform(df['Metin'])

xTrain, xTest, yTrain, yTest = train_test_split(x, df['Etiket'], test_size=0.2, random_state=42, stratify=df['Etiket'])

yTrainOh = to_categorical(yTrain, num_classes=classes)
yTestOh = to_categorical(yTest, num_classes=classes)

model = Sequential()
model.add(Dense(128, input_dim=x.shape[1], activation='relu'))
model.add(Dense(256, activation='relu'))  
model.add(Dense(64, activation='relu'))
model.add(Dense(classes, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(xTrain, yTrainOh, epochs=20, batch_size=32, validation_data=(xTest, yTestOh))

def analiz(vectorizer, veri, dosyaAdı):
    veriVec = vectorizer.transform(veri)
    tahminler = model.predict(veriVec)
    tahminSınıfları = tf.keras.backend.eval(tf.argmax(tahminler, axis=1))

    sonuçlarDf = pd.DataFrame({'Metin': veri,})
    sonuçlarDf['Tahmin'] = encoder.inverse_transform(tahminSınıfları)
    sonuçlarDf.to_csv(dosyaAdı, index=False)


veriDf = pd.read_csv('C:/Users/berka/OneDrive/Masaüstü/yapayzeka/haber/datasets/veri_seti_haber.csv')
veri = veriDf['Metin'].tolist()

analiz(vectorizer, veri, dosyaAdı='C:/Users/berka/OneDrive/Masaüstü/yapayzeka/haber/datasets/analiz_sonuclari_haber.csv')