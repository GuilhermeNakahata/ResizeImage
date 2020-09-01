import os
import glob
import cv2 as cv

X_path = glob.glob(os.path.join('DiretorioEscolhido/NomePasta', '*'))

X = []

for f in X_path:
    try:
        cv.imwrite(f,cv.resize(cv.imread(f), (224, 224), interpolation=cv.INTER_AREA))

    except:
        print(f)


