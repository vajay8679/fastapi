from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body

from typing import Optional
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

class Post(BaseModel):
  title: str
  content: str
  published: bool =True
  rating: Optional[int] =None

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


#Get all
@app.get("/posts")
def get_posts():
  cursor.execute("""select * from posts""")
  posts =  cursor.fetchall()
  print(posts)
  return {"data": posts}



#Post Data
@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
  cursor.execute("""Insert into posts(title,content,published) values(%s,%s,%s) RETURNING *""",
                 (post.title,post.content,post.published))
  new_post = cursor.fetchone()
  conn.commit()
  return {"data": new_post}  


#Get one
@app.get("/posts/{id}")
def get_post(id: int):
  cursor.execute("""Select * from posts where id = %s """,(str(id),))
  post = cursor.fetchone()
  # print(post)
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id : {id} not found")
  return {"post_detail": post}


#Delete One
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
  cursor.execute("""DELETE from posts where id = %s returning *""",(str(id),))
  delete_post = cursor.fetchone()
  conn.commit()
  if delete_post == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with Id {id} is not found")
  return Response(status_code=status.HTTP_204_NO_CONTENT)


#Update one data
@app.put("/posts/{id}")
def update_post(id:int,post:Post):
  cursor.execute("""Update posts set title = %s , content= %s, published = %s where id = %s RETURNING *""", 
                 (post.title,post.content,post.published,str(id)))
  updated_post = cursor.fetchone()
  conn.commit()
  if updated_post ==None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with Id {id} not found")
  return {"data" : updated_post}