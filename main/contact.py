from flask.ext import wtf
import wtforms

class ContactUpdateForm(wtf.Form):
	name = wtforms.StringField('Name', [wtforms.validators.required()])		
	email = wtforms.StringField('Email', [wtforms.validators.optional(), 
				wtforms.validators.email()])		
	phone = wtforms.StringField('Phone', [wtforms.validators.optional()])		
	address = wtforms.TextAreaField('Address', [wtforms.validators.optional()])		