# **COMPSCI 235 - LAB 7**
###### Name: Dylan Choy
###### UPI: dcho282

## **Notes**

SQLAlchemy
- ORM (Object Relational Mapper) helps us map Python objects to the database, avoiding the need to write out SQL query statements
- SQLAlchemy supports many relational databases, such as Microsoft SQL Server, MySQL, and PostgreSQL
- SQLAlchemy is a standalone package that does not have any ties to Flask

## **Hands-on Lab Activity:**

### Questions

**1.** Write down teh steps you will precede for implementing the SQLite features in the Flask server
> Add an environment variable called `SQLALCHEMY_DATABASE_URL` in the `.env` file
> Create a file called `orm.py` under `./covid/adapters/data/`, where it stores all the `Table` instances that we are going to use in our application, and a `map_model_to_tables` function that maps these tables to our model entities found in `./covid/domain/model.py`
> Under the newly created file `database_repository.py`:
    > Create a `SessionContextManager` class which enables the use of SQLAlchemy sessions
    > Create a `SqlAlchemyRepository` class which implements the same methods as `memory_repository.py`, except we retrieve the data from SQLite using SQLAlchemy session
> Create a database engine and session factory in `./covid/__init__.py` before starting the Flask server
> Create a new database for testing purposes

**2.** So far we encountered two sessions, one is the SQLAlchemy session, another is the web session. Are they the same? If not, briefly explain what each session does.
> An SQLAlchemy session established all database conversations through internal explicit transactions. It is the "holding zone" for objects during its lifespan.
> A web session is a group of user interactions with a website, taking place within a set timeframe. 

**3.** SQLite is a built-in package for Python. Why do we need SQLAlchemy ORM? Can you explain the benefits of using SQLAlchemy?
> ORM allows us to translate (maps) domain models to table rows in a database, and vice versa.
> The benefits of using SQLAlchemy are:
    > Programmers can work with objects only, without having to use SQL statements in code compared to SQLite
    > It allows querying the database in terms of domain model structures we may have
    > Certain objects are marked as persistent, after that, any changes in those objects are synchronised with the database regardless of any explicit code written
    > The framework allows for mapping of objects to the relational database tables
