import os
from PIL import Image
from PhotoSigner import add_sign


def openFileIfImage(folderPath, file):
    filename, fileExtension = os.path.splitext(file)
    acceptedExtensions = ['.png', '.jpg', '.jpeg']
    if fileExtension.lower() in acceptedExtensions: return Image.open(f"{folderPath}/{file}")


if __name__ == '__main__':
    folderPath = input("Dimmi la cartella sorgente. Mi andrò a prendere tutte le immagini al suo interno: ")
    pics = next(os.walk(folderPath))[2]
    pics = [openFileIfImage(folderPath, image) for image in pics]
    add_sign(pics, 'sign.png', f"{folderPath}/signed")

    print("Finito. Controlla...")

