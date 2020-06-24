import os
import sys
import pdb

import skimage.measure
import numpy as np
from PIL import Image

###### Vimeo ######

def save_vimeo_dain():
    path='../../output/Vimeo90k/superslomo/'
    output='../../output/Vimeo90k/superslomo-dbpn/'
    img_list = []

    dir_seq = os.listdir(path)
    dir_seq.sort()

    for sequence in dir_seq:
        imgs = os.listdir(path + sequence+'/')
        imgs.sort()

        for im in imgs:
            # OS operation
            os.system("python eval.py --input_dir {} --test_dataset {} --output {}".format(path, sequence+'/'+im, output))
            #pdb.set_trace()



###### Vid4 ######
def save_vid4_dain():
    path='../../output/Vid4/superslomo/'
    output='../../output/Vid4/superslomo-dbpn/'
    img_list = []

    dir_seq = os.listdir(path)
    dir_seq.sort()

    for sequence in dir_seq:
        #pdb.set_trace()
        os.system("python eval.py --input_dir {} --test_dataset {} --output {}".format(path, sequence+'/', output))



###### SPMCS ######
def save_spmcs_dain():
    path='../../output/SPMCS/superslomo/'
    output='../../output/SPMCS/superslomo-dbpn/'
    img_list = []

    dir_seq = os.listdir(path)
    dir_seq.sort()

    for sequence in dir_seq:
        #pdb.set_trace()
        os.system("python eval.py --input_dir {} --test_dataset {} --output {}".format(path, sequence+'/', output))
        #pdb.set_trace()






###### Vid4 ######
def save_vid4_first():
    path='../../data/Vid4/'
    output='../../output/Vid4/dbpn/'
    img_list = []

    dir_seq = os.listdir(path)
    dir_seq.sort()

    for sequence in dir_seq:
        #pdb.set_trace()
        os.system("python eval_resized.py --input_dir {} --test_dataset {} --output {}".format(path, sequence+'/', output))







###########################################################
if __name__ == '__main__':
    save_vid4_first()