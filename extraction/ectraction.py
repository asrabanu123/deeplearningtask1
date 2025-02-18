import os
import random
import shutil
import sys

class Processing:
    def get_used_images(self, train_folder):
        try:
            used_images = set()
            for class_folder in os.listdir(train_folder):
                class_path = os.path.join(train_folder, class_folder)
                if os.path.isdir(class_path):
                    for img in os.listdir(class_path):
                        used_images.add(f"{class_folder}/{img}")
            return used_images
        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            print(f'Error Type: {er_type}\nError Msg: {er_msg}\nError Line: {er_line.tb_lineno}')

    def splitting_images(self, root_folder, test_folder, val_folder, train_folder, used_images):
        try:
            for folder in os.listdir(root_folder):
                folder_path = os.path.join(root_folder, folder)
                if os.path.isdir(folder_path):
                    images = [i for i in os.listdir(folder_path) if i.lower().endswith(('.jpg', '.jpeg', '.png'))]
                    images_with_class = [f'{folder}/{img}' for img in images]

                    available_images = list(set(images_with_class) - used_images)
                    available_filenames = [img.split('/')[-1] for img in available_images]

                    num_val = min(50, len(available_filenames) // 2)
                    num_test = min(50, len(available_filenames) - num_val)

                    val_images = available_filenames[:num_val]
                    test_images = available_filenames[num_val:num_val+num_test]

                    if len(val_images)<50 or len(test_images)<50:
                        print(f'Not enough images in {folder}, so duplicating to fill it.')
                        train_class_folder = os.path.join(train_folder, folder)
                        if os.path.exists(train_class_folder):
                            train_images = [j for j in os.listdir(train_class_folder) if j.lower().endswith(('.png', '.jpeg', '.jpg'))]

                            while len(val_images)<50 and train_images:
                                val_images.append(random.choice(train_images))
                            while len(test_images)<50 and train_images:
                                test_images.append(random.choice(train_images))

                    val_class_folder = os.path.join(val_folder, folder)
                    test_class_folder = os.path.join(test_folder, folder)

                    os.makedirs(val_class_folder, exist_ok=True)
                    os.makedirs(test_class_folder, exist_ok=True)

                    for img in val_images:
                        shutil.copy2(os.path.join(folder_path, img), os.path.join(val_class_folder, img))

                    for img in test_images:
                        shutil.copy2(os.path.join(folder_path, img), os.path.join(test_class_folder, img))

                    print(f'{folder} copied {len(val_images)} to {val_class_folder}')
                    print(f'{folder} copied {len(test_images)} to {test_class_folder}')

            print('Validation and Testing dataset creation completed!!')
        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            print(f'Error Type: {er_type}\nError Msg: {er_msg}\nError Line: {er_line.tb_lineno}')

if __name__ == "__main__":
    try:
        train_path = r"C:\Users\asrabanu\PycharmProjects\PythonProject\Food Classification Dataset\dataset\training"
        test_path = r"C:\Users\asrabanu\PycharmProjects\PythonProject\Food Classification Dataset\dataset\testing"
        val_path = r"C:\Users\asrabanu\PycharmProjects\PythonProject\Food Classification Dataset\dataset\validation"
        root_path = r"C:\Users\asrabanu\PycharmProjects\PythonProject\Food Classification Dataset\dataset"
        process = Processing()
        used_images = process.get_used_images(train_path)
        process.splitting_images(root_path, test_path, val_path, train_path, used_images)
    except Exception as e:
        er_type, er_msg, er_line = sys.exc_info()
        print(f'Error Type: {er_type}\nError Msg: {er_msg}\nError Line: {er_line.tb_lineno}')

