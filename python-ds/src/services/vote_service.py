from src.lib.xml_util import get_root, get_row
from src.model.vote import Vote
import logging

xml_dir = '/Users/yuq/openspace/data/python-ds/data/Tags.xml'

logger = logging.getLogger(__name__)


def save_votes_from_xml_to_db(file_name):
    root = get_root(file_name)
    rows = get_row(root)
    num = 0
    for row in rows:
        post_id = row.get('PostId')
        vote_type_id = row.get('VoteTypeId')
        creation_date = row.get('CreationDate')

        vote = Vote.create(post_id=post_id,
                           vote_type_id=vote_type_id,
                           creation_date=creation_date)
        num += 1
        try:
            vote.save()
        except:
            logger.error("Error occurred when insert vote=%s to DB", vote)







