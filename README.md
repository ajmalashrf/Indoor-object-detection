# Indoor Object Detection System for Visually Impaired Assistance

This repository contains a starter implementation of an AI-powered assistive system that helps visually impaired users understand indoor environments. The project combines real-time object detection, spoken alerts, and a browser-based interface for monitoring detections.

## Features

- Real-time webcam/video-frame processing through a Flask application.
- YOLO-based object detection using the `ultralytics` package.
- Audio feedback engine with throttled spoken alerts for detected indoor objects.
- Modular architecture to swap in a custom fine-tuned model later.
- Simple responsive dashboard for live status and detection summaries.
- Deployment-friendly structure for local development or cloud hosting.

## Project Structure

```text
.
├── app.py
├── detector.py
├── audio_feedback.py
├── config.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── css/styles.css
│   └── js/app.js
├── docs/
│   └── project_workflow.md
└── notebooks/
    └── dataset_preparation_template.ipynb
```

## Workflow

Dataset Collection → Image Preprocessing → Object Detection Model Training → Model Evaluation → Real-time Camera Detection → Audio Alert Integration → Web Application Development → Model Integration → Application Deployment

## Recommended Tech Stack

- **Python** for the application and model integration.
- **OpenCV** for video capture and frame annotation.
- **YOLO / Ultralytics** for object detection.
- **NumPy / Pandas** for preprocessing and analytics.
- **pyttsx3 / gTTS** for optional voice alerts.
- **Flask** for the web interface and streaming.
- **HTML / CSS / JavaScript** for the frontend.
- **Render / Streamlit Cloud** for deployment.

## Dataset Sources

You can build or fine-tune the object detector using datasets from:

- Kaggle (search for indoor object detection datasets)
- COCO Dataset
- Open Images Dataset

## Getting Started

### 1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## Model Notes

- By default the app expects a YOLO model that can be loaded by `ultralytics.YOLO`.
- You can point to a custom model using the `MODEL_PATH` environment variable.
- The default target classes are indoor-friendly objects such as chairs, couches, tables, beds, toilets, doors (if supported by your custom dataset), and obstacles.

## Environment Variables

| Variable | Default | Purpose |
| --- | --- | --- |
| `MODEL_PATH` | `yolov8n.pt` | Path to YOLO weights |
| `CONFIDENCE_THRESHOLD` | `0.45` | Minimum confidence to keep detections |
| `CAMERA_INDEX` | `0` | Webcam index |
| `ENABLE_AUDIO` | `true` | Enables spoken feedback |
| `ALERT_COOLDOWN_SECONDS` | `4` | Minimum seconds between repeated alerts |

## Next Steps

- Replace the default YOLO weights with a fine-tuned indoor object detector.
- Add navigation-specific logic such as left/center/right guidance.
- Persist detection logs for user studies and evaluation.
- Deploy using Render, Docker, or a GPU-enabled edge device.
