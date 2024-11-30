from project.models.comment import Comment
from project.models.user import User


def filter_comments_by_author(comments: list[Comment], author: User):
    return [c for c in comments if c.author_id == author.id]
