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
ext_musica = [".mp3", ".wav", ".mpeg-4"]

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


def ordenarArchivos(extension, nombre_archivo):
    move = False

    for i in ext_texto:
        if extension == i:
            textos = os.listdir(ruta_descargas+"Texto")
            archivos = []
            for texto in textos:
                archivos.append(texto)

            if nombre_archivo+extension not in archivos:
                shutil.move(ruta_descargas+nombre_archivo +
                            extension, ruta_descargas+"Texto")
                move = True
            else:
                os.rename(ruta_descargas+nombre_archivo+extension,
                          ruta_descargas+nombre_archivo+" (1)"+extension)
                nombre_archivo = nombre_archivo+" (1)"

                shutil.move(ruta_descargas+nombre_archivo +
                            extension, ruta_descargas+"Texto")
                move = True

    for i in ext_video:
        if extension == i:
            videos = os.listdir(ruta_descargas+"Video")
            archivos = []
            for video in videos:
                archivos.append(video)

            if nombre_archivo+extension not in archivos:
                shutil.move(ruta_descargas+nombre_archivo +
                            extension, ruta_descargas+"Video")
                move = True
            else:
                os.rename(ruta_descargas+nombre_archivo+extension,
                          ruta_descargas+nombre_archivo+" (1)"+extension)
                nombre_archivo = nombre_archivo+" (1)"

                shutil.move(ruta_descargas+nombre_archivo +
                            extension, ruta_descargas+"Video")
                move = True

    for i in ext_foto:
        if extension == i:
            fotos = os.listdir(ruta_descargas+"Fotos")
            archivos = []
            for foto in fotos:
                archivos.append(foto)

            if nombre_archivo+extension not in archivos:
                shutil.move(ruta_descargas+nombre_archivo +
                            extension, ruta_descargas+"Fotos")
                move = True
            else:
                os.rename(ruta_descargas+nombre_archivo+extension,
                          ruta_descargas+nombre_archivo+" (1)"+extension)
                nombre_archivo = nombre_archivo+" (1)"

                shutil.move(ruta_descargas+nombre_archivo +
                            extension, ruta_descargas+"Fotos")
                move = True

    for i in ext_ejecutables:
        if extension == i:
            ejecutables = os.listdir(ruta_descargas+"Ejecutables")
            archivos = []
            for ejecutable in ejecutables:
                archivos.append(ejecutable)

            if nombre_archivo+extension not in archivos:
                shutil.move(ruta_descargas+nombre_archivo +
                            extension, ruta_descargas+"Ejecutables")
                move = True
            else:
                os.rename(ruta_descargas+nombre_archivo+extension,
                          ruta_descargas+nombre_archivo+" (1)"+extension)
                nombre_archivo = nombre_archivo+" (1)"

                shutil.move(ruta_descargas+nombre_archivo +
                            extension, ruta_descargas+"Ejecutables")
                move = True

    for i in ext_musica:
        if extension == i:
            musicas = os.listdir(ruta_descargas+"Musica")
            archivos = []
            for musica in musicas:
                archivos.append(musica)

            if nombre_archivo+extension not in archivos:
                shutil.move(ruta_descargas+nombre_archivo +
                            extension, ruta_descargas+"Musica")
                move = True
            else:
                os.rename(ruta_descargas+nombre_archivo+extension,
                          ruta_descargas+nombre_archivo+" (1)"+extension)
                nombre_archivo = nombre_archivo+" (1)"

                shutil.move(ruta_descargas+nombre_archivo +
                            extension, ruta_descargas+"Musica")
                move = True

    if extension != "" and move == False:
        if extension == i:
            otros = os.listdir(ruta_descargas+"Otros")
            archivos = []
            for otro in otros:
                archivos.append(otro)

            if nombre_archivo+extension not in archivos:
                shutil.move(ruta_descargas+nombre_archivo +
                            extension, ruta_descargas+"Otros")
                move = True
            else:
                os.rename(ruta_descargas+nombre_archivo+extension,
                          ruta_descargas+nombre_archivo+" (1)"+extension)
                nombre_archivo = nombre_archivo+" (1)"

                shutil.move(ruta_descargas+nombre_archivo +
                            extension, ruta_descargas+"Otros")
                move = True


def limpiarTemporales():
    shutil.rmtree(ruta_temporales, ignore_errors=True, onerror=None)


def limpiarPapelera():
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)


def main():
    crearCarpetas()
    for archivo in os.listdir(ruta_descargas):
        nombre_archivo, extension = os.path.splitext(archivo)
        ordenarArchivos(extension, nombre_archivo)
    limpiarTemporales()
    limpiarPapelera()


main()
