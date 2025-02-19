# from flask import Flask, render_template, request
# import mysql.connector
# import os

# app = Flask(__name__)

# # Database configuration (replace with your actual credentials)
# db_config = {
#     'user': 'root',
#     'password': '1234',
#     'host': 'localhost',
#     'database': 'smart_inventory'
# }


# def connect_db():
#     try:
#         conn = mysql.connector.connect(**db_config)
#         print("Database connection established successfully!")  # Debugging
#         return conn
#     except mysql.connector.Error as err:
#         print(f"Database connection failed: {err}")  # Debugging
#         return None


# @app.route('/register_store', methods=['GET', 'POST'])
# def register_store():
#     error = None
#     if request.method == 'POST':
#         store_name = request.form.get('store_name')
#         if not store_name:
#             error = "Store name is required"
#             return render_template('register_store.html', error=error)

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 sql = "INSERT INTO stores (store_name) VALUES (%s)"
#                 cursor.execute(sql, (store_name,))
#                 conn.commit()
#                 cursor.close()
#                 conn.close()
#                 message = "Success!"

#                 return render_template('register_success.html', store_name=store_name, message = message)
#             except mysql.connector.Error as db_err:
#                 error = f"Database error: {db_err}"
#                 return render_template('register_store.html', error=error)
#         else:
#             error = "Failed to connect to the database"

#     return render_template('register_store.html', error=error)


# @app.route('/')
# def index():
#     return render_template('login.html')


# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for  # Added redirect and url_for
# import mysql.connector
# import os

# app = Flask(__name__)

# # Database configuration (replace with your actual credentials)
# db_config = {
#     'user': 'root',
#     'password': '1234',
#     'host': 'localhost',
#     'database': 'smart_inventory'
# }


# def connect_db():
#     try:
#         conn = mysql.connector.connect(**db_config)
#         print("Database connection established successfully!")  # Debugging
#         return conn
#     except mysql.connector.Error as err:
#         print(f"Database connection failed: {err}")  # Debugging
#         return None


# @app.route('/register_store', methods=['GET', 'POST'])
# def register_store():
#     error = None
#     if request.method == 'POST':
#         store_name = request.form.get('store_name')
#         if not store_name:
#             error = "Store name is required"
#             return render_template('register_store.html', error=error)

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 sql = "INSERT INTO stores (store_name) VALUES (%s)"
#                 cursor.execute(sql, (store_name,))
#                 conn.commit()
#                 store_id = cursor.lastrowid  # Get the store ID

#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('login'))  # Redirect to login page

#             except mysql.connector.Error as db_err:
#                 error = f"Database error: {db_err}"
#                 return render_template('register_store.html', error=error)
#         else:
#             error = "Failed to connect to the database"

#     return render_template('register_store.html', error=error)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         store_id = request.form.get('store_id')  # Get store ID from the form

#         conn = connect_db()
#         if conn:
#             cursor = conn.cursor()
#             sql = "SELECT * FROM stores WHERE id = %s"
#             cursor.execute(sql, (store_id,))
#             store = cursor.fetchone()  # Get store details
#             cursor.close()
#             conn.close()

#             if store:
#                 # Login successful, redirect to dashboard
#                 return redirect(url_for('dashboard', store_id=store_id))
#             else:
#                 # Login failed
#                 return render_template('login.html', error="Invalid store ID")
#         else:
#             return render_template('login.html', error="Failed to connect to the database")

#     return render_template('login.html')

# @app.route('/dashboard/<store_id>') #Added a route for the dashboard
# def dashboard(store_id):
#     return render_template('dashboard.html', store_id = store_id)


# @app.route('/')
# def index():
#     return render_template('login.html')

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for
# import mysql.connector
# import os

# app = Flask(__name__)

# # Database configuration (replace with your actual credentials)
# db_config = {
#     'user': 'root',
#     'password': '1234',
#     'host': 'localhost',
#     'database': 'smart_inventory'
# }


# def connect_db():
#     try:
#         conn = mysql.connector.connect(**db_config)
#         print("Database connection established successfully!")
#         return conn
#     except mysql.connector.Error as err:
#         print(f"Database connection failed: {err}")
#         return None


# @app.route('/register_store', methods=['GET', 'POST'])
# def register_store():
#     error = None
#     if request.method == 'POST':
#         store_name = request.form.get('store_name')
#         if not store_name:
#             error = "Store name is required"
#             return render_template('register_store.html', error=error)

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 sql = "INSERT INTO stores (store_name) VALUES (%s)"
#                 cursor.execute(sql, (store_name,))
#                 conn.commit()
#                 store_id = cursor.lastrowid  # Get the store ID
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('login'))  # Redirect to login page

#             except mysql.connector.Error as db_err:
#                 error = f"Database error: {db_err}"
#                 return render_template('register_store.html', error=error)
#         else:
#             error = "Failed to connect to the database"

#     return render_template('register_store.html', error=error)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         store_id = request.form.get('store_id')  # Get store ID from the form

#         conn = connect_db()
#         if conn:
#             cursor = conn.cursor()
#             sql = "SELECT * FROM stores WHERE id = %s"
#             cursor.execute(sql, (store_id,))
#             store = cursor.fetchone()  # Get store details
#             cursor.close()
#             conn.close()

#             if store:
#                 # Login successful, redirect to dashboard
#                 return redirect(url_for('dashboard', store_id=store_id))
#             else:
#                 # Login failed
#                 return render_template('login.html', error="Invalid store ID")
#         else:
#             return render_template('login.html', error="Failed to connect to the database")

#     return render_template('login.html')


# @app.route('/dashboard/<store_id>')
# def dashboard(store_id):
#     return render_template('dashboard.html', store_id=store_id)


# @app.route('/')
# def index():
#     return render_template('login.html')


# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for
# import mysql.connector
# import os

# app = Flask(__name__)

# # Database configuration (replace with your actual credentials)
# db_config = {
#     'user': 'root',
#     'password': '1234',
#     'host': 'localhost',
#     'database': 'smart_inventory'
# }


# def connect_db():
#     try:
#         conn = mysql.connector.connect(**db_config)
#         print("Database connection established successfully!")
#         return conn
#     except mysql.connector.Error as err:
#         print(f"Database connection failed: {err}")
#         return None


# @app.route('/register_store', methods=['GET', 'POST'])
# def register_store():
#     error = None
#     if request.method == 'POST':
#         store_name = request.form.get('store_name')
#         if not store_name:
#             error = "Store name is required"
#             return render_template('register_store.html', error=error)

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 # Check if store already exists
#                 sql = "SELECT id FROM stores WHERE store_name = %s"
#                 cursor.execute(sql, (store_name,))
#                 existing_store = cursor.fetchone()

#                 if existing_store:
#                     error = "Store already exists!"
#                     return render_template('register_store.html', error=error)

#                 sql = "INSERT INTO stores (store_name) VALUES (%s)"
#                 cursor.execute(sql, (store_name,))
#                 conn.commit()
#                 store_id = cursor.lastrowid  # Get the store ID
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('login'))  # Redirect to login page

#             except mysql.connector.Error as db_err:
#                 error = f"Database error: {db_err}"
#                 return render_template('register_store.html', error=error)
#         else:
#             error = "Failed to connect to the database"

#     return render_template('register_store.html', error=error)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         store_id = request.form.get('store_id')  # Get store ID from the form

#         conn = connect_db()
#         if conn:
#             cursor = conn.cursor()
#             sql = "SELECT * FROM stores WHERE id = %s"
#             cursor.execute(sql, (store_id,))
#             store = cursor.fetchone()  # Get store details
#             cursor.close()
#             conn.close()

#             if store:
#                 # Login successful, redirect to dashboard
#                 return redirect(url_for('dashboard', store_id=store_id))
#             else:
#                 # Login failed
#                 return render_template('login.html', error="Invalid store ID")
#         else:
#             return render_template('login.html', error="Failed to connect to the database")

#     return render_template('login.html')


# @app.route('/logout')
# def logout():
#     return redirect(url_for('login'))

# @app.route('/dashboard/<store_id>')
# def dashboard(store_id):
#     return render_template('dashboard.html', store_id=store_id)


# @app.route('/add_product/<store_id>', methods=['GET', 'POST'])
# def add_product(store_id):
#     if request.method == 'POST':
#         product_name = request.form.get('product_name')
#         quantity = request.form.get('quantity')
#         low_stock_threshold = request.form.get('low_stock_threshold')
#         product_code = request.form.get('product_code')

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 sql = "INSERT INTO products (store_id, product_name, quantity, low_stock_threshold, product_code) VALUES (%s, %s, %s, %s, %s)"
#                 val = (store_id, product_name, quantity, low_stock_threshold, product_code)
#                 cursor.execute(sql, val)
#                 conn.commit()
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('dashboard', store_id=store_id)) #Redirect
#             except mysql.connector.Error as db_err:
#                 return f"Database error: {db_err}"
#         else:
#             return "Failed to connect to the database"
        
#         return redirect(url_for('dashboard', store_id=store_id))
#     else:
#         return render_template('add_product.html', store_id=store_id)


#     return render_template('add_product.html', store_id=store_id)

# @app.route('/view_products/<store_id>')
# def view_products(store_id):
#     conn = connect_db()
#     if conn:
#         try:
#             cursor = conn.cursor()
#             sql = "SELECT * FROM products WHERE store_id = %s"
#             cursor.execute(sql, (store_id,))
#             products = cursor.fetchall()
#             cursor.close()
#             conn.close()
#             return render_template('view_products.html', store_id=store_id, products=products)
#         except mysql.connector.Error as db_err:
#             return f"Database error: {db_err}"
#     else:
#         return "Failed to connect to the database"


# @app.route('/')
# def index():
#     return render_template('login.html')


# if __name__ == '__main__':
#     app.run(debug=True)





# from flask import Flask, render_template, request, redirect, url_for
# import mysql.connector
# import os

# app = Flask(__name__)

# # Database configuration (replace with your actual credentials)
# db_config = {
#     'user': 'root',
#     'password': '1234',
#     'host': 'localhost',
#     'database': 'smart_inventory'
# }

# def connect_db():
#     try:
#         conn = mysql.connector.connect(**db_config)
#         print("Database connection established successfully!")
#         return conn
#     except mysql.connector.Error as err:
#         print(f"Database connection failed: {err}")
#         return None

# @app.route('/register_store', methods=['GET', 'POST'])
# def register_store():
#     error = None
#     if request.method == 'POST':
#         store_name = request.form.get('store_name')
#         if not store_name:
#             error = "Store name is required"
#             return render_template('register_store.html', error=error)

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 # Check if store already exists
#                 sql = "SELECT id FROM stores WHERE store_name = %s"
#                 cursor.execute(sql, (store_name,))
#                 existing_store = cursor.fetchone()

#                 if existing_store:
#                     error = "Store already exists!"
#                     return render_template('register_store.html', error=error)

#                 sql = "INSERT INTO stores (store_name) VALUES (%s)"
#                 cursor.execute(sql, (store_name,))
#                 conn.commit()
#                 store_id = cursor.lastrowid  # Get the store ID
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('login'))  # Redirect to login page

#             except mysql.connector.Error as db_err:
#                 error = f"Database error: {db_err}"
#                 return render_template('register_store.html', error=error)
#         else:
#             error = "Failed to connect to the database"

#     return render_template('register_store.html', error=error)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         store_id = request.form.get('store_id')  # Get store ID from the form

#         conn = connect_db()
#         if conn:
#             cursor = conn.cursor()
#             sql = "SELECT * FROM stores WHERE id = %s"
#             cursor.execute(sql, (store_id,))
#             store = cursor.fetchone()  # Get store details
#             cursor.close()
#             conn.close()

#             if store:
#                 # Login successful, redirect to dashboard
#                 return redirect(url_for('dashboard', store_id=store_id))
#             else:
#                 # Login failed
#                 return render_template('login.html', error="Invalid store ID")
#         else:
#             return render_template('login.html', error="Failed to connect to the database")

#     return render_template('login.html')

# @app.route('/logout')
# def logout():
#     return redirect(url_for('login'))

# @app.route('/dashboard/<store_id>')
# def dashboard(store_id):
#     return render_template('dashboard.html', store_id=store_id)

# @app.route('/add_product/<store_id>', methods=['GET', 'POST'])
# def add_product(store_id):
#     if request.method == 'POST':
#         product_name = request.form.get('product_name')
#         quantity = request.form.get('quantity')
#         low_stock_threshold = request.form.get('low_stock_threshold')
#         product_code = request.form.get('product_code')

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 sql = "INSERT INTO products (store_id, product_name, quantity, low_stock_threshold, product_code) VALUES (%s, %s, %s, %s, %s)"
#                 val = (store_id, product_name, quantity, low_stock_threshold, product_code)
#                 cursor.execute(sql, val)
#                 conn.commit()
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('dashboard', store_id=store_id)) #Redirect
#             except mysql.connector.Error as db_err:
#                 return f"Database error: {db_err}"
#         else:
#             return "Failed to connect to the database"

