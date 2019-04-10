import json
from pathlib import Path
from flask import Flask, render_template


app = Flask(__name__)
app.root = Path(__file__).parent


@app.route('/')
def index():
    models = get_models()
    return render_template('index.html', models=models)


def get_models():
    models = [p.stem for p in list((app.root/"models").glob("*")) if p.is_dir()]
    return models


@app.route('/settings')
def settings():
    configs = get_configs()
    return render_template('settings.html', configs=configs)


def get_configs():
    configs = json.load(open(app.root/"static/config/config.json"))
    return configs


@app.route('/infer/<path:wsiname>')
def infer(wsiname):
    return render_template('infer.html', wsiname=wsiname)


@app.route('/result/<path:wsiname>')
def result(wsiname):
    return render_template('result.html', wsiname=wsiname)


@app.route('/new')
def new():
    return render_template('new.html')


@app.route('/training/<path:wsidirname>')
def training(wsidirname):
    setup_training()
    return render_template('training.html',
                           wsidirname=wsidirname)

def setup_training():
    app.model = ""


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)  # どこからでもアクセス可能に
