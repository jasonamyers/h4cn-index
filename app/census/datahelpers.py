from sqlalchemy import Table, MetaData, create_engine
from config import SQLALCHEMY_DATABASE_URI

metadata = MetaData()
engine = create_engine(SQLALCHEMY_DATABASE_URI)


def build_table(table_name):
    return Table(table_name, metadata, autoload=True, autoload_with=engine)
