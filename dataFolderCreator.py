import os
import shutil

def folderCreator(src_path: str, dst_path: str):
    os.mkdir(os.path.join(dst_path, "stanford40"))
    dst_path = os.path.join(dst_path, "stanford40")
    os.mkdir(os.path.join(dst_path, "train"))
    os.mkdir(os.path.join(dst_path, "valid"))    
    actions_dir = os.path.join(src_path, 'ImageSplits\\actions.txt')
    
    #read labels with actions.txt
    labels = list()
    with open(actions_dir, "r") as ac:
        ac.readline()   # first line is not needed 
                        # line0 = "action_name			number_of_images"
        
        while True:
            line = ac.readline()
            if line == '':
                break # end of file
            labels.append(line.split()[0])
            os.mkdir(os.path.join(dst_path, "train", line.split()[0]))
            os.mkdir(os.path.join(dst_path, "valid", line.split()[0]))
    
    #fill folder train and valid with proper image
    for label in labels:
        label_train = label + "_train.txt"
        label_test = label + "_test.txt"

        train_label_list = os.path.join(src_path, "ImageSplits", label_train)
        move2folder(train_label_list, src_path, dst_path, train = True)

        test_label_list = os.path.join(src_path, "ImageSplits", label_test)
        move2folder(test_label_list, src_path, dst_path, train = False)

# move files in label_list from src to dst
def move2folder(label_list, src, dst, train : bool):
    with open(label_list, "r") as lines:
            
            if train == True:
                dst = os.path.join(dst, "train")
            else:
                dst = os.path.join(dst, "valid")
            
            while True:
                line = lines.readline()
                if line == '':
                    break # end of file
                src0 = os.path.join(src, "JPEGImages", line[:-1])
                dst0 = os.path.join(dst, line[:-9], line[:-1])

                shutil.copyfile(src0, dst0)