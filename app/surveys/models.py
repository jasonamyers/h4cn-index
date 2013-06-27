from app import db


class Surveys(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    desc = db.Column(db.String(1000))
    questions = db.relationship('Questions', backref='surveys', lazy='dynamic')
    active = db.Column(db.Boolean())

    def __init__(self, name, desc, active):
        self.name = name
        self.desc = desc
        self.active = active


class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000))
    questions_id = db.Column(db.Integer, db.ForeignKey('surveys.id'))

    def __init__(self, name, text):
        self.name = name
        self.text = text
