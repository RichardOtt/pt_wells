import sqlalchemy
import sys
import os

def get_wells(depth, gradient):
    query_raw = """SELECT latitude, longitude, depth, gradient
        FROM wells
        WHERE depth >= :depth AND gradient >= :gradient;"""
    
    sql_connect_string = os.getenv("DB_URL")
    engine = sqlalchemy.create_engine(sql_connect_string)
    
    with engine.connect() as conn:
        query = sqlalchemy.text(query_raw)
        results = conn.execute(query, {'depth': depth, 'gradient': gradient})
    
    return results.fetchall()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: database.py depth gradient")
        sys.exit()
    depth = sys.argv[1]
    grad = sys.argv[2]
    for row in get_wells(depth, grad):
        print(row)