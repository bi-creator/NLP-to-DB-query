import psycopg2
def executeQuery(query):
    conn = psycopg2.connect(
        database="FirstDb", user='postgres', password='manjith', host='localhost', port= '5432'
        )
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchone()
    conn.close()
    return(data)
