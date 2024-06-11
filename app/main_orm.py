# from fastapi import FastAPI,Response,status,HTTPException,Depends
# from typing import Optional,List
# from random import randrange
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time
# from sqlalchemy.orm import Session
# from . import models
# from .database import engine,SessionLocal
# from app import models,schemas,utils
# from app.database import engine, SessionLocal
# from app.database import engine, get_db


from fastapi import FastAPI
from fastapi.params import Body
from app import models
from app.database import engine
from app.routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware

from .config import settings


# models.Base.metadata.create_all(bind=engine) #dont need with alembic

# origins = ['https://www.google.com','https://www.youtube.com']
origins = ['*']


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# while True:
#   try:
#     conn = psycopg2.connect(host='localhost',database='fastapi',user='root',password='root',cursor_factory=RealDictCursor)
#     cursor = conn.cursor()
#     print("Database connection was successfull!!")
#     break
#   except Exception as error:
#     print("Connecting to database failed")
#     print("Error :", error)
#     time.sleep(2)



# @app.get("/sqlalchemy")
# def test_post(db:Session = Depends(get_db)):
# #   posts = db.query(models.Post)
# #   print(posts)
# #   return {"data":"posts"}
#   posts = db.query(models.Post).all()
# #   return {"data":posts}
#   return posts

@app.get("/")
def root():
  return {"message": "Hello World"}



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


  
