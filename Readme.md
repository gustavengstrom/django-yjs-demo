# Example project for a working setup of Django, Channels and Yjs 

## Uses
Django
Django channels
pycrdt
pycrdt-websocket

## Setup
```
pip install -r requirements.txt
brew install rust
python -m uvicorn collab_editor.asgi:application --port 8001 --reload
```