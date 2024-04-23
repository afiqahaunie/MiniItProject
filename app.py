from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template("main_page.html")

@app.route('/color')
def color():
    return render_template("color.html")

if __name__ == '__main__':
    app.run(debug = True)

