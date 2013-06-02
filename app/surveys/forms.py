from flask import Flask, request, flash, redirect, url_for, render_template

from flask.ext.wtf import Form
from wtforms import BooleanField, TextField, PasswordField, validators

class SurveyForm(Form):
    name = TextField('Name', [validators.Required()]) 
    desc = TextField('Description', [validators.Length(max=1000)])

class QuestionForm(Form):
    question = TextField('Question', [validators.Required()])
