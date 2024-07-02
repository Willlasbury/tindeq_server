from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import tindeq, weights, users, grip_style

app = FastAPI()

origins = ["http://localhost:5173", "http://localhost:4173", "https://fingertester.netlify.app"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(tindeq.router)
app.include_router(weights.router)
app.include_router(grip_style.router)
