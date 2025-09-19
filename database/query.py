from .connect import get_connect

conn = get_connect()

def is_register(chat_id):
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE chat_id=?", (chat_id,))
        return cur.fetchone()


def save_user(chat_id, fullname, phone, lat, long, username=None):
    try:
        with conn:
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO users (chat_id, fullname, username, phone, lat, long)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (chat_id, fullname, username, phone, lat, long),
            )
        return "Success"
    except Exception as e:
        print("save_user xato:", e)
        return None


def get_foods():
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM food")
        return cur.fetchall()


def get_food(id):
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM food WHERE id=?", (id,))
        return cur.fetchone()


def save_order(food_id, user_id, quantity, price):
    with conn:
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO orders (food_id, user_id, quantity, price, status)
            VALUES (?, ?, ?, ?, ?)
            """,
            (food_id, user_id, quantity, price, "new"),
        )


def get_order_info(user_id):
    with conn:
        cur = conn.cursor()
        cur.execute(
            """
            SELECT 
                food.name,
                orders.quantity,
                orders.price,
                orders.status,
                orders.created_at
            FROM orders
            JOIN food ON orders.food_id = food.id
            WHERE orders.user_id = ?
            ORDER BY orders.created_at DESC
            """,
            (user_id,),
        )
        return cur.fetchall()


# --- ADMIN FUNKSIYALAR ---

def is_admin(chat_id):
    try:
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE chat_id=?", (chat_id,))
            return cur.fetchone()
    except:
        return None


def is_new_foods():
    try:
        with conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT 
                    o.id AS order_id,
                    f.name AS food_name,
                    u.chat_id AS user_id,
                    o.quantity,
                    o.price,
                    (o.quantity * o.price) AS total_price,
                    o.status
                FROM orders o
                JOIN food f ON o.food_id = f.id
                JOIN users u ON o.user_id = u.id
                WHERE o.status = 'new'
            """)
            return cur.fetchall()
    except:
        return None


def is_progress_foods():
    try:
        with conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT 
                    o.id AS order_id,
                    f.name AS food_name,
                    u.chat_id AS user_id,
                    o.quantity,
                    o.price,
                    (o.quantity * o.price) AS total_price,
                    o.status
                FROM orders o
                JOIN food f ON o.food_id = f.id
                JOIN users u ON o.user_id = u.id
                WHERE o.status = 'in_progress'
            """)
            return cur.fetchall()
    except:
        return None


def is_finished_foods():
    try:
        with conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT 
                    o.id AS order_id,
                    f.name AS food_name,
                    u.chat_id AS user_id,
                    o.quantity,
                    o.price,
                    (o.quantity * o.price) AS total_price,
                    o.status
                FROM orders o
                JOIN food f ON o.food_id = f.id
                JOIN users u ON o.user_id = u.id
                WHERE o.status = '🏁 Finished'
            """)
            return cur.fetchall()
    except Exception as e:
        print("Finished orders olishda xato:", e)
        return None


def update_order(order_id):
    try:
        with conn:
            cur = conn.cursor()
            cur.execute("UPDATE orders SET status='cancel' WHERE id=?", (order_id,))
        return True
    except:
        return None


def update_order_status(order_id: int, status: str):
    try:
        with conn:
            cur = conn.cursor()
            cur.execute("UPDATE orders SET status=? WHERE id=?", (status, order_id))
        return True
    except Exception as e:
        print("Update xato:", e)
        return None


def add_food(data: dict):
    try:
        with conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO food (name, description, image, price, quantity) VALUES (?, ?, ?, ?, ?)",
                (data["name"], data["desc"], data["image"], data["price"], data["quantity"]),
            )
        return True
    except Exception as e:
        print("add_food xato:", e)
        return None


def delete_food(food_id: int):
    try:
        with conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM food WHERE id=?", (food_id,))
        return True
    except Exception as e:
        print("Delete xato:", e)
        return None
