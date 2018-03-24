from peewee import *
from base import Base
from datetime import datetime


class PostLink(Base):
    post_id = CharField()
    related_post_id = CharField()
    link_type_id = CharField()
    creation_date = DateTimeField(default=datetime.now())

    def __repr__(self):
        return "<PostLink {'post_id': %s, 'related_post_id': %s, 'link_type_id': %s, " \
               "'creation_date': %s} >" \
               % (self.post_id, self.related_post_id, self.link_type_id, self.creation_date)
