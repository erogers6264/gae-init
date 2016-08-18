from google.appengine.ext import nbd
import model

class Contact(model.Base):
	user_key = nbd.KeyProperty(kind=model.User,required=True)
	name = nbd.StringProperty(required=True)
	email = nbd.StringProperty(default='')
	phone = nbd.StringProperty(default='')
	address = nbd.StringProperty(default='')