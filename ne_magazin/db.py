import sqlite3

DB_NAME = "shop.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
        create table if not exists users (
            id integer primary key autoincrement,
            username text unique not null,
            password text not null,
            points integer default 0
        )
    ''')

    cursor.execute('''
        create table if not exists products (
            id integer primary key autoincrement,
            name text not null,
            cost integer not null,
            count integer not null
        )
    ''')

    cursor.execute('''
        create table if not exists orders (
            id integer primary key autoincrement,
            user_id integer not null,
            product_id integer not null,
            count integer not null,
            foreign key (user_id) references users(id),
            foreign key (product_id) references products(id)
        )
    ''')

    cursor.execute('''
        create table if not exists tickets (
            uuid text primary key,
            available boolean default 1,
            user_id integer,
            foreign key (user_id) references users(id)
        )
    ''')

    conn.commit()
    conn.close()


def seed_tickets():
    import uuid
    conn = connect()
    cursor = conn.cursor()

    for _ in range(3):
        ticket_uuid = str(uuid.uuid4())
        cursor.execute("insert into tickets (uuid, available) values (?, 1)", (ticket_uuid,))

    conn.commit()
    conn.close()

def clear_data():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("delete from users")
    cursor.execute("delete from products")
    cursor.execute("delete from orders")
    cursor.execute("delete from tickets")
    conn.commit()
    conn.close()
    print("Все данные очищены.")

