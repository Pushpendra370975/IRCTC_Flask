import psycopg2

def book_seat(data):
    user_id = data['user_id']
    train_id = data['train_id']
    conn = psycopg2.connect("dbname=irctc user=admin password=admin")
    cur = conn.cursor()
    try:
        cur.execute("SELECT available_seats FROM trains WHERE id = %s FOR UPDATE", (train_id,))
        result = cur.fetchone()
        if result and result[0] > 0:
            cur.execute("UPDATE trains SET available_seats = available_seats - 1 WHERE id = %s", (train_id,))
            cur.execute("INSERT INTO bookings (user_id, train_id, seat_number) VALUES (%s, %s, %s) RETURNING id", (user_id, train_id, result[0]))
            conn.commit()
            return {"message": "Booking successful", "booking_id": cur.fetchone()[0]}
        else:
            return {"error": "No available seats"}, 400
    finally:
        cur.close()
        conn.close()

def get_booking(booking_id):
    conn = psycopg2.connect("dbname=irctc user=admin password=admin")
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookings WHERE id = %s", (booking_id,))
    booking = cur.fetchone()
    cur.close()
    conn.close()
    return {"booking": booking} if booking else {"error": "Booking not found"}, 404