# Waste Sense

AI-Powered Waste Classification with **YOLO26s** - Real-time detection of glass, metal, paper, and plastic.

## Overview

- `index.html` - Frontend web interface (upload images, live camera, video files)
- `server.py` - FastAPI backend serving the YOLO `best.pt` model
- `requirements.txt` - Python dependencies

The browser cannot run PyTorch `.pt` files directly. The HTML supports two modes:
- **Demo mode** (default): simulated detections for UI preview
- **Backend mode**: connects to the FastAPI server at `http://localhost:8000/predict`

## Quick Start

### 1. Place your trained model
Copy your `best.pt` (from Google Drive) into the project root next to `server.py`.

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the backend
```bash
uvicorn server:app --host 0.0.0.0 --port 8000
```

### 4. Open the frontend
Open `index.html` in your browser. In the **Settings** tab, set the API endpoint to:
```
http://localhost:8000/predict
```
Click **Test Connection** - the badge should change from `Demo Mode` to `API Connected`.

## Detection Classes

| ID | Class | Color |
|----|--------|--------|
| 0 | glass | #1565C0 |
| 1 | metal | #B71C1C |
| 2 | paper | #2E7D32 |
| 3 | plastic | #E65100 |

## Architecture

- Model: YOLO26s (Ultralytics)
- Input size: 640px
- Framework: PyTorch + Ultralytics
- API: FastAPI with CORS enabled

## License

MIT
