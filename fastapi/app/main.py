from typing import Optional
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from config import config

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
