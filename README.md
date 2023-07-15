# Stanford40DataLoader
this code create dataloader from stanford40 source file
Show, Attend and Distill: Knowledge Distillation via Attention-based Feature Matching
Official pytorch implementation of "Show, Attend and Distill: Knowledge Distillation via Attention-based Feature Matching" (AAAI-2021)

# Requirements
Python3 \n
PyTorch (> 1.2.0) \n
torchvision
numpy

from this link download all files
http://vision.stanford.edu/Datasets/40actions.html

then give the extracted folder path as data_src and give a destination path for load data as data_dst
program create a folder named Stanford40 in data_dst path that included train and valid folders for creating dataLoader with dataset.py
for example:

python main.py --data_src D:\Stanford40-DataSet --data_dst D:\Image --data Stanford40 --batch_size 64
# run
Run main.py to create the dataloders.

python main.py --data_src PATH_TO_DATA --data_dst PATH_TO_DATA --data Stanford40 --batch_size 64
