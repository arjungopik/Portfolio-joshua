from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:user@localhost:5432/portfolio'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class FormData(db.Model):
    __tablename__ = 'tesimonials'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    mobile_number = db.Column(db.String)
    message = db.column(db.String)

class ContactUs(db.Model):
    __tablename__= 'contactus'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    mobile_number = db.Column(db.String)
    message = db.column(db.String)


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
        contact_data = ContactUs(name= name,email = email, mobile_number = mobile_number,message = message)
        db.session.add(contact_data)
        db.session.commit()
        
    return redirect(url_for('index'))

@app.route('/tesimonial', methods=['POST','GET'])
def testimonial():
    if request.method =='POST':
        return render_template('testimonial_creation.html')


@app.route('/testimonial_creation',methods = ['POST','GET'])
def testimonial_cration():
    if request.method == 'POST':
        name = request.form.get('fname')
        email = request.form.get('email') 
        mobile_number = request.form.get('mobile_number')
        message = request.form.get('message')
        form_data = FormData(name=name,email=email,mobile_number=mobile_number,message=message)
        db.session.add(form_data)
        db.session.commit()
        

    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 