# Easy-SR-Img
This respository allows an easy deployment of Single Image Super Resolution (SISR) on custom images.

Supported algorithms are
- RCAN: ECCV 2018 from [yulunzhang/RCAN](https://github.com/yulunzhang/RCAN)
- EDSR: CVPRW 2017 from [thstkdgus35/EDSR](https://github.com/thstkdgus35/EDSR-PyTorch)
- MDSR: CVPRW 2017 also from [thstkdgus35/EDSR](https://github.com/thstkdgus35/EDSR-PyTorch)
- DBPN: CVPR 2018 from [alterzero/DBPN](https://github.com/alterzero/DBPN-Pytorch)

## Motivation
Isn't it just so tedious to run all the SISR algorithms for your research?
Maybe you want to try out a couple of SR methods for your personal photographs, yet to find that the released codes have different environments, dependencies, settings, data configurations and not exactly configured for custom images (or datasets).
You just want to quickly try some methods out, but it's such a pain in the neck configuring all of them to your personal needs.

This `Easy-SR-Img` project allows you (and me) of avoiding all the fuss.

For several state-of-the-art SR algorithms, `Easy-SR-Img` automatically creates and configures all of the different environments, while applying each of the different SR algorithms to a custom image(s) boils down to a single crisp command-line.

## Setup
We provide a shell script installing the appropriate packages and environments for running the SR algorithms via `conda` (which can be obtained by installing [Anaconda](https://www.anaconda.com/)).

For each supported algorithm, we provide different environment setups which only need to be run once.

Please take the following steps: 
1. `cd Easy-SR-Img`
2. `bash setup.sh`
3. `conda activate Easy-SR-1`
4. Install PyTorch, e.g., `conda install pytorch=0.4.0 cuda90 -c pytorch`
5. Install torchvision e.g., `conda install -c pytorch torchvision`

After that, just run the commands for an algorithm.
The run code will automatically set the appropriate environment for each algorithm execution.

The shell script will also automatically save required pretrained model weights.

### Environment details
The algorithm (environment-name) was originally tested with: 
- RCAN (Easy-SR-1): `python>=3.6`, `torch>=0.4.0`, `CUDA>=8.0`, `cuDNN>=5.1`
- EDSR (Easy-SR-1): `python>=3.6`, `torch>=0.4.0`, `scipy==1.1.0`, `CUDA>=8.0`, `cuDNN>=5.1`
- MDSR (Easy-SR-1): `python>=3.6`, `torch>=0.4.0`, `scipy==1.1.0`, `CUDA>=8.0`, `cuDNN>=5.1`
- DBPN (Easy-SR-1): `python>=3.5`, `torch>=1.0.0`, `opencv-contrib-python==4.2.0.34`

## Execution
Place all of the images you want to test in the `input` folder.
the results will appear in the `output` folder named as `<image-name>_<method-name>_x<scale>`, e.g., `image_EDSR_x4.png`.

The following are the command-line executions:

```bash
# RCAN with scales 2,3,4,8
python run.py --method RCAN --scale 2
python run.py --method RCAN --scale 3
python run.py --method RCAN --scale 4
python run.py --method RCAN --scale 8

# EDSR with scales 2,3,4,8
python run.py --method EDSR --scale 2
python run.py --method EDSR --scale 3
python run.py --method EDSR --scale 4
python run.py --method EDSR --scale 8

# MDSR running multi-scale 2,3,4
python run.py --method MDSR

# DBPN with scales 2,4,8
python run.py --method DBPN --scale 2
python run.py --method DBPN --scale 4
python run.py --method DBPN --scale 8
```

## License
The provided implementation is strictly for nonprofit purposes only. 
The copyright of the individual algorithms provided in this project belong to the respective authors.