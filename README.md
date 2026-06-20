# Object Detection using OpenCV

A simple real-time face detection application built with Python and OpenCV. The application uses Haar Cascade Classifiers to detect human faces from a webcam feed and draws bounding boxes around detected faces.

## Features

* Real-time face detection using webcam
* Face detection using OpenCV Haar Cascades
* Bounding box visualization
* Detection label display
* Modular code structure with helper functions

## Requirements

* Python 3.8+
* Webcam
* OpenCV

## Installation

### Clone the Repository

```bash
git clone https://github.com/shaikhyakubhossain/object-detection.git
cd object-detection
```

### Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python main.py
```

A webcam window will open and detected faces will be highlighted with a green rectangle.

## Controls

| Key | Action           |
| --- | ---------------- |
| Q   | Quit Application |

## How It Works

1. Captures video frames from the webcam.
2. Converts each frame to grayscale.
3. Uses OpenCV's Haar Cascade face detector.
4. Detects faces in real time.
5. Draws bounding boxes and labels around detected faces.
6. Displays the processed video stream.

## Technologies Used

* Python
* OpenCV
* NumPy

## Future Improvements

* Eye detection
* Smile detection
* Multiple object detection
* YOLOv8 integration
* Image upload support
* Web-based interface using Flask/FastAPI
* Confidence score display

## License

This project is licensed under the MIT License. See the LICENSE file for details.
