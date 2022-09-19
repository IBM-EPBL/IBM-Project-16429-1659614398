from flask import Flask,render_template #package or module importing

app = Flask(__name__) #flask running procedure

#routing concept using render template---
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/blog')
def blog():
    return render_template("blog.html")
@app.route('/login')
def login():
    return render_template("login.html")
@app.route('/register')
def register():
    return render_template("register.html")

#end of routing 
if __name__ == "__main__":
    app.run(debug=True)