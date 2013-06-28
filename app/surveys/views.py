from flask import Blueprint, request, render_template, redirect, url_for

from app import db
from app.surveys.models import Surveys, Questions
from app.surveys.forms import SurveyForm, QuestionForm

mod = Blueprint('surveys', __name__, url_prefix='/surveys')


@mod.route('/')
def surveys():
    surveys = Surveys.query.filter(Surveys.active == True).all()
    return render_template('surveys/index.html', surveys=surveys)


@mod.route('/create', methods=['GET', 'POST', ])
def surveys_create():
    form = SurveyForm(request.form)
    if request.method == 'GET':
        return render_template('surveys/create.html', form=form)
    elif request.method == 'POST':
        survey = Surveys(form.name.data, form.desc.data, form.active.data)
        db.session.add(survey)
        db.session.commit()
        return redirect(url_for('surveys.surveys_show', id=survey.id))


@mod.route('/<int:id>')
def surveys_show(id):
    survey = Surveys.query.get(id)
    return render_template('surveys/show.html', survey=survey)


@mod.route('/<int:id>/questions/add/')
def question_add(id):
    if request.method == 'POST':
        question = Questions(request.form['question_text'])
        db.session.add(question)
        db.session.commit()
        return {'success': 'The question was added'}
