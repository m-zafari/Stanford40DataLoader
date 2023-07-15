import os
from torchvision import transforms, datasets
import torch.utils.data as data
import torch

def loader_creator(batch_size, data_dir, data):
    data_dir = os.path.join(data_dir, data)
    
    n_class = 40
    image_size = 224
    
    transform_train = transforms.Compose(
        [transforms.RandomResizedCrop(224), transforms.RandomHorizontalFlip(), transforms.ToTensor(),
         transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)), ])

    transform_test = transforms.Compose([transforms.Resize(256), transforms.CenterCrop(224),
        transforms.ToTensor(), transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)), ])

    trainset = datasets.ImageFolder(root=os.path.join(data_dir, 'train'), transform=transform_train)
    testset = datasets.ImageFolder(root=os.path.join(data_dir, 'valid'), transform=transform_test)

    train_loader = torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=True,
                                               num_workers=4, pin_memory=True)
    test_loader = torch.utils.data.DataLoader(testset, batch_size=batch_size, shuffle=False, pin_memory=True,
                                              num_workers=2)
    return train_loader, test_loader, n_class, image_size
