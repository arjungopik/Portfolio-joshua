from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


    
@app.route('/contactus', methods=['POST','GET'])
def submit_form():
    if request.method=='POST':
        name = request.form.get("fname")
        email = request.form.get("email")
        mobile_number = request.form.get("mobile_number")
        message = request.form.get("message")
        # print(name,mobile_number,email,message)
        # working
    return render_template('index.html')

@app.route('/tesimonial', methods=['POST','GET'])
def testimonial():
    if request.method =='POST':
        return render_template('testimonial_creation.html')



if __name__ == '__main__':
    app.run(debug=True)
