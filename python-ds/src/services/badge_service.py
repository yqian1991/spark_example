from src.lib.xml_util import get_root, get_row
from src.model.badge import Badge
import logging

xml_dir = '/Users/yuq/openspace/data/python-ds/data/Badges.xml'

logger = logging.getLogger(__name__)

s_to_bool = {
    'true': True,
    'True': True,
    'false': False,
    'False': False
}


def save_badge_from_xml_to_db(file_name):
    root = get_root(file_name)
    rows = get_row(root)
    count = 0
    for row in rows:
        user_id = row.get('UserId')
        name = row.get('Name')
        date = row.get('Date')
        class_id = row.get('Class')
        tag_based = s_to_bool[row.get('TagBased')]
        badge = Badge.create(user_id=user_id,
                             name=name,
                             date=date,
                             class_id=class_id,
                             tag_based=tag_based)
        count += 1
        try:
            badge.save()
        except:
            logger.error("Error occurred when insert badge=%s to DB", badge)