#     return render_template('add_product.html', store_id=store_id)

# @app.route('/view_products/<store_id>')
# def view_products(store_id):
#     conn = connect_db()
#     if conn:
#         try:
#             cursor = conn.cursor()
#             sql = "SELECT *, CASE WHEN quantity <= low_stock_threshold THEN TRUE ELSE FALSE END AS low_stock_warning FROM products WHERE store_id = %s"
#             cursor.execute(sql, (store_id,))
#             products = cursor.fetchall()
#             cursor.close()
#             conn.close()
#             return render_template('view_products.html', store_id=store_id, products=products)
#         except mysql.connector.Error as db_err:
#             return f"Database error: {db_err}"
#     else:
#         return "Failed to connect to the database"

# @app.route('/')
# def index():
#     return render_template('login.html')

# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, render_template, request, redirect, url_for
# import mysql.connector
# import os

# app = Flask(__name__)

# # Database configuration (replace with your actual credentials)
# db_config = {
#     'user': 'root',
#     'password': '1234',
#     'host': 'localhost',
#     'database': 'smart_inventory'
# }

# def connect_db():
#     try:
#         conn = mysql.connector.connect(**db_config)
#         print("Database connection established successfully!")
#         return conn
#     except mysql.connector.Error as err:
#         print(f"Database connection failed: {err}")
#         return None

# @app.route('/register_store', methods=['GET', 'POST'])
# def register_store():
#     error = None
#     if request.method == 'POST':
#         store_name = request.form.get('store_name')
#         if not store_name:
#             error = "Store name is required"
#             return render_template('register_store.html', error=error)

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 # Check if store already exists
#                 sql = "SELECT id FROM stores WHERE store_name = %s"
#                 cursor.execute(sql, (store_name,))
#                 existing_store = cursor.fetchone()

#                 if existing_store:
#                     error = "Store already exists!"
#                     return render_template('register_store.html', error=error)

#                 sql = "INSERT INTO stores (store_name) VALUES (%s)"
#                 cursor.execute(sql, (store_name,))
#                 conn.commit()
#                 store_id = cursor.lastrowid  # Get the store ID
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('login'))  # Redirect to login page

#             except mysql.connector.Error as db_err:
#                 error = f"Database error: {db_err}"
#                 return render_template('register_store.html', error=error)
#         else:
#             error = "Failed to connect to the database"

#     return render_template('register_store.html', error=error)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         store_id = request.form.get('store_id')  # Get store ID from the form

#         conn = connect_db()
#         if conn:
#             cursor = conn.cursor()
#             sql = "SELECT * FROM stores WHERE id = %s"
#             cursor.execute(sql, (store_id,))
#             store = cursor.fetchone()  # Get store details
#             cursor.close()
#             conn.close()

#             if store:
#                 # Login successful, redirect to dashboard
#                 return redirect(url_for('dashboard', store_id=store_id))
#             else:
#                 # Login failed
#                 return render_template('login.html', error="Invalid store ID")
#         else:
#             return render_template('login.html', error="Failed to connect to the database")

#     return render_template('login.html')

# @app.route('/logout')
# def logout():
#     return redirect(url_for('login'))

# @app.route('/dashboard/<store_id>')
# def dashboard(store_id):
#     return render_template('dashboard.html', store_id=store_id)

# @app.route('/add_product/<store_id>', methods=['GET', 'POST'])
# def add_product(store_id):
#     if request.method == 'POST':
#         product_name = request.form.get('product_name')
#         quantity = request.form.get('quantity')
#         low_stock_threshold = request.form.get('low_stock_threshold')
#         product_code = request.form.get('product_code')

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 sql = "INSERT INTO products (store_id, product_name, quantity, low_stock_threshold, product_code) VALUES (%s, %s, %s, %s, %s)"
#                 val = (store_id, product_name, quantity, low_stock_threshold, product_code)
#                 cursor.execute(sql, val)
#                 conn.commit()
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('dashboard', store_id=store_id)) #Redirect
#             except mysql.connector.Error as db_err:
#                 return f"Database error: {db_err}"
#         else:
#             return "Failed to connect to the database"

#     return render_template('add_product.html', store_id=store_id)

# @app.route('/view_products/<store_id>')
# def view_products(store_id):
#     conn = connect_db()
#     if conn:
#         try:
#             cursor = conn.cursor()
#             sql = "SELECT id, store_id, product_name, quantity, low_stock_threshold, product_code, CASE WHEN quantity <= low_stock_threshold THEN TRUE ELSE FALSE END AS low_stock_warning FROM products WHERE store_id = %s"
#             cursor.execute(sql, (store_id,))
#             products = cursor.fetchall()
#             cursor.close()
#             conn.close()
#             return render_template('view_products.html', store_id=store_id, products=products)
#         except mysql.connector.Error as db_err:
#             return f"Database error: {db_err}"
#     else:
#         return "Failed to connect to the database"

# @app.route('/')
# def index():
#     return render_template('login.html')

# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, render_template, request, redirect, url_for
# import mysql.connector
# import os

# app = Flask(__name__)

# # Database configuration (replace with your actual credentials)
# db_config = {
#     'user': 'root',
#     'password': '1234',
#     'host': 'localhost',
#     'database': 'smart_inventory'
# }

# def connect_db():
#     try:
#         conn = mysql.connector.connect(**db_config)
#         print("Database connection established successfully!")
#         return conn
#     except mysql.connector.Error as err:
#         print(f"Database connection failed: {err}")
#         return None

# @app.route('/register_store', methods=['GET', 'POST'])
# def register_store():
#     error = None
#     if request.method == 'POST':
#         store_name = request.form.get('store_name')
#         if not store_name:
#             error = "Store name is required"
#             return render_template('register_store.html', error=error)

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 # Check if store already exists
#                 sql = "SELECT id FROM stores WHERE store_name = %s"
#                 cursor.execute(sql, (store_name,))
#                 existing_store = cursor.fetchone()

#                 if existing_store:
#                     error = "Store already exists!"
#                     return render_template('register_store.html', error=error)

#                 sql = "INSERT INTO stores (store_name) VALUES (%s)"
#                 cursor.execute(sql, (store_name,))
#                 conn.commit()
#                 store_id = cursor.lastrowid  # Get the store ID
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('login'))  # Redirect to login page

#             except mysql.connector.Error as db_err:
#                 error = f"Database error: {db_err}"
#                 return render_template('register_store.html', error=error)
#         else:
#             error = "Failed to connect to the database"

#     return render_template('register_store.html', error=error)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         store_id = request.form.get('store_id')  # Get store ID from the form

#         conn = connect_db()
#         if conn:
#             cursor = conn.cursor()
#             sql = "SELECT * FROM stores WHERE id = %s"
#             cursor.execute(sql, (store_id,))
#             store = cursor.fetchone()  # Get store details
#             cursor.close()
#             conn.close()

#             if store:
#                 # Login successful, redirect to dashboard
#                 return redirect(url_for('dashboard', store_id=store_id))
#             else:
#                 # Login failed
#                 return render_template('login.html', error="Invalid store ID")
#         else:
#             return render_template('login.html', error="Failed to connect to the database")

#     return render_template('login.html')

# @app.route('/logout')
# def logout():
#     return redirect(url_for('login'))

# @app.route('/dashboard/<store_id>')
# def dashboard(store_id):
#     return render_template('dashboard.html', store_id=store_id)

# @app.route('/add_product/<store_id>', methods=['GET', 'POST'])
# def add_product(store_id):
#     if request.method == 'POST':
#         product_name = request.form.get('product_name')
#         quantity = request.form.get('quantity')
#         low_stock_threshold = request.form.get('low_stock_threshold')
#         product_code = request.form.get('product_code')

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 sql = "INSERT INTO products (store_id, product_name, quantity, low_stock_threshold, product_code) VALUES (%s, %s, %s, %s, %s)"
#                 val = (store_id, product_name, quantity, low_stock_threshold, product_code)
#                 cursor.execute(sql, val)
#                 conn.commit()
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('dashboard', store_id=store_id)) #Redirect
#             except mysql.connector.Error as db_err:
#                 return f"Database error: {db_err}"
#         else:
#             return "Failed to connect to the database"

#     return render_template('add_product.html', store_id=store_id)

# @app.route('/view_products/<store_id>')
# def view_products(store_id):
#     conn = connect_db()
#     if conn:
#         try:
#             cursor = conn.cursor()
#             sql = "SELECT id, store_id, product_name, quantity, low_stock_threshold, product_code, (quantity <= low_stock_threshold) AS low_stock_warning FROM products WHERE store_id = %s"
#             cursor.execute(sql, (store_id,))
#             products = cursor.fetchall()
#             cursor.close()
#             conn.close()
#             return render_template('view_products.html', store_id=store_id, products=products)
#         except mysql.connector.Error as db_err:
#             return f"Database error: {db_err}"
#     else:
#         return "Failed to connect to the database"

# @app.route('/edit_product/<product_id>', methods=['GET', 'POST'])
# def edit_product(product_id):
#     conn = connect_db()
#     if conn:
#         cursor = conn.cursor()

#         if request.method == 'POST':
#             product_name = request.form.get('product_name')
#             quantity = request.form.get('quantity')
#             low_stock_threshold = request.form.get('low_stock_threshold')
#             product_code = request.form.get('product_code')

#             try:
#                 sql = "UPDATE products SET product_name=%s, quantity=%s, low_stock_threshold=%s, product_code=%s WHERE id=%s"
#                 val = (product_name, quantity, low_stock_threshold, product_code, product_id)
#                 cursor.execute(sql, val)
#                 conn.commit()
#             except mysql.connector.Error as db_err:
#                 return f"Database error during update: {db_err}"

#             # Fetch store_id before redirecting
#             sql = "SELECT store_id FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             result = cursor.fetchone()
#             if result:
#                 store_id = result[0]
#             else:
#                 return "Product not found"  # Or handle the error appropriately

#             cursor.close()
#             conn.close()
#             return redirect(url_for('view_products', store_id=store_id))

#         else:  # GET request
#             try:
#                 sql = "SELECT id, store_id, product_name, quantity, low_stock_threshold, product_code FROM products WHERE id = %s"
#                 cursor.execute(sql, (product_id,))
#                 product = cursor.fetchone()
#                 if product:
#                     store_id = product[1]  # Access store_id from the fetched product
#                     return render_template('edit_product.html', product=product, store_id=store_id)  # Pass store_id here
#                 else:
#                     return "Product not found"  # Or handle the error appropriately
#             except mysql.connector.Error as db_err:
#                 return f"Database error during select: {db_err}"
#             finally:
#                  cursor.close()
#                  conn.close()
#     else:
#         return "Failed to connect to the database"

# @app.route('/')
# def index():
#     return render_template('login.html')

# if __name__ == '__main__':
#     app.run(debug=True)


# This works!!! 
# from flask import Flask, render_template, request, redirect, url_for
# import mysql.connector
# import os

# app = Flask(__name__, static_folder='static')

# # Database configuration (replace with your actual credentials)
# db_config = {
#     'user': 'root',
#     'password': '1234',
#     'host': 'localhost',
#     'database': 'smart_inventory'
# }

# def connect_db():
#     try:
#         conn = mysql.connector.connect(**db_config)
#         print("Database connection established successfully!")
#         return conn
#     except mysql.connector.Error as err:
#         print(f"Database connection failed: {err}")
#         return None

# import qrcode

# @app.route('/register_store', methods=['GET', 'POST'])
# def register_store():
#     error = None
#     if request.method == 'POST':
#         store_name = request.form.get('store_name')
#         if not store_name:
#             error = "Store name is required"
#             return render_template('register_store.html', error=error)

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 # Check if store already exists
#                 sql = "SELECT id FROM stores WHERE store_name = %s"
#                 cursor.execute(sql, (store_name,))
#                 existing_store = cursor.fetchone()

#                 if existing_store:
#                     error = "Store already exists!"
#                     return render_template('register_store.html', error=error)

#                 sql = "INSERT INTO stores (store_name) VALUES (%s)"
#                 cursor.execute(sql, (store_name,))
#                 conn.commit()
#                 store_id = cursor.lastrowid  # Get the store ID

#                 # Generate QR Code
#                 qr = qrcode.QRCode(
#                     version=1,
#                     error_correction=qrcode.constants.ERROR_CORRECT_L,
#                     box_size=10,
#                     border=4,
#                 )
#                 # Modified to create link
#                 qr_data = f"{request.url_root}qr_login/{store_id}"

#                 qr.add_data(qr_data)  # Encode the store ID in the QR code
#                 qr.make(fit=True)

#                 img = qr.make_image(fill_color="black", back_color="white")

