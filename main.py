import argparse
from dataFolderCreator import *
from dataset import *

def main():
    parser = argparse.ArgumentParser()
    # data
    parser.add_argument('--data_src', default=r'D:\Stanford40-DataSet')
    parser.add_argument('--data_dst', default=r'D:\Image')
    parser.add_argument('--data', default='Stanfor40')
    parser.add_argument('--batch_size', default=64, type=int)
    
    args = parser.parse_args()

    folderCreator(args.data_src, args.data_dst)

    train_loader, test_loader, num_classes, image_size = loader_creator(args.batch_size, args.data_dst, args.data)

if __name__ == '__main__':
    main()
