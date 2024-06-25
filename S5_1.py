import os

def split_path(path):
    folder_path, full_file_name = os.path.split(path)
    file_name, file_extension = os.path.splitext(full_file_name)
    
    return folder_path, file_name, file_extension


file_path = 'C:/Users/User/Documents/Doc.doc'
path, name, extension = split_path(file_path)

print("Путь: ", path)
print("Имя файла: ", name)
print("Расширение файла: ", extension)