#                 # Ensure the 'static/qrcodes' directory exists
#                 qr_dir = os.path.join(app.static_folder, 'qrcodes')
#                 os.makedirs(qr_dir, exist_ok=True)

#                 qr_code_path = os.path.join('qrcodes', f'store_{store_id}.png')
#                 img_path = os.path.join(app.static_folder, qr_code_path)
#                 img.save(img_path)

#                 # Update the stores table with the QR code path
#                 sql = "UPDATE stores SET qr_code_path = %s WHERE id = %s"
#                 cursor.execute(sql, (qr_code_path, store_id))
#                 conn.commit()
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('login'))  # Redirect to login page

#             except mysql.connector.Error as db_err:
#                 error = f"Database error: {db_err}"
#                 return render_template('register_store.html', error=error)
#         else:
#             error = "Failed to connect to the database"

#     return render_template('register_store.html', error=error)



# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         store_id = request.form.get('store_id')  # Get store ID from the form

#         conn = connect_db()
#         if conn:
#             cursor = conn.cursor()
#             sql = "SELECT * FROM stores WHERE id = %s"
#             cursor.execute(sql, (store_id,))
#             store = cursor.fetchone()  # Get store details
#             cursor.close()
#             conn.close()

#             if store:
#                 # Login successful, redirect to dashboard
#                 return redirect(url_for('dashboard', store_id=store_id))
#             else:
#                 # Login failed
#                 return render_template('login.html', error="Invalid store ID")
#         else:
#             return render_template('login.html', error="Failed to connect to the database")

#     return render_template('login.html')

# @app.route('/logout')
# def logout():
#     return redirect(url_for('login'))

# @app.route('/dashboard/<store_id>')
# def dashboard(store_id):
#     return render_template('dashboard.html', store_id=store_id)

# @app.route('/add_product/<store_id>', methods=['GET', 'POST'])
# def add_product(store_id):
#     if request.method == 'POST':
#         product_name = request.form.get('product_name')
#         quantity = request.form.get('quantity')
#         low_stock_threshold = request.form.get('low_stock_threshold')
#         product_code = request.form.get('product_code')

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 sql = "INSERT INTO products (store_id, product_name, quantity, low_stock_threshold, product_code) VALUES (%s, %s, %s, %s, %s)"
#                 val = (store_id, product_name, quantity, low_stock_threshold, product_code)
#                 cursor.execute(sql, val)
#                 conn.commit()
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('dashboard', store_id=store_id)) #Redirect
#             except mysql.connector.Error as db_err:
#                 return f"Database error: {db_err}"
#         else:
#             return "Failed to connect to the database"

#     return render_template('add_product.html', store_id=store_id)

# @app.route('/view_products/<store_id>')
# def view_products(store_id):
#     conn = connect_db()
#     if conn:
#         try:
#             cursor = conn.cursor()
#             sql = "SELECT id, store_id, product_name, quantity, low_stock_threshold, product_code, (quantity <= low_stock_threshold) AS low_stock_warning FROM products WHERE store_id = %s"
#             cursor.execute(sql, (store_id,))
#             products = cursor.fetchall()
#             cursor.close()
#             conn.close()
#             return render_template('view_products.html', store_id=store_id, products=products)
#         except mysql.connector.Error as db_err:
#             return f"Database error: {db_err}"
#     else:
#         return "Failed to connect to the database"

# @app.route('/edit_product/<product_id>', methods=['GET', 'POST'])
# def edit_product(product_id):
#     conn = connect_db()
#     if conn:
#         cursor = conn.cursor()

#         if request.method == 'POST':
#             product_name = request.form.get('product_name')
#             quantity = request.form.get('quantity')
#             low_stock_threshold = request.form.get('low_stock_threshold')
#             product_code = request.form.get('product_code')

#             try:
#                 sql = "UPDATE products SET product_name=%s, quantity=%s, low_stock_threshold=%s, product_code=%s WHERE id=%s"
#                 val = (product_name, quantity, low_stock_threshold, product_code, product_id)
#                 cursor.execute(sql, val)
#                 conn.commit()
#             except mysql.connector.Error as db_err:
#                 return f"Database error during update: {db_err}"

#             # Fetch store_id before redirecting
#             sql = "SELECT store_id FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             result = cursor.fetchone()
#             if result:
#                 store_id = result[0]
#             else:
#                 return "Product not found"  # Or handle the error appropriately

#             cursor.close()
#             conn.close()
#             return redirect(url_for('view_products', store_id=store_id))

#         else:  # GET request
#             try:
#                 sql = "SELECT id, store_id, product_name, quantity, low_stock_threshold, product_code FROM products WHERE id = %s"
#                 cursor.execute(sql, (product_id,))
#                 product = cursor.fetchone()
#                 if product:
#                     store_id = product[1]  # Access store_id from the fetched product
#                     return render_template('edit_product.html', product=product, store_id=store_id)  # Pass store_id here
#                 else:
#                     return "Product not found"  # Or handle the error appropriately
#             except mysql.connector.Error as db_err:
#                 return f"Database error during select: {db_err}"
#             finally:
#                  cursor.close()
#                  conn.close()
#     else:
#         return "Failed to connect to the database"

# @app.route('/delete_product/<product_id>')
# def delete_product(product_id):
#     conn = connect_db()
#     if conn:
#         try:
#             cursor = conn.cursor()

#             # Get the store_id before deleting
#             sql = "SELECT store_id FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             result = cursor.fetchone()
#             if result:
#                 store_id = result[0]
#             else:
#                 return "Product not found"

#             sql = "DELETE FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             conn.commit()
#             cursor.close()
#             conn.close()
#             return redirect(url_for('view_products', store_id=store_id))
#         except mysql.connector.Error as db_err:
#             return f"Database error: {db_err}"
#     else:
#         return "Failed to connect to the database"

# @app.route('/qr_login/<store_id>')
# def qr_login(store_id):
#     # Redirects to the dashboard using the store_id from the QR code
#     return redirect(url_for('dashboard', store_id=store_id))

# @app.route('/')
# def index():
#     return render_template('login.html')

# if __name__ == '__main__':
#     app.run(debug=True)

# idk if this works or not with password and qr
# from flask import Flask, render_template, request, redirect, url_for
# import mysql.connector
# import os
# import qrcode

# app = Flask(__name__, static_folder='static')

# # Database configuration (replace with your actual credentials)
# db_config = {
#     'user': 'root',
#     'password': '1234',
#     'host': 'localhost',
#     'database': 'smart_inventory'
# }

# def connect_db():
#     try:
#         conn = mysql.connector.connect(**db_config)
#         print("Database connection established successfully!")
#         return conn
#     except mysql.connector.Error as err:
#         print(f"Database connection failed: {err}")
#         return None

# @app.route('/register_store', methods=['GET', 'POST'])
# def register_store():
#     error = None
#     if request.method == 'POST':
#         store_name = request.form.get('store_name')
#         if not store_name:
#             error = "Store name is required"
#             return render_template('register_store.html', error=error)

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 # Check if store already exists
#                 sql = "SELECT id FROM stores WHERE store_name = %s"
#                 cursor.execute(sql, (store_name,))
#                 existing_store = cursor.fetchone()

#                 if existing_store:
#                     error = "Store already exists!"
#                     return render_template('register_store.html', error=error)

#                 sql = "INSERT INTO stores (store_name) VALUES (%s)"
#                 cursor.execute(sql, (store_name,))
#                 conn.commit()
#                 store_id = cursor.lastrowid  # Get the store ID

#                 # Generate QR Code
#                 qr = qrcode.QRCode(
#                     version=1,
#                     error_correction=qrcode.constants.ERROR_CORRECT_L,
#                     box_size=10,
#                     border=4,
#                 )
#                 # Modified to create link
#                 qr_data = f"{request.url_root}qr_login/{store_id}"

#                 qr.add_data(qr_data)  # Encode the store ID in the QR code
#                 qr.make(fit=True)

#                 img = qr.make_image(fill_color="black", back_color="white")

#                 # Ensure the 'static/qrcodes' directory exists
#                 qr_dir = os.path.join(app.static_folder, 'qrcodes')
#                 os.makedirs(qr_dir, exist_ok=True)

#                 qr_code_path = os.path.join('qrcodes', f'store_{store_id}.png')
#                 img_path = os.path.join(app.static_folder, qr_code_path)
#                 img.save(img_path)

#                 # Update the stores table with the QR code path
#                 sql = "UPDATE stores SET qr_code_path = %s WHERE id = %s"
#                 cursor.execute(sql, (qr_code_path, store_id))
#                 conn.commit()
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('login'))  # Redirect to login page

#             except mysql.connector.Error as db_err:
#                 error = f"Database error: {db_err}"
#                 return render_template('register_store.html', error=error)
#         else:
#             error = "Failed to connect to the database"

#     return render_template('register_store.html', error=error)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     qr_code_path = None
#     store_id_for_qr = None
#     stores = []  # List to hold store information for the dropdown

#     conn = connect_db()
#     if not conn:
#         error = "Failed to connect to the database"
#         return render_template('login.html', error=error, stores=stores)

#     cursor = conn.cursor()

#     # Fetch all stores for the dropdown
#     sql = "SELECT id, store_name FROM stores"
#     cursor.execute(sql)
#     stores = cursor.fetchall()

#     if request.method == 'POST':
#         store_id = request.form.get('store_id')  # Get store ID from the form
#         password = request.form.get('password')

#         # Validate if store_id and password are correct
#         sql = "SELECT * FROM stores WHERE id = %s AND password = %s"  # Assuming you have a password field in stores
#         cursor.execute(sql, (store_id, password))
#         store = cursor.fetchone()

#         if store:
#             cursor.close()
#             conn.close()
#             return redirect(url_for('dashboard', store_id=store_id))
#         else:
#             error = "Invalid store ID or password"

#     # Retrieve QR code path for selected store
#     selected_store_id = request.args.get('store_id')  # From query parameters (after dropdown selection)

#     if selected_store_id:
#         sql = "SELECT id, qr_code_path FROM stores WHERE id = %s"
#         cursor.execute(sql, (selected_store_id,))
#         store = cursor.fetchone()
#         if store:
#             qr_code_path = store[1]
#             store_id_for_qr = store[0]
#         else:
#             error = "Store not found"

#     cursor.close()
#     conn.close()
#     return render_template('login.html', error=error, qr_code_path=qr_code_path,
#                            store_id_for_qr=store_id_for_qr, stores=stores, selected_store_id=selected_store_id)

# @app.route('/logout')
# def logout():
#     return redirect(url_for('login'))

# @app.route('/dashboard/<store_id>')
# def dashboard(store_id):
#     return render_template('dashboard.html', store_id=store_id)

# @app.route('/add_product/<store_id>', methods=['GET', 'POST'])
# def add_product(store_id):
#     if request.method == 'POST':
#         product_name = request.form.get('product_name')
#         quantity = request.form.get('quantity')
#         low_stock_threshold = request.form.get('low_stock_threshold')
#         product_code = request.form.get('product_code')

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 sql = "INSERT INTO products (store_id, product_name, quantity, low_stock_threshold, product_code) VALUES (%s, %s, %s, %s, %s)"
#                 val = (store_id, product_name, quantity, low_stock_threshold, product_code)
#                 cursor.execute(sql, val)
#                 conn.commit()
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('dashboard', store_id=store_id)) #Redirect
#             except mysql.connector.Error as db_err:
#                 return f"Database error: {db_err}"
#         else:
#             return "Failed to connect to the database"

#     return render_template('add_product.html', store_id=store_id)

# @app.route('/view_products/<store_id>')
# def view_products(store_id):
#     conn = connect_db()
#     if conn:
#         try:
#             cursor = conn.cursor()
#             sql = "SELECT id, store_id, product_name, quantity, low_stock_threshold, product_code, (quantity <= low_stock_threshold) AS low_stock_warning FROM products WHERE store_id = %s"
#             cursor.execute(sql, (store_id,))
#             products = cursor.fetchall()
#             cursor.close()
#             conn.close()
#             return render_template('view_products.html', store_id=store_id, products=products)
#         except mysql.connector.Error as db_err:
#             return f"Database error: {db_err}"
#     else:
#         return "Failed to connect to the database"

# @app.route('/edit_product/<product_id>', methods=['GET', 'POST'])
# def edit_product(product_id):
#     conn = connect_db()
#     if conn:
#         cursor = conn.cursor()

#         if request.method == 'POST':
#             product_name = request.form.get('product_name')
#             quantity = request.form.get('quantity')
#             low_stock_threshold = request.form.get('low_stock_threshold')
#             product_code = request.form.get('product_code')

#             try:
#                 sql = "UPDATE products SET product_name=%s, quantity=%s, low_stock_threshold=%s, product_code=%s WHERE id=%s"
#                 val = (product_name, quantity, low_stock_threshold, product_code, product_id)
#                 cursor.execute(sql, val)
#                 conn.commit()
#             except mysql.connector.Error as db_err:
#                 return f"Database error during update: {db_err}"

