# Vehicle Speed Detection
#### Master of Computer Applications Mini-Project...


### Vehicle Speed Detection Using Python & OpenCV
===================================================
#### Project Description

##### This project demonstrates a Vehicle Speed Detection System using Python and OpenCV.
##### It captures live video from a laptop webcam, detects moving objects, and estimates their speed based on movement between frames.

##### The project is developed for academic learning and demonstration purposes.

### Features

* Live webcam video capture

* Moving object detection

* Speed calculation (approximate)

* Real-time speed display

* Video recording support

* Safe exit using ESC key

### Technologies Used

* Python 3

* OpenCV

* NumPy

### Project Structure
```
Vehicle_Speed_Detection/
├── main.py
├── config.py
├── utils.py
├── speed_calculation.py
├── requirements.txt
└── README.md
```

### How It Works

* Webcam captures live video frames

* Moving objects are detected using background subtraction

* Object movement is tracked frame-by-frame

* Speed is calculated using distance and time

* Speed is displayed on the video output

1. How to Run
```
Install required libraries:

pip install -r requirements.txt

```

2. Run the project:
```
python main.py

```

3. Webcam opens and shows live video

4. Press ESC to close the application

### Output

> Live video feed

> Bounding box on detected object

> Speed displayed in km/h (approximate)

> Recorded video saved automatically

### Note

* Speed values are approximate

* Webcam is used for demonstration only

* Real-world accuracy requires calibrated traffic cameras

### Author

#### Venugopal Vallapaneni
#### MCA Mini Project
