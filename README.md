# Pre-trained Image Classifier for Dog Breed Identification

<br><br>This repository contains a pre-trained image classifier implemented in Python, capable of identifying dog breeds using Convolutional Neural Networks (CNNs). The project uses three different CNN architectures: AlexNet, VGG, and ResNet, each with unique structures and capabilities.
<br><br><br><br>

## Overview
The classifier is designed to classify images into different dog breeds and determine if an image contains a dog or not. It utilizes the following components:

- ***Dog Breed Classifier:*** The core of the project, using pre-trained CNN models to classify dog breeds from input images.
- **Dog Detector:** Determines whether an image contains a dog or not.
- **Image Preprocessing:** Includes image normalization, resizing, and transformation to ensure compatibility with the CNN models.
- **Results Analysis**: Evaluates the classifier's performance, calculating various statistics such as accuracy, correct matches, and misclassifications.

1. Clone the repository to your local machine:  
`git clone https://github.com/DJRoche509/Pre-trained-Image-Classifier-to-Identify-Dog-Breeds.git`
2. Navigate to the project directory:
`cd Pre-trained-Image-Classifier-to-Identify-Dog-Breeds`
3. Install the required packages:
 `pip install -r requirements.txt`
<br><br>

### Instructions
1. Testing the Classifier:
- Use test_classifier.py to test the classifier's performance on a set of images.
`python test_classifier.py`
- The results will be displayed, showing accuracy, correct matches, and misclassifications.
2. Using the Classifier:
- Save local dog images in the repository titled `uploaded_images`. Then, use the provided functions to classify dog breeds in your own Python applications.
- In your terminal, run the following shell script command:
`
sh run_models_batch_uploaded.sh
`  
- Next, see the result in the following text files, "resnet_uploaded-images.txt", "alexnet_uploaded-images.txt", and "vgg_uploaded-images.txt", in the main local repository.
  - **resnet_uploaded-images.txt** - that contains the results using CNN model architecture ResNet
  - **alexnet_uploaded-images.txt** - that contains the results using CNN model architecture AlexNet
  - **vgg_uploaded-images.txt** - that contains the results using CNN model architecture VGG
    
  <br/>
  Here is an excerpt from <strong><em>alexnet_uploaded-images.txt</em></strong> after running the shell command shown above. <br/>

  ![image](https://github.com/DJRoche509/Pre-trained-Image-Classifier-to-Identify-Dog-Breeds/assets/100164051/6a3364b4-5ee6-4ce8-adbe-e765fa7ab5dc)


  <br>

  Running the main class file, <strong><em>check_images.py</em></strong>, in cmd as `python3 check_images.py` should result similarly to the image below: <br/>
  
  ![image](https://github.com/DJRoche509/Pre-trained-Image-Classifier-to-Identify-Dog-Breeds/assets/100164051/17dad239-c43f-4604-9a7a-9a901a9b8afe)


## CNN Architectures
### AlexNet
AlexNet is a deep CNN architecture designed for large-scale visual recognition tasks. It consists of five convolutional layers followed by three fully connected layers. To use AlexNet in the classifier, provide `--arch alexnet` as a command line argument.

### VGG
VGG (Visual Geometry Group) is a CNN architecture known for its simplicity and depth. It uses 3x3 convolutional layers throughout the architecture. To use VGG in the classifier, provide `--arch vgg` as a command line argument.

### ResNet
ResNet (Residual Neural Network) is a CNN architecture designed to handle the vanishing gradient problem in deep networks. It utilizes residual connections to allow gradients to flow easily during training. To use ResNet in the classifier, provide `--arch resnet` as a command line argument.
<br><br>

## Contributing
Feel free to contribute to this project by opening issues for bugs or feature requests. Pull requests are also welcome.

<br/> <br/>
![image](https://github.com/DJRoche509/Pre-trained-Image-Classifier-to-Identify-Dog-Breeds/assets/100164051/3fb67e35-4e43-46f4-be6e-81f86931f6bb)
