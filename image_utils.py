import os
import shutil

def create_directory(directory):
    """Создает директорию, если она не существует."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def extract_images(source_folder, destination_folder):
    """Извлекает картинки из подпапок и помещает их в новую папку."""
    for folder in ['1', '2', '3']:
        for image_number in range(1, 4):  # Для картинок 1, 2, 3
            source_image = os.path.join(source_folder, folder, f'{image_number}.jpg')
            if os.path.exists(source_image):
                # Создаем путь к новой папке для изображения 
                new_folder = os.path.join(destination_folder, f'{image_number}')
                create_directory(new_folder)
                # Копируем изображение в новую папку с новым именем
                new_image_name = f'{folder}_{image_number}.jpg'
                destination_image = os.path.join(new_folder, new_image_name)
                shutil.copy(source_image, destination_image)
                print(f'Копируем {source_image} в {destination_image}')
