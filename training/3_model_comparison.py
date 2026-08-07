import pandas as pd
import matplotlib.pyplot as plt

# Accuracy values from training
results = {
    "Decision Tree": 71.00,
    "Random Forest": 86.25,
    "Logistic Regression": 58.00,
    "KNN": 12.00,
    "SVM": 16.00
}

# Create DataFrame
df = pd.DataFrame(
    list(results.items()),
    columns=["Model", "Accuracy"]
)

print(df)

# Save CSV
df.to_csv("models/model_results.csv", index=False)

# Plot
plt.figure(figsize=(8,5))
plt.bar(df["Model"], df["Accuracy"])
plt.title("Model Accuracy Comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy (%)")
plt.xticks(rotation=20)
plt.tight_layout()

plt.savefig("models/model_accuracy.png")

print("\nComparison files saved successfully.")