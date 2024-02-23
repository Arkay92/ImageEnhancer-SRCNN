# ImageEnhancer-SRCNN

Welcome to the ImageEnhancer-SRCNN repository. This project leverages the power of Super-Resolution Convolutional Neural Networks (SRCNN) to enhance and upscale images. Built with TensorFlow and Flask, it provides an easy-to-use web interface for upscaling images with state-of-the-art deep learning techniques.

## Features
Image upscaling via a pre-trained SRCNN model
Simple web interface to upload and upscale images
Option to download upscaled images or receive them as base64 encoded strings
Detailed error handling for robust user experience

## Installation
To get started with ImageEnhancer-SRCNN, follow these installation steps:

## Clone the repository:
```
git clone https://github.com/Arkay92/ImageEnhancer-SRCNN.git
cd ImageEnhancer-SRCNN
```

## Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage
To run the application, execute the following command from the project's root directory:

```
python main.py
```

## Upscaling Images
Send a POST request to http://localhost:5000/upscale with the following JSON payload:
```
{
  "image_path": "path/to/your/image.jpg",
  "save_to_file": true
}
image_path: Relative or absolute path to the image you want to upscale.
save_to_file: Set to true if you want the upscaled image saved to a file, or false to receive a base64 encoded string.
```

## Response
The response will be a JSON object containing either the path to the upscaled image or the base64 encoded string of the upscaled image, based on your request.

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestions that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

## Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request

## License
Distributed under the MIT License. See LICENSE for more information.

## Contact
Robert McMenemy - @Arkay92
Project Link: https://github.com/Arkay92/ImageEnhancer-SRCNN
