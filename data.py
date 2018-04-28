import json
from peewee import *
import time
from error_handler import InvalidUsage

database = SqliteDatabase('hobbyhorse.db')

def create_tables():
	database.connect()
	database.create_tables([Horse], True)

def before_request_handler():
	database.connect()

def after_request_handler():
	database.close()

class Horse(Model):
	horse_id = IntegerField()
	name = FixedCharField()
	birthday = DateField()
	gender = FixedCharField()
	owner = IntegerField()
	# price = IntegerField()
	# record = CharField()
	# genetics = BlobField()
	# stats = BlobField()

	class Meta:
		database = database

def get_horses(stable_id=None):
	horses = Horse.select().where(Horse.owner == stable_id)
	return horses

def create_horse():
	try:
		with database.transaction():
			horse = Horse.create(
				horse_id=2,
				name='Poney22',
				birthday=time.time(),
				gender='unk',
				owner=1
			)
	except IntegrityError, e:
		InvalidUsage('Failed to create horse')

def race_info(race_id):
	pass

def race_horses(entries, race_info):
	pass