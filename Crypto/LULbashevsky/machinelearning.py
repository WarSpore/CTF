from tensorflow.keras.utils import plot_model
from torchviz import make_dot
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import BinaryCrossentropy
from tensorflow.keras.callbacks import LearningRateScheduler, EarlyStopping
from tensorflow.keras.layers import Dropout, LeakyReLU
from sklearn.model_selection import train_test_split
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pwn import *
from sklearn.preprocessing import StandardScaler
import shap
from lime.lime_tabular import LimeTabularExplainer

train = pd.read_csv('S2G\Crypto\LULbashevsky\\train.csv')
test = pd.read_csv('S2G\Crypto\LULbashevsky\\test.csv')

model = Sequential([
    Dense(128, activation='relu', input_dim=256, kernel_regularizer=tf.keras.regularizers.l2(0.01)),
    Dropout(0.3),
    Dense(64, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)),
    Dropout(0.3),
    Dense(1, activation='sigmoid')  # Use sigmoid for binary classification
])


scaler = StandardScaler()


T_total = 1000

X_train = train[train.columns[:-1]]
y_train = train[train.columns[-1]]

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)

# Build the model
model = Sequential([
    Dense(128, activation='relu', input_dim=X_train.shape[1], kernel_regularizer=tf.keras.regularizers.l2(0.01)),
    Dropout(0.3),
    Dense(64, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)),
    Dropout(0.3),
    Dense(1, activation='sigmoid')  # Sigmoid for binary classification
])

# Compile the model
model.compile(optimizer='Adam', loss='binary_crossentropy', metrics=['accuracy'])

# Callbacks
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
lr_scheduler = LearningRateScheduler(lambda epoch: float(0.0001 * tf.math.exp(-0.1 * epoch)))

# Fit the model
history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=100, callbacks=[early_stopping, lr_scheduler])

X_test = test[test.columns[:-1]]
X_test = scaler.transform(X_test)
y_test = test[test.columns[-1]]
y_pred = model.predict(X_test)
y_pred = np.array([item for sublist in y_pred for item in sublist])
y_pred = np.where(y_pred >= 0.5,1,0)
print("accuracy:",(np.mean(y_pred == y_test)))

plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()