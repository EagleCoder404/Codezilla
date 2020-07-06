from app import db,login
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(str(id))

class User(UserMixin,db.Model):
    id = db.Column(db.String,primary_key=True)
    first_name = db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(50),nullable=True)
    password_hash = db.Column(db.String(128))

    def set_password(self,p):
        self.password_hash = generate_password_hash(p)
    
    def check_password(self,p):
        return check_password_hash(self.password_hash,p)

    def __repr__(self):
        return "[{}]".format(self.id)
        
class Pearl(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String,nullable=False)
    video = db.Column(db.String,nullable=False)
    language = db.Column(db.String,nullable=False,default="generic")

    def __repr__(self):
        return '[{} {}]'.format(self.id,self.title)
        