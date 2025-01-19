import os
from image_utils import extract_images

def main():
    # Путь к папке А, Б, В, Г 
    base_folder = r'C:\Users\Karina\Desktop\Проект вуз\Проект 3'
    folders = ['А', 'Б', 'В', 'Г']
    
    for folder in folders:
        source_folder = os.path.join(base_folder, folder)
        # Создаем папку назначения внутри каждой папки А, Б, В, Г
        destination_folder = os.path.join(source_folder, 'new_images')
        extract_images(source_folder, destination_folder)

if __name__ == "__main__":
    main()
