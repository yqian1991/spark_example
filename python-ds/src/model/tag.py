from peewee import *
from base import Base


class Tag(Base):
    tag_name = CharField()
    count = IntegerField()
    excerpt_post_id = CharField()
    wiki_post_id = CharField()

    def __repr__(self):
        return "<Tag {'name': %s, 'count': %s, 'excerpt_post_id': %s, " \
               "'wiki_post_id': %s} >" \
               % (self.tag_name, self.count, self.excerpt_post_id, self.wiki_post_id)
