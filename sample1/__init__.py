import os
from string import digits


def rename_files():
    file_names = os.listdir(r"C:\Users\HP\Desktop\prank\prank")
    print(file_names)

    #print("rename\"hi how are you\"")
    os.chdir(r"C:\Users\HP\Desktop\prank\prank")
    current_working_directory = os.getcwd()
    print(current_working_directory)

    #os.rename("2chennai.jpg", "chennai.jpg")
    for filename in file_names:
        os.rename(filename,filename.translate(str.maketrans('','',"0123456789")))


rename_files()