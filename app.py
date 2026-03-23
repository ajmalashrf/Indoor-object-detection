from __future__ import annotations

import logging
from typing import Iterator

import cv2
from flask import Flask, Response, jsonify, render_template

from audio_feedback import AudioFeedback
from config import settings
from detector import IndoorObjectDetector

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


detector = IndoorObjectDetector()
audio_feedback = AudioFeedback(settings.alert_cooldown_seconds) if settings.enable_audio else None
video_capture = cv2.VideoCapture(settings.camera_index)
latest_detections: list[dict[str, str | float]] = []


@app.route("/")
def index() -> str:
    return render_template("index.html", settings=settings)


@app.route("/health")
def health() -> Response:
    camera_ready = bool(video_capture.isOpened())
    return jsonify(
        {
            "status": "ok" if camera_ready else "degraded",
            "camera_ready": camera_ready,
            "model_path": settings.model_path,
            "audio_enabled": settings.enable_audio,
        }
    )


@app.route("/detections")
def detections() -> Response:
    return jsonify({"items": latest_detections})


@app.route("/video_feed")
def video_feed() -> Response:
    return Response(generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")


def generate_frames() -> Iterator[bytes]:
    global latest_detections

    while True:
        success, frame = video_capture.read()
        if not success:
            logger.warning("Unable to read frame from the configured camera.")
            break

        detections = detector.detect(frame)
        latest_detections = [
            {"label": item.label, "confidence": round(item.confidence, 2)} for item in detections
        ]

        if audio_feedback is not None:
            for item in detections:
                audio_feedback.speak_detection(item.label)

        annotated_frame = detector.annotate(frame, detections)
        success, buffer = cv2.imencode(".jpg", annotated_frame)
        if not success:
            continue

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + buffer.tobytes() + b"\r\n"
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
