from flask import Flask


##ek web server banaya
app=Flask(__name__)


@app.route("/")
def welcome():
    return "hello bro"
@app.route("/please")
def x():

    return "deal done"

if __name__=="__main__":
    app.run(debug=True)
