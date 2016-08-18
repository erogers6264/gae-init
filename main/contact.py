import flask
import auth
import model
from main import app

from flask.ext import wtf
import wtforms


class ContactUpdateForm(wtf.Form):
	name = wtforms.StringField('Name', [wtforms.validators.required()])		
	email = wtforms.StringField('Email', [wtforms.validators.optional(), 
				wtforms.validators.email()])		
	phone = wtforms.StringField('Phone', [wtforms.validators.optional()])		
	address = wtforms.TextAreaField('Address', [wtforms.validators.optional()])


@app.route('/contact/create/', methods=['GET', 'POST'])
@auth.login_required
def createContact():
	form = ContactUpdateForm()
	if form.validate_on_submit():
		contact_db = model.Contact(
			user_key=auth.current_user_key(),
			name=form.name.data,
			email=form.email.data,
			phone=form.phone.data,
			address=form.address.data)
		contact_db.put()
		return flask.redirect(flask.url_for('welcome'))
	return flask.render_template(
		'contact_create.html',
		html_class='contact-create',
		title='Create Contact',
		form=form)
	