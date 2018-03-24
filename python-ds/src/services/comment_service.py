from src.lib.xml_util import get_root, get_row
from src.model.comment import Comment
import logging

xml_dir = '/Users/yuq/openspace/data/python-ds/data/Comments.xml'

logger = logging.getLogger(__name__)


def save_comment_from_xml_to_db(file_name):
    root = get_root(file_name)
    rows = get_row(root)
    count = 0
    for row in rows:
        post_id = row.get('PostId')
        score = row.get('Score')
        text = row.get('Text')
        user_id = row.get('UserId')
        creation_date = row.get('CreationDate')

        comment = Comment.create(post_id=post_id,
                                 score=score,
                                 text=text,
                                 user_id=user_id,
                                 creation_date=creation_date)
        count += 1
        try:
            comment.save()
        except:
            logger.error("Error occurred when insert comment=%s to DB", comment)







