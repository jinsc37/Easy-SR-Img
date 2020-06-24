import time
import os
import sys
import argparse

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torch.autograd import Variable
import torchvision.transforms as transforms
import torch.nn.functional as F

import math
import random
import numpy as np
import numpy
from PIL import Image

from scipy.misc import imread, imsave
import skimage.measure

from models.models3 import FullNet
#from utils import Logger
import datasets
from datasets import Vimeo90K_test_triplet, Vid4_test_triplet, SPMCS_test_triplet, SPMCS_comp_triplet, SPMCS_blur_triplet

import pdb

#CUDA_VISIBLE_DEVICES=0,1 python test_vimeo_tri.py

class AverageMeter(object):
    """Computes and stores the average and current value"""
    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val):
        self.val = val
        self.sum += val
        self.count += 1.0
        self.avg = self.sum / self.count



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



def test_vimeo_tri(model=FullNet(), model_dict='./trained_models/FullNet_v3.pth'):
    torch.backends.cudnn.benchmark = True # to speed up
    PIXEL_MAX = 255.0

    ### Assign model
    model = model
    model = model.cuda()
    model = nn.DataParallel(model)
    model = model.eval() # deploy mode
    model.load_state_dict(torch.load(model_dict))

    ### Keep track of metric average
    interp_error = AverageMeter()
    psnr_error = AverageMeter()
    ssim_error = AverageMeter()

    ### Input & target memory allocation (otherwise memory will accumulate?)
    Tensor = torch.cuda.FloatTensor  # define a tensor data structure

    #input_f1 = Tensor(1, 3, 256, 448)
    #input_f2 = Tensor(1, 3, 256, 448)
    #input_f3 = Tensor(1, 3, 256, 448)

    ### Dataset loader
    composed = transforms.Compose([ datasets.ToTensor_tri() ]) # Order of ToTensor important!
    dataloader = DataLoader(Vimeo90K_test_triplet(transform=composed), 
                        batch_size=1, shuffle=False, num_workers=4)

    with torch.no_grad():
        for i, batch in enumerate(dataloader):
            ### Set model input
            f1 = Variable(batch['frame1'], requires_grad=False)
            f2 = Variable(batch['frame2'], requires_grad=False)
            f3 = Variable(batch['frame3'], requires_grad=False)

            ### Test FullNet #########################################
            f1 = F.interpolate(f1, scale_factor=0.25, mode='bilinear', align_corners=False)
            f3 = F.interpolate(f3, scale_factor=0.25, mode='bilinear', align_corners=False)

            fset = Tensor(f1.size(0), 2, f1.size(1), f1.size(2), f1.size(3))
            fset[:,0,:,:,:] = f1
            fset[:,1,:,:,:] = f3
            #tic = time.time()
            f2_hat = model(fset)
            #tic = time.time()

            fr_out = (f2_hat.squeeze().cpu().permute(1,2,0).numpy()*255).round().astype(numpy.uint8)
            fr_mid = (f2.squeeze().cpu().permute(1,2,0).numpy()*255).round().astype(numpy.uint8)

            ### Compute metrics

            # IE
            diff_rgb = 128.0 + fr_out - fr_mid
            avg_interp_error_abs = np.mean(np.abs(diff_rgb - 128.0))
            interp_error.update(avg_interp_error_abs)

            # PSNR
            psnr_error.update(psnr(fr_mid, fr_out))

            # SSIM
            ssim_error.update(ssim(fr_mid, fr_out))


            sys.stdout.write('\r[' + str(i+1) + '/3782] IE: ' + str(round(interp_error.avg,4)) + ' | PSNR: ' + str(round(psnr_error.avg,4)) + ' | SSIM: ' + str(round(ssim_error.avg,4)))
            sys.stdout.flush()

    print("\nAverage IE: " + str(round(interp_error.avg,4)))
    print("Average PSNR: " + str(round(psnr_error.avg,4)))
    print("Average SSIM: " + str(round(ssim_error.avg,4)))





if __name__ == '__main__':

    test_vimeo_tri()