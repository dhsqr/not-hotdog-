# Not Hotdog (Silicon Valley Fun Project)

A playful side project inspired by the show *Silicon Valley* — Jian Yang’s “Not Hotdog” app.  

This app uses a pretrained **ResNet-18** model from PyTorch to classify images as **Hotdog 🌭** or **Not Hotdog ❌**.  
Deployed on [Hugging Face Spaces](https://huggingface.co/spaces/your-space-link).

---

## Demo
👉 Try it live here: [Not Hotdog App](https://huggingface.co/spaces/your-space-link)

---

## Features
- Loads a pretrained **ResNet-18** (ImageNet weights).  
- Accepts uploaded images (via Gradio).  
- Returns either:
  - **Hotdog 🌭** if the predicted label contains "hotdog".  
  - **Not Hotdog ❌** otherwise.  

---

## Installation

Clone the repo:

```bash
git clone https://github.com/your-username/not-hotdog-app.git
cd not-hotdog-app
```

Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run locally:

```bash
python app.py
```

This will start a local Gradio interface.  
Open the link printed in the terminal and upload an image to test.

---

## Files
- `app.py` — main application script (Gradio + ResNet-18).  
- `requirements.txt` — dependencies needed to run the app.  

---

## Notes
- This is a lighthearted experiment inspired by pop culture.  
- The value was in **setting up, debugging, and deploying** an AI app, not building a new model.  

---

## License
MIT License
