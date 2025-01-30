from werkzeug.security import generate_password_hash, check_password_hash

def register_user(data):
    conn = psycopg2.connect("dbname=irctc user=admin password=admin")
    cur = conn.cursor()
    password_hash = generate_password_hash(data['password'])
    cur.execute("INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)", (data['username'], password_hash, data['role']))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "User registered successfully"}

def login_user(data):
    conn = psycopg2.connect("dbname=irctc user=admin password=admin")
    cur = conn.cursor()
    cur.execute("SELECT id, password_hash FROM users WHERE username = %s", (data['username'],))
    user = cur.fetchone()
    cur.close()
    conn.close()
    if user and check_password_hash(user[1], data['password']):
        return {"message": "Login successful", "user_id": user[0]}
    return {"error": "Invalid credentials"}, 401
