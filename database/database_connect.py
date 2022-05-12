import settings
from api import app
from tortoise.contrib.fastapi import register_tortoise


def connect_database():
    register_tortoise(app=app, config=settings.DATABASE_CONFIG)
