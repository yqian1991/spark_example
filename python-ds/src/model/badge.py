from datetime import datetime
from peewee import *
from base import Base


class Badge(Base):
    user_id = CharField()
    name = CharField(unique=True)
    date = DateTimeField(default=datetime.now)
    class_id = CharField(unique=True)
    tag_based = BooleanField(default=True)

    def __repr__(self):
        return "<Badge {'user_id': %s, 'name': %s, 'date': %s, 'class_id': %s, 'tag_based': %s}>" \
               % (self.user_id, self.name, self.date, self.class_id, self.tag_based)
