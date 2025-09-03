import tensorflow as tf
from tensorflow.keras import layers, models

# ========================
# データセット読み込み
# ========================
train_ds = tf.keras.utils.image_dataset_from_directory(
    "../dataset",
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(128, 128),
    batch_size=32
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    "../dataset",
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(128, 128),
    batch_size=32
)

class_names = train_ds.class_names
print("クラス:", class_names)

# ========================
# データ前処理
# ========================
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.map(lambda x, y: (x/255.0, y)).cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds   = val_ds.map(lambda x, y: (x/255.0, y)).cache().prefetch(buffer_size=AUTOTUNE)

# ========================
# CNNモデル定義
# ========================
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
    layers.MaxPooling2D((2,2)),

    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),

    layers.Conv2D(128, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),

    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(len(class_names), activation='softmax')
])

model.compile(optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])

# ========================
# 学習
# ========================
history = model.fit(train_ds, validation_data=val_ds, epochs=10)

# ========================
# 保存
# ========================
model.save("../saved_model/game_classifier.h5")
print("モデルを保存しました！")
