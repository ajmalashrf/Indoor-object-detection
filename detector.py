from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import cv2
from ultralytics import YOLO

from config import settings


@dataclass
class Detection:
    label: str
    confidence: float
    bbox: tuple[int, int, int, int]


class IndoorObjectDetector:
    def __init__(self, model_path: str | None = None, confidence_threshold: float | None = None) -> None:
        self.model = YOLO(model_path or settings.model_path)
        self.confidence_threshold = confidence_threshold or settings.confidence_threshold
        self.target_labels = set(settings.target_labels)

    def detect(self, frame: Any) -> list[Detection]:
        results = self.model.predict(source=frame, conf=self.confidence_threshold, verbose=False)
        detections: list[Detection] = []

        for result in results:
            names = result.names
            for box in result.boxes:
                confidence = float(box.conf[0])
                class_id = int(box.cls[0])
                label = names[class_id]
                if label not in self.target_labels:
                    continue
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                detections.append(Detection(label=label, confidence=confidence, bbox=(x1, y1, x2, y2)))

        return detections

    @staticmethod
    def annotate(frame: Any, detections: list[Detection]) -> Any:
        for detection in detections:
            x1, y1, x2, y2 = detection.bbox
            caption = f"{detection.label} {detection.confidence:.2f}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (20, 184, 166), 2)
            cv2.rectangle(frame, (x1, y1 - 24), (x2, y1), (20, 184, 166), -1)
            cv2.putText(
                frame,
                caption,
                (x1 + 6, y1 - 6),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (15, 15, 15),
                1,
                cv2.LINE_AA,
            )
        return frame
