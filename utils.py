import numpy as np
import matplotlib.pyplot as plt
import cv2
from sklearn.mixture import GaussianMixture as gmm
import argparse


def get_bic(reshaped_img, values=np.arange(1, 10)):

    gmm_models = [gmm(n_components=i, covariance_type='tied').fit(
        reshaped_img) for i in values]
    bic_values = [m.bic(reshaped_img) for m in gmm_models]

    return values, bic_values


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("path", help="Relative path to image file")

    args = parser.parse_args()

    img = cv2.imread(args.path).reshape((-1, 3))
    vals, bic_vals = get_bic(img)
    plt.plot(vals, bic_vals)
    plt.show()
