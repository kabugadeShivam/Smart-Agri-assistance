import pandas as pd
import random

diseases = {

    "Tomato": [

        ("Late Blight","Fungal"),
        ("Early Blight","Fungal"),
        ("Leaf Mold","Fungal"),
        ("Bacterial Spot","Bacterial"),
        ("Septoria Leaf Spot","Fungal"),
        ("Target Spot","Fungal"),
        ("Yellow Leaf Curl Virus","Viral"),
        ("Mosaic Virus","Viral")

    ],

    "Potato":[

        ("Late Blight","Fungal"),
        ("Early Blight","Fungal"),
        ("Common Scab","Bacterial"),
        ("Black Scurf","Fungal")

    ],

    "Rice":[

        ("Blast","Fungal"),
        ("Brown Spot","Fungal"),
        ("Sheath Blight","Fungal"),
        ("Bacterial Leaf Blight","Bacterial")

    ],

    "Wheat":[

        ("Stem Rust","Fungal"),
        ("Leaf Rust","Fungal"),
        ("Loose Smut","Fungal")

    ]

}

symptoms = [

    "Brown spots on leaves",
    "Yellowing of leaves",
    "Leaf curling",
    "Wilting",
    "Stem lesions",
    "Fruit rot",
    "White fungal growth",
    "Leaf drying"

]

treatments = [

    "Remove infected leaves",
    "Apply recommended fungicide",
    "Use certified seeds",
    "Improve drainage",
    "Avoid overhead irrigation",
    "Apply copper-based fungicide"

]

organics = [

    "Neem oil spray",
    "Trichoderma application",
    "Compost tea",
    "Garlic extract spray"

]

chemicals = [

    "Mancozeb",
    "Copper Oxychloride",
    "Metalaxyl",
    "Chlorothalonil",
    "Carbendazim"

]

prevent = [

    "Crop rotation",
    "Proper spacing",
    "Disease-free seeds",
    "Balanced fertilization",
    "Field sanitation"

]

weather = [

    "High humidity",
    "Cool weather",
    "Heavy rainfall",
    "Poor air circulation"

]

rows = []

count = 1

for crop in diseases:

    for disease, dtype in diseases[crop]:

        for i in range(40):

            rows.append({

                "Disease_ID": f"DIS{count:04d}",

                "Crop": crop,

                "Disease_Name": disease,

                "Disease_Type": dtype,

                "Causal_Organism": "Various",

                "Symptoms": random.choice(symptoms),

                "Treatment": random.choice(treatments),

                "Organic_Control": random.choice(organics),

                "Chemical_Control": random.choice(chemicals),

                "Prevention": random.choice(prevent),

                "Favorable_Conditions": random.choice(weather),

                "Severity": random.choice(

                    ["Low","Medium","High"]

                ),

                "Yield_Loss_Percentage":

                    random.randint(5,60),

                "Recommended_Fertilizer":

                    "Balanced NPK",

                "Keywords":

                    f"{crop},{disease}"

            })

            count += 1

df = pd.DataFrame(rows)

df.to_csv(

    "knowledge/plant_diseases.csv",

    index=False

)

print(df.head())

print()

print("Rows:",len(df))