#             # Fetch store_id before redirecting
#             sql = "SELECT store_id FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             result = cursor.fetchone()
#             if result:
#                 store_id = result[0]
#             else:
#                 return "Product not found"  # Or handle the error appropriately

#             cursor.close()
#             conn.close()
#             return redirect(url_for('view_products', store_id=store_id))

#         else:  # GET request
#             try:
#                 sql = "SELECT id, store_id, product_name, quantity, low_stock_threshold, product_code FROM products WHERE id = %s"
#                 cursor.execute(sql, (product_id,))
#                 product = cursor.fetchone()
#                 if product:
#                     store_id = product[1]  # Access store_id from the fetched product
#                     return render_template('edit_product.html', product=product, store_id=store_id)  # Pass store_id here
#                 else:
#                     return "Product not found"  # Or handle the error appropriately
#             except mysql.connector.Error as db_err:
#                 return f"Database error during select: {db_err}"
#             finally:
#                  cursor.close()
#                  conn.close()
#     else:
#         return "Failed to connect to the database"

# @app.route('/delete_product/<product_id>')
# def delete_product(product_id):
#     conn = connect_db()
#     if conn:
#         try:
#             cursor = conn.cursor()

#             # Get the store_id before deleting
#             sql = "SELECT store_id FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             result = cursor.fetchone()
#             if result:
#                 store_id = result[0]
#             else:
#                 return "Product not found"

#             sql = "DELETE FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             conn.commit()
#             cursor.close()
#             conn.close()
#             return redirect(url_for('view_products', store_id=store_id))
#         except mysql.connector.Error as db_err:
#             return f"Database error: {db_err}"
#     else:
#         return "Failed to connect to the database"

# @app.route('/qr_login/<store_id>')
# def qr_login(store_id):
#     # Redirects to the dashboard using the store_id from the QR code
#     return redirect(url_for('dashboard', store_id=store_id))

# @app.route('/')
# def index():
#     return render_template('login.html')

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for
# import mysql.connector
# import os
# import qrcode  # Import the qrcode library

# app = Flask(__name__, static_folder='static')

# # Database configuration (replace with your actual credentials)
# db_config = {
#     'user': 'root',
#     'password': '1234',
#     'host': 'localhost',
#     'database': 'smart_inventory'
# }

# def connect_db():
#     try:
#         conn = mysql.connector.connect(**db_config)
#         print("Database connection established successfully!")
#         return conn
#     except mysql.connector.Error as err:
#         print(f"Database connection failed: {err}")
#         return None

# @app.route('/register_store', methods=['GET', 'POST'])
# def register_store():
#     error = None
#     if request.method == 'POST':
#         store_name = request.form.get('store_name')
#         password = request.form.get('password')  # Get password from the form
#         if not store_name:
#             error = "Store name is required"
#             return render_template('register_store.html', error=error)
#         if not password:
#             error = "Password is required"
#             return render_template('register_store.html', error=error)

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 # Check if store already exists
#                 sql = "SELECT id FROM stores WHERE store_name = %s"
#                 cursor.execute(sql, (store_name,))
#                 existing_store = cursor.fetchone()

#                 if existing_store:
#                     error = "Store already exists!"
#                     return render_template('register_store.html', error=error)

#                 sql = "INSERT INTO stores (store_name, password) VALUES (%s, %s)"  # Store password too
#                 cursor.execute(sql, (store_name, password))
#                 conn.commit()
#                 store_id = cursor.lastrowid  # Get the store ID

#                 # Generate QR Code
#                 qr = qrcode.QRCode(
#                     version=1,
#                     error_correction=qrcode.constants.ERROR_CORRECT_L,
#                     box_size=10,
#                     border=4,
#                 )
#                 # Modified to create link
#                 qr_data = f"{request.url_root}qr_login/{store_id}"

#                 qr.add_data(qr_data)  # Encode the store ID in the QR code
#                 qr.make(fit=True)

#                 img = qr.make_image(fill_color="black", back_color="white")

#                 # Ensure the 'static/qrcodes' directory exists
#                 qr_dir = os.path.join(app.static_folder, 'qrcodes')
#                 os.makedirs(qr_dir, exist_ok=True)

#                 qr_code_path = os.path.join('qrcodes', f'store_{store_id}.png')
#                 img_path = os.path.join(app.static_folder, qr_code_path)
#                 img.save(img_path)

#                 # Update the stores table with the QR code path
#                 sql = "UPDATE stores SET qr_code_path = %s WHERE id = %s"
#                 cursor.execute(sql, (qr_code_path, store_id))
#                 conn.commit()
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('login'))  # Redirect to login page

#             except mysql.connector.Error as db_err:
#                 error = f"Database error: {db_err}"
#                 return render_template('register_store.html', error=error)
#         else:
#             error = "Failed to connect to the database"

#     return render_template('register_store.html', error=error)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     qr_code_path = None
#     stores = []  # List to hold store information for the dropdown
#     selected_store_name = None

#     conn = connect_db()
#     if not conn:
#         error = "Failed to connect to the database"
#         return render_template('login.html', error=error, stores=stores, qr_code_path = qr_code_path)

#     cursor = conn.cursor()

#     # Fetch all stores for the dropdown
#     sql = "SELECT id, store_name FROM stores"
#     cursor.execute(sql)
#     stores = cursor.fetchall()

#     if request.method == 'POST':
#         store_name = request.form.get('store_name')  # Get store name from the form
#         password = request.form.get('password')  # Get the password

#         # Validate if store_id and password are correct
#         sql = "SELECT * FROM stores WHERE store_name = %s AND password = %s"  # Check password
#         cursor.execute(sql, (store_name, password))
#         store = cursor.fetchone()  # Get store details

#         if store:
#             # Login successful, redirect to dashboard
#             cursor.close()
#             conn.close()
#             return redirect(url_for('dashboard', store_id=store[0]))
#         else:
#             # Login failed
#             error = "Incorrect store name or password. Please try again."  # Display error

#     # Retrieve QR code path for selected store
#     selected_store_name = request.args.get('store_name')  # From query parameters (after dropdown selection)

#     if selected_store_name:
#         sql = "SELECT id, qr_code_path FROM stores WHERE store_name = %s"
#         cursor.execute(sql, (selected_store_name,))
#         store = cursor.fetchone()
#         if store:
#             qr_code_path = store[1]
#         else:
#             error = "Store not found"

#     cursor.close()
#     conn.close()
#     return render_template('login.html', error=error, qr_code_path=qr_code_path,
#                            stores=stores, selected_store_name=selected_store_name)

# @app.route('/logout')
# def logout():
#     return redirect(url_for('login'))

# @app.route('/dashboard/<store_id>')
# def dashboard(store_id):
#     return render_template('dashboard.html', store_id=store_id)

# @app.route('/add_product/<store_id>', methods=['GET', 'POST'])
# def add_product(store_id):
#     if request.method == 'POST':
#         product_name = request.form.get('product_name')
#         quantity = request.form.get('quantity')
#         low_stock_threshold = request.form.get('low_stock_threshold')
#         product_code = request.form.get('product_code')

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 sql = "INSERT INTO products (store_id, product_name, quantity, low_stock_threshold, product_code) VALUES (%s, %s, %s, %s, %s)"
#                 val = (store_id, product_name, quantity, low_stock_threshold, product_code)
#                 cursor.execute(sql, val)
#                 conn.commit()
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('dashboard', store_id=store_id)) #Redirect
#             except mysql.connector.Error as db_err:
#                 return f"Database error: {db_err}"
#         else:
#             return "Failed to connect to the database"

#     return render_template('add_product.html', store_id=store_id)

# @app.route('/view_products/<store_id>')
# def view_products(store_id):
#     conn = connect_db()
#     if conn:
#         try:
#             cursor = conn.cursor()
#             sql = "SELECT id, store_id, product_name, quantity, low_stock_threshold, product_code, (quantity <= low_stock_threshold) AS low_stock_warning FROM products WHERE store_id = %s"
#             cursor.execute(sql, (store_id,))
#             products = cursor.fetchall()
#             cursor.close()
#             conn.close()
#             return render_template('view_products.html', store_id=store_id, products=products)
#         except mysql.connector.Error as db_err:
#             return f"Database error: {db_err}"
#     else:
#         return "Failed to connect to the database"

# @app.route('/edit_product/<product_id>', methods=['GET', 'POST'])
# def edit_product(product_id):
#     conn = connect_db()
#     if conn:
#         cursor = conn.cursor()

#         if request.method == 'POST':
#             product_name = request.form.get('product_name')
#             quantity = request.form.get('quantity')
#             low_stock_threshold = request.form.get('low_stock_threshold')
#             product_code = request.form.get('product_code')

#             try:
#                 sql = "UPDATE products SET product_name=%s, quantity=%s, low_stock_threshold=%s, product_code=%s WHERE id=%s"
#                 val = (product_name, quantity, low_stock_threshold, product_code, product_id)
#                 cursor.execute(sql, val)
#                 conn.commit()
#             except mysql.connector.Error as db_err:
#                 return f"Database error during update: {db_err}"

#             # Fetch store_id before redirecting
#             sql = "SELECT store_id FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             result = cursor.fetchone()
#             if result:
#                 store_id = result[0]
#             else:
#                 return "Product not found"  # Or handle the error appropriately

#             cursor.close()
#             conn.close()
#             return redirect(url_for('view_products', store_id=store_id))

#         else:  # GET request
#             try:
#                 sql = "SELECT id, store_id, product_name, quantity, low_stock_threshold, product_code FROM products WHERE id = %s"
#                 cursor.execute(sql, (product_id,))
#                 product = cursor.fetchone()
#                 if product:
#                     store_id = product[1]  # Access store_id from the fetched product
#                     return render_template('edit_product.html', product=product, store_id=store_id)  # Pass store_id here
#                 else:
#                     return "Product not found"  # Or handle the error appropriately
#             except mysql.connector.Error as db_err:
#                 return f"Database error during select: {db_err}"
#             finally:
#                  cursor.close()
#                  conn.close()
#     else:
#         return "Failed to connect to the database"

# @app.route('/delete_product/<product_id>')
# def delete_product(product_id):
#     conn = connect_db()
#     if conn:
#         try:
#             cursor = conn.cursor()

#             # Get the store_id before deleting
#             sql = "SELECT store_id FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             result = cursor.fetchone()
#             if result:
#                 store_id = result[0]
#             else:
#                 return "Product not found"

#             sql = "DELETE FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             conn.commit()
#             cursor.close()
#             conn.close()
#             return redirect(url_for('view_products', store_id=store_id))
#         except mysql.connector.Error as db_err:
#             return f"Database error: {db_err}"
#     else:
#         return "Failed to connect to the database"

# @app.route('/qr_login/<store_id>')
# def qr_login(store_id):
#     # Redirects to the dashboard using the store_id from the QR code
#     return redirect(url_for('dashboard', store_id=store_id))

# @app.route('/')
# def index():
#     return render_template('login.html')

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, render_template, request, redirect, url_for
# import mysql.connector
# import os
# import qrcode  # Import the qrcode library

# app = Flask(__name__, static_folder='static')

# # Database configuration (replace with your actual credentials)
# db_config = {
#     'user': 'root',
#     'password': '1234',
#     'host': 'localhost',
#     'database': 'smart_inventory'
# }

# def connect_db():
#     try:
#         conn = mysql.connector.connect(**db_config)
#         print("Database connection established successfully!")
#         return conn
#     except mysql.connector.Error as err:
#         print(f"Database connection failed: {err}")
#         return None

# @app.route('/register_store', methods=['GET', 'POST'])
# def register_store():
#     error = None
#     if request.method == 'POST':
#         store_name = request.form.get('store_name')
#         password = request.form.get('password')
#         if not store_name:
#             error = "Store name is required"
#             return render_template('register_store.html', error=error)
#         if not password:
#             error = "Password is required"
#             return render_template('register_store.html', error=error)

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 # Check if store already exists
#                 sql = "SELECT id FROM stores WHERE store_name = %s"
#                 cursor.execute(sql, (store_name,))
#                 existing_store = cursor.fetchone()

#                 if existing_store:
#                     error = "Store already exists!"
#                     return render_template('register_store.html', error=error)

#                 sql = "INSERT INTO stores (store_name, password) VALUES (%s, %s)"
#                 cursor.execute(sql, (store_name, password))
#                 conn.commit()
#                 store_id = cursor.lastrowid  # Get the store ID

#                 # Generate QR Code
#                 qr = qrcode.QRCode(
#                     version=1,
#                     error_correction=qrcode.constants.ERROR_CORRECT_L,
#                     box_size=10,
#                     border=4,
#                 )
#                 # Modified to create link
#                 qr_data = f"{request.url_root}qr_login/{store_id}"

