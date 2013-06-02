from flask import Blueprint, request, render_template

from app import db
from app.surveys.models import Surveys, Questions
from app.surveys.forms import SurveyForm, QuestionForm

mod = Blueprint('surveys', __name__, url_prefix='/surveys')

@mod.route('')
def surveys():
    return render_template('surveys/index.html')

@mod.route('/create', methods=['GET', 'POST', ])
def surveys_create():
   form = SurveyForm(request.form)
   if request.method == 'GET':
       return render_template('surveys/create.html', form=form)
   elif request.method == 'POST':
       return render_template('surveys/create_results.html', form=request.form)
