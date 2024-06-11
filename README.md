# 1. Python FastAPI Course Intro: Part #1 Python API Course
https://www.youtube.com/watch?v=Yw4LmMQXXFs&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=2&ab_channel=SanjeevThiyagarajan

# 2. Python + VS Code setup on mac: Part #2 Python API Course
https://www.youtube.com/watch?v=I5-qJ8SsU-E&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=2&ab_channel=SanjeevThiyagarajan


# 3. Python + VS Code setup on Windows: Part #3 Python API Course
https://www.youtube.com/watch?v=gc4gzrSZles&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=3&ab_channel=SanjeevThiyagarajan


# 4. What are Python Virtual Environments VENV: Part 4 Python API Course
https://www.youtube.com/watch?v=YDSx_il_7Ho&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=4&ab_channel=SanjeevThiyagarajan


# 5. Setup Python Virtual Environment on Windows: Part #5 Python API Course
https://www.youtube.com/watch?v=LZUCVqMDgP8&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=5&ab_channel=SanjeevThiyagarajan

python3 -m venv .venv

source .venv/bin/activate

# 6. Setup Python Virtual Environment on Mac: Part #6 Python API Course
https://www.youtube.com/watch?v=Czm16fj7H3M&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=6&ab_channel=SanjeevThiyagarajan


# 7. Initialize FastAPI Project: Part #7 Python API Course
https://www.youtube.com/watch?v=PuQzQNJZ4c8&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=7&ab_channel=SanjeevThiyagarajan


user guide official document - https://fastapi.tiangolo.com/tutorial/


operation that will require waiting before giving the results 

# we have to use  async keyword for await (waiting)
burgers = await get_burgers(2)

async def get_burgers(number: int):
    # Do some asynchronous stuff to create the burgers
    return burgers


@app.get('/burgers')
async def read_burgers():
    burgers = await get_burgers(2)
    return burgers


# This is not asynchronous
def get_sequential_burgers(number: int):
    # Do some sequential stuff to create the burgers
    return burgers

# install fastapi 
pip install fastapi

# to see all dependency
pip freeze

install - Formatter extension for Visual Studio Code using autopep8



uvicorn main:app --reload

fastapi dev main.py


# 8. FastAPI Path Operations: Part #8 Python API Course
https://www.youtube.com/watch?v=JcYmdPD2yvs&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=8&ab_channel=SanjeevThiyagarajan


# 9. Setup Postman: Part #9 Python API Course
https://www.youtube.com/watch?v=SI4ll4TXRT0&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=9&ab_channel=SanjeevThiyagarajan


# 10. HTTP Post Requests: Part #10 Python API Course
https://www.youtube.com/watch?v=nQ_Rw0joB-Y&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=10&ab_channel=SanjeevThiyagarajan


# 11. Schema Validation with Pydantic: Part #11 Python API Course
https://www.youtube.com/watch?v=MXojMTb_JKo&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=12&ab_channel=SanjeevThiyagarajan

pydantic - https://docs.pydantic.dev/latest/concepts/models/#model-methods-and-properties


# 12. What is CRUD? and best pracitces: Part #12 Python API Course
https://www.youtube.com/watch?v=tm8dfjK1S8M&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=12&ab_channel=SanjeevThiyagarajan

create - post -          posts       - @app.post("/posts")
read -   get -           posts/:id   - @app.get("/posts/{id}")
read -   get -           posts/      - @app.get("/posts")
update - patch/put -     posts/:id   - @app.put("/posts/{id}")   - put -all fields update(give all fields in payload) , patch - specific field update (give only one field)
create - delete -        posts/:id   - @app.delete("/posts/{id}")


# 13. Creating Posts FastAPI: Part #13 Python API Course
https://www.youtube.com/watch?v=50YYelLKm3w&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=13&ab_channel=SanjeevThiyagarajan


# 14. Postman Saving Requests: Part #14 Python API Course
https://www.youtube.com/watch?v=L1rgJrHEc6s&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=14&ab_channel=SanjeevThiyagarajan


# 15. Get Post by ID: Part #15 Python API Course
https://www.youtube.com/watch?v=ByrcTmvDaO4&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=15&ab_channel=SanjeevThiyagarajan


# 16. Path Order Matters: Part #16 Python API Course
https://www.youtube.com/watch?v=9YEGAQW_X7I&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=16&ab_channel=SanjeevThiyagarajan

# 17. Change Response Status Code: Part #17 Python API Course
https://www.youtube.com/watch?v=7L755E8KVQg&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=17&ab_channel=SanjeevThiyagarajan

