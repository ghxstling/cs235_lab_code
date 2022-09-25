# **COMPSCI 235 - LAB 6**
###### Name: Dylan Choy
###### UPI: dcho282

## **Notes**

Appropriate Uses for SQLite
- SQLite is useful for caching data and for use in embedded environments, such as Android
- It does **not** have administration, and is more suitable for **low traffic**
    - SQLite should **NOT** be used for web applications during production, as there are better relational database options such as MySQL, PostgreSQL and Microsoft SQL Server

SQL Query Example
- With the 'covid-19.db' file opened in DB Browser, we can execute the following SQL queries to gather specific information:
```sql
SELECT * FROM articles LIMIT 10;
-- Grab the first 10 articles from the articles table

SELECT * FROM articles ORDER BY date LIMIT 10 OFFSET 20;
-- Order all articles by date first, then grab all 10 articles on the 3rd page (we constrain each page to contain 10 articles per page)

SELECT * FROM articles WHERE title LIKE '%Covid 19%'
-- Grab all articles that contain 'Covid 19' in its title
```

Joining Tables Example
```sql
-- Left join example: Finding all comments by 'mjackson'
SELECT * FROM comments LEFT JOIN users ON users.id = comments.user_id WHERE users.user_name = 'mjackson';
```

## **Hands-on Lab Activity:**

### Questions

**Task 1: Creating conditional select queries**
**(a).** What is the query for selecting the 2nd page of articles with the title containing "US" and with each page limiting to 10 rows?
> The related query is:
```sql
SELECT * FROM articles WHERE title LIKE '%US%' LIMIT 10 OFFSET 10;
```

**(b).** Are search keywords case sensitive? If not, how can we only select "US", but not "us"?
> Search keywords are not case sensitive. We can use the `PRAGMA` keyword to set the value of `case_sensitive_like` to `1`, then run the query again:
```sql
PRAGMA case_sensitive_like=1;
SELECT * FROM articles WHERE title LIKE '%US%';
```
> However, by executing `PRAGMA case_sensitive_like=1;` means that all subsequent queries using the `LIKE` keyword will become case sensitive too. 

**Task 2: Joining tables**
Scenario: When a user wants to access his comments, he doesnt't know his `user_id`.
**(a).** How can `mjackson` find all articles he has commented? Only return `article_id` and `article title`.\
Note that he may comment multiple times on 1 article, but we only wnat to return the same article in 1 row.
> We can run the following query:
```sql
select article_id, articles.title, comment, user_id, user_name from comments
join articles on articles.id = comments.article_id
join users on users.id = comments.user_id where users.user_name = 'mjackson';
```

**(b).** Give one eaxmple for each type of joins: inner, left, right, and outer.
> Inner Join:
```sql
select * from comments
inner join users on comments.user_id = users.id;
```

> Left Join:
```sql
select * from articles
left join comments on comments.article_id = articles.id where comments.article_id = articles.id;
```

> Right Join:
```sql
select * from comments
right join users on comments.user_id = users.id;
```

> Outer Join:
```sql
select * from article_tags
outer join articles on article_tags.article_id = articles.id
outer join tags on article_tags.tag_id = tags.id;
```

**Task 3. Creating a Table**
We want to create a new table called "reading_lists", so that a user can add articles into their reading list.\
Just like Netflix, each user can only have one reading list.
**(a).** What fields would you include in the table?
> `id`, `user_id`, `article_id`, `article_name`

**(b).** What is the schema of the table?
> The schema for `reading_list` would look like:
```sql
CREATE TABLE reading_lists (
    id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    article_id INTEGER NOT NULL,
    article_title VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (article_id) REFERENCES articles(id),
    FOREIGN KEY (article_title) REFERENCES articles(title)
)
```
