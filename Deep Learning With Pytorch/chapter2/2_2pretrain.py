from torchvision import models

dir(models)

alexnet=models.AlexNet()
resnet=models.resnet101(pretrained=True)

print(resnet)

from torchvision import transforms

preprocess=transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrops(224),
    transforms.ToTensor(),
    transforms.Nomalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )])

from PIL import Image
img=Image.open("../data/p1ch2/bobby.jpg")