from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise


def create_app(test_config=None):
    app = FastAPI()
    origins = [
        "http://localhost",
        "http://localhost:8080",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    register_tortoise(
        app,
        db_url='sqlite://sapi.db',
        modules={'models': ["db"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )

    return app


TORTOISE_ORM = {
    "connections": {
        "default": 'sqlite://ip.db'
    },
    "apps": {
        "models": {
            "models": [
                "db", "aerich.models"
            ],
            "default_connection": "default",
        },
    },
}