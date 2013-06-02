from app import db

class Surveys(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    desc = db.Column(db.String(1000))
    questions = db.relationship('Question', backref='question', lazy='dynamic')

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000))

    def __init__(self, name, text):
        self.name = name
        self.text = text