#                 qr.add_data(qr_data)  # Encode the store ID in the QR code
#                 qr.make(fit=True)

#                 img = qr.make_image(fill_color="black", back_color="white")

#                 # Ensure the 'static/qrcodes' directory exists
#                 qr_dir = os.path.join(app.static_folder, 'qrcodes')
#                 os.makedirs(qr_dir, exist_ok=True)

#                 qr_code_path = os.path.join('qrcodes', f'store_{store_id}.png')
#                 img_path = os.path.join(app.static_folder, qr_code_path)
#                 img.save(img_path)

#                 # Update the stores table with the QR code path
#                 sql = "UPDATE stores SET qr_code_path = %s WHERE id = %s"
#                 cursor.execute(sql, (qr_code_path, store_id))
#                 conn.commit()
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('login'))  # Redirect to login page

#             except mysql.connector.Error as db_err:
#                 error = f"Database error: {db_err}"
#                 return render_template('register_store.html', error=error)
#         else:
#             error = "Failed to connect to the database"

#     return render_template('register_store.html', error=error)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     qr_code_path = None
#     stores = []  # List to hold store information for the dropdown
#     selected_store_name = None

#     conn = connect_db()
#     if not conn:
#         error = "Failed to connect to the database"
#         return render_template('login.html', error=error, stores=stores, qr_code_path=qr_code_path)

#     cursor = conn.cursor()

#     # Fetch all stores for the dropdown
#     sql = "SELECT id, store_name FROM stores"
#     cursor.execute(sql)
#     stores = cursor.fetchall()

#     if request.method == 'POST':
#         store_name = request.form.get('store_name')
#         password = request.form.get('password')

#         # Validate if store_id and password are correct
#         sql = "SELECT * FROM stores WHERE store_name = %s AND password = %s"
#         cursor.execute(sql, (store_name, password))
#         store = cursor.fetchone()

#         if store:
#             # Login successful, redirect to dashboard
#             cursor.close()
#             conn.close()
#             return redirect(url_for('dashboard', store_id=store[0]))
#         else:
#             # Login failed
#             error = "Incorrect store name or password. Please try again."

#     # Retrieve QR code path for selected store
#     selected_store_name = request.args.get('store_name')

#     if selected_store_name:
#         sql = "SELECT id, qr_code_path FROM stores WHERE store_name = %s"
#         cursor.execute(sql, (selected_store_name,))
#         store = cursor.fetchone()
#         if store:
#             qr_code_path = store[1]
#         else:
#             error = "Store not found"

#     cursor.close()
#     conn.close()
#     return render_template('login.html', error=error, qr_code_path=qr_code_path,
#                            stores=stores, selected_store_name=selected_store_name)

# @app.route('/logout')
# def logout():
#     return redirect(url_for('login'))

# @app.route('/dashboard/<store_id>')
# def dashboard(store_id):
#     return render_template('dashboard.html', store_id=store_id)

# @app.route('/add_product/<store_id>', methods=['GET', 'POST'])
# def add_product(store_id):
#     if request.method == 'POST':
#         product_name = request.form.get('product_name')
#         quantity = request.form.get('quantity')
#         low_stock_threshold = request.form.get('low_stock_threshold')
#         product_code = request.form.get('product_code')

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 sql = "INSERT INTO products (store_id, product_name, quantity, low_stock_threshold, product_code) VALUES (%s, %s, %s, %s, %s)"
#                 val = (store_id, product_name, quantity, low_stock_threshold, product_code)
#                 cursor.execute(sql, val)
#                 conn.commit()
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('dashboard', store_id=store_id)) #Redirect
#             except mysql.connector.Error as db_err:
#                 return f"Database error: {db_err}"
#         else:
#             return "Failed to connect to the database"

#     return render_template('add_product.html', store_id=store_id)

# @app.route('/view_products/<store_id>')
# def view_products(store_id):
#     conn = connect_db()
#     if conn:
#         try:
#             cursor = conn.cursor()
#             sql = "SELECT id, store_id, product_name, quantity, low_stock_threshold, product_code, (quantity <= low_stock_threshold) AS low_stock_warning FROM products WHERE store_id = %s"
#             cursor.execute(sql, (store_id,))
#             products = cursor.fetchall()
#             cursor.close()
#             conn.close()
#             return render_template('view_products.html', store_id=store_id, products=products)
#         except mysql.connector.Error as db_err:
#             return f"Database error: {db_err}"
#     else:
#         return "Failed to connect to the database"

# @app.route('/edit_product/<product_id>', methods=['GET', 'POST'])
# def edit_product(product_id):
#     conn = connect_db()
#     if conn:
#         cursor = conn.cursor()

#         if request.method == 'POST':
#             product_name = request.form.get('product_name')
#             quantity = request.form.get('quantity')
#             low_stock_threshold = request.form.get('low_stock_threshold')
#             product_code = request.form.get('product_code')

#             try:
#                 sql = "UPDATE products SET product_name=%s, quantity=%s, low_stock_threshold=%s, product_code=%s WHERE id=%s"
#                 val = (product_name, quantity, low_stock_threshold, product_code, product_id)
#                 cursor.execute(sql, val)
#                 conn.commit()
#             except mysql.connector.Error as db_err:
#                 return f"Database error during update: {db_err}"

#             # Fetch store_id before redirecting
#             sql = "SELECT store_id FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             result = cursor.fetchone()
#             if result:
#                 store_id = result[0]
#             else:
#                 return "Product not found"  # Or handle the error appropriately

#             cursor.close()
#             conn.close()
#             return redirect(url_for('view_products', store_id=store_id))

#         else:  # GET request
#             try:
#                 sql = "SELECT id, store_id, product_name, quantity, low_stock_threshold, product_code FROM products WHERE id = %s"
#                 cursor.execute(sql, (product_id,))
#                 product = cursor.fetchone()
#                 if product:
#                     store_id = product[1]  # Access store_id from the fetched product
#                     return render_template('edit_product.html', product=product, store_id=store_id)  # Pass store_id here
#                 else:
#                     return "Product not found"  # Or handle the error appropriately
#             except mysql.connector.Error as db_err:
#                 return f"Database error: {db_err}"
#             finally:
#                  cursor.close()
#                  conn.close()
#     else:
#         return "Failed to connect to the database"

# @app.route('/delete_product/<product_id>')
# def delete_product(product_id):
#     conn = connect_db()
#     if conn:
#         try:
#             cursor = conn.cursor()

#             # Get the store_id before deleting
#             sql = "SELECT store_id FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             result = cursor.fetchone()
#             if result:
#                 store_id = result[0]
#             else:
#                 return "Product not found"

#             sql = "DELETE FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             conn.commit()
#             cursor.close()
#             conn.close()
#             return redirect(url_for('view_products', store_id=store_id))
#         except mysql.connector.Error as db_err:
#             return f"Database error: {db_err}"
#     else:
#         return "Failed to connect to the database"

# @app.route('/qr_login/<store_id>')
# def qr_login(store_id):
#     # Redirects to the dashboard using the store_id from the QR code
#     return redirect(url_for('dashboard', store_id=store_id))

# @app.route('/')
# def index():
#     return render_template('login.html')

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, redirect, url_for
# import mysql.connector
# import os
# import qrcode  # Import the qrcode library

# app = Flask(__name__, static_folder='static')

# # Database configuration (replace with your actual credentials)
# db_config = {
#     'user': 'root',
#     'password': '1234',
#     'host': 'localhost',
#     'database': 'smart_inventory'
# }

# def connect_db():
#     try:
#         conn = mysql.connector.connect(**db_config)
#         print("Database connection established successfully!")
#         return conn
#     except mysql.connector.Error as err:
#         print(f"Database connection failed: {err}")
#         return None

# @app.route('/register_store', methods=['GET', 'POST'])
# def register_store():
#     error = None
#     if request.method == 'POST':
#         store_name = request.form.get('store_name')
#         password = request.form.get('password')
#         if not store_name:
#             error = "Store name is required"
#             return render_template('register_store.html', error=error)
#         if not password:
#             error = "Password is required"
#             return render_template('register_store.html', error=error)

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 # Check if store already exists
#                 sql = "SELECT id FROM stores WHERE store_name = %s"
#                 cursor.execute(sql, (store_name,))
#                 existing_store = cursor.fetchone()

#                 if existing_store:
#                     error = "Store already exists!"
#                     return render_template('register_store.html', error=error)

#                 sql = "INSERT INTO stores (store_name, password) VALUES (%s, %s)"
#                 cursor.execute(sql, (store_name, password))
#                 conn.commit()
#                 store_id = cursor.lastrowid  # Get the store ID

#                 # Generate QR Code
#                 qr = qrcode.QRCode(
#                     version=1,
#                     error_correction=qrcode.constants.ERROR_CORRECT_L,
#                     box_size=10,
#                     border=4,
#                 )
#                 # Modified to create link
#                 qr_data = f"{request.url_root}qr_login/{store_id}"

#                 qr.add_data(qr_data)  # Encode the store ID in the QR code
#                 qr.make(fit=True)

#                 img = qr.make_image(fill_color="black", back_color="white")

#                 # Ensure the 'static/qrcodes' directory exists
#                 qr_dir = os.path.join(app.static_folder, 'qrcodes')
#                 os.makedirs(qr_dir, exist_ok=True)

#                 qr_code_path = os.path.join('qrcodes', f'store_{store_id}.png')
#                 img_path = os.path.join(app.static_folder, qr_code_path)
#                 img.save(img_path)

#                 # Update the stores table with the QR code path
#                 sql = "UPDATE stores SET qr_code_path = %s WHERE id = %s"
#                 cursor.execute(sql, (qr_code_path, store_id))
#                 conn.commit()
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('login'))  # Redirect to login page

#             except mysql.connector.Error as db_err:
#                 error = f"Database error: {db_err}"
#                 return render_template('register_store.html', error=error)
#         else:
#             error = "Failed to connect to the database"

#     return render_template('register_store.html', error=error)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     qr_code_path = None
#     stores = []  # List to hold store information for the dropdown
#     selected_store_name = None

#     conn = connect_db()
#     if not conn:
#         error = "Failed to connect to the database"
#         return render_template('login.html', error=error, stores=stores, qr_code_path=qr_code_path)

#     cursor = conn.cursor()

#     # Fetch all stores for the dropdown
#     sql = "SELECT id, store_name FROM stores"
#     cursor.execute(sql)
#     stores = cursor.fetchall()

#     if request.method == 'POST':
#         store_name = request.form.get('store_name')
#         password = request.form.get('password')

#         # Validate if store_id and password are correct
#         sql = "SELECT * FROM stores WHERE store_name = %s AND password = %s"
#         cursor.execute(sql, (store_name, password))
#         store = cursor.fetchone()

#         if store:
#             # Login successful, redirect to dashboard
#             cursor.close()
#             conn.close()
#             return redirect(url_for('dashboard', store_id=store[0]))
#         else:
#             # Login failed
#             error = "Incorrect store name or password. Please try again."

#     # Retrieve QR code path for selected store
#     selected_store_name = request.args.get('store_name')

#     if selected_store_name:
#         sql = "SELECT id, qr_code_path FROM stores WHERE store_name = %s"
#         cursor.execute(sql, (selected_store_name,))
#         store = cursor.fetchone()
#         if store:
#             qr_code_path = store[1]
#         else:
#             error = "Store not found"

#     cursor.close()
#     conn.close()
#     return render_template('login.html', error=error, qr_code_path=qr_code_path,
#                            stores=stores, selected_store_name=selected_store_name)

# @app.route('/logout')
# def logout():
#     return redirect(url_for('login'))

# @app.route('/dashboard/<store_id>')
# def dashboard(store_id):
#     return render_template('dashboard.html', store_id=store_id)

# @app.route('/add_product/<store_id>', methods=['GET', 'POST'])
# def add_product(store_id):
#     if request.method == 'POST':
#         product_name = request.form.get('product_name')
#         quantity = request.form.get('quantity')
#         low_stock_threshold = request.form.get('low_stock_threshold')
#         product_code = request.form.get('product_code')

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 sql = "INSERT INTO products (store_id, product_name, quantity, low_stock_threshold, product_code) VALUES (%s, %s, %s, %s, %s)"
#                 val = (store_id, product_name, quantity, low_stock_threshold, product_code)
#                 cursor.execute(sql, val)
#                 conn.commit()
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('dashboard', store_id=store_id)) #Redirect
#             except mysql.connector.Error as db_err:
#                 return f"Database error: {db_err}"
#         else:
#             return "Failed to connect to the database"

#     return render_template('add_product.html', store_id=store_id)

