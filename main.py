from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    price: int
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {
        "id": 1,
        "title": "Title of post 1", 
        "content": "content of post 1"
    },

    {
        "id": 2,
        "title": "Title of post 2", 
        "content": "content of post 2"
    },

]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


@app.get("/")
def root():
    return { "message" : "Welcome to my Api" }


@app.get("/posts")
def get_posts():
    return {"data" : my_posts}


@app.post('/posts')
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data" : post_dict}


# @app.get("/posts/latest")
# def get_latest_post():
#     post = my_posts[len(my_posts)-1]
#     return {"detail ": post}


@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    print(post)
    return {"Post_details " : post}

