"""Startup code for Lab 7 SQLAlchemy  Task 2

This code provides the minimal boilerplate for SQLAlchemy ORM.
It is based on [ORM Quick Start](https://docs.sqlalchemy.org/en/14/orm/quickstart.html)

Feel free to add additional functions if necessary.

Author: Luke Chang (xcha011@aucklanduni.ac.nz)
Date: 21/09/2022

NOTE: Tested on Python 3.9.14

Install
```
# Go to the project directory
cd lab7

python3.9 -m venv venv

# On Linux and Mac:
source ./venv/bin/activate

# On Windows
venv\Scripts\activate.bat

pip install -r requirements.txt
```
"""

import datetime

from sqlalchemy import Column, Date, Integer, String, create_engine, select, join, delete, update
from sqlalchemy.orm import Session, declarative_base

# Set echo to True, so we know what is running behind the scene.
engine = create_engine('sqlite:///covid-19.db', echo=True)
session = Session(engine)

# To make the code as short as possible, we use the base model implemented by 
# sqlalchemy.orm
Base = declarative_base()


class Article(Base):
    __tablename__ = 'articles'

    id = Column('id', Integer, primary_key=True)
    date = Column('date', Date)
    title = Column('title', String)
    first_paragraph = Column('first_paragraph', String)
    hyperlink = Column('hyperlink', String)
    image_hyperlink = Column('image_hyperlink', String)

    def __repr__(self):
        # NOTE: ``!r'' is for converting the value to a string using repr().
        return f'{self.id!r}. [{self.title!r}]({self.hyperlink!r})'


def search_article(keyword, session=session):
    """Search the title by the keyword and then return a list of Article objects.
    NOTE: The keyword is not case sensitive.
    """
    # "stmt" is the abbreviation for "Statement"
    stmt = select(Article).where(Article.title.contains(keyword))
    results = session.execute(stmt).all()
    return results

def get_article_by_id(article_id, session=session):
    # TODO: Add your code here
    stmt = select(Article).where(Article.id == article_id)
    article = session.execute(stmt).all()
    return article

class Comment(Base):
    __tablename__ = 'comments'
    
    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', Integer)
    article_id = Column('article_id', Integer)
    comment = Column('comment', String)
    timestamp = Column('timestamp', Date)

    def __repr__(self):
        # NOTE: ``!r'' is for converting the value to a string using repr().
        return f'{self.id!r}. [{self.user_id!r}]({self.comment!r})({self.timestamp!r})'

class User(Base):
    __tablename__ = 'users'
    
    id = Column('id', Integer, primary_key=True)
    user_name = Column('user_name', String)
    password = Column('password', String)

    def __repr__(self):
        # NOTE: ``!r'' is for converting the value to a string using repr().
        return f'{self.id!r}. [{self.user_name!r}]({self.password!r})'

def get_comment_by_id(comment_id, session=session):
    stmt = select(Comment).where(Comment.id == comment_id)
    comment = session.execute(stmt).all()
    return comment

def get_comment_by_user(user_name, session=session):
    """Join users and comments table, and use user_name to filter comments
    NOTE: You need to create the User class first!
    """
    j = join(Comment, User, Comment.user_id == User.id)
    stmt = select(Comment).select_from(j).filter(User.user_name == user_name)
    comment = session.execute(stmt).all()
    return comment

def delete_comment(comment_id, session=session):
    stmt = delete(Comment).where(Comment.id == comment_id)
    results = session.execute(stmt)
    return results

def update_comment(comment_id, comment):
    # TODO: Add your code here
    # This function should return the updated comment.
    # Note that you also want to update the timestamp with current time. 
    # (Use the `datetime` library)
    stmt = update(Comment).where(Comment.id == comment_id).values(
        id=98,
        user_id=1,
        article_id=2,
        comment=comment,
        timestamp=datetime.datetime.now()
    )
    comment = session.execute(stmt)
    return comment

if __name__ == '__main__':
    # articles = search_article('australia')
    # for article in articles:
    #     print(article)

    # article_by_id = get_article_by_id(article_id=7)
    # print(article_by_id)
    # article_by_id = get_article_by_id(article_id=23)
    # print(article_by_id)

    # comment_by_user = get_comment_by_user('thorke')
    # print(comment_by_user)
    # comment_by_user = get_comment_by_user('fmercury')
    # print(comment_by_user)

    # print(delete_comment(5))

    print(update_comment(99, 'testsrgrosixzg'))
