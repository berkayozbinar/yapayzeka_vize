import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import classification_report, confusion_matrix
import tensorflow as tf
from keras.utils import to_categorical
import matplotlib.pyplot as plt
import seaborn as sns

tf.compat.v1.disable_eager_execution()

# Örnek olarak CSV dosyasından veri setini yükleme
df = pd.read_csv('C:/Users/berka/OneDrive/Masaüstü/yapayzeka/yorum/trainer/egitici_veri_yorum.csv')

# Etiketleri sayısal hale getir
label_encoder = LabelEncoder()
df['Etiket'] = label_encoder.fit_transform(df['Durum'])
num_classes = len(label_encoder.classes_)  # Sınıf sayısını dinamik olarak al

# TF-IDF vektörleştirmeyi uygula
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df['Yorum'])

# Veri setini eğitim ve test setlerine ayır
X_train, X_test, y_train, y_test = train_test_split(X, df['Etiket'], test_size=0.2, random_state=42, stratify=df['Etiket'])

# Etiketleri one-hot encode et
y_train_one_hot = to_categorical(y_train, num_classes=num_classes)
y_test_one_hot = to_categorical(y_test, num_classes=num_classes)

# Modeli oluştur
model = Sequential()
model.add(Dense(128, input_dim=X.shape[1], activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))  # Çıkış sayısını sınıf sayısı ile eşleştir
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Modeli eğit
model.fit(X_train, y_train_one_hot, epochs=10, batch_size=32, validation_data=(X_test, y_test_one_hot))

# Modelin performansını değerlendir
y_pred_prob = model.predict(X_test)
y_pred = tf.keras.backend.eval(tf.argmax(y_pred_prob, axis=1))

# Karmaşıklık Matrisini Görselleştirme
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='g', cmap='Blues', xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
plt.xlabel('Tahmin Edilen')
plt.ylabel('Gerçek')
plt.title('Karmaşıklık Matrisi')
plt.show()

# Sınıf Dağılımını Görselleştirme
plt.figure(figsize=(6, 6))
plt.pie(y_test.value_counts(), labels=label_encoder.classes_, autopct='%1.1f%%', startangle=140)
plt.title('Sınıf Dağılımı')
plt.show()

# Classification Report'ı ekrana yazdırma
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

model.save('C:/Users/berka/OneDrive/Masaüstü/yapayzeka/models/yorum.h5', include_optimizer=False, save_format='h5')
