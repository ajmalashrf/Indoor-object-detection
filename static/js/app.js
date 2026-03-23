const detectionsList = document.getElementById('detections-list');
const healthIndicator = document.getElementById('health-indicator');
const refreshButton = document.getElementById('refresh-button');

async function refreshHealth() {
  try {
    const response = await fetch('/health');
    const payload = await response.json();
    healthIndicator.textContent = payload.camera_ready ? 'Camera Ready' : 'Camera Unavailable';
    healthIndicator.style.background = payload.camera_ready
      ? 'rgba(34,197,94,0.18)'
      : 'rgba(248,113,113,0.18)';
    healthIndicator.style.color = payload.camera_ready ? '#86efac' : '#fca5a5';
  } catch (error) {
    healthIndicator.textContent = 'Health Check Failed';
    healthIndicator.style.background = 'rgba(248,113,113,0.18)';
    healthIndicator.style.color = '#fca5a5';
  }
}

async function refreshDetections() {
  try {
    const response = await fetch('/detections');
    const payload = await response.json();
    detectionsList.innerHTML = '';

    if (!payload.items.length) {
      detectionsList.innerHTML = '<li class="empty-state">Waiting for detected objects…</li>';
      return;
    }

    payload.items.forEach((item) => {
      const li = document.createElement('li');
      li.className = 'detection-chip';
      li.textContent = `${item.label} — confidence ${item.confidence}`;
      detectionsList.appendChild(li);
    });
  } catch (error) {
    detectionsList.innerHTML = '<li class="empty-state">Unable to load detections.</li>';
  }
}

refreshButton.addEventListener('click', refreshDetections);
refreshHealth();
refreshDetections();
setInterval(refreshHealth, 10000);
setInterval(refreshDetections, 3000);
