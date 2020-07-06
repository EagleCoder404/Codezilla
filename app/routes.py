from app import app,db
from flask import render_template,url_for,redirect,flash,request
from app.forms import LoginForm,RegisterForm,AddPearl
from app.models import User,Pearl
from flask_login import logout_user,login_user,login_required,current_user

@app.route("/login",methods=['GET','POST'])
@app.route("/index",methods=['GET','POST'])
@app.route("/",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main",id=1))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(id=login_form.email.data).first()
        if user is None or not user.check_password(login_form.password.data):
            flash("Invalid details")
            return redirect(url_for('login'))
        login_user(user,remember=login_form.remember.data)
        # next_page = request.args.get('next')
        # if not next_page or url_parse(next_page).netloc != '':
        #     next_page = url_for('main')
        return redirect(url_for('main',id=1))
    return render_template('login.html',login=login_form)

@app.route("/main/<int:id>")
@login_required
def main(id):
    pearls = Pearl.query.all()
    cur = Pearl.query.get(id)
    return render_template('main.html',pearls=pearls,cur=cur)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/register",methods=['GET','POST'])
def register():
    register_form = RegisterForm()

    if register_form.validate_on_submit():
        flash("{} registered".format(register_form.email.data))
        u = User(id = register_form.email.data, first_name=register_form.first_name.data,last_name = register_form.last_name.data)
        u.set_password(register_form.password.data)
        try:
            db.session.add(u)
            db.session.commit()
        except:
            return "Something went wrong"
        return redirect(url_for('login'))
    
    return render_template("register.html",register=register_form)

@app.route("/add",methods=['GET','POST'])
@login_required
def add():
    form = AddPearl()
    if form.validate_on_submit():
        pearl = Pearl(title=form.title.data,video=form.video.data,language=form.language.data)
        db.session.add(pearl)
        db.session.commit()
        flash("{} added".format(form.title.data))
        redirect(url_for('add'))
    return  render_template("add.html",form=form)
