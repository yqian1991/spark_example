from peewee import *
from base import Base


class User(Base):
    reputation = CharField()
    creation_date = DateTimeField()
    display_name = CharField()
    last_access_date = DateTimeField()
    website_url = CharField()
    location = CharField()
    about_me = TextField()
    views = IntegerField()
    upvotes = IntegerField()
    downvotes = IntegerField()
    account_id = CharField()

    def __repr__(self):
        return "<User {'account_id': %s, 'display_name': %s, 'reputation': %s, " \
               "'website_url': %s} >" \
               % (self.account_id, self.display_name, self.reputation, self.website_url)
