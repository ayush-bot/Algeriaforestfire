from flask import Flask,render_template,request

##ek web server banaya
app=Flask(__name__)


@app.route("/")
def welcome():
    return "<html><H1>hi ...what are you doing</H1></html>"


@app.route("/index",methods=['GET'])
def x():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        x=request.form['name']
        return f" hello {x}"        
    return render_template('form.html')



if __name__=="__main__":
    app.run(debug=True)
