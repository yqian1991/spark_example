from peewee import *
from base import Base
from datetime import datetime


class Post(Base):
    post_type_id = CharField()
    score = DecimalField()
    view_count = IntegerField()
    body = TextField()
    owner_user_id = CharField()
    last_activity_date = DateTimeField()
    title = CharField()
    tags = CharField()
    answer_count = IntegerField()
    comment_count = IntegerField()
    favorite_count = IntegerField()
    closed_date = DateTimeField
    creation_date = DateTimeField(default=datetime.now())
    last_editor_user_id = CharField()
    last_edit_date = DateTimeField

    def __repr__(self):
        return "<Post {'post_type_id': %s, 'score': %s, 'title': %s, " \
               "'tags': %s} >" \
               % (self.post_type_id, self.score, self.title, self.tags)
