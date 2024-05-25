from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)
DATABASE = 'shop.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS customer (
            customer_id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS product (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS purchase (
            purchase_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            purchase_date TEXT,
            FOREIGN KEY (customer_id) REFERENCES customer (customer_id),
            FOREIGN KEY (product_id) REFERENCES product (product_id)
        )
    ''')
    conn.commit()
    conn.close()

def populate_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM customer')
    if c.fetchone()[0] == 0:
        c.executemany('INSERT INTO customer (customer_id, name, age) VALUES (?, ?, ?)', [
            (1, 'Suyon', 2002),
            (2, 'Seonghyun', 2003),
            (3, 'Kimgeon', 2004),
            (4, 'Kimseongjun', 2005),
            (5, 'ITM', 2000),
            (6, 'Seoultech', 1999),
            (7, 'MIT', 1998),
            (8, 'CIA', 1997),
            (9, 'FBI', 1996)
        ])
    c.execute('SELECT COUNT(*) FROM product')
    if c.fetchone()[0] == 0:
        c.executemany('INSERT INTO product (product_id, product_name) VALUES (?, ?)', [
            (1, 'AK-47'),
            (2, 'C4'),
            (3, 'Ammo'),
            (4, 'Biscuit'),
            (5, 'Baguette'),
            (6, 'Water Bottle'),
            (7, 'Water 20Box'),
            (8, 'Pencil'),
            (9, 'MG-42'),
            (10, 'M16'),
            (11, 'RPG'),
            (12, 'Evian Water'),
            (13, 'Chair'),
            (14, 'MacBook M2'),
            (15, 'iPad'),
            (16, 'Galaxy 15'),
            (17, 'Keyboard'),
            (18, 'Mouse'),
            (19, 'Monitor'),
            (20, 'Desk')
        ])
    c.execute('SELECT COUNT(*) FROM purchase')
    if c.fetchone()[0] == 0:
        c.executemany('INSERT INTO purchase (purchase_id, customer_id, product_id, quantity, purchase_date) VALUES (?, ?, ?, ?, ?)', [
            (1, 1, 1, 3, '2024-01-01'),
            (2, 1, 2, 2, '2024-01-02'),
            (3, 1, 3, 5, '2024-01-03'),
            (4, 2, 4, 1, '2024-01-01'),
            (5, 2, 5, 3, '2024-01-02'),
            (6, 3, 6, 10, '2024-01-01'),
            (7, 3, 7, 8, '2024-01-02'),
            (8, 3, 8, 2, '2024-01-03'),
            (9, 1, 9, 1, '2024-01-04'),
            (10, 1, 10, 1, '2024-01-05'),
            (11, 2, 11, 2, '2024-01-06'),
            (12, 2, 12, 3, '2024-01-07'),
            (13, 4, 1, 4, '2024-01-08'),
            (14, 4, 2, 5, '2024-01-09'),
            (15, 4, 3, 6, '2024-01-10'),
            (16, 4, 4, 7, '2024-01-11'),
            (17, 4, 5, 8, '2024-01-12'),
            (18, 4, 6, 9, '2024-01-13'),
            (19, 4, 7, 10, '2024-01-14'),
            (20, 4, 8, 11, '2024-01-15'),
            (21, 5, 13, 1, '2024-02-01'),
            (22, 5, 14, 1, '2024-02-02'),
            (23, 5, 15, 1, '2024-02-03'),
            (24, 5, 16, 1, '2024-02-04'),
            (25, 6, 17, 2, '2024-03-01'),
            (26, 6, 18, 2, '2024-03-02'),
            (27, 6, 19, 2, '2024-03-03'),
            (28, 6, 20, 2, '2024-03-04'),
            (29, 7, 13, 1, '2024-04-01'),
            (30, 7, 14, 1, '2024-04-02'),
            (31, 7, 15, 1, '2024-04-03'),
            (32, 7, 16, 1, '2024-04-04'),
            (33, 8, 17, 3, '2024-05-01'),
            (34, 8, 18, 3, '2024-05-02'),
            (35, 8, 19, 3, '2024-05-03'),
            (36, 8, 20, 3, '2024-05-04'),
            (37, 9, 1, 5, '2024-06-01'),
            (38, 9, 2, 4, '2024-06-02'),
            (39, 9, 3, 6, '2024-06-03'),
            (40, 9, 4, 5, '2024-06-04'),
            (41, 9, 5, 4, '2024-06-05'),
            (42, 9, 6, 3, '2024-06-06'),
            (43, 9, 7, 2, '2024-06-07'),
            (44, 9, 8, 1, '2024-06-08'),
            (45, 9, 9, 1, '2024-06-09'),
            (46, 9, 10, 1, '2024-06-10'),
            (47, 9, 11, 1, '2024-06-11'),
            (48, 9, 12, 1, '2024-06-12'),
            (49, 9, 13, 1, '2024-06-13'),
            (50, 9, 14, 1, '2024-06-14')
        ])
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_customer', methods=['POST'])
def add_customer():
    data = request.get_json()
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('INSERT INTO customer (name, age) VALUES (?, ?)', (data['name'], data['age']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Customer added successfully!"})

@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.get_json()
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('INSERT INTO product (product_name) VALUES (?)', (data['product_name'],))
    conn.commit()
    conn.close()
    return jsonify({"message": "Product added successfully!"})

@app.route('/add_purchase', methods=['POST'])
def add_purchase():
    data = request.get_json()
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('INSERT INTO purchase (customer_id, product_id, quantity, purchase_date) VALUES (?, ?, ?, ?)', 
              (data['customer_id'], data['product_id'], data['quantity'], data['purchase_date']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Purchase added successfully!"})

@app.route('/get_customers', methods=['GET'])
def get_customers():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM customer')
    customers = [{"customer_id": row[0], "name": row[1], "age": row[2]} for row in c.fetchall()]
    conn.close()
    return jsonify(customers)

@app.route('/get_products', methods=['GET'])
def get_products():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM product')
    products = [{"product_id": row[0], "product_name": row[1]} for row in c.fetchall()]
    conn.close()
    return jsonify(products)

@app.route('/get_purchases', methods=['GET'])
def get_purchases():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM purchase')
    purchases = [{"purchase_id": row[0], "customer_id": row[1], "product_id": row[2], "quantity": row[3], "purchase_date": row[4]} for row in c.fetchall()]
    conn.close()
    return jsonify(purchases)

@app.route('/search_cart', methods=['GET'])
def search_cart():
    customer_id = request.args.get('customer_id')
    product_name = request.args.get('product_name')
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        SELECT purchase.purchase_id, customer.name, product.product_name, purchase.quantity, purchase.purchase_date
        FROM purchase
        JOIN customer ON purchase.customer_id = customer.customer_id
        JOIN product ON purchase.product_id = product.product_id
        WHERE customer.customer_id = ? AND product.product_name = ?
    ''', (customer_id, product_name))
    cart_items = [{"purchase_id": row[0], "customer_name": row[1], "product_name": row[2], "quantity": row[3], "purchase_date": row[4]} for row in c.fetchall()]
    conn.close()
    return jsonify(cart_items)

if __name__ == '__main__':
    init_db()
    populate_db()
    app.run(debug=True)
