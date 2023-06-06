import string
import random
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
urls = {}


def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['original_url']
        if original_url:
            short_url = generate_short_url()
            urls[short_url] = original_url
            return render_template('index.html', short_url=short_url)
    return render_template('index.html')


@app.route('/<short_url>')
def redirect_to_original_url(short_url):
    if short_url in urls:
        return redirect(urls[short_url])
    else:
        return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
