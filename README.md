# Easy-SR-Img: Image Super-Resolution Algorithm
This respository allows an easy deployment of Single Image Super Resolution (SISR) on custom images.

Supported algorithms are
- RCAN: ECCV 2018 from [yulunzhang/RCAN](https://github.com/yulunzhang/RCAN)
- EDSR: CVPRW 2017 from [thstkdgus35/EDSR](https://github.com/thstkdgus35/EDSR-PyTorch)
- MDSR: CVPRW 2017 also from [thstkdgus35/EDSR](https://github.com/thstkdgus35/EDSR-PyTorch)
- DBPN

## Motivation
Isn't it just so tedious to run all the SISR algorithms for your research?
Maybe you want to try out a couple of SR methods for your personal photographs, yet to find that the released codes have different environments, dependencies, settings, data configurations and not exactly configured for custom images (or datasets).
We just wanted to quickly try some methods out, but it's such a pain in the neck configuring all them to your personal needs.

This `Easy-SR-Img` project allows you (and me) of avoiding all the fuss.

For several state-of-the-art SR algorithms, `Easy-SR-Img` automatically creates and configures all the different environments, while applying each of the different SR algorithms to a custom image(s) boils down to a single crisp command-line.

## Setup
We provide a shell script installing the appropriate packages and environments for running the SR algorithms via `conda` (which can be obtained by installing [Anaconda](https://www.anaconda.com/)).

For each supported algorithm, we provide different environments which only need to be run once via:

```bash
sh set_env.sh
```

After that, just run the commands for an algorithm.
The run code will automatically set the appropriate environment for execution.

The shell script will also automatically save required pretrained model weights.

### Environment details
The code (environment-name) was originally tested with: 
- RCAN (Easy-SR-RCAN): `python>=3.6`, `torch>=0.4.0`, `CUDA>=8.0`, `cuDNN>=5.1`
- EDSR (Easy-SR-RCAN): `python>=3.6`, `torch>=0.4.0`, `scipy==1.1.0`, `CUDA>=8.0`, `cuDNN>=5.1`
- MDSR (Easy-SR-RCAN): `python>=3.6`, `torch>=0.4.0`, `scipy==1.1.0`, `CUDA>=8.0`, `cuDNN>=5.1`

## Execution
The following are the command-line executions:

can process all images in a directory, for multiple or nested directories, execute this code accordingly. 


```bash
# RCAN+
# RCANplus_BIX2
python main.py --data_test MyImage --scale 2 --model RCAN --n_resgroups 10 --n_resblocks 20 --n_feats 64 --pre_train ../model/RCAN_BIX2.pt --test_only --save_results --chop --self_ensemble --save 'RCANplus' --testpath ../LR/LRBI --testset Set5
# RCANplus_BIX3
```



## License
The provided implementation is strictly for nonprofit purposes only. 
The copyright of the individual algorithms provided in this project belong to the respective authors.