from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    movie = request.args.get('movie', '')
    return render_template('main.html', movie=movie)

if __name__ == '__main__':
    app.run(debug=True)
