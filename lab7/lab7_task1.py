"""Startup code for Lab 7 SQLAlchemy Task 1

The code tests your understanding on the basic functionality of SQLAlchemy.

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
from sqlalchemy import (Column, Date, Integer, MetaData, String, Table,
                        create_engine)

# Set echo to True, so we know what is running behind the scene.
engine = create_engine('sqlite:///covid-19.db', echo=True)
meta = MetaData()

comments_table = Table(
    'comments',
    meta,
    Column('id', Integer, primary_key=True),
    # TODO: Add your code here
    Column('user_id', Integer),
    Column('article_id', Integer),
    Column('comment', String),
    Column('timestamp', Date)
)
connection = engine.connect()


def select_all():
    """Select all rows from comments."""
    select = comments_table.select()
    # To access generated SQL SELECT query
    print('Query:\n', select)  # Same as: select.__str__()

    result = connection.execute(select)  # LegacyCursorResult object
    article_list = result.all()

    for article in article_list[:5]:
        print(article)


def insert(user_id, article_id, comment):
    """Insert an article."""
    insert = comments_table.insert().values(
        user_id=user_id,
        article_id=article_id,
        comment=comment,
        timestamp=datetime.datetime.now()
    )
    print('Query:\n', insert)
    connection.execute(insert)


def update(comment_id, new_comment):
    """Update the title where id == 1."""
    update = comments_table.update() \
        .where(comments_table.c.id == comment_id) \
        .values(
            comment=new_comment
        )
    print('Query:\n', update)
    connection.execute(update)

    select = comments_table.select().where(comments_table.c.id == 1)
    result = connection.execute(select)
    print(result.all())


def delete(comment_id):
    """Delete an article with a given id."""
    delete = comments_table.delete().where(comments_table.c.id == comment_id)
    print('Query:\n', delete)
    connection.execute(delete)

    select = comments_table.select().where(comments_table.c.id == comment_id)
    result = connection.execute(select)
    print(result.all())


if __name__ == '__main__':
    """Uncomment the functions below one at a time."""
    # select_all()

    # insert(
    #     user_id=2,
    #     article_id=4,
    #     comment='POG CHAMP'
    # )

    # insert(
    #     user_id=2,
    #     article_id=4,
    #     comment='WOOOOOOOOOO'
    # )

    # update(
    #     comment_id=1,
    #     new_comment='lmfaoooo'
    # )

    # delete(
    #     comment_id=4
    # )
