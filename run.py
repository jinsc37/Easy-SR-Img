import os
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--method', default='RCAN')
parser.add_argument('--scale', default=2)
parser.add_argument('--in_path', default='./baby.png')

opt = parser.parse_args()
print(opt)



os.system('cd methods/RCAN-EDSR-MDSR/code')

if opt.method == 'RCAN':

	print("##### RCAN allowed scales: 2,3,4,8 #####")
	subprocess.run("python main.py --data_test MyImage \
								   --scale {} --model RCAN \
								   --n_resgroups 10 --n_resblocks 20 --n_feats 64 \
								   --pre_train ../model/RCAN_BIX{}.pt \
								   --test_only --save_results --chop --self_ensemble --save 'RCANplus' \
								   --testpath ../../.. --testset input".format(opt.scale, opt.scale), shell=True, cwd='methods/RCAN-EDSR-MDSR/code')


elif opt.method == 'EDSR':

	print("##### EDSR allowed scales: 2,3,4,8 #####")
	subprocess.run("python main.py --data_test MyImage \
								   --scale {} --model EDSR \
								   --pre_train ../model/EDSR_baseline_x{}.pt \
								   --test_only --save_results --chop \
								   --testpath ../../.. --testset input".format(opt.scale,opt.scale), shell=True, cwd='methods/RCAN-EDSR-MDSR/code')

elif opt.method == 'MDSR':

	print("##### MDSR saving scales: 2,3,4 #####")
	subprocess.run("python main.py --data_test MyImage \
								   --scale 2+3+4 --model MDSR \
								   --pre_train ../model/MDSR_baseline.pt \
								   --test_only --save_results --chop \
								   --testpath ../../.. --testset input", shell=True, cwd='methods/RCAN-EDSR-MDSR/code')

else:
	print("##### No such method name #####")
	print("##### Please select from RCAN | EDSR | MDSR #####")
