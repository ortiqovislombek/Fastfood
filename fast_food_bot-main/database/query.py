from .connect import get_connect

conn = get_connect()
conn.autocommit = True

def is_register(chat_id):
    with  conn as db:
        with db.cursor() as dbc:
            try:
                dbc.execute("select * from users where chat_id = %s",(chat_id,))

                return dbc.fetchone()
            except:
                return None
        

def save_user(chat_id,fullname,phone,lat,long,username=None):
    with  conn as db:
        with db.cursor() as dbc:
            try:
                dbc.execute("""
                    Insert into users (chat_id,fullname,username, phone,lat,long) values(%s,%s,%s,%s,%s,%s);
                    """,(chat_id,fullname,username,phone,lat,long))
                return "Success"
            except:

                return None
            
        

def get_foods():
    with conn as db:
        with db.cursor() as dbc:

            dbc.execute("select * from food")
            foods = dbc.fetchall()

    return foods


def get_food(id):
    with conn as db:
        with db.cursor() as dbc:
            dbc.execute("select * from food where id =%s",(id,))
            foods = dbc.fetchone()
    return foods


def save_order(food_id,user_id,quantity,price):

    with conn as db:
        with db.cursor() as dbc:

            dbc.execute("""
        Insert into orders (food_id,user_id,quantity,price,status) values(%s,%s,%s,%s,%s)
    """,(food_id,user_id,quantity,price,"new"))
            

def is_admin(chat_id):

    try:

        with conn as db:
            with db.cursor() as dbc:

                dbc.execute("select * from users where chat_id = %s",(chat_id,))
                data = dbc.fetchone()
                
        return data

    except:
        return None
    

def is_new_foods():
    try:

        with conn as db:
            with db.cursor() as dbc:

                dbc.execute("""
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
WHERE o.status = 'new';
                
""")
                data = dbc.fetchall()
                
        return data

    except:
        return None



def is_progress_foods():
    try:

        with conn as db:
            with db.cursor() as dbc:

                dbc.execute("""
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
WHERE o.status = 'in_progress';
                
""")
                data = dbc.fetchall()
                
        return data

    except:
        return None



def update_order(order_id):
    try:

        with conn as db:
            with db.cursor() as dbc:
                dbc.execute("update orders set status = 'cancel' where id = %s",(order_id,))
                
        return True

    except:
        return None
    
                


