from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker
import json

#Create class manager, which will handle the database.
class Manager:
    Base = declarative_base()
    session = None

    #Create function which will create the database.
    def create_engine(self):
        engine = create_engine("sqlite:///C:\\Users\\arian\\Documents\\UTEC\\Desarrollo Basado en Plataformas\\RestorApp\\database\\midb.db?check_same_thread=False", echo=True)
        self.Base.metadata.create_all(engine)
        return engine

    #Create function which will get our session within the database.
    def get_session(self, engine):
        if self.session == None: #We check that there's not an open session
            Session = sessionmaker(bind=engine)
            session = Session()
        return session
