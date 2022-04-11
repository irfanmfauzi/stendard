from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from config import setting

engine = create_engine(
    f'{setting.DB_ENGINE}+psycopg2://{setting.DB_USERNAME}:{setting.DB_PASS}@{setting.DB_HOST}/{setting.DB_NAME}')
session = sessionmaker(bind=engine)

BaseModel = declarative_base()
