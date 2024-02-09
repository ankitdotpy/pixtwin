PixTwin
---
PixTwin is a simple image search engine for discovering visual twins pictures. Simply upload an image, and PixTwin scours its extensive database to find visually similar images.

### Requirements
Refer `requirements.txt`

### Usage
```sh
git clone https://github.com/ankitdotpy/pixtwin.git
cd pixtwin
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd pixtwin
touch .env # paste your elasticsearch cloud id and api key in this file
python3 -m index_es.py
flask run
```

### To Do
embeddings are not good, need better model for that