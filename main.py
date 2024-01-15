from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import tindeq, weights, users

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def test():
    return {
        "message":"hello"
    }
app.include_router(users.router)
app.include_router(tindeq.router)
app.include_router(weights.router)
