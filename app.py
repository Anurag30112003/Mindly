from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")
    
@app.route('/meditation')
def meditation():
    return render_template("meditation.html")

@app.route('/music')
def music():
    return render_template("music.html")

@app.route('/write')
def write():
    return render_template("write.html")


if __name__ == '__main__':
    app.run(debug = True)