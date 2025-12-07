from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split


df = pd.read_csv('Final_Label_data.csv')  # Assuming a CSV file with a column 'text'

df["label"] = df["label"].map({
    "non-critical": 0,
    "critical": 1
})

texts = df["log_text"].tolist()
labels = df["label"].values 


model = SentenceTransformer('all-MiniLM-L6-v2')

embeddings = model.encode(
    texts,
    batch_size=16,
    show_progress_bar=True,
)

X_train, X_test, y_train, y_test = train_test_split(
    embeddings, labels, test_size=0.20, random_state=42
)


ann = tf.keras.Sequential([
    tf.keras.layers.Dense(units=128, activation="relu", input_shape=(embeddings.shape[1],)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(units=64, activation="relu"),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(units=1, activation="sigmoid")
])

#Compiling ANN
ann.compile(optimizer="adam",loss="binary_crossentropy",metrics=['accuracy'])

#Fitting ANN
ann.fit(X_train,y_train,batch_size=16,epochs = 10, validation_data=(X_test, y_test))