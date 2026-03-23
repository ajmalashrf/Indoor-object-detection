import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    model_path: str = os.getenv("MODEL_PATH", "yolov8n.pt")
    confidence_threshold: float = float(os.getenv("CONFIDENCE_THRESHOLD", "0.45"))
    camera_index: int = int(os.getenv("CAMERA_INDEX", "0"))
    enable_audio: bool = os.getenv("ENABLE_AUDIO", "true").lower() == "true"
    alert_cooldown_seconds: int = int(os.getenv("ALERT_COOLDOWN_SECONDS", "4"))
    target_labels: tuple[str, ...] = (
        "chair",
        "couch",
        "bed",
        "dining table",
        "tv",
        "potted plant",
        "door",
        "person",
        "suitcase",
        "backpack",
        "refrigerator",
        "microwave",
        "oven",
        "sink",
        "toilet",
    )


settings = Settings()
