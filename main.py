from fastapi import FastAPI

app = FastAPI()

# GET 1: Welcome message
@app.get("/")
def home():
    return {"message":  "Welcome to Hello FastAPI!"}

# GET 2: Plain string greeting
@app.get("/hello")
def hello():
    return {"message": "Hello, FastAPI!"}

# GET 3: Application information
@app.get("/info")
def info():
    return {
        "name": "Hello FastAPI",
        "version": "1.0.0",
        "description": "A simple FastAPI application with five GET endpoints."
    }

# GET 4: Return a list of items
app.get("/items")
def get_items():
 return [
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Keyboard"},
        {"id": 3, "name": "Mouse"}
    ]

# GET 5: Return an item using its ID
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {
        "item_id": item_id,
        "name": f"Item {item_id}"
    }