from fastapi import FastAPI

app = FastAPI()

posts: list[dict] = [
    {"id": 1, "name": "abhishek"},
    {"id": 2, "name": "ram"},
    {"id": 3, "name": "krish"},
]


@app.get("/")
def home():
    return {"message": "hello ji kaise ho saare"}


@app.get("/posts")
def posts_list():
    return posts[0]["name"]
