#86% of storage used … If you run out of space, you can't save to Drive or use Gmail. Get 30 GB of storage for ₹59.00 ₹0 for 1 month.
from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit',methods=['POST'])
def submit():
    username=request.form['username']
    rollno=request.form['rollno']
    email=request.form['email']
    year=request.form['year']
    return render_template('result.html',name=username,roll=rollno,mail=email,yr=year)
if __name__=='__main__':
    app.run(debug=True)