from flask import (
    Flask, render_template, redirect, url_for, request, flash, session
)
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError
from validate_email_address import validate_email
from werkzeug.security import check_password_hash
from wtforms import (
    StringField, FloatField, PasswordField, SubmitField
)
from wtforms.validators import DataRequired, Email, EqualTo


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Create the database and the table
with app.app_context():
    db.create_all()

class ExpenseForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()], render_kw={"placeholder": "Description"})
    amount = FloatField('Amount', validators=[DataRequired()], render_kw={"placeholder": "Amount"})
    submit = SubmitField('Add Expense')

class UserRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserRegistrationForm()
    if form.validate_on_submit():
        password = form.password.data
        confirm_password = form.confirm_password.data

        if password != confirm_password:
            flash('Passwords do not match. Please enter matching passwords.', 'danger')
        elif not validate_email(form.email.data):
            flash('Invalid email address format. Please enter a valid email address.', 'danger')
        else:
            existing_user = User.query.filter_by(email=form.email.data).first()

            if existing_user:
                flash('Email address is already in use. Please choose a different email.', 'danger')
            else:
                try:
                    new_user = User(username=form.username.data, email=form.email.data, password=password)
                    db.session.add(new_user)
                    db.session.commit()
                    flash('Registration successful. You can now log in.', 'success')
                    return redirect(url_for('login'))
                except IntegrityError as e:
                    db.session.rollback()
                    flash('An error occurred during registration. Please try again.', 'danger')

    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Error in {getattr(form, field).label.text}: {error}', 'danger')

    return render_template('register.html', form=form)

@app.route('/')
def home():
    if 'user_id' in session:
        user_id = session['user_id']
        user = User.query.get(user_id)

        if user:
            expenses = Expense.query.filter_by(user_id=user.id).all()
            return render_template('home.html', user=user, expenses=expenses)

    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identifier = request.form['identifier']  # Use a single input field for both username and email
        password = request.form['password']

        # Check if the identifier is an email
        is_email = '@' in identifier

        # Update the query to filter by username or email
        if is_email:
            user = User.query.filter_by(email=identifier, password=password).first()
        else:
            user = User.query.filter_by(username=identifier, password=password).first()

        if user:
            session['user_id'] = user.id
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')



@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logout successful', 'success')
    return redirect(url_for('login'))

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    form = ExpenseForm()
    if form.validate_on_submit():
        description = request.form['description']
        amount = request.form['amount']
        user_id = session['user_id']

        new_expense = Expense(description=description, amount=amount, user_id=user_id)
        db.session.add(new_expense)
        db.session.commit()
        flash('Expense added successfully', 'success')
        return redirect(url_for('home'))
    return render_template('add_expense.html', form=form)

@app.route('/delete_expense/<int:expense_id>', methods=['POST'])
def delete_expense(expense_id):
    expense = Expense.query.get(expense_id)
    if expense:
        db.session.delete(expense)
        db.session.commit()
        flash('Expense deleted successfully', 'success')
    else:
        flash('Expense not found', 'danger')

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
