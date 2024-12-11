from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/storia')
def history():
    return render_template('storia.html')

@app.route('/attrazioni')
def attractions():
    return render_template('attrazioni.html')

@app.route('/eventi')
def events():
    return render_template('turismo.html')

if __name__ == '__main__':
    app.run(debug=True)
