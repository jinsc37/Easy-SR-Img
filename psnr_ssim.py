import numpy as np
import numpy
from PIL import Image

from scipy.misc import imread, imsave



def psnr(img_orig, img_out, peak=255):
    mse = np.mean(np.square(img_orig - img_out))
    psnr = 10 * np.log10(peak*peak / mse)
    return psnr


def ssim(img1, img2):
    """Return the Structural Similarity Map corresponding to input images img1 
    and img2 (images are assumed to be uint8)
    
    This function attempts to mimic precisely the functionality of ssim.m a 
    MATLAB provided by the author's of SSIM
    https://ece.uwaterloo.ca/~z70wang/research/ssim/ssim_index.m
    """
    rgb_weights = [0.2989, 0.5870, 0.1140]
    img1 = np.dot(img1, rgb_weights)
    img2 = np.dot(img2, rgb_weights)

    K1 = 0.01
    K2 = 0.03
    L = 255 #bitdepth of image

    C1 = (K1*L)**2
    C2 = (K2*L)**2

    mu1 = np.mean(img1)
    mu2 = np.mean(img2)
    mu1_sq = mu1*mu1
    mu2_sq = mu2*mu2
    mu1_mu2 = mu1*mu2

    sigma1_sq = np.mean(img1*img1) - mu1_sq
    sigma2_sq = np.mean(img2*img2) - mu2_sq
    sigma12 = np.mean(img1*img2) - mu1_mu2

    return ((2*mu1_mu2 + C1)*(2*sigma12 + C2))/((mu1_sq + mu2_sq + C1)*
            (sigma1_sq + sigma2_sq + C2))





if __name__ == '__main__':

    path_out = 'output/baby_EDSR_x2.png'
    path_gt = 'input/baby_x4.png'

    output = imread(path_out)
    GT = imread(path_gt)

    print(psnr(GT, output))
    print(ssim(GT, output))