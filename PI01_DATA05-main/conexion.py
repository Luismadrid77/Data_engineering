import pymysql
from sqlalchemy import create_engine

cadena_cone = 'mysql+pymysql://root:123456789@localhost:3306/proyecto01'

cone = create_engine(cadena_cone)
conn = cone.connect()

