from peewee import *
from base import Base


class Vote(Base):
    post_id = CharField()
    vote_type_id = CharField()
    creation_date = DateTimeField()

    def __repr__(self):
        return "<Vote {'post_id': %s, 'vote_type_id': %s, 'creation_date': %s} >" \
               % (self.tag_name, self.vote_type_id, self.creation_date)
