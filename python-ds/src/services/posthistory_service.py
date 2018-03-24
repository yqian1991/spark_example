from src.lib.xml_util import get_root, get_row
from src.model.post_history import PostHistory
import logging

xml_dir = '/Users/yuq/openspace/data/python-ds/data/PostHistory.xml'

logger = logging.getLogger(__name__)


def save_posthistory_from_xml_to_db(file_name):
    root = get_root(file_name)
    rows = get_row(root)
    count = 0
    for row in rows:
        post_id = row.get('PostId')
        post_history_type_id = row.get('PostHistoryTypeId')
        revision_guid = row.get('RevisionGUID')
        text = row.get('Text')
        user_id = row.get('UserId')
        creation_date = row.get('CreationDate')

        post_history = PostHistory.create(post_id=post_id,
                                          post_history_type_id=post_history_type_id,
                                          text=text,
                                          user_id=user_id,
                                          creation_date=creation_date,
                                          revision_guid=revision_guid)
        count += 1
        try:
            post_history.save()
        except:
            logger.error("Error occurred when insert PostHistory=%s to DB", post_history)