# 18. Deleting Posts: Part #18 Python API Course
https://www.youtube.com/watch?v=QxlryV2Zoi4&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=18&ab_channel=SanjeevThiyagarajan


# 19. Updating Posts: Part #19 Python API Course
https://www.youtube.com/watch?v=HWfDZfB27us&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=19&ab_channel=SanjeevThiyagarajan



# 20. FastAPI Automatic Documentation: Part #20 Python API Course
https://www.youtube.com/watch?v=KUxCGqu-Xhg&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=20&ab_channel=SanjeevThiyagarajan

http://127.0.0.1:8000/doc
http://127.0.0.1:8000/redoc


# 21. Adding a SRC Directory: Part #21 Python API Course
https://www.youtube.com/watch?v=eyivIxifgPQ&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=21&ab_channel=SanjeevThiyagarajan


# 22. What is a Database: Part #22 Python API Course
https://www.youtube.com/watch?v=QRGo5YJulew&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=22&ab_channel=SanjeevThiyagarajan


# 23. Install Postgres on Windows: Part #23 Python API Course
https://www.youtube.com/watch?v=LJWscdUf0bU&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=23&ab_channel=SanjeevThiyagarajan


sudo -i -u postgres
psql


zec@zec-HP-EliteBook-840-G3:~$ sudo -i -u postgres
postgres@zec-HP-EliteBook-840-G3:~$ psql
psql (16.2 (Ubuntu 16.2-1.pgdg20.04+1))
Type "help" for help.

postgres=# \password postgres
Enter new password for user "postgres": 
Enter it again: 
postgres=# CREATE DATABASE mydatabase;
CREATE DATABASE
postgres=# CREATE USER root WITH PASSWORD 'root';
CREATE ROLE
postgres=# GRANT ALL PRIVILEGES ON DATABASE mydatabase TO root;
GRANT
postgres=# \q
postgres@zec-HP-EliteBook-840-G3:~$ 


# 24.Installing Postgres Database on Mac: Part #24 Python API Course
https://www.youtube.com/watch?v=GpIGZKYEOzM&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=25&ab_channel=SanjeevThiyagarajan


# 25. SQL Database Tables & Schema Basics: Part #25 Python API Course
https://www.youtube.com/watch?v=OmdSGetfoFE&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=25&ab_channel=SanjeevThiyagarajan


# 26. PgAdmin tutorial: Part #26 Python API Course
https://www.youtube.com/watch?v=iJiJnCzo71E&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=28&ab_channel=SanjeevThiyagarajan

sudo systemctl status postgresql
sudo -i -u postgres
psql

# create password for root user
\password root

CREATE DATABASE mydatabase;


CREATE USER root WITH PASSWORD 'root';

GRANT ALL PRIVILEGES ON DATABASE mydatabase TO root;
GRANT ALL PRIVILEGES ON DATABASE fastapi TO root;
---------------
/du
ALTER USER root WITH PASSWORD 'newpassword';



Access PostgreSQL Prompt: Switch to the PostgreSQL user and access the PostgreSQL prompt:

sudo -i -u postgres
psql


postgres=#
# Set a Password for the PostgreSQL User: It is a good practice to set a password for the postgres user. Inside the PostgreSQL 

\password postgres

# Follow the prompts to enter and confirm the new password.

# Create a New Database and User (Optional): You can create a new database and user if needed. For example:
ALTER ROLE myuser CREATEDB;

# Create a new database:

CREATE DATABASE mydatabase;

# Create a new user with a password:
CREATE USER myuser WITH PASSWORD 'mypassword';

# Grant privileges to the new user:
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;

# Exit the PostgreSQL Prompt: To exit the PostgreSQL prompt, type:
\q

# to show databases

\l

SELECT datname FROM pg_database;



# install pgadmin in ubuntu
https://www.pgadmin.org/download/pgadmin-4-apt/


ec@zec-HP-EliteBook-840-G3:~$ sudo -i -u postgres
[sudo] password for zec: 
postgres@zec-HP-EliteBook-840-G3:~$ psql
psql (16.2 (Ubuntu 16.2-1.pgdg20.04+1))
Type "help" for help.

postgres=# ALTER ROLE root CREATEDB;
ALTER ROLE
postgres=# 





https://www.postgresql.org/docs/current/datatype.html



# 27. SQL Basics: Part #27 Python API Course
https://www.youtube.com/watch?v=75NTErLHh40&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=29&ab_channel=SanjeevThiyagarajan



