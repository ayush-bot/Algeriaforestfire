from flask import Flask,render_template,request,redirect,url_for

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


@app.route('/sucess/<int:score>')
def success(score):
    return "The score is " + str(score) 


@app.route('/marks/<int:marks>')
def marks(marks):
    res=""
    if marks>=50:
        res="PASS"
    else:
        res="FAIL"
    exp={"marks":marks,"res":res}
        
    return render_template('result.html',result=exp)


@app.route('/exams/<int:no>')
def exams(no):
    
    return render_template('read.html',result=no)


@app.route('/forms',methods=['GET','POST'])
def forms():
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
 
        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('new.html')
    return redirect(url_for('marks',marks=total_score))



if __name__=="__main__":
    app.run(debug=True)
