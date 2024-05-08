PixTwin
---
PixTwin is a simple image search engine for discovering visual twins pictures. Simply upload an image, and PixTwin scours its extensive database to find visually similar images.

<iframe width="1916" height="801" src="https://www.youtube.com/embed/k20J3KcZYeU" title="pixtwin demo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

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
