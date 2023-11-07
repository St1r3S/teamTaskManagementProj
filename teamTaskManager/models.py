from mongoengine import StringField, IntField, BooleanField, Document


# Create your models here.
class Task(Document):
    name = StringField()
    additional_info = StringField()
    priority = IntField(min_value=1, max_value=9)
    is_completed = BooleanField(default=False)


class Worker(Document):
    first_name = StringField()
    last_name = StringField()
    role = StringField()
    is_busy = BooleanField(default=False)
