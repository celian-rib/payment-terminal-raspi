import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

if os.environ.get('PROD') == None :
    engine = create_engine('sqlite:///db/dev.sqlite3')
else :
    engine = create_engine('sqlite:///db/prod.sqlite3')

_SessionFactory = scoped_session(sessionmaker(bind=engine))

db = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import database.scan
    import database.user
    Base.metadata.create_all(bind=engine)

class Database():
    @staticmethod
    def drop_all():
        Base.metadata.drop_all(engine)

    def __init__(self, auto_commit=False, create_all=False):
        self.auto_commit = auto_commit
        self.session_factory = session_factory()

        if create_all:
            Base.metadata.create_all(engine)

    def __enter__(self):
        return self.session_factory

    def __exit__(self, type, value, traceback):
        if self.auto_commit:
            self.session_factory.commit()
        self.session_factory.flush()
        self.session_factory.close()

def session_factory():
    return _SessionFactory()