import os

env = os.environ

default_settings = {
    'sqlalchemy.url': env.get(
        'DATABASE_URL',
        'postgres://pyramid_api:pyramid_api@localhost/pyramid_api',
    ),
}
