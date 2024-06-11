from fastapi import FastAPI,Response,status,HTTPException,Depends, APIRouter
from typing import List,Optional
from sqlalchemy.orm import Session
from app import models,schemas,utils
from app.database import engine, get_db
from app import oauth2
from sqlalchemy import func

router = APIRouter(
  prefix="/posts",
  tags=["Posts"]
)

# @router.get("/",response_model=List[schemas.Post])
@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db:Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user),limit:int = 10,skip:int = 0,search:Optional[str]=""):
  # posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all() #all individual post based on login
  # posts = db.query(models.Post).all() #all common post
  # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

  post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

  # print(post)

  # print(limit)
  # print(search)
  # return posts
  return post



@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db:Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
#   new_post = models.Post(title = post.title,content = post.content,published = post.published)

  print(current_user.id)
  print(current_user.email)
  new_post = models.Post(owner_id = current_user.id, **post.dict())
#   print(post.dict())
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  return new_post


# @router.get("/{id}",response_model=schemas.Post)
@router.get("/{id}",response_model=schemas.PostOut)
def get_post(id: int,db:Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

  # post = db.query(models.Post).filter(models.Post.id == id).first()

  post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()

  # print(post)
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id : {id} not found")
  
  return post



@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
  post_query = db.query(models.Post).filter(models.Post.id == id)
 
  post = post_query.first()
  if post == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with Id {id} is not found")
  
  if post.owner_id != current_user.id:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform request action")
  
  post_query.delete(synchronize_session=False)
  db.commit()

  return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/{id}",response_model=schemas.Post)
def update_post(id:int,updated_post:schemas.PostCreate,db:Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
  new_post = db.query(models.Post).filter(models.Post.id == id)
  post = new_post.first()

  if post ==None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with Id {id} not found")
  
  if post.owner_id != current_user.id:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform request action")
  
  new_post.update(updated_post.dict(),synchronize_session=False)
  db.commit()

  return new_post.first()
