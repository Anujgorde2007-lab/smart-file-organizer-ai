import os
import shutil

folder_path = input("Enter folder path: ")

file_types = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Code": [".py", ".java", ".cpp"],
    "Videos": [".mp4", ".mkv"]
}

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        for category, extensions in file_types.items():
            if file.lower().endswith(tuple(extensions)):
                category_folder = os.path.join(folder_path, category)

                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)

                shutil.move(file_path, os.path.join(category_folder, file))
                break

print("Files organized successfully!")
