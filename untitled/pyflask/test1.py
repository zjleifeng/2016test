from flask import Flask ,request
app=Flask(__name__)

@app.route('/')
def index():
    return "hello zhang!"

@app.route('/user/<name>')
def user(name):
    return "hello %s" %name

@app.route('/')
def index1():
    user_agent=request.headers.get("user-Agent")
    return "you browes is %s"%user_agent

if __name__=="__main__":
    app.run(debug=True)