# 28. SQL Basics Filtering with "where": Part #28 Python API Course
https://www.youtube.com/watch?v=ITVfvbsEE8E&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=30&ab_channel=SanjeevThiyagarajan



# 29. SQL Operators: Part #29 Python API Course
https://www.youtube.com/watch?v=LkTBdfejlMI&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=31&ab_channel=SanjeevThiyagarajan


# 30. SQL "IN" Operator: Part #30 Python API Course
https://www.youtube.com/watch?v=nsxkn2RauJY&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=32&ab_channel=SanjeevThiyagarajan

# 31. Pattern Matching in SQL with "LIKE": Part #31 Python API Course
https://www.youtube.com/watch?v=zPBkPYOvuaw&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=33&ab_channel=SanjeevThiyagarajan


# 32. SQL ORDER & SORT results: Part 32: Python API Course
https://www.youtube.com/watch?v=L0j2z_HHXd0&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=34&ab_channel=SanjeevThiyagarajan


# 33. SQL Inserting data: Part #34 Python API Course
https://www.youtube.com/watch?v=KAxoMJGanYo&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=35&ab_channel=SanjeevThiyagarajan


insert into products(price, name, inventory) values(45, "car", 25) retruning *;  -- return single result this one   

insert into products(price, name, inventory) values(45, "car", 25), (33,"bike", 30) retruning id,name,price;  -- 2 record 

# 34. SQL Updating Rows: Part #36 Python API Course
https://www.youtube.com/watch?v=DPC5HKAgQaI&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=36&ab_channel=SanjeevThiyagarajan


# 35. Create App Database: Part #37 Python API Course
https://www.youtube.com/watch?v=glT4RebVYE0&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=37&ab_channel=SanjeevThiyagarajan


# 36. Connecting to a database Python: Part #38 Python API Course
https://www.youtube.com/watch?v=7Z1Sljh0ym8&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=38&ab_channel=SanjeevThiyagarajan


follow doc to connect postgress db 
https://www.psycopg.org/docs/usage.html

sudo apt-get install libpq-dev

pip install psycopg2

sudo apt-get install libpq-dev


db connection->



