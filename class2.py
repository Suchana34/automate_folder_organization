from easygui import *
import os
import subprocess


file_path = os.getcwd()
file_name = os.path.join(file_path, "rules.txt")

my_file_name = open(file_name,"a+")
 
msgbox("enter dir of the folder u want to automate",'folder name')
folder = diropenbox()
my_file_name.write(folder)
my_file_name.write("\nR")

for i in range(0,8):
    choice = buttonbox("choose the file type","choices",("jpg","mp3","pdf","exe","mp4","doc","srt","docx"))

    if choice=="jpg":
        msgbox("enter dir of the folder for jpg files",'jpg files')
        jpg_folder = diropenbox()
        my_file_name.write("\njpg:")
        my_file_name.write(jpg_folder)


    elif choice=="mp3":
        msgbox("enter dir of the folder for mp3 files",'mp3 files')
        mp3_folder = diropenbox()
        my_file_name.write("\nmp3:")
        my_file_name.write(mp3_folder)    

    elif choice=="pdf":
        msgbox("enter dir of the folder for pdf files",'pdf files')
        pdf_folder = diropenbox()
        my_file_name.write("\npdf:")
        my_file_name.write(pdf_folder)


    elif choice=="exe":
        msgbox("enter dir of the folder for exe files",'exe files')
        exe_folder = diropenbox()
        my_file_name.write("\nexe:")
        my_file_name.write(exe_folder)



    elif choice=="mp4":
        msgbox("enter dir of the folder for mp4 files",'mp4 files')
        mp4_folder = diropenbox()
        my_file_name.write("\nmp4:")
        my_file_name.write(mp4_folder)



    elif choice=="doc":
        msgbox("enter dir of the folder for doc files",'doc files')
        doc_folder = diropenbox()
        my_file_name.write("\ndoc:")
        my_file_name.write(doc_folder)



    elif choice=="srt":
        msgbox("enter dir of the folder for srt files",'srt files')
        srt_folder = diropenbox()
        my_file_name.write("\nsrt:")
        my_file_name.write(srt_folder)


    elif choice=="docx":
        msgbox("enter dir of the folder for docx files",'docx files')
        docx_folder = diropenbox()
        my_file_name.write("\ndocx:")
        my_file_name.write(docx_folder)


subprocess.call("python class1.py", shell=True)

my_file_name.close()

my_file_name = open(file_name,"w").close()  #clears the prev data