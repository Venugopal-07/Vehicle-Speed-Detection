# Vehicle Speed Detection
### Master of Computer Applications Mini-Project

---

## Vehicle Speed Detection Using Python & OpenCV

### Project Description

This project demonstrates a **Vehicle Speed Detection System** using **Python and OpenCV**.  
It captures live video from a **laptop webcam**, detects moving objects, tracks their movement, and estimates their speed based on frame-to-frame displacement.

The project is developed for **academic learning and demonstration purposes** and is suitable for **MCA mini-project submission and GitHub portfolio**.

---

### Python Version Compatibility

This project is developed and tested with the following Python versions:

- **Python 3.11.x** – Recommended (most stable with OpenCV)
- **Python 3.12.1** – Supported with compatible libraries

> ⚠️ Important Notes:
> - NumPy **2.x is NOT supported**
> - Use **NumPy 1.26.4** for OpenCV compatibility

---

### Features

- Live webcam video capture  
- Moving object (vehicle/demo object) detection  
- Speed calculation (approximate)  
- Real-time speed display on video  
- **Automatic video recording**  
- **Resizable window**  
- **Supports laptop minimize, maximize, and all screen sizes**  
- **Fullscreen toggle using `F` key**  
- **Safe exit using `ESC` key with video save confirmation**  
- Clear on-screen instructions for user control  

---

### Technologies Used

- **Python 3.11 / 3.12.1**
- **OpenCV**
- **NumPy**

---

### Project Structure
```
Vehicle-Speed-Detection/
├── main.py
├── config.py
├── utils.py
├── speed_calculation.py
├── requirements.txt
└── README.md

```

---

### How It Works

- Webcam captures live video frames  
- Background subtraction detects moving objects  
- Object movement is tracked frame-by-frame  
- Speed is calculated using distance and time  
- Speed is displayed on the video output  
- Each frame is recorded and saved as a video file  
- Application window dynamically adjusts to laptop screen size  

---

### How to Run

1. Install Required Libraries

```
pip install -r requirements.txt

```
2. Run the Project
```
python main.py

```
### Application Controls

* When the camera window opens, the following controls are available:

*   F key → Toggle Fullscreen ON / OFF

*   ESC key → Close camera and save the recorded video

* These instructions are also displayed directly on the video screen for user convenience.

### Output

>Live video feed from webcam

> Bounding box around detected object

> Speed displayed in km/h (approximate)

> Recorded video saved automatically as:
```
recorded_output.mp4

```
### Note
* Speed values are approximate

* Webcam is used for demonstration only

* Real-world accuracy requires:

-   Fixed traffic cameras

-   Camera calibration

-   Known distance references

### Author
#### Venugopal Vallapaneni
#### MCA – Mini Project