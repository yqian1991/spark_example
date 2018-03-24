from src.lib.xml_util import get_root, get_row
from src.model.tag import Tag
import logging

xml_dir = '/Users/yuq/openspace/data/python-ds/data/Tags.xml'

logger = logging.getLogger(__name__)


def save_tags_from_xml_to_db(file_name):
    root = get_root(file_name)
    rows = get_row(root)
    num = 0
    for row in rows:
        tag_name = row.get('TagName')
        count = row.get('Count')
        excerpt_post_id = row.get('ExcerptPostId')
        wiki_post_id = row.get('WikiPostId')

        tag = Tag.create(tag_name=tag_name,
                         excerpt_post_id=excerpt_post_id,
                         wiki_post_id=wiki_post_id,
                         count=count)
        num += 1
        try:
            tag.save()
        except:
            logger.error("Error occurred when insert tag=%s to DB", tag)







