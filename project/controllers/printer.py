# -*- coding: utf-8 -*-
from project import app
from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class CreateForm(FlaskForm):
	text = StringField('Text:', validators=[DataRequired()])


@app.route('/')
def start():
	return render_template('printer/index.html')


@app.route('/print', methods=['GET', 'POST'])
def printer():
	form = CreateForm(request.form)
	print form.errors
	if request.method == 'POST':
		text=request.form['text']
		if form.validate():
			from project.models.Printer import Printer
			printer = Printer()
			printer.show_string(form.text.data)
			#tutaj można coś z tymi danymi zrobić, np dodać je do bazki :)
			return render_template('printer/index.html')
	return render_template('printer/print.html', form=form)
