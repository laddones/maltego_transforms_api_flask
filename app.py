from flask import Flask, request, render_template
import config
import requests as rq

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/LeakCheck')
def api():

    check = str(request.args.get('check'))
    if check:
        # response = rq.get(f'https://leakcheck.net/api?key={config.key}&check={check}&type={type_api}').json()
        response = rq.get(f'https://leakcheck.net/api/public?key={config.key}&check={check}').json()

        return response

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')