# @app.route('/view_products/<store_id>')
# def view_products(store_id):
#     conn = connect_db()
#     if conn:
#         try:
#             cursor = conn.cursor()
#             sql = "SELECT id, store_id, product_name, quantity, low_stock_threshold, product_code, (quantity <= low_stock_threshold) AS low_stock_warning FROM products WHERE store_id = %s"
#             cursor.execute(sql, (store_id,))
#             products = cursor.fetchall()
#             cursor.close()
#             conn.close()
#             return render_template('view_products.html', store_id=store_id, products=products)
#         except mysql.connector.Error as db_err:
#             return f"Database error: {db_err}"
#     else:
#         return "Failed to connect to the database"

# @app.route('/edit_product/<product_id>', methods=['GET', 'POST'])
# def edit_product(product_id):
#     conn = connect_db()
#     if conn:
#         cursor = conn.cursor()

#         if request.method == 'POST':
#             product_name = request.form.get('product_name')
#             quantity = request.form.get('quantity')
#             low_stock_threshold = request.form.get('low_stock_threshold')
#             product_code = request.form.get('product_code')

#             try:
#                 sql = "UPDATE products SET product_name=%s, quantity=%s, low_stock_threshold=%s, product_code=%s WHERE id=%s"
#                 val = (product_name, quantity, low_stock_threshold, product_code, product_id)
#                 cursor.execute(sql, val)
#                 conn.commit()
#             except mysql.connector.Error as db_err:
#                 return f"Database error during update: {db_err}"

#             # Fetch store_id before redirecting
#             sql = "SELECT store_id FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             result = cursor.fetchone()
#             if result:
#                 store_id = result[0]
#             else:
#                 return "Product not found"  # Or handle the error appropriately

#             cursor.close()
#             conn.close()
#             return redirect(url_for('view_products', store_id=store_id))

#         else:  # GET request
#             try:
#                 sql = "SELECT id, store_id, product_name, quantity, low_stock_threshold, product_code FROM products WHERE id = %s"
#                 cursor.execute(sql, (product_id,))
#                 product = cursor.fetchone()
#                 if product:
#                     store_id = product[1]  # Access store_id from the fetched product
#                     return render_template('edit_product.html', product=product, store_id=store_id)  # Pass store_id here
#                 else:
#                     return "Product not found"  # Or handle the error appropriately
#             except mysql.connector.Error as db_err:
#                 return f"Database error: {db_err}"
#             finally:
#                  cursor.close()
#                  conn.close()
#     else:
#         return "Failed to connect to the database"

# @app.route('/delete_product/<product_id>')
# def delete_product(product_id):
#     conn = connect_db()
#     if conn:
#         try:
#             cursor = conn.cursor()

#             # Get the store_id before deleting
#             sql = "SELECT store_id FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             result = cursor.fetchone()
#             if result:
#                 store_id = result[0]
#             else:
#                 return "Product not found"

#             sql = "DELETE FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             conn.commit()
#             cursor.close()
#             conn.close()
#             return redirect(url_for('view_products', store_id=store_id))
#         except mysql.connector.Error as db_err:
#             return f"Database error: {db_err}"
#     else:
#         return "Failed to connect to the database"

# @app.route('/qr_login/<store_id>')
# def qr_login(store_id):
#     # Redirects to the dashboard using the store_id from the QR code
#     return redirect(url_for('dashboard', store_id=store_id))

# @app.route('/')
# def index():
#     return render_template('login.html')

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, redirect, url_for
# import mysql.connector
# import os
# import qrcode  # Import the qrcode library

# app = Flask(__name__, static_folder='static')

# # Database configuration (replace with your actual credentials)
# db_config = {
#     'user': 'root',
#     'password': '1234',
#     'host': 'localhost',
#     'database': 'smart_inventory'
# }

# def connect_db():
#     try:
#         conn = mysql.connector.connect(**db_config)
#         print("Database connection established successfully!")
#         return conn
#     except mysql.connector.Error as err:
#         print(f"Database connection failed: {err}")
#         return None

# @app.route('/register_store', methods=['GET', 'POST'])
# def register_store():
#     error = None
#     if request.method == 'POST':
#         store_name = request.form.get('store_name')
#         password = request.form.get('password')
#         if not store_name:
#             error = "Store name is required"
#             return render_template('register_store.html', error=error)
#         if not password:
#             error = "Password is required"
#             return render_template('register_store.html', error=error)

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 # Check if store already exists
#                 sql = "SELECT id FROM stores WHERE store_name = %s"
#                 cursor.execute(sql, (store_name,))
#                 existing_store = cursor.fetchone()

#                 if existing_store:
#                     error = "Store already exists!"
#                     return render_template('register_store.html', error=error)

#                 sql = "INSERT INTO stores (store_name, password) VALUES (%s, %s)"
#                 cursor.execute(sql, (store_name, password))
#                 conn.commit()
#                 store_id = cursor.lastrowid  # Get the store ID

#                 # Generate QR Code
#                 qr = qrcode.QRCode(
#                     version=1,
#                     error_correction=qrcode.constants.ERROR_CORRECT_L,
#                     box_size=10,
#                     border=4,
#                 )
#                 # Modified to create link
#                 qr_data = f"{request.url_root}qr_login/{store_id}"

#                 qr.add_data(qr_data)  # Encode the store ID in the QR code
#                 qr.make(fit=True)

#                 img = qr.make_image(fill_color="black", back_color="white")

#                 # Ensure the 'static/qrcodes' directory exists
#                 qr_dir = os.path.join(app.static_folder, 'qrcodes')
#                 os.makedirs(qr_dir, exist_ok=True)

#                 qr_code_path = os.path.join('qrcodes', f'store_{store_id}.png')
#                 img_path = os.path.join(app.static_folder, qr_code_path)
#                 img.save(img_path)

#                 # Update the stores table with the QR code path
#                 sql = "UPDATE stores SET qr_code_path = %s WHERE id = %s"
#                 cursor.execute(sql, (qr_code_path, store_id))
#                 conn.commit()
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('login'))  # Redirect to login page

#             except mysql.connector.Error as db_err:
#                 error = f"Database error: {db_err}"
#                 return render_template('register_store.html', error=error)
#         else:
#             error = "Failed to connect to the database"

#     return render_template('register_store.html', error=error)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     qr_code_path = None
#     stores = []  # List to hold store information for the dropdown
#     selected_store_name = None

#     conn = connect_db()
#     if not conn:
#         error = "Failed to connect to the database"
#         return render_template('login.html', error=error, stores=stores, qr_code_path = qr_code_path)

#     cursor = conn.cursor()

#     # Fetch all stores for the dropdown
#     sql = "SELECT id, store_name FROM stores"
#     cursor.execute(sql)
#     stores = cursor.fetchall()

#     if request.method == 'POST':
#         store_name = request.form.get('store_name')  # Get store name from the form
#         password = request.form.get('password')  # Get the password

#         # Validate if store_id and password are correct
#         sql = "SELECT * FROM stores WHERE store_name = %s AND password = %s"  # Check password
#         cursor.execute(sql, (store_name, password))
#         store = cursor.fetchone()  # Get store details

#         if store:
#             # Login successful, redirect to dashboard
#             cursor.close()
#             conn.close()
#             return redirect(url_for('dashboard', store_id=store[0]))
#         else:
#             # Login failed
#             error = "Incorrect store name or password. Please try again."  # Display error

#     # Retrieve QR code path for selected store
#     selected_store_name = request.args.get('store_name')  # From query parameters (after dropdown selection)

#     if selected_store_name:
#         sql = "SELECT id, qr_code_path FROM stores WHERE store_name = %s"
#         cursor.execute(sql, (selected_store_name,))
#         store = cursor.fetchone()
#         if store:
#             qr_code_path = store[1]
#         else:
#             error = "Store not found"

#     cursor.close()
#     conn.close()
#     return render_template('login.html', error=error, qr_code_path=qr_code_path,
#                            stores=stores, selected_store_name=selected_store_name)

# @app.route('/logout')
# def logout():
#     return redirect(url_for('login'))

# @app.route('/dashboard/<store_id>')
# def dashboard(store_id):
#     return render_template('dashboard.html', store_id=store_id)

# @app.route('/add_product/<store_id>', methods=['GET', 'POST'])
# def add_product(store_id):
#     if request.method == 'POST':
#         product_name = request.form.get('product_name')
#         quantity = request.form.get('quantity')
#         low_stock_threshold = request.form.get('low_stock_threshold')
#         product_code = request.form.get('product_code')

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 sql = "INSERT INTO products (store_id, product_name, quantity, low_stock_threshold, product_code) VALUES (%s, %s, %s, %s, %s)"
#                 val = (store_id, product_name, quantity, low_stock_threshold, product_code)
#                 cursor.execute(sql, val)
#                 conn.commit()
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('dashboard', store_id=store_id)) #Redirect
#             except mysql.connector.Error as db_err:
#                 return f"Database error: {db_err}"
#         else:
#             return "Failed to connect to the database"

#     return render_template('add_product.html', store_id=store_id)

# @app.route('/view_products/<store_id>')
# def view_products(store_id):
#     conn = connect_db()
#     if conn:
#         try:
#             cursor = conn.cursor()
#             sql = "SELECT id, store_id, product_name, quantity, low_stock_threshold, product_code, (quantity <= low_stock_threshold) AS low_stock_warning FROM products WHERE store_id = %s"
#             cursor.execute(sql, (store_id,))
#             products = cursor.fetchall()
#             cursor.close()
#             conn.close()
#             return render_template('view_products.html', store_id=store_id, products=products)
#         except mysql.connector.Error as db_err:
#             return f"Database error: {db_err}"
#     else:
#         return "Failed to connect to the database"

# @app.route('/edit_product/<product_id>', methods=['GET', 'POST'])
# def edit_product(product_id):
#     conn = connect_db()
#     if conn:
#         cursor = conn.cursor()

#         if request.method == 'POST':
#             product_name = request.form.get('product_name')
#             quantity = request.form.get('quantity')
#             low_stock_threshold = request.form.get('low_stock_threshold')
#             product_code = request.form.get('product_code')

#             try:
#                 sql = "UPDATE products SET product_name=%s, quantity=%s, low_stock_threshold=%s, product_code=%s WHERE id=%s"
#                 val = (product_name, quantity, low_stock_threshold, product_code, product_id)
#                 cursor.execute(sql, val)
#                 conn.commit()
#             except mysql.connector.Error as db_err:
#                 return f"Database error during update: {db_err}"

#             # Fetch store_id before redirecting
#             sql = "SELECT store_id FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             result = cursor.fetchone()
#             if result:
#                 store_id = result[0]
#             else:
#                 return "Product not found"  # Or handle the error appropriately

#             cursor.close()
#             conn.close()
#             return redirect(url_for('view_products', store_id=store_id))

#         else:  # GET request
#             try:
#                 sql = "SELECT id, store_id, product_name, quantity, low_stock_threshold, product_code FROM products WHERE id = %s"
#                 cursor.execute(sql, (product_id,))
#                 product = cursor.fetchone()
#                 if product:
#                     store_id = product[1]  # Access store_id from the fetched product
#                     return render_template('edit_product.html', product=product, store_id=store_id)  # Pass store_id here
#                 else:
#                     return "Product not found"  # Or handle the error appropriately
#             except mysql.connector.Error as db_err:
#                 return f"Database error: {db_err}"
#             finally:
#                  cursor.close()
#                  conn.close()
#     else:
#         return "Failed to connect to the database"

# @app.route('/delete_product/<product_id>')
# def delete_product(product_id):
#     conn = connect_db()
#     if conn:
#         try:
#             cursor = conn.cursor()

#             # Get the store_id before deleting
#             sql = "SELECT store_id FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             result = cursor.fetchone()
#             if result:
#                 store_id = result[0]
#             else:
#                 return "Product not found"

#             sql = "DELETE FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             conn.commit()
#             cursor.close()
#             conn.close()
#             return redirect(url_for('view_products', store_id=store_id))
#         except mysql.connector.Error as db_err:
#             return f"Database error: {db_err}"
#     else:
#         return "Failed to connect to the database"

# @app.route('/qr_login/<store_id>')
# def qr_login(store_id):
#     # Redirects to the dashboard using the store_id from the QR code
#     return redirect(url_for('dashboard', store_id=store_id))

# @app.route('/')
# def index():
#     return render_template('login.html')

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for
# import mysql.connector
# import os
# import qrcode  # Import the qrcode library

# app = Flask(__name__, static_folder='static')

# # Database configuration (replace with your actual credentials)
# db_config = {
#     'user': 'root',
#     'password': '1234',
#     'host': 'localhost',
#     'database': 'smart_inventory'
# }

# def connect_db():
#     try:
#         conn = mysql.connector.connect(**db_config)
#         print("Database connection established successfully!")
#         return conn
#     except mysql.connector.Error as err:
#         print(f"Database connection failed: {err}")
#         return None

