# mongoengine database module
from mongoengine import *
from datetime import datetime
import logging

class Comment(EmbeddedDocument):
	name = StringField()
	comment = StringField()
	timestamp = DateTimeField(default=datetime.now())
	
class Idea(Document):

	creator = StringField(max_length=120, required=True, verbose_name="First name")
	title = StringField(max_length=120, required=True)
	slug = StringField()
	idea = StringField(required=True, verbose_name="What is your idea?")
	latitude = StringField(max_length=120, required=True)
	longitude = StringField(max_length=120, required=True)

	# Category is a list of Strings
	categories = ListField(StringField(max_length=30))

	# Comments is a list of Document type 'Comments' defined above
	comments = ListField( EmbeddedDocumentField(Comment) )

	# Timestamp will record the date and time idea was created.
	timestamp = DateTimeField(default=datetime.now())

#All classes info goes here
#Creating a new user, from example goes in the app.py

#class User(Document):
    #email = StringField(required=True)
    #first_name = StringField(max_length=50)
    #last_name = StringField(max_length=50)