from src.lib.xml_util import get_root, get_row
from src.model.post import Post
import logging

xml_dir = '/Users/yuq/openspace/data/python-ds/data/Posts.xml'

logger = logging.getLogger(__name__)


def save_posts_from_xml_to_db(file_name):
    root = get_root(file_name)
    rows = get_row(root)
    count = 0
    for row in rows:
        creation_date = row.get('CreationDate')
        post_type_id = row.get('PostTypeId')
        score = row.get('Score')
        view_count = row.get('ViewCount')
        body = row.get('Body')
        owner_user_id = row.get('OwnerUserId')
        last_activity_date = row.get('LastActivityDate')
        title = row.get('Title')
        tags = row.get('Tags')
        answer_count = row.get('AnswerCount')
        comment_count = row.get('CommentCount')
        favorite_count = row.get('FavoriteCount')
        closed_date = row.get('ClosedDate')
        last_editor_user_id = row.get('LastEditorUserId')
        last_edit_date = row.get('LastEditDate')

        post = Post.create(post_type_id=post_type_id,
                           score=score,
                           view_count=view_count,
                           body=body,
                           owner_user_id=owner_user_id,
                           last_activity_date=last_activity_date,
                           title=title,
                           tags=tags,
                           answer_count=answer_count,
                           comment_count=comment_count,
                           favorite_count=favorite_count,
                           closed_date=closed_date,
                           last_editor_user_id=last_editor_user_id,
                           last_edit_date=last_edit_date,
                           creation_date=creation_date)
        count += 1
        try:
            post.save()
        except:
            logger.error("Error occurred when insert Post=%s to DB", post)







