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




my_posts = [{"title":"Title of 1","content":"Content of 1","id":1},{"title":"Food fanda","content":"Foood was very good","id":2}]
#request get method url: "/"

def find_post(id):
  for p in my_posts:
    if p['id'] == id:
      return p
    
  
def find_index_post(id):
  for i,p in enumerate(my_posts):
    if p['id'] == id:
      return i

@app.get("/")
def root():
  return {"message": "Hello World"}


# @app.get("/posts")
# def get_posts():
#   return {"data": my_posts}


@app.get("/posts")
def get_posts():
  cursor.execute("""select * from posts""")
  posts =  cursor.fetchall()
  print(posts)
  return {"data": posts}


# @app.post("/createposts")
# def create_post(payload: dict=Body(...)):
#   print(payload)
#   return {"new_post": f"title is: {payload['title']} and conetent is : {payload['content']}"}

# @app.post("/posts",status_code=status.HTTP_201_CREATED)
# def create_post(post: Post):
#   print(post)
# #   print(post.title)
# #   print(post.published)
# #   print(post.rating)
# #   print(post.dict())
#   post_dict = post.dict()
#   post_dict['id'] = randrange(1,1000000)
#   my_posts.append(post_dict)
#   return {"data": post_dict}  


@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
  cursor.execute("""Insert into posts(title,content,published) values(%s,%s,%s) RETURNING *""",
                 (post.title,post.content,post.published))
  new_post = cursor.fetchone()
  conn.commit()
  return {"data": new_post}  

@app.get("/posts/latest")
def get_latest_post():
  lates_post = my_posts[len(my_posts) - 1]
  return {"message": lates_post}


# @app.get("/posts/{id}")
# def get_post(id: int,response: Response):
#   print(id)
#   # post = find_post(int(id))
#   # return {"message": f"Here is the Id: {id}"}
#   post = find_post(id)
#   if not post:
#     # response.status_code = 404
#     # response.status_code = status.HTTP_404_NOT_FOUND
#     # return {"message": f"Post with id {id} not found"}
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id : {id} not found")
#   return {"message": post}


@app.get("/posts/{id}")
def get_post(id: int):
  cursor.execute("""Select * from posts where id = %s """,(str(id),))
  post = cursor.fetchone()
  # print(post)
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id : {id} not found")
  return {"post_detail": post}


# @app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id:int):
#   #deleteing post
#   #find the index in the array that has required id
#   index = find_index_post(id)
#   if index == None:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with Id {id} is not found")

#   my_posts.pop(index)
#   return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
  cursor.execute("""DELETE from posts where id = %s returning *""",(str(id),))
  delete_post = cursor.fetchone()
  conn.commit()
  if delete_post == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with Id {id} is not found")
  return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put("/posts/{id}")
# def update_post(id:int,post:Post):
#   # print(post)
#   index = find_index_post(id)

#   if index ==None:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with Id {id} not found")
  
#   new_post = post.dict()
#   new_post['id'] = id
#   my_posts[index] = new_post

#   return {"data" : new_post}


@app.put("/posts/{id}")
def update_post(id:int,post:Post):

  cursor.execute("""Update posts set title = %s , content= %s, published = %s where id = %s RETURNING *""", 
                 (post.title,post.content,post.published,str(id)))
  updated_post = cursor.fetchone()
  conn.commit()
  if updated_post ==None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with Id {id} not found")
  return {"data" : updated_post}