while True:
  try:
    conn = psycopg2.connect(host='localhost',database='fastapi',user='root',password='root',cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print("Database connection was successfull!!")
    break
  except Exception as error:
    print("Connecting to database failed")
    print("Error :", error)
    time.sleep(2)


# 37. Retrieve Posts Python Sql: Part #39 Python API Course
https://www.youtube.com/watch?v=JIJd90QZGQ4&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=39&ab_channel=SanjeevThiyagarajan

-Get all data

@app.get("/posts")
def get_posts():
  cursor.execute("""select * from posts""")
  posts =  cursor.fetchall()
  print(posts)
  return {"data": posts}


# 38. Create Posts Python Sql: #40 Python API course
https://www.youtube.com/watch?v=ObR9fHpvYi4&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=40&ab_channel=SanjeevThiyagarajan

-Post Single Record

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
  cursor.execute("""Insert into posts(title,content,published) values(%s,%s,%s) RETURNING *""",
                 (post.title,post.content,post.published))
  new_post = cursor.fetchone()
  conn.commit()
  return {"data": new_post}  

# 39. Fetch Posts by Id SQL Python: Part #41 Python API Course
https://www.youtube.com/watch?v=xDdua5yW-88&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=41&ab_channel=SanjeevThiyagarajan


-Get Single Record

@app.get("/posts/{id}")
def get_post(id: int):
  cursor.execute("""Select * from posts where id = %s """,(str(id),))
  post = cursor.fetchone()
  # print(post)
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id : {id} not found")
  return {"post_detail": post}



# 40. Delete Posts SQL Python: Part #42 Python API Course
https://www.youtube.com/watch?v=AsuIzBBbs6w&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=42&ab_channel=SanjeevThiyagarajan

-Delete single Post

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
  cursor.execute("""DELETE from posts where id = %s returning *""",(str(id),))
  delete_post = cursor.fetchone()
  conn.commit()
  if delete_post == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with Id {id} is not found")
  return Response(status_code=status.HTTP_204_NO_CONTENT)



# 41. Update Posts SQL Python: Part #43 Python API Course
https://www.youtube.com/watch?v=WePTe687gHI&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=43&ab_channel=SanjeevThiyagarajan


RETURNING *   - we can get returining update,insert,delete  object return all the column 



@app.put("/posts/{id}")
def update_post(id:int,post:Post):

  cursor.execute("""Update posts set title = %s , content= %s, published = %s where id = %s RETURNING *""", 
                 (post.title,post.content,post.published,str(id)))
  updated_post = cursor.fetchone()
  conn.commit()
  if updated_post ==None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with Id {id} not found")
  return {"data" : updated_post}



# 42. What is an ORM: Part #44 Python API Course
https://www.youtube.com/watch?v=WrvbIGZTSy0&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=44&ab_channel=SanjeevThiyagarajan


# 43. Sqlalchemy Python Setup: Part #40 Python API Course
https://www.youtube.com/watch?v=MHn1T2IZTLI&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=45&ab_channel=SanjeevThiyagarajan


SQLALCHAMEY-


https://docs.sqlalchemy.org/en/14/

https://docs.sqlalchemy.org/en/14/tutorial/index.html
https://docs.sqlalchemy.org/en/14/orm/session.html


pip install sqlalchemy
pip freeze
(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ pip install sqlalchemy


FASTAPI doc to connect with database - https://fastapi.tiangolo.com/tutorial/sql-databases/



database.py
main_orm.py
models.py

run
(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ uvicorn app.main_orm:app --reload


# 44. Sqlalchemy get all rows: Part #47 Python API Course
https://www.youtube.com/watch?v=aKu6tM7lHM4&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=46&ab_channel=SanjeevThiyagarajan


main_orm file


# 45. Sqlalchemy create row: Part #48 Python API Course
https://www.youtube.com/watch?v=S2keI887K-c&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=47&ab_channel=SanjeevThiyagarajan

create post -> main_orm file

# 46. Sqlalchemy Get Row by ID: Part #49 Python API Course
https://www.youtube.com/watch?v=Xza7gncxfmQ&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=48&ab_channel=SanjeevThiyagarajan



# 47. Sqlalchemy delete row: Part #50 Python API Course
https://www.youtube.com/watch?v=zoHCNrgEpFE&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=49&ab_channel=SanjeevThiyagarajan

https://docs.sqlalchemy.org/en/20/orm/session_basics.html#update-and-delete-with-arbitrary-where-clause


# 48. Sqlalchemy Update Row: Part #51 Python API Course
https://www.youtube.com/watch?v=q1qBr0OHrBI&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=50&ab_channel=SanjeevThiyagarajan



# 49. Pydantic vs Sqlalchemy Models: Part #52 Python API Course
https://www.youtube.com/watch?v=Yn174prreT8&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=51&ab_channel=SanjeevThiyagarajan

# 50. Pydantic Models Deep Dive: Part #53 Python API Course
https://www.youtube.com/watch?v=hpq6uk_ra_k&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=52&ab_channel=SanjeevThiyagarajan


schemas.py

# 51. FastAPI Response Model: Part #54 Python API Course
https://www.youtube.com/watch?v=nIVg0aY_cHU&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=53&ab_channel=SanjeevThiyagarajan



# 52. Create User Table: Part #55 Python API Course
https://www.youtube.com/watch?v=TCHQQ1b4Fz8&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=54&ab_channel=SanjeevThiyagarajan


# 53. User Registration Path: Part #56 Python API Course
https://www.youtube.com/watch?v=1A6H1Rrm0Tc&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=55&ab_channel=SanjeevThiyagarajan


# 54. Hashing User Password: Part #57 Python API Corse
https://www.youtube.com/watch?v=3TjiriUQeKk&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=56&ab_channel=SanjeevThiyagarajan



security - https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/

pip install "passlib[bcrypt]"


utils.py for hash password


# 55. Get User By Id: Part #58 Python API Course
https://www.youtube.com/watch?v=yEYXF9XtbE0&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=58&ab_channel=SanjeevThiyagarajan


# 56. FastAPI Routers: Part #59 Python API course
https://www.youtube.com/watch?v=D-3JJLpECGQ&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=59


# 57. FastAPI Prefix & Tags: Part #60 Python API Course
https://www.youtube.com/watch?v=4zwUOOrcihk&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=60

# 58. JWT Token Basics: Part #61 Python API Course
https://www.youtube.com/watch?v=BN9xKkzC55I&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=61


session based auth - we store sometyhing on backend api or database
JWT - somwething we store in frontent or client side


JWT

client                                      API

  /login (username+password)   ----------> if credentials are valid sign JWT Token (token)
  token sent to client         <----------    {token}

  /post/{token}             -------------->  verify token is valid

  Data given from API to client <-----------


  header - algorithm & type
  payload - data
  verify signature- base64urlencode(heade),base64urlencode(payload)


  ![alt text](image.png)


# 59. Login Proccess Flow: Part #62 Python API Course
https://www.youtube.com/watch?v=j4zfEisXsP4&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=63

![alt text](image-1.png)


# 60. Creating a JWT Token: Part #63 Python API Course
https://www.youtube.com/watch?v=wMdfkMQLAtA&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=64


https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/

pip install python-jose[cryptography]

pip install pyjwt


# to get a string like this run:
# openssl rand -hex 32


for - SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

#to check token
https://jwt.io/

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozNCwiZXhwIjoxNzE3MzM3ODMxfQ.4jolUpsJZY3SSmTBSvgW09QDL6wCTw1FL3U5IgtR4sc


# 61. OAUTH2 passwordRequestForm: Part #64 Python API Course
https://www.youtube.com/watch?v=abcGYup96MQ&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=65


# 62. Verify user is logged in: Part #65 Python API Course
https://www.youtube.com/watch?v=bDHtmflqZ4w&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=66


# 63. Testing Expired Tokens: Part #67 Python API Course
https://www.youtube.com/watch?v=daXIcUZYMTc&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=67


# 64. Postgres foreign keys: Part 71 Python API Course
https://www.youtube.com/watch?v=JtvgpKaMuhA&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=70


# 65. SqlAlchemy Foreign Keys: Part #72 Python API Course
https://www.youtube.com/watch?v=2WMXZgpADcQ&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=72


# 66. Update Post Schema to include user: Part #73 Python API Course
https://www.youtube.com/watch?v=sC_8fm4C5bU&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=73


# 67. Assigning owner id when create new post: Part #74 Python API Course
https://www.youtube.com/watch?v=gpWI4SO_XU4&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=74


# 68. Delete and Update only your own posts: Part #75 Python API Course
https://www.youtube.com/watch?v=FLRjiEYnm5Y&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=75


# 69. Retrieve Only Your Own Posts: Part #76 Python API Course
https://www.youtube.com/watch?v=RdaYFmUHZDw&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=77


# 70. sqlalchemy relationships: Part #77 Python API Course
https://www.youtube.com/watch?v=5JZMcCnVm3g&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=78


# 71. Query Parameters: Part #78 Python API Course
https://www.youtube.com/watch?v=cwdl9XBvwCc&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=79

http://127.0.0.1:8000/posts?limit=2

skip - http://127.0.0.1:8000/posts?limit=2&skip=7

search - http://127.0.0.1:8000/posts?limit=2&skip=0&search=new post
         http://127.0.0.1:8000/posts?search=new post


http://127.0.0.1:8000/posts?search=new%20post


# 71. Cleanup main.py file: Part #79 Python API Course
https://www.youtube.com/watch?v=dwb8qYJ3znc&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=80


# 72. Environment Variables: Part #80 Python API Course
https://www.youtube.com/watch?v=NCbeHpBVAvU&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=81


zec@zec-HP-EliteBook-840-G3:~$ export MY_DB_URL=*localhost:5432*
zec@zec-HP-EliteBook-840-G3:~$ printenv
echo %MY_DB_URL%


pip install pydantic-settings

from pydantic_settings import BaseSettings


in .gitignore

__pycache__
.venv/
.env



# 73. Vote/Like theory: Part #81 Python API Course
https://www.youtube.com/watch?v=mAaqiuT_FQw&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=82


# 74. Creating votes table pgadmin: Part #82 Python API Course
https://www.youtube.com/watch?v=6qhisaAcyKA&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=83


# 75. Votes with sqlalchemy: Part #83 Python API Course
https://www.youtube.com/watch?v=7O8Km1BIbj0&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=84


# 76. FastAPI Votes Route: Part# 84 Python API Course
https://www.youtube.com/watch?v=QlBkAHzVbE4&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=85


# 77. SQL Joins: Part #85 Python API Course
https://www.youtube.com/watch?v=cyfg7RP-u-0&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=87

https://www.postgresql.org/docs/current/tutorial-join.html


SELECT * FROM public.votes
ORDER BY user_id ASC, post_id ASC 


select posts.*,email,users.id from posts left join users on posts.owner_id = users.id

select users.id, count(*) from posts left join users on posts.owner_id = users.id group by users.id

select users.id,COUNT(*) from posts right join users on posts.owner_id = users.id group by users.id

select users.id,COUNT(posts.id) as user_post_count from posts right join users on posts.owner_id = users.id group by users.id

select * from votes

select * from posts left join votes on posts.id = votes.post_id;

select posts.id, count(*) from posts left join votes on posts.id = votes.post_id group by posts.id

select posts.*, count(votes.post_id) as votes from posts left join votes on posts.id = votes.post_id where posts.id = 19 group by posts.id

select * from posts left join votes on posts.id = votes.post_id 

select * from posts right join votes on posts.id = votes.post_id;


# 78. SQL Joins w/ SqlAlchemy: Part #86 Python API Course
https://www.youtube.com/watch?v=N7jIZnyEFek&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=88


http://127.0.0.1:8000/posts?search=SQL

http://127.0.0.1:8000/posts?limit=2


# 79. Get One Post Join: Part #87 Python API Course
https://www.youtube.com/watch?v=L_aCVz9vQmw&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=89

# 80. Database Migrations what is it: Part #88 Python API Course
https://www.youtube.com/watch?v=bLJ9jNWza6Y&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=90



# Best 6 Ai Tools For Designers

https://www.youtube.com/watch?v=yPuP5Wbvh9s&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=95

6 AI Tools

Tools mentioned:
Dall E2: https://labs.openai.com/
Astria: https://www.strmr.com/examples
Jasper: https://beta.jasper.ai/
Luma Ai: https://lumalabs.ai/
Runway ML: https://runwayml.com/
Durable: https://durable.co/ai-website-builder 


# Making Automatic YouTube videos with Python
https://www.youtube.com/watch?v=ZmSb3LZDdf0&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=97



# Python API Development Course: Part 2
https://www.youtube.com/watch?v=1N0nhahVdqs&t=225s


https://alembic.sqlalchemy.org/en/latest/tutorial.html

pip install alembic

alembic --help

(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic init

alembic init --help

(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic init alembic

(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic revision --help

# generate table file inside verison folder
(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic revision -m "create posts table"

https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations

(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic --help


(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic current

(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic upgrade --help


run below command to create table
(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic upgrade 93f19f84a922


# new version file to create table
(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic revision -m "add content column to posts table"

(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic current

(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic heads

(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic upgrade head

(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic downgrade 93f19f84a922

# to remove column
(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic downgrade -1


(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic revision -m "add user table"


(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic current

(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic history

(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic upgrade head

(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic revision -m "add foreign-key to posts table"

(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic revision -m "add last few columns to posts table"

(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic upgrade +1

(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic upgrade +1
root
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 5e1dadf0dfa8 -> 63e7c5ecfcf7, add foreign-key to posts table
(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic current
root
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
63e7c5ecfcf7
(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic heads
8317fd93a016 (head)
(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic upgrade head
root
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 63e7c5ecfcf7 -> 8317fd93a016, add last few columns to posts table
(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ 

(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic revision --autogenerate -m "auto-vote"
root
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'votes'
INFO  [alembic.ddl.postgresql] Detected sequence named 'posts_id_seq' as owned by integer column 'posts(id)', assuming SERIAL and omitting
INFO  [alembic.autogenerate.compare] Detected added index ''ix_posts_id'' on '('id',)'
  Generating /home/zec/Documents/Ajay/FastAPI-1/alembic/versions/901a8174c46e_auto_vote.py ...  done
(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ 


(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic revision --autogenerate -m "add phone number"
root
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added column 'users.phone_number'
  Generating /home/zec/Documents/Ajay/FastAPI-1/alembic/versions/d5df6c05a180_add_phone_number.py ...  done
(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ alembic upgrade head
root
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 901a8174c46e -> d5df6c05a180, add phone number
(.venv) zec@zec-HP-EliteBook-840-G3:~/Documents/Ajay/FastAPI-1$ 


# on console of goole.com error

fetch('http://localhost:8000/').then(res=>res.json()).then(console.log)
Promise {<pending>}
www.google.com/:1 Access to fetch at 'http://localhost:8000/' from origin 'https://www.google.com' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.
VM836:1 
        
        
       GET http://localhost:8000/ net::ERR_FAILED 200 (OK)
(anonymous) @ VM836:1



fetch('http://localhost:8000/').then(res=> res.json()).then(console.log)


# https://fastapi.tiangolo.com/tutorial/cors/?h=cors


pip freeze

# create and find all packages in requirements.txt file
pip freeze > requirements.txt


# any one can install all package
pip install -r requirements.txt



# GIT

git init