from src.lib.xml_util import get_root, get_row
from src.model.post_link import PostLink
import logging

xml_dir = '/Users/yuq/openspace/data/python-ds/data/PostLinks.xml'

logger = logging.getLogger(__name__)


def save_postlinks_from_xml_to_db(file_name):
    root = get_root(file_name)
    rows = get_row(root)
    count = 0
    for row in rows:
        post_id = row.get('PostId')
        related_post_id = row.get('RelatedPostId')
        link_type_id = row.get('LinkTypeId')
        creation_date = row.get('CreationDate')

        post_link = PostLink.create(post_id=post_id,
                                    related_post_id=related_post_id,
                                    link_type_id=link_type_id,
                                    creation_date=creation_date)
        count += 1
        try:
            post_link.save()
        except:
            logger.error("Error occurred when insert PostLink=%s to DB", post_link)







