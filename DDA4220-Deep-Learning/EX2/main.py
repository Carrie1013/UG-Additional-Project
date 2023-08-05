import torch
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torch.optim as optim
from torch.optim.lr_scheduler import StepLR
import torch.nn as nn
from torch.utils.data import DataLoader

import os

# This is a quite simple CNN with 3 convolutional layers
class SimpleCNN(nn.Module):
    def __init__(self, num_classes=5):
        super().__init__()
        # the first layer of the CNN
        self.conv1 = nn.Sequential(
            nn.Conv2d(3, 64, 7, stride=1),
            nn.ReLU(inplace=True),
            nn.BatchNorm2d(64), # 为提高模型精确性，此处在conv层加入batchnorm层
            nn.MaxPool2d(2, 2)
        )
        # the second layer of the CNN
        self.conv2 = nn.Sequential(
            nn.Conv2d(64, 128, 5, stride=2, padding=2),
            nn.ReLU(inplace=True),
            nn.BatchNorm2d(128), # 为提高模型精确性，此处在conv层加入batchnorm层
            nn.MaxPool2d(2, 2)
        )
        self.conv3 = nn.Sequential(
            # GRADED FUNCTION: Please define the third layer of the CNN. 
            # Conv2D with 128 5x5 filters and stride of 2
            # ReLU
            # MaxPool2d with 2x2 filters and stride of 2
            ### START SOLUTION HERE ###
            nn.Conv2d(128, 256, 5, stride=2, padding=2), #out_channels应为128，此模型为下一层修改为了256
            nn.ReLU(inplace=True),
            nn.BatchNorm2d(256), # 增加了batchnorm层
            nn.MaxPool2d(2, 2)
            ### END SOLUTION HERE ###
        )
        self.conv4 = nn.Sequential(
            nn.Conv2d(in_channels=256, out_channels=512, kernel_size=3),
            nn.ReLU(inplace=True),
            nn.BatchNorm2d(512),
            nn.MaxPool2d(2, 2)
        )
        self.avgpool = nn.AdaptiveAvgPool2d(1) # 增加了一层卷积并且最后使用了adaptive avgpool

        self.classifier = nn.Sequential(
            # GRADED FUNCTION: Please define the classifier
            # Linear with input size of 128 x width? x height? and output size of 4096
            # ReLU
            # Linear with input size of 4096 and output size of 4096
            # ReLU
            # Linear with input size of 4096 and output size of number of classes
            ### START SOLUTION HERE ###
            # （由于增加avgpool后，input由n*w*h改变为1dim）
            nn.Linear(512, 4096),
            nn.Dropout(0.4), # 层间添加drpout防止过拟合
            nn.ReLU(inplace=True),
            nn.Dropout(0.4),
            nn.Linear(4096, 4096),
            nn.Dropout(0.4),
            nn.ReLU(inplace=True),
            nn.Dropout(0.4),
            nn.Linear(4096, 256), # 4096与最后的5class相差较大所以改为逐渐降低
            nn.Dropout(0.4),
            nn.ReLU(inplace=True),
            nn.Dropout(0.4),
            nn.Linear(256, num_classes)

            ### END SOLUTION HERE ###
            ### 最后提交的模型由以下classifier层得到 ###
            # nn.Linear(512, 800),
            # nn.Dropout(0.4),
            # nn.ReLU(inplace=True),
            # nn.Dropout(0.4),
            # nn.Linear(800, 400),
            # nn.Dropout(0.4),
            # nn.ReLU(inplace=True),
            # nn.Dropout(0.4),
            # nn.Linear(400, num_classes)
        )

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        # GRADED FUNCTION: Flatten Layer
        ### START SOLUTION HERE ###
        x = self.conv4(x)
        x = torch.flatten(
            self.avgpool(x),1
        )
        ### END SOLUTION HERE ###
        x = self.classifier(x)
        return x

def train(train_loader, model, loss_fn, optimizer, device):
    for i, (image, annotation) in enumerate(train_loader):
        # move data to the same device as model
        image = image.to(device)
        annotation = annotation.to(device)

        # zero the parameter gradients
        optimizer.zero_grad()
        # forward and compute prediction error
        output = model(image)
        loss = loss_fn(output, annotation)
        # backward + optimize
        loss.backward()
        optimizer.step()

        # print statistics
        if i % 20 == 0:    # print every 20 iterates
            print(f'iterate {i + 1}: loss={loss:>7f}')

def val(val_loader, model, device):
    # switch to evaluate mode
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for i, (image, annotation) in enumerate(val_loader):
            # move data to the same device as model
            image = image.to(device)
            annotation = annotation.to(device)

            # network forward
            output = model(image)

            # for compute accuracy
            _, predicted = torch.max(output.data, 1)
            total += annotation.size(0)
            correct += (predicted == annotation).sum().item()

    # GRADED FUNCTION: calculate the accuracy using variables before
    # use variable named 'acc' to store the accuracy
    ### START SOLUTION HERE ###
    acc = correct / total
    ### END SOLUTION HERE ###
    print(f'total val accuracy: {100 * acc:>2f} %')
    return acc


if __name__ == '__main__':
    # define image transform
    transform = transforms.Compose([
                    transforms.RandomResizedCrop(224),
                    transforms.RandomHorizontalFlip(),
                    transforms.ToTensor(),
                    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                         std=[0.229, 0.224, 0.225]),
                    ])
    batch_size = 128 # 本solution中将batch size由64改为128

    # loda data
    traindir = os.path.join('./EX2/flower_dataset', 'train')
    valdir = os.path.join('./EX2/flower_dataset', 'val')    
    # GRADED FUNCTION: define train_loader and val_loader
    ### START SOLUTION HERE ###
    train_dataset = datasets.ImageFolder(traindir, transform)
    val_dataset = datasets.ImageFolder(valdir, transform)

    train_loader = DataLoader(train_dataset, batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size, shuffle=True)

    ### END SOLUTION HERE ###

    # device used to train
    device = torch.device("cuda:0")
    # GRADED FUNCTION: define a SimpleCNN model and move it to the device
    # use variable named 'model' to store this model
    ### START SOLUTION HERE ###
    device = torch.device("cuda:0")
    model = SimpleCNN().to(device)
    ### END SOLUTION HERE ###

    # Classification Cross-Entropy loss 
    loss_fn = nn.CrossEntropyLoss()

    # GRADED FUNCTION: Please define the optimizer as SGD with lr=0.05, momentum=0.9, weight_decay=0.0001
    ### START SOLUTION HERE ###
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.90, weight_decay=0.0001) #此处修改learing rate为0.01
    ### END SOLUTION HERE ###

    # GRADED FUNCTION: Please define the scheduler
    # the learning rate will decay 0.05 every 5 steps
    ### START SOLUTION HERE ###
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer=optimizer, T_max=50) # 本solution改为表现更好的Cosine scheduler
    ### END SOLUTION HERE ###

    # create model save path
    os.makedirs('work_dir', exist_ok=True)

    max_acc = -float('inf')
    for epoch in range(50): #增加到50
        print('-' * 30, 'epoch', epoch + 1, '-' * 30)

        # train
        train(train_loader, model, loss_fn, optimizer, device)
        print('lr: {}'.format(optimizer.param_groups[0]['lr']))

        # validation
        acc = val(val_loader, model, device)

        # save best model
        if acc > max_acc:
            pt_path = os.path.join('work_dir', 'best.pt')
            torch.save(model.state_dict(), pt_path)
            print('save model')
            max_acc = acc

        # decay learning rate
        scheduler.step()
    print('Finished Training')