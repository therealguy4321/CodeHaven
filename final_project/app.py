import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///market.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any previous user
    session.clear()

    # User reached route via post
    if request.method == "POST":
        # Ensure user submits username
        if not request.form.get("username"):
            return apology("Must enter username")

        # Ensure user submits email
        elif not request.form.get("email"):
            return apology("Must enter email")

        # Ensure user provides password
        elif not request.form.get("password"):
            return apology("Must enter password")

        # Ensure user confirms password
        elif not request.form.get("confirmation"):
            return apology("Must confirm password")

        # Ensure passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords do not match")

        # Check database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username does not already exist
        if len(rows) != 0:
            return apology("Username already exists")

        # Check database for email
        rows = db.execute(
            "SELECT * FROM users WHERE email = ?", request.form.get("email")
        )

        # Ensure username does not already exist
        if len(rows) != 0:
            return apology("Email has already been used")

        # Insert new user into database
        db.execute(
            "INSERT INTO users (username, email, password) VALUES(?, ?, ?)",
            request.form.get("username"),
            request.form.get("email"),
            generate_password_hash(request.form.get("password")),
        )

        # Check database for newly inserted user
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to homepage
        return redirect("/")

    # User reached route via GET
    else:
        return render_template("register.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username or email is submitted
        username_or_email = request.form.get("username_or_email")
        if not username_or_email:
            return apology("must provide username or email", 403)

        # Ensure password is submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = :input OR email = :input",
            input=username_or_email,
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["password"], request.form.get("password")
        ):
            return apology("invalid username/email and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Check if "cart" is not in session and initialize it
        if "cart" not in session:
            session["cart"] = []

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")




@app.route("/")
@login_required
def index():
    """Show portfolio of goods"""
    # Get the products for sale
    goods = db.execute("SELECT * FROM products")

    # # Get the user's cash balance
    # user_id = session["user_id"]
    # user = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=user_id).fetchone()
    # cash = user["cash"] if user else 0  # Default to 0 if user not found

    return render_template("index.html", goods=goods) #cash=cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy goods"""
    if request.method == "POST":
        # Get the selected product ID from the form
        product_id = request.form.get("product_id")

        # Retrieve product details from the database based on the product_id
        product = db.execute("SELECT * FROM products WHERE id = :id", id=product_id).fetchone()


        if "cart" not in session:
            session["cart"] = []

         # Append product as a dictionary
        session["cart"].append({
            "id": product[0]["id"],
            "name": product[0]["name"],
            "description": product[0]["description"],
            "price": product[0]["price"]
        })

        # Redirect back to the index page after adding to the cart
        return redirect(url_for('index'))

    # Retrieve all products from the database to display on the page
    products = db.execute("SELECT * FROM products")

    return render_template("buy.html", products=products)


# New route to remove items from the cart
@app.route("/remove_from_cart", methods=["POST"])
def remove_from_cart():
    product_id = request.form.get("product_id")

    if product_id and "cart" in session:
        try:
            # Attempt to convert product_id to integer
            product_id = int(product_id)
        except ValueError:
            # If conversion to integer fails, assume it's already a string
            pass

        # Remove the product with the specified ID from the cart
        updated_cart = [item for item in session["cart"] if str(item.get("id")) != str(product_id)]

        # Update the cart in the session
        session["cart"] = updated_cart

    return redirect(url_for("cart"))


@app.route("/cart", methods=["GET", "POST"])
@login_required
def cart():
    """View the shopping cart"""
    cart = session.get('cart', [])  # Retrieve the cart from the session, default to an empty list

    return render_template("cart.html", cart=session.get("cart", []))


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell Goods"""
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        description = request.form.get("description")
        price = request.form.get("price")

        # Add goods to the table
        db.execute("INSERT INTO products (name, description, price) VALUES (?, ?, ?)", name, description, price)

    return render_template("sell.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
