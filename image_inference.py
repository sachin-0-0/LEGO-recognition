import cv2
import matplotlib.pyplot as plt
import numpy as np
import torch 
import torchvision.models as models

from image_training import FineTuneModel

cap = cv2.VideoCapture('/dev/video4')

# original_model = models.__dict__['alexnet'](pretrained=True)

from torchvision.models import AlexNet_Weights
original_model = models.__dict__['alexnet'](weights=AlexNet_Weights.IMAGENET1K_V1)


model = FineTuneModel(original_model, 'alexnet', 140)
model.features = torch.nn.DataParallel(model.features)
model.cuda()

checkpoint = torch.load('model_best.pth.tar')
model.load_state_dict(checkpoint['state_dict'])

while True:
    ret, frame = cap.read()

    # Preprocess the frame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (224, 224))  # Resize to match the model's input size
    frame = frame / 255.0  # Normalize pixel values
    frame = np.transpose(frame, (2, 0, 1))  # Transpose dimensions for PyTorch

    # Convert to PyTorch tensor
    frame_tensor = torch.tensor(frame, dtype=torch.float32)
    frame_tensor = frame_tensor.unsqueeze(0)  # Add batch dimension
    
    # Perform object recognition
    with torch.no_grad():
        output = model.forward(frame_tensor.cuda())
    _, predicted = torch.max(output.data, 1)
    
    
    # res = model(frame)

    res = model(frame_tensor.cuda())


    print(res)

    display_frame = np.transpose(frame, (1, 2, 0))

    plt.imshow(display_frame)
    plt.pause(0.5)

cap.release()