# @app.route('/register_store', methods=['GET', 'POST'])
# def register_store():
#     error = None
#     if request.method == 'POST':
#         store_name = request.form.get('store_name')
#         password = request.form.get('password')
#         if not store_name:
#             error = "Store name is required"
#             return render_template('register_store.html', error=error)
#         if not password:
#             error = "Password is required"
#             return render_template('register_store.html', error=error)

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 # Check if store already exists
#                 sql = "SELECT id FROM stores WHERE store_name = %s"
#                 cursor.execute(sql, (store_name,))
#                 existing_store = cursor.fetchone()

#                 if existing_store:
#                     error = "Store already exists!"
#                     return render_template('register_store.html', error=error)

#                 sql = "INSERT INTO stores (store_name, password) VALUES (%s, %s)"
#                 cursor.execute(sql, (store_name, password))
#                 conn.commit()
#                 store_id = cursor.lastrowid  # Get the store ID

#                 # Generate QR Code
#                 qr = qrcode.QRCode(
#                     version=1,
#                     error_correction=qrcode.constants.ERROR_CORRECT_L,
#                     box_size=10,
#                     border=4,
#                 )
#                 # Modified to create link
#                 qr_data = f"{request.url_root}qr_login/{store_id}"

#                 qr.add_data(qr_data)  # Encode the store ID in the QR code
#                 qr.make(fit=True)

#                 img = qr.make_image(fill_color="black", back_color="white")

#                 # Ensure the 'static/qrcodes' directory exists
#                 qr_dir = os.path.join(app.static_folder, 'qrcodes')
#                 os.makedirs(qr_dir, exist_ok=True)

#                 qr_code_path = os.path.join('qrcodes', f'store_{store_id}.png')
#                 img_path = os.path.join(app.static_folder, qr_code_path)
#                 img.save(img_path)

#                 # Update the stores table with the QR code path
#                 sql = "UPDATE stores SET qr_code_path = %s WHERE id = %s"
#                 cursor.execute(sql, (qr_code_path, store_id))
#                 conn.commit()
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('login'))  # Redirect to login page

#             except mysql.connector.Error as db_err:
#                 error = f"Database error: {db_err}"
#                 return render_template('register_store.html', error=error)
#         else:
#             error = "Failed to connect to the database"

#     return render_template('register_store.html', error=error)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     qr_code_path = None
#     stores = []  # List to hold store information for the dropdown
#     selected_store_name = None

#     conn = connect_db()
#     if not conn:
#         error = "Failed to connect to the database"
#         return render_template('login.html', error=error, stores=stores, qr_code_path = qr_code_path)

#     cursor = conn.cursor()

#     # Fetch all stores for the dropdown
#     sql = "SELECT id, store_name FROM stores"
#     cursor.execute(sql)
#     stores = cursor.fetchall()

#     if request.method == 'POST':
#         store_name = request.form.get('store_name')
#         password = request.form.get('password')

#         # Validate if store_id and password are correct
#         sql = "SELECT * FROM stores WHERE store_name = %s AND password = %s"
#         cursor.execute(sql, (store_name, password))
#         store = cursor.fetchone()

#         if store:
#             # Login successful, redirect to dashboard
#             cursor.close()
#             conn.close()
#             return redirect(url_for('dashboard', store_id=store[0]))
#         else:
#             # Login failed
#             error = "Incorrect store name or password. Please try again."

#     # Retrieve QR code path for selected store
#     selected_store_name = request.args.get('store_name')

#     if selected_store_name:
#         sql = "SELECT id, qr_code_path FROM stores WHERE store_name = %s"
#         cursor.execute(sql, (selected_store_name,))
#         store = cursor.fetchone()
#         if store:
#             qr_code_path = store[1]
#         else:
#             error = "Store not found"

#     cursor.close()
#     conn.close()
#     return render_template('login.html', error=error, qr_code_path=qr_code_path,
#                            stores=stores, selected_store_name=selected_store_name)

# @app.route('/logout')
# def logout():
#     return redirect(url_for('login'))

# @app.route('/dashboard/<store_id>')
# def dashboard(store_id):
#     return render_template('dashboard.html', store_id=store_id)

# @app.route('/add_product/<store_id>', methods=['GET', 'POST'])
# def add_product(store_id):
#     if request.method == 'POST':
#         product_name = request.form.get('product_name')
#         quantity = request.form.get('quantity')
#         low_stock_threshold = request.form.get('low_stock_threshold')
#         product_code = request.form.get('product_code')

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 sql = "INSERT INTO products (store_id, product_name, quantity, low_stock_threshold, product_code) VALUES (%s, %s, %s, %s, %s)"
#                 val = (store_id, product_name, quantity, low_stock_threshold, product_code)
#                 cursor.execute(sql, val)
#                 conn.commit()
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('dashboard', store_id=store_id)) #Redirect
#             except mysql.connector.Error as db_err:
#                 return f"Database error: {db_err}"
#         else:
#             return "Failed to connect to the database"

#     return render_template('add_product.html', store_id=store_id)

# @app.route('/view_products/<store_id>')
# def view_products(store_id):
#     conn = connect_db()
#     if conn:
#         try:
#             cursor = conn.cursor()
#             sql = "SELECT id, store_id, product_name, quantity, low_stock_threshold, product_code, (quantity <= low_stock_threshold) AS low_stock_warning FROM products WHERE store_id = %s"
#             cursor.execute(sql, (store_id,))
#             products = cursor.fetchall()
#             cursor.close()
#             conn.close()
#             return render_template('view_products.html', store_id=store_id, products=products)
#         except mysql.connector.Error as db_err:
#             return f"Database error: {db_err}"
#     else:
#         return "Failed to connect to the database"

# @app.route('/edit_product/<product_id>', methods=['GET', 'POST'])
# def edit_product(product_id):
#     conn = connect_db()
#     if conn:
#         cursor = conn.cursor()

#         if request.method == 'POST':
#             product_name = request.form.get('product_name')
#             quantity = request.form.get('quantity')
#             low_stock_threshold = request.form.get('low_stock_threshold')
#             product_code = request.form.get('product_code')

#             try:
#                 sql = "UPDATE products SET product_name=%s, quantity=%s, low_stock_threshold=%s, product_code=%s WHERE id=%s"
#                 val = (product_name, quantity, low_stock_threshold, product_code, product_id)
#                 cursor.execute(sql, val)
#                 conn.commit()
#             except mysql.connector.Error as db_err:
#                 return f"Database error during update: {db_err}"

#             # Fetch store_id before redirecting
#             sql = "SELECT store_id FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             result = cursor.fetchone()
#             if result:
#                 store_id = result[0]
#             else:
#                 return "Product not found"  # Or handle the error appropriately

#             cursor.close()
#             conn.close()
#             return redirect(url_for('view_products', store_id=store_id))

#         else:  # GET request
#             try:
#                 sql = "SELECT id, store_id, product_name, quantity, low_stock_threshold, product_code FROM products WHERE id = %s"
#                 cursor.execute(sql, (product_id,))
#                 product = cursor.fetchone()
#                 if product:
#                     store_id = product[1]  # Access store_id from the fetched product
#                     return render_template('edit_product.html', product=product, store_id=store_id)  # Pass store_id here
#                 else:
#                     return "Product not found"  # Or handle the error appropriately
#             except mysql.connector.Error as db_err:
#                 return f"Database error: {db_err}"
#             finally:
#                  cursor.close()
#                  conn.close()
#     else:
#         return "Failed to connect to the database"

# @app.route('/delete_product/<product_id>')
# def delete_product(product_id):
#     conn = connect_db()
#     if conn:
#         try:
#             cursor = conn.cursor()

#             # Get the store_id before deleting
#             sql = "SELECT store_id FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             result = cursor.fetchone()
#             if result:
#                 store_id = result[0]
#             else:
#                 return "Product not found"

#             sql = "DELETE FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             conn.commit()
#             cursor.close()
#             conn.close()
#             return redirect(url_for('view_products', store_id=store_id))
#         except mysql.connector.Error as db_err:
#             return f"Database error: {db_err}"
#     else:
#         return "Failed to connect to the database"

# @app.route('/qr_login/<store_id>')
# def qr_login(store_id):
#     # Redirects to the dashboard using the store_id from the QR code
#     return redirect(url_for('dashboard', store_id=store_id))

# @app.route('/')
# def index():
#     return render_template('login.html')

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, render_template, request, redirect, url_for, send_from_directory
# import mysql.connector
# import os
# import qrcode
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# import hashlib

# app = Flask(__name__, static_folder='static')
# app.config['SECRET_KEY'] = os.urandom(24)

# # Database configuration (replace with your actual credentials)
# db_config = {
#     'user': 'your_user',
#     'password': 'your_password',
#     'host': 'localhost',
#     'database': 'smart_inventory'
# }

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

# class User(UserMixin):
#     def __init__(self, id):
#         self.id = id

# @login_manager.user_loader
# def load_user(user_id):
#     return User(user_id)

# def connect_db():
#     try:
#         conn = mysql.connector.connect(**db_config)
#         print("Database connection established successfully!")
#         return conn
#     except mysql.connector.Error as err:
#         print(f"Database connection failed: {err}")
#         return None

# def hash_password(password):
#     return hashlib.sha256(password.encode('utf-8')).hexdigest()

# @app.route('/register_store', methods=['GET', 'POST'])
# def register_store():
#     error = None
#     if request.method == 'POST':
#         store_name = request.form.get('store_name')
#         if not store_name:
#             error = "Store name is required"
#             return render_template('register_store.html', error=error)

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 # Check if store already exists
#                 sql = "SELECT id FROM stores WHERE store_name = %s"
#                 cursor.execute(sql, (store_name,))
#                 existing_store = cursor.fetchone()

#                 if existing_store:
#                     error = "Store already exists!"
#                     return render_template('register_store.html', error=error)

#                 sql = "INSERT INTO stores (store_name) VALUES (%s)"
#                 cursor.execute(sql, (store_name,))
#                 conn.commit()
#                 store_id = cursor.lastrowid  # Get the store ID

#                 # Generate QR Code
#                 qr = qrcode.QRCode(
#                     version=1,
#                     error_correction=qrcode.constants.ERROR_CORRECT_L,
#                     box_size=10,
#                     border=4,
#                 )
#                 qr_data = f"{request.url_root}qr_login/{store_id}"
#                 qr.add_data(qr_data)
#                 qr.make(fit=True)
#                 img = qr.make_image(fill_color="black", back_color="white")

#                 # Ensure the 'static/qrcodes' directory exists
#                 qr_dir = os.path.join(app.static_folder, 'qrcodes')
#                 os.makedirs(qr_dir, exist_ok=True)

#                 qr_code_path = os.path.join('qrcodes', f'store_{store_id}.png')
#                 img_path = os.path.join(app.static_folder, qr_code_path)
#                 img.save(img_path)

#                 # Update the stores table with the QR code path
#                 sql = "UPDATE stores SET qr_code_path = %s WHERE id = %s"
#                 cursor.execute(sql, (qr_code_path, store_id))
#                 conn.commit()
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('login'))  # Redirect to login page

#             except mysql.connector.Error as db_err:
#                 error = f"Database error: {db_err}"
#                 return render_template('register_store.html', error=error)

#         return render_template('register_store.html', error=error)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     qr_code_path = None
#     stores = [] #List of stores will be rendered in the HTML
#     if request.method == 'POST':
#         store_name = request.form.get('store_name')
#         password = request.form.get('password')

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 # SQL Query to select the store
#                 sql = "SELECT id FROM stores WHERE store_name = %s AND password = %s"
#                 cursor.execute(sql, (store_name, hash_password(password)))
#                 store = cursor.fetchone()
#                 #If there is a store
#                 if store:
#                     user = User(store[0])
#                     login_user(user)
#                     cursor.close()
#                     conn.close()
#                     #Redirects to the dashboard
#                     return redirect(url_for('dashboard', store_id=store[0]))
#                 else:
#                     error = "Invalid store name or password"
#                 cursor.close()
#                 conn.close()
#             except mysql.connector.Error as db_err:
#                 error = f"Database error: {db_err}"
#         else:
#             error = "Failed to connect to the database"
    
#     conn = connect_db()
#     if conn:
#         try:
#             cursor = conn.cursor()
#             # SQL Query to get all stores
#             sql = "SELECT id, store_name FROM stores"
#             cursor.execute(sql)
#             stores = cursor.fetchall()
#             cursor.close()
#             conn.close()
#         except mysql.connector.Error as db_err:
#             error = f"Database error: {db_err}"

#     return render_template('login.html', error=error, stores=stores)

# @app.route('/qr_login/<store_id>')
# def qr_login(store_id):
#     conn = connect_db()
#     if conn:
#         cursor = conn.cursor()
#         sql = "SELECT id FROM stores WHERE id = %s"
#         cursor.execute(sql, (store_id,))
#         store = cursor.fetchone()
#         cursor.close()
#         conn.close()

