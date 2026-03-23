# ==============================
# VEHICLE DAMAGE DETECTOR (AUTO 200 IMAGES)
# ==============================

import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import os, cv2, random, urllib.request

# ==============================
# 1. CREATE DATASET
# ==============================

base_path = "/content/vehicle_data"
damage_path = os.path.join(base_path, "damage")
nodamage_path = os.path.join(base_path, "no_damage")

os.makedirs(damage_path, exist_ok=True)
os.makedirs(nodamage_path, exist_ok=True)

# Car image base URLs (stable Unsplash)
car_urls = [
    "https://images.unsplash.com/photo-1503376780353-7e6692767b70",
    "https://images.unsplash.com/photo-1493238792000-8113da705763",
    "https://images.unsplash.com/photo-1549924231-f129b911e442",
    "https://images.unsplash.com/photo-1511919884226-fd3cad34687c",
    "https://images.unsplash.com/photo-1605559424843-9e4c228a2c5a"
]

# download + generate images
count = 0

for i in range(100):   # 100 original → 200 total after damage
    try:
        url = random.choice(car_urls) + f"?w=400&sig={i}"
        path = f"/content/car_{i}.jpg"
        urllib.request.urlretrieve(url, path)

        img = cv2.imread(path)
        if img is None:
            continue

        # Save normal image
        cv2.imwrite(f"{nodamage_path}/n{i}.jpg", img)

        # Create fake damage (scratch simulation)
        damaged = img.copy()
        h, w, _ = damaged.shape

        for _ in range(random.randint(3,7)):
            x1 = random.randint(0, w)
            y1 = random.randint(0, h)
            x2 = random.randint(0, w)
            y2 = random.randint(0, h)
            color = (0,0,0)
            thickness = random.randint(1,3)
            cv2.line(damaged, (x1,y1), (x2,y2), color, thickness)

        cv2.imwrite(f"{damage_path}/d{i}.jpg", damaged)

        count += 1

    except:
        continue

print(f"Dataset Ready ✅ Total pairs: {count} (≈{count*2} images)")

# ==============================
# 2. LOAD DATA
# ==============================

img_size = 64

data = tf.keras.preprocessing.image_dataset_from_directory(
    base_path,
    image_size=(img_size, img_size),
    batch_size=16
)

data = data.map(lambda x,y: (x/255.0, y))

print("Data Loaded ✅")

# ==============================
# 3. MODEL
# ==============================

model = models.Sequential([
    layers.Conv2D(32,3,activation='relu',input_shape=(64,64,3)),
    layers.MaxPooling2D(),

    layers.Conv2D(64,3,activation='relu'),
    layers.MaxPooling2D(),

    layers.Conv2D(128,3,activation='relu'),
    layers.MaxPooling2D(),

    layers.Flatten(),
    layers.Dense(64,activation='relu'),
    layers.Dense(1,activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# ==============================
# 4. TRAIN
# ==============================

model.fit(data, epochs=5)

# ==============================
# 5. TEST
# ==============================

from google.colab import files
from tensorflow.keras.preprocessing import image

while True:
    print("\nUpload Vehicle Image (Cancel to stop) ")

    uploaded = files.upload()

    if len(uploaded) == 0:
        print("Stopped ")
        break

    for file in uploaded.keys():
        img = image.load_img(file, target_size=(64,64))
        img_array = image.img_to_array(img)/255.0
        img_array = np.expand_dims(img_array, axis=0)

        pred = model.predict(img_array)[0][0]

        print("\nRESULT 🚗")

        if pred > 0.5:
            print(f"Not Damaged ({round(pred*100,2)}%)")
        else:
            print(f"Damaged ({round((1-pred)*100,2)}%)")
