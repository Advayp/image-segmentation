import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture as gmm
import cv2
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("path", help="Relative path to the image file")
parser.add_argument("-c", "--components",
                    help="Set the number of mixture components. Defaults to 6.", type=int)
parser.add_argument(
    "-o", "--output", help="Name of the output file. Defaults to `output`.", type=str)

args = parser.parse_args()

name = args.output if args.output else 'output'

n = args.components if args.components else 6

img = cv2.imread(args.path)
img_reshaped = img.reshape((-1, 3))

gmm_model = gmm(n_components=n, covariance_type="tied").fit(img_reshaped)
gmm_labels = gmm_model.predict(
    img_reshaped).reshape(img.shape[0], img.shape[1])

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.subplot(1, 2, 2)
plt.imshow(gmm_labels, cmap='gray')
plt.show()

plt.imshow(gmm_labels, cmap='gray')
plt.savefig(f'{name}.png')
