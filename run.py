import os
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--method', default='RCAN')
parser.add_argument('--scale', default=2)

opt = parser.parse_args()
print(opt)


if opt.method == 'RCAN':
	# Go to code directory
	os.system('cd methods/RCAN-EDSR-MDSR/code')

	# Check current environment
	curr_env = os.environ['CONDA_DEFAULT_ENV']

	if curr_env != 'SISR-1':
		print('ERROR: Please run conda activate SISR-1')
	else:
		print("##### RCAN allowed scales: 2,3,4,8 #####")
		subprocess.run("python main.py --data_test MyImage \
									   --scale {} --model RCAN \
									   --n_resgroups 10 --n_resblocks 20 --n_feats 64 \
									   --pre_train ../model/RCAN_BIX{}.pt \
									   --test_only --save_results --chop --self_ensemble --save 'RCANplus' \
									   --testpath ../../.. --testset input".format(opt.scale, opt.scale), shell=True, cwd='methods/RCAN-EDSR-MDSR/code')

elif opt.method == 'EDSR':
	# Go to code directory
	os.system('cd methods/RCAN-EDSR-MDSR/code')

	# Check current environment
	curr_env = os.environ['CONDA_DEFAULT_ENV']

	if curr_env != 'SISR-1':
		print('ERROR: Please run conda activate SISR-1')
	else:
		print("##### EDSR allowed scales: 2,3,4,8 #####")
		subprocess.run("python main.py --data_test MyImage \
									   --scale {} --model EDSR \
									   --pre_train ../model/EDSR_baseline_x{}.pt \
									   --test_only --save_results --chop \
									   --testpath ../../.. --testset input".format(opt.scale,opt.scale), shell=True, cwd='methods/RCAN-EDSR-MDSR/code')

elif opt.method == 'MDSR':
	# Go to code directory
	os.system('cd methods/RCAN-EDSR-MDSR/code')

	# Check current environment
	curr_env = os.environ['CONDA_DEFAULT_ENV']
	
	if curr_env != 'SISR-1':
		print('ERROR: Please run conda activate SISR-1')
	else:
		print("##### MDSR saving scales: 2,3,4 #####")
		subprocess.run("python main.py --data_test MyImage \
									   --scale 2+3+4 --model MDSR \
									   --pre_train ../model/MDSR_baseline.pt \
									   --test_only --save_results --chop \
									   --testpath ../../.. --testset input", shell=True, cwd='methods/RCAN-EDSR-MDSR/code')

elif opt.method == 'DBPN':
	# Go to code directory
	os.system('cd methods/DBPN')

	# Check current environment
	curr_env = os.environ['CONDA_DEFAULT_ENV']
	
	if curr_env != 'SISR-1':
		print('ERROR: Please run conda activate SISR-1')
	else:
		print("##### DBPN allowed scales: 2,4,8 #####")
		subprocess.run("python eval.py --input_dir '../../'\
									   --upscale_factor {}\
									   --model 'models/DBPN_x{}.pth'\
									   --test_dataset 'input/' --output '../../output'".format(opt.scale,opt.scale), shell=True, cwd='methods/DBPN')


else:
	print("##### No such method name #####")
	print("##### Please select from RCAN | EDSR | MDSR | DBPN #####")
