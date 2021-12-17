import os
import shutil

usuario=os.getlogin()
ruta_descargas="C:/Users/{}/Downloads/".format(usuario)

ext_foto=[".png",".jpg",".jpeg",".gif",".psd",".bmp",".svg"]
ext_video=[".mp4",".avi",".mkv",".flv",".mov",".wmv",".divx"]
ext_texto=[".docx",".doc",".txt",".pdf",".pptx"]

def ordenarArchivos(archivo, extension):
    move=False
    for i in ext_texto:
        if extension == i:
            shutil.move(ruta_descargas+archivo, ruta_descargas+"Texto")
            move=True
    for i in ext_video:
        if extension == i:
            shutil.move(ruta_descargas+archivo, ruta_descargas+"Video")
            move=True
    for i in ext_foto:
        if extension == i:
            shutil.move(ruta_descargas+archivo, ruta_descargas+"Fotos")
            move=True

    if extension!="" and move==False:
        shutil.move(ruta_descargas+archivo, ruta_descargas+"Otros")

def main():
    for archivo in os.listdir(ruta_descargas):
        nombre_archivo, extension = os.path.splitext(archivo)
        ordenarArchivos(archivo, extension)

main()