from peewee import *
from base import Base
from datetime import datetime


class Comment(Base):
    post_id = CharField()
    score = DecimalField()
    text = TextField()
    user_id = CharField()
    creation_date = DateTimeField(default=datetime.now())

    def __repr__(self):
        return "<Comment {'post_id': %s, 'score': %s, 'text': %s, 'user_id': %s, 'creation_date': %s} >" \
               % (self.post_id, self.score, self.text, self.user_id, self.creation_date)
