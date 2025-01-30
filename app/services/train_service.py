def add_train(data):
    conn = psycopg2.connect("dbname=irctc user=admin password=admin")
    cur = conn.cursor()
    cur.execute("INSERT INTO trains (name, source, destination, total_seats, available_seats) VALUES (%s, %s, %s, %s, %s)",
                (data['name'], data['source'], data['destination'], data['total_seats'], data['total_seats']))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Train added successfully"}

def get_trains(source, destination):
    conn = psycopg2.connect("dbname=irctc user=admin password=admin")
    cur = conn.cursor()
    cur.execute("SELECT * FROM trains WHERE source = %s AND destination = %s", (source, destination))
    trains = cur.fetchall()
    cur.close()
    conn.close()
    return {"trains": trains}
