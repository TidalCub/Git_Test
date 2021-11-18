import sqlalchemy as db
from sqlalchemy import Table, Column, Integer, String, MetaData, delete, Float, Numeric, update, Boolean
import pandas as pd
from sqlalchemy.orm import sessionmaker
from  sqlalchemy.sql.expression import func


engine = db.create_engine('sqlite:///products.db',connect_args={'check_same_thread': False})
meta = MetaData()
conn = engine.connect()
Session = sessionmaker(bind = engine)
session = Session()

Services = Table(
    'Services', meta,
        Column('ID', Integer, primary_key = True),
        Column('Name', String),
        Column('img_URL',String),
        Column('Desc',String),
)
meta.create_all(engine)
print(session.query(Services).all())