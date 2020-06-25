#!/bin/bash


## Setup environments

### SISR-1 ###
echo Creating SISR-1 environment...

conda create --name SISR-1 python=3.6 numpy

source ~/anaconda3/etc/profile.d/conda.sh
conda activate SISR-1

conda install matplotlib
conda install imageio
conda install -c anaconda scikit-image
conda install scipy=1.1.0
conda install -c conda-forge tqdm
pip install opencv-contrib-python

echo Now please install pytorch=0.4.0 and torchvision
echo e.g., conda install pytorch=0.4.0 cuda90 -c pytorch
echo e.g., conda install -c pytorch torchvision 


### PyTorch install
#conda install pytorch=0.4.0 cuda90 -c pytorch

### gdown install
#pip install gdown


## Setup pretrained model weights
#cd methods/RCAN/model
#gdown https://drive.google.com/uc?id=10bEK-NxVtOS9-XSeyOZyaRmxUTX3iIRa
#unzip models_ECCV2018RCAN.zip
#rm models_ECCV2018RCAN.zip

#mv ./models_ECCV2018RCAN/RCAN_BDX3.pt ./
#mv ./models_ECCV2018RCAN/RCAN_BIX2.pt ./
#mv ./models_ECCV2018RCAN/RCAN_BIX3.pt ./
#mv ./models_ECCV2018RCAN/RCAN_BIX4.pt ./
#mv ./models_ECCV2018RCAN/RCAN_BIX8.pt ./

#rm -r models_ECCV2018RCAN
#cd ../../..

















