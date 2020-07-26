import os
import glob
import cv2 as cv

# Compilando todos os caminhos.
X_path = glob.glob(os.path.join('Chokkan/', '*'))

X = []

# Tamanho da imagem escolhido foi de 224x224, a maioria das redes neurais prontas utilizam o 224x224
for f in X_path:
    try:
        cv.imwrite(f,cv.resize(cv.imread(f), (224, 224), interpolation=cv.INTER_AREA))

    except:
        print(f)


