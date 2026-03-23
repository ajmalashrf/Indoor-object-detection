# Project Workflow

## 1. Dataset Collection
- Gather indoor images containing furniture, appliances, doors, and common obstacles.
- Prefer balanced examples across lighting conditions, room types, and camera heights.
- Keep labels aligned with the classes expected by the assistive application.

## 2. Image Preprocessing
- Resize images to match the target model input dimensions.
- Normalize image data and remove corrupt samples.
- Verify annotations and bounding boxes before training.

## 3. Model Training
- Start from a pretrained YOLO checkpoint.
- Fine-tune using indoor-specific classes.
- Track precision, recall, and mAP during validation.

## 4. Model Evaluation
- Review false positives that may produce distracting alerts.
- Test for missed obstacles that impact navigation safety.
- Measure inference speed for real-time webcam performance.

## 5. Real-Time Inference
- Capture webcam frames with OpenCV.
- Run object detection and annotate the live feed.
- Filter detections to indoor-relevant classes and confidence thresholds.

## 6. Accessibility Layer
- Convert detections into spoken alerts with cooldown control.
- Prioritize nearby hazards and reduce repetitive notifications.
- Extend with directional guidance where appropriate.

## 7. Deployment
- Package the app for Flask-based hosting.
- Add cloud deployment configuration for Render or Streamlit if needed.
- Validate camera/audio support in the target environment.
