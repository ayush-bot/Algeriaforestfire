from flask import Flask,render_template

##ek web server banaya
app=Flask(__name__)


@app.route("/")
def welcome():
    return "<html><H1>hi ...what are you doing</H1></html>"
@app.route("/index")
def x():
    return render_template("index.html")
@app.route('/about')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True)
