import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2

# ----------------------------
# Dataset Paths
# ----------------------------

train_dir = "data/PlantVillage/dataset/train"
valid_dir = "data/PlantVillage/dataset/validation"
test_dir = "data/PlantVillage/dataset/test"

IMG_SIZE = (224, 224)
BATCH_SIZE = 32

# ----------------------------
# Load Dataset
# ----------------------------

train_dataset = tf.keras.utils.image_dataset_from_directory(
    train_dir,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)

validation_dataset = tf.keras.utils.image_dataset_from_directory(
    valid_dir,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)

class_names = train_dataset.class_names

print("\nDisease Classes:\n")
print(class_names)

# ----------------------------
# Normalize Images
# ----------------------------

normalization = layers.Rescaling(1.0 / 255)

train_dataset = train_dataset.map(
    lambda x, y: (normalization(x), y)
)

validation_dataset = validation_dataset.map(
    lambda x, y: (normalization(x), y)
)

# Improve performance
AUTOTUNE = tf.data.AUTOTUNE

train_dataset = train_dataset.prefetch(buffer_size=AUTOTUNE)
validation_dataset = validation_dataset.prefetch(buffer_size=AUTOTUNE)

# ----------------------------
# MobileNetV2 Base Model
# ----------------------------

base_model = MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights="imagenet"
)

base_model.trainable = False

# ----------------------------
# Build Model
# ----------------------------

model = models.Sequential([

    base_model,

    layers.GlobalAveragePooling2D(),

    layers.Dropout(0.3),

    layers.Dense(
        256,
        activation="relu"
    ),

    layers.Dropout(0.3),

    layers.Dense(
        len(class_names),
        activation="softmax"
    )

])

# ----------------------------
# Compile
# ----------------------------

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# ----------------------------
# Train
# ----------------------------

history = model.fit(
    train_dataset,
    validation_data=validation_dataset,
    epochs=5
)

# ----------------------------
# Save Model
# ----------------------------

model.save("models/plant_disease_model.keras")

print("\n✅ Plant Disease Model Saved Successfully!")