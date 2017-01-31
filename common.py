import re
from sqlalchemy import create_engine

def sql_engine():

    fin = open("sql_credentials.txt")

    username = ""
    password = ""
    database = ""
    
    for line in fin:
        matches = re.search("(\w+) : (.+)",line)

        if matches is not None:

            if matches.group(1) == "username":
                username = matches.group(2)

            if matches.group(1) == "password":
                password = matches.group(2)

            if matches.group(1) == "database":
                database = matches.group(2)

    connect_param = "postgresql://{}:{}@joshuacook.me:5432/{}".format(\
        username, password, database)

    engine = create_engine(connect_param)

    return engine

def get_databases(engine):

    sql = "SELECT * FROM category"
    categories = pd.read_sql("SELECT * FROM category", con=engine)

    sql = "SELECT * FROM page"
    pages = pd.read_sql("SELECT * FROM page", con=engine)

    return (categories, pages)
