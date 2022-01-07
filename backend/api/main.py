"""Main."""
import logging
import os
import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .interfaces.db import db_models
from .interfaces.db.database import engine
from .external_interfaces import user_router, record_router

db_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://192.168.0.21:3000",
    "http://0.0.0.0:8000",

]

if 'ALLOW_ORIGIN' in os.environ:
    origins.append(os.environ['ALLOW_ORIGIN'])

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router.router, prefix="/api")
app.include_router(record_router.router, prefix="/api")


logger = logging.getLogger(__name__)

sh = logging.StreamHandler(sys.stdout)
sh.setLevel(logging.DEBUG)


