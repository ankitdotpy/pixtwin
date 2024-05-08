PixTwin
---
PixTwin is a simple image search engine for discovering visual twins pictures. Simply upload an image, and PixTwin scours its extensive database to find visually similar images.

[![Watch the video](https://img.youtube.com/vi/k20J3KcZYeU/default.jpg)](https://youtu.be/k20J3KcZYeU)

### Requirements
Refer `requirements.txt`

### Usage
1. Clone the repository
```sh
git clone https://github.com/ankitdotpy/pixtwin.git
```
2. Create a virtual environment and install dependencies
```sh
cd pixtwin
touch .env # add your elasticsearch api key and cloud id here
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Index the images and run the flask app
```sh
cd pixtwin
touch .env # paste your elasticsearch cloud id and api key in this file
python3 -m index_es.py
flask run
```
