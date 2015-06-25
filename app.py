from flask import Flask,  render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/classify')
def classify():
    return render_template('classify.html')

@app.route('/stats')
def stats():
    return render_template('stats.html')

if __name__ == '__main__':
    app.run(debug=True)
