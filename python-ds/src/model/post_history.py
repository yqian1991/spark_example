from peewee import *
from base import Base
from datetime import datetime


class PostHistory(Base):
    post_history_type_id = CharField()
    post_id = CharField()
    revision_guid = CharField()
    text = TextField()
    user_id = CharField()
    creation_date = DateTimeField(default=datetime.now())

    def __repr__(self):
        return "<PostHistory {'post_id': %s, 'post_history_type_id': %s, 'text': %s, 'user_id': %s, " \
               "'creation_date': %s, 'revision_guid': %s} >" \
               % (self.post_id, self.post_history_type_id, self.text, self.user_id, self.creation_date, self.revision_guid)
