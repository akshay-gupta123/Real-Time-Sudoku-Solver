import numpy as np
import cv2
import joblib
import os
import torch
from torchvision import transforms
from classification.model.cnn import Net

device = torch.device("cpu")
model_path = os.path.join(os.getcwd(),"classfication","model","mnist_cnn.pt")

model = Net().to(device)
model.load_state_dict(torch.load(model_path,map_location=device))
model.eval()


transform=transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
    ])

# Digits array contains digits of grid in column major order
def predictDigits(digits: np.ndarray):
    assert (len(digits) == 81)
    res = ""
    for i in range(9):
        for j in range(9):
            digit = predictDigit(digits[j*9 + i])
            res += str(digit)
    return res
    #return "009000780830019000610000403001900027000040000590008300905000072000590048082000900"


def predictDigit(digit: np.ndarray):
    # Less than 10 pixels coloured
    if np.sum(digit) < 10*255:
        return 0
    
    processed_digit = transform(digit).permute(0,1,2).unsqueeze(0)
    with torch.no_grad():
        
        prob = model(processed_digit)
        prob2 = prob[0].cpu().numpy()
    return np.argmax(prob2)
