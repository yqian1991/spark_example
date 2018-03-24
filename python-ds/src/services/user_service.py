from src.lib.xml_util import get_root, get_row
from src.model.user import User
import logging

xml_dir = '/Users/yuq/openspace/data/python-ds/data/Users.xml'

logger = logging.getLogger(__name__)


def save_users_from_xml_to_db(file_name):
    root = get_root(file_name)
    rows = get_row(root)
    num = 0
    for row in rows:
        reputation = row.get('Reputation')
        creation_date = row.get('CreationDate')
        display_name = row.get('DisplayName')
        last_access_date = row.get('LastAccessDate')
        website_url = row.get('WebsiteUrl')
        location = row.get('Location')
        about_me = row.get('AboutMe')
        views = row.get('Views')
        upvotes = row.get('UpVotes')
        downvotes = row.get('DownVotes')
        account_id = row.get('AccountId')

        user = User.create(reputation=reputation,
                           creation_date=creation_date,
                           display_name=display_name,
                           last_access_date=last_access_date,
                           website_url=website_url,
                           location=location,
                           about_me=about_me,
                           views=views,
                           upvotes=upvotes,
                           downvotes=downvotes,
                           account_id=account_id)
        num += 1
        try:
            user.save()
        except:
            logger.error("Error occurred when insert user=%s to DB", user)







