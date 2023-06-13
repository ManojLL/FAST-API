from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote
engine = create_engine("mysql+pymysql://root:j123@localhost:3306/qr_container")
sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
base = declarative_base()
# connection = engine.connect()
