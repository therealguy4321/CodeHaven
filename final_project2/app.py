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
db = SQL("sqlite:///C:/kira tech/110260523-main/final_project2/market.db")


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



@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