#         if store:
#             user = User(store_id)
#             login_user(user)
#             return redirect(url_for('dashboard', store_id=store_id))
#         else:
#             return "Invalid store ID"
#     else:
#         return "Failed to connect to the database"

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('login'))

# @app.route('/dashboard/<store_id>')
# @login_required
# def dashboard(store_id):
#     conn = connect_db()
#     if conn:
#         cursor = conn.cursor()
#         sql = "SELECT store_name, qr_code_path FROM stores WHERE id = %s"
#         cursor.execute(sql, (store_id,))
#         store = cursor.fetchone()
#         cursor.close()
#         conn.close()

#         if store:
#             store_name = store[0]
#             qr_code_path = store[1]
#             return render_template('dashboard.html', store_id=store_id, store_name=store_name, qr_code_path=qr_code_path)
#         else:
#             return "Store not found"
#     else:
#         return "Failed to connect to the database"

# @app.route('/add_product/<store_id>', methods=['GET', 'POST'])
# @login_required
# def add_product(store_id):
#     if request.method == 'POST':
#         product_name = request.form.get('product_name')
#         quantity = request.form.get('quantity')
#         low_stock_threshold = request.form.get('low_stock_threshold')
#         product_code = request.form.get('product_code')

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 sql = "INSERT INTO products (store_id, product_name, quantity, low_stock_threshold, product_code) VALUES (%s, %s, %s, %s, %s)"
#                 val = (store_id, product_name, quantity, low_stock_threshold, product_code)
#                 cursor.execute(sql, val)
#                 conn.commit()
#                 cursor.close()
#                 conn.close()

#                 return redirect(url_for('dashboard', store_id=store_id)) #Redirect
#             except mysql.connector.Error as db_err:
#                 return f"Database error: {db_err}"
#         else:
#             return "Failed to connect to the database"

#     return render_template('add_product.html', store_id=store_id)

# @app.route('/view_products/<store_id>')
# @login_required
# def view_products(store_id):
#     conn = connect_db()
#     if conn:
#         try:
#             cursor = conn.cursor()
#             sql = "SELECT id, store_id, product_name, quantity, low_stock_threshold, product_code, (quantity <= low_stock_threshold) AS low_stock_warning FROM products WHERE store_id = %s"
#             cursor.execute(sql, (store_id,))
#             products = cursor.fetchall()
#             cursor.close()
#             conn.close()
#             return render_template('view_products.html', store_id=store_id, products=products)
#         except mysql.connector.Error as db_err:
#             return f"Database error: {db_err}"
#     else:
#         return "Failed to connect to the database"

# @app.route('/edit_product/<product_id>', methods=['GET', 'POST'])
# @login_required
# def edit_product(product_id):
#     conn = connect_db()
#     if conn:
#         cursor = conn.cursor()

#         if request.method == 'POST':
#             product_name = request.form.get('product_name')
#             quantity = request.form.get('quantity')
#             low_stock_threshold = request.form.get('low_stock_threshold')
#             product_code = request.form.get('product_code')

#             try:
#                 sql = "UPDATE products SET product_name=%s, quantity=%s, low_stock_threshold=%s, product_code=%s WHERE id=%s"
#                 val = (product_name, quantity, low_stock_threshold, product_code, product_id)
#                 cursor.execute(sql, val)
#                 conn.commit()
#             except mysql.connector.Error as db_err:
#                 return f"Database error during update: {db_err}"

#             # Fetch store_id before redirecting
#             sql = "SELECT store_id FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             result = cursor.fetchone()
#             if result:
#                 store_id = result[0]
#             else:
#                 return "Product not found"  # Or handle the error appropriately

#             cursor.close()
#             conn.close()
#             return redirect(url_for('view_products', store_id=store_id))

#         else:  # GET request
#             try:
#                 sql = "SELECT id, store_id, product_name, quantity, low_stock_threshold, product_code FROM products WHERE id = %s"
#                 cursor.execute(sql, (product_id,))
#                 product = cursor.fetchone()
#                 if product:
#                     store_id = product[1]  # Access store_id from the fetched product
#                     return render_template('edit_product.html', product=product, store_id=store_id)  # Pass store_id here
#                 else:
#                     return "Product not found"  # Or handle the error appropriately
#             except mysql.connector.Error as db_err:
#                 return f"Database error during select: {db_err}"
#             finally:
#                  cursor.close()
#                  conn.close()

#     return "Failed to connect to the database"

# @app.route('/delete_product/<product_id>')
# @login_required
# def delete_product(product_id):
#     conn = connect_db()
#     if conn:
#         try:
#             cursor = conn.cursor()

#             # Get the store_id before deleting
#             sql = "SELECT store_id FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             result = cursor.fetchone()
#             if result:
#                 store_id = result[0]
#             else:
#                 return "Product not found"

#             sql = "DELETE FROM products WHERE id = %s"
#             cursor.execute(sql, (product_id,))
#             conn.commit()
#             cursor.close()
#             conn.close()
#             return redirect(url_for('view_products', store_id=store_id))
#         except mysql.connector.Error as db_err:
#             return f"Database error: {db_err}"
#         else:
#             return "Failed to connect to the database"

#     return "Failed to connect to the database"

# @app.route('/')
# def index():
#     return render_template('login.html')

# if __name__ == '__main__':
#     app.run(debug=True)





from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os
import qrcode

app = Flask(__name__, static_folder='static')

# Database configuration (replace with your actual credentials)
db_config = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'database': 'smart_inventory'
}

def connect_db():
    try:
        conn = mysql.connector.connect(**db_config)
        print("Database connection established successfully!")
        return conn
    except mysql.connector.Error as err:
        print(f"Database connection failed: {err}")
        return None

@app.route('/register_store', methods=['GET', 'POST'])
def register_store():
    error = None
    if request.method == 'POST':
        store_name = request.form.get('store_name')
        if not store_name:
            error = "Store name is required"
            return render_template('register_store.html', error=error)

        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                # Check if store already exists
                sql = "SELECT id FROM stores WHERE store_name = %s"
                cursor.execute(sql, (store_name,))
                existing_store = cursor.fetchone()

                if existing_store:
                    error = "Store already exists!"
                    return render_template('register_store.html', error=error)

                sql = "INSERT INTO stores (store_name) VALUES (%s)"
                cursor.execute(sql, (store_name,))
                conn.commit()
                store_id = cursor.lastrowid  # Get the store ID

                # Generate QR Code
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                # Modified to create link
                qr_data = f"{request.url_root}qr_login/{store_id}"

                qr.add_data(qr_data)  # Encode the store ID in the QR code
                qr.make(fit=True)

                img = qr.make_image(fill_color="black", back_color="white")

                # Ensure the 'static/qrcodes' directory exists
                qr_dir = os.path.join(app.static_folder, 'qrcodes')
                os.makedirs(qr_dir, exist_ok=True)

                qr_code_path = os.path.join('qrcodes', f'store_{store_id}.png')
                img_path = os.path.join(app.static_folder, qr_code_path)
                img.save(img_path)

                # Update the stores table with the QR code path
                sql = "UPDATE stores SET qr_code_path = %s WHERE id = %s"
                cursor.execute(sql, (qr_code_path, store_id))
                conn.commit()
                cursor.close()
                conn.close()

                return redirect(url_for('login'))  # Redirect to login page

            except mysql.connector.Error as db_err:
                error = f"Database error: {db_err}"
                return render_template('register_store.html', error=error)
        else:
            error = "Failed to connect to the database"

    return render_template('register_store.html', error=error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    qr_code_path = None
    store_id_for_qr = None
    stores = []  # List to hold store information for the dropdown

    conn = connect_db()
    if not conn:
        error = "Failed to connect to the database"
        return render_template('login.html', error=error, stores=stores)

    cursor = conn.cursor()

    # Fetch all stores for the dropdown
    sql = "SELECT id, store_name FROM stores"
    cursor.execute(sql)
    stores = cursor.fetchall()

    if request.method == 'POST':
        store_id = request.form.get('store_id')  # Get store ID from the form
        password = request.form.get('password')

        # Validate if store_id and password are correct
        sql = "SELECT * FROM stores WHERE id = %s AND password = %s"  # Assuming you have a password field in stores
        cursor.execute(sql, (store_id, password))
        store = cursor.fetchone()

        if store:
            cursor.close()
            conn.close()
            return redirect(url_for('dashboard', store_id=store_id))
        else:
            error = "Invalid store ID or password"

    # Retrieve QR code path for selected store
    selected_store_id = request.args.get('store_id')  # From query parameters (after dropdown selection)

    if selected_store_id:
        sql = "SELECT id, qr_code_path FROM stores WHERE id = %s"
        cursor.execute(sql, (selected_store_id,))
        store = cursor.fetchone()
        if store:
            qr_code_path = store[1]
            store_id_for_qr = store[0]
        else:
            error = "Store not found"

    cursor.close()
    conn.close()
    return render_template('login.html', error=error, qr_code_path=qr_code_path,
                           store_id_for_qr=store_id_for_qr, stores=stores, selected_store_id=selected_store_id)

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

@app.route('/dashboard/<store_id>')
def dashboard(store_id):
    return render_template('dashboard.html', store_id=store_id)

@app.route('/add_product/<store_id>', methods=['GET', 'POST'])
def add_product(store_id):
    if request.method == 'POST':
        product_name = request.form.get('product_name')
        quantity = request.form.get('quantity')
        low_stock_threshold = request.form.get('low_stock_threshold')
        product_code = request.form.get('product_code')

        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                sql = "INSERT INTO products (store_id, product_name, quantity, low_stock_threshold, product_code) VALUES (%s, %s, %s, %s, %s)"
                val = (store_id, product_name, quantity, low_stock_threshold, product_code)
                cursor.execute(sql, val)
                conn.commit()
                cursor.close()
                conn.close()

                return redirect(url_for('dashboard', store_id=store_id)) #Redirect
            except mysql.connector.Error as db_err:
                return f"Database error: {db_err}"
        else:
            return "Failed to connect to the database"

    return render_template('add_product.html', store_id=store_id)

@app.route('/view_products/<store_id>')
def view_products(store_id):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "SELECT id, store_id, product_name, quantity, low_stock_threshold, product_code, (quantity <= low_stock_threshold) AS low_stock_warning FROM products WHERE store_id = %s"
            cursor.execute(sql, (store_id,))
            products = cursor.fetchall()
            cursor.close()
            conn.close()
            return render_template('view_products.html', store_id=store_id, products=products)
        except mysql.connector.Error as db_err:
            return f"Database error: {db_err}"
    else:
        return "Failed to connect to the database"

@app.route('/edit_product/<product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()

        if request.method == 'POST':
            product_name = request.form.get('product_name')
            quantity = request.form.get('quantity')
            low_stock_threshold = request.form.get('low_stock_threshold')
            product_code = request.form.get('product_code')

            try:
                sql = "UPDATE products SET product_name=%s, quantity=%s, low_stock_threshold=%s, product_code=%s WHERE id=%s"
                val = (product_name, quantity, low_stock_threshold, product_code, product_id)
                cursor.execute(sql, val)
                conn.commit()
            except mysql.connector.Error as db_err:
                return f"Database error during update: {db_err}"

            # Fetch store_id before redirecting
            sql = "SELECT store_id FROM products WHERE id = %s"
            cursor.execute(sql, (product_id,))
            result = cursor.fetchone()
            if result:
                store_id = result[0]
            else:
                return "Product not found"  # Or handle the error appropriately

            cursor.close()
            conn.close()
            return redirect(url_for('view_products', store_id=store_id))

        else:  # GET request
            try:
                sql = "SELECT id, store_id, product_name, quantity, low_stock_threshold, product_code FROM products WHERE id = %s"
                cursor.execute(sql, (product_id,))
                product = cursor.fetchone()
                if product:
                    store_id = product[1]  # Access store_id from the fetched product
                    return render_template('edit_product.html', product=product, store_id=store_id)  # Pass store_id here
                else:
                    return "Product not found"  # Or handle the error appropriately
            except mysql.connector.Error as db_err:
                return f"Database error during select: {db_err}"
            finally:
                 cursor.close()
                 conn.close()
    else:
        return "Failed to connect to the database"

@app.route('/delete_product/<product_id>')
def delete_product(product_id):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()

            # Get the store_id before deleting
            sql = "SELECT store_id FROM products WHERE id = %s"
            cursor.execute(sql, (product_id,))
            result = cursor.fetchone()
            if result:
                store_id = result[0]
            else:
                return "Product not found"

            sql = "DELETE FROM products WHERE id = %s"
            cursor.execute(sql, (product_id,))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('view_products', store_id=store_id))
        except mysql.connector.Error as db_err:
            return f"Database error: {db_err}"
    else:
        return "Failed to connect to the database"

@app.route('/qr_login/<store_id>')
def qr_login(store_id):
    # Redirects to the dashboard using the store_id from the QR code
    return redirect(url_for('dashboard', store_id=store_id))

@app.route('/')
def index():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)