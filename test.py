import os

print("Current Folder:")
print(os.getcwd())

print("\nModels Folder Exists?")
print(os.path.exists("models"))

print("\nFiles inside models folder:")

if os.path.exists("models"):
    print(os.listdir("models"))
else:
    print("models folder not found!")