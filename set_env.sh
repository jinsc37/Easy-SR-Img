#!/bin/bash

# RCAN

## Setup environments
conda create --name Easy-SR-RCAN python=3.6 numpy
conda activate Easy-SR-RCAN

conda install matplotlib
conda install imageio
conda install -c anaconda scikit-image
conda install -c pytorch torchvision 
conda install scipy=1.1.0

### PyTorch install
conda install pytorch=0.4.0 cuda90 -c pytorch

### gdown install
pip install gdown


## Setup pretrained model weights
cd methods/RCAN/model
gdown https://drive.google.com/uc?id=10bEK-NxVtOS9-XSeyOZyaRmxUTX3iIRa
unzip models_ECCV2018RCAN.zip
rm models_ECCV2018RCAN.zip

mv ./models_ECCV2018RCAN/RCAN_BDX3.pt ./
mv ./models_ECCV2018RCAN/RCAN_BIX2.pt ./
mv ./models_ECCV2018RCAN/RCAN_BIX3.pt ./
mv ./models_ECCV2018RCAN/RCAN_BIX4.pt ./
mv ./models_ECCV2018RCAN/RCAN_BIX8.pt ./

rm -r models_ECCV2018RCAN

cd ../../..

















