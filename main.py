import os
from datetime import datetime, timedelta
from glob import iglob

list_read = []
"""Составим список путей в которых прога
 будет искать старые файлы"""

with open(r"\\nasback\temp\spisok.txt", 'r') as file:
    list_read = file.read().split('\n')
print(list_read)

def delete_old_files(folder_path):
    # Получаем текущую дату и вычитаем 3 месяца
    three_months_ago = datetime.now() - timedelta(days=90)

    # Перебираем все файлы и подкаталоги в папке
    for key, file_path in enumerate (iglob(folder_path)):
        print(file_path)
        # Получаем время последнего изменения файла
        file_mtime = datetime.utcfromtimestamp(os.stat(file_path).st_ctime)
        # Если время последнего изменения файла меньше трех месяцев назад, удаляем файл
        if file_mtime < three_months_ago:
            try:
                os.remove(file_path)
                print(f"Удален файл: {file_path}")
            except:
                print('Ошибка, файл не удален!!!')
        else:
            print(f"файл свежий: {file_path}")

if __name__=='__main__':
    for folder_path in list_read:
        delete_old_files(folder_path)
