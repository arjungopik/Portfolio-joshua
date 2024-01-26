from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:user@localhost:5432/portfolio'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class FormData(db.Model):
    __tablename__ = 'new_testimonials'  # Renamed table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    mobile_number = db.Column(db.String)
    linkedin = db.Column(db.String)
    twitter = db.Column(db.String)
    facebook = db.Column(db.String)
    message = db.Column(db.String) 

class TestimonialData(db.Model):
    __tablename__ = 'cnf_testimonials'  # Renamed table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    mobile_number = db.Column(db.String)
    linkedin = db.Column(db.String)
    twitter = db.Column(db.String)
    facebook = db.Column(db.String)
    message = db.Column(db.String) 

class ContactUs(db.Model):
    __tablename__ = 'new_contactus'  # Renamed table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    mobile_number = db.Column(db.String)
    message = db.Column(db.String)  

@app.route('/')
def index():
    row= TestimonialData.query.limit(9).all()
    return render_template('index.html',row=row)


    
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
        print(name,email,mobile_number,message)
    else:
        print("eoorrr")
    return redirect(url_for('index'))

@app.route('/tesimonial', methods=['POST','GET'])
def testimonial():
    if request.method =='POST':
        return render_template('testimonial_creation.html')
@app.route('/article')
def article():
    return render_template('articles.html')


@app.route('/testimonial_creation',methods = ['POST','GET'])
def testimonial_cration():
    if request.method == 'POST':
        name = request.form.get('fname')
        email = request.form.get('email') 
        mobile_number = request.form.get('mobile_number')
        linkedin = request.form.get('linkedin')
        twitter = request.form.get('twitter')
        facebook= request.form.get('facebook')
        message = request.form.get('message')

        form_data = FormData(name=name,email=email,mobile_number=mobile_number,linkedin = linkedin ,facebook = facebook,twitter = twitter,message=message)
        db.session.add(form_data)
        db.session.commit()
        
    
    return redirect(url_for('index'))
@app.route('/testimonial_entry')
def tesimonial_entry():
    tps_data = FormData.query.all()
    td = TestimonialData.query.all()
    return render_template('testimonial_entry.html', tps_data=tps_data,td=td)

@app.route('/contacts')
def contactus():
    tps_data = ContactUs.query.all()
    return render_template('contactus.html', tps_data=tps_data)

@app.route('/posttestmonial/<id>',methods = ['POST','GET'])
def testmposting(id):
    if request.method == 'POST':
        if request.form['submit_button'] == "Post":
            row = FormData.query.get(id)
            name=row.name
            email = row.email 
            mobile_number = row.mobile_number
            linkedin = row.linkedin
            twitter = row.twitter
            facebook= row.facebook
            message = row.message
            cnfData = TestimonialData(name=name,email=email,mobile_number=mobile_number,linkedin=linkedin,twitter=twitter,facebook=facebook,message=message)
            db.session.add(cnfData)
            db.session.delete(row)
            db.session.commit()
        elif request.form['submit_button'] == "Delete":
            row = FormData.query.get(id)
            db.session.delete(row)
            db.session.commit()
    return redirect(url_for('tesimonial_entry'))

@app.route('/edittestmonial/<id>',methods = ['POST','GET'])
def testmedit(id):
    if request.method == 'POST':
        if request.form['submit_button'] == "Remove":
            row = TestimonialData.query.get(id)
            name=row.name
            email = row.email 
            mobile_number = row.mobile_number
            linkedin = row.linkedin
            twitter = row.twitter
            facebook= row.facebook
            message = row.message
            cnfData = FormData(name=name,email=email,mobile_number=mobile_number,linkedin=linkedin,twitter=twitter,facebook=facebook,message=message)
            db.session.add(cnfData)
            db.session.delete(row)
            db.session.commit()
            for i in range(100):
                print(id)
        
    return redirect(url_for('tesimonial_entry'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False,host='0.0.0.0') 