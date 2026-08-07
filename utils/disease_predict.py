import tensorflow as tf
import numpy as np

IMG_SIZE = (224, 224)

# Load model once
model = tf.keras.models.load_model("models/plant_disease_model.keras")

CLASS_NAMES = [
    "Pepper__bell___Bacterial_spot",
    "Pepper__bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_leaf_spot",
    "Tomato_Spider_mites_Two_spotted_spider_mite",
    "Tomato__Target_Spot",
    "Tomato__Tomato_YellowLeaf__Curl_Virus",
    "Tomato__Tomato_mosaic_virus",
    "Tomato_healthy"
]


def predict_disease(image):

    image = image.resize(IMG_SIZE)

    image = np.array(image)

    image = image / 255.0

    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image, verbose=0)

    index = np.argmax(prediction)

    confidence = float(np.max(prediction)) * 100

    disease = CLASS_NAMES[index]

    return disease, confidence