import os
import shutil
import tempfile
import winshell

usuario = os.getlogin()
ruta_descargas = "C:/Users/{}/Downloads/".format(usuario)
ruta_temporales = tempfile.gettempdir()

# Definicion de extensiones de archivos
ext_foto = [".png", ".jpg", ".jpeg", ".gif", ".psd", ".bmp", ".svg"]
ext_video = [".mp4", ".avi", ".mkv", ".flv", ".mov", ".wmv", ".divx"]
ext_texto = [".docx", ".doc", ".txt", ".pdf", ".pptx"]
ext_ejecutables = [".exe", ".dll", ".cmd", ".bat"]
ext_musica=[".mp3", ".wav", ".mpeg-4"]

# Creacion de carpetas si es necesario

def crearCarpetas():
    carpetas = []

    for dir in os.listdir(ruta_descargas):
        nombre_carpeta, extension = os.path.splitext(dir)
        if extension == "":
            carpetas.append(nombre_carpeta)

    if "Video" or "Texto" or "Fotos" or "Otros" or "Ejecutables" or "Musica" not in carpetas:
        if "Video" not in carpetas:
            os.makedirs(ruta_descargas + "Video")
        if "Texto" not in carpetas:
            os.makedirs(ruta_descargas + "Texto")
        if "Fotos" not in carpetas:
            os.makedirs(ruta_descargas + "Fotos")
        if "Otros" not in carpetas:
            os.makedirs(ruta_descargas + "Otros")
        if "Ejecutables" not in carpetas:
            os.makedirs(ruta_descargas + "Ejecutables")
        if "Musica" not in carpetas:
            os.makedirs(ruta_descargas + "Musica")

# Funcion ordenar archivos segun extension

def ordenarArchivos(archivo, extension):
    move = False
    for i in ext_texto:
        if extension == i:
            shutil.move(ruta_descargas+archivo, ruta_descargas+"Texto")
            move = True
    for i in ext_video:
        if extension == i:
            shutil.move(ruta_descargas+archivo, ruta_descargas+"Video")
            move = True
    for i in ext_foto:
        if extension == i:
            shutil.move(ruta_descargas+archivo, ruta_descargas+"Fotos")
            move = True
    for i in ext_ejecutables:
        if extension == i:
            shutil.move(ruta_descargas+archivo, ruta_descargas+"Ejecutables")
            move = True

    if extension != "" and move == False:
        shutil.move(ruta_descargas+archivo, ruta_descargas+"Otros")


def limpiarTemporales():
    shutil.rmtree(ruta_temporales, ignore_errors=True, onerror=None)

def limpiarPapelera():
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)

def main():
    crearCarpetas()
    for archivo in os.listdir(ruta_descargas):
        nombre_archivo, extension = os.path.splitext(archivo)
        ordenarArchivos(archivo, extension)
    limpiarTemporales()
    limpiarPapelera()

main()
