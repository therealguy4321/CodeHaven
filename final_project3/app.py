from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passwords.db'
db = SQLAlchemy(app)

class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

class PasswordForm(FlaskForm):
    account = StringField('Account', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Save')

@app.route('/')
def index():
    passwords = Password.query.all()
    return render_template('index.html', passwords=passwords)

@app.route('/add_password', methods=['GET', 'POST'])
def add_password():
    form = PasswordForm()
    if form.validate_on_submit():
        new_password = Password(account=form.account.data, password=form.password.data)
        db.session.add(new_password)
        db.session.commit()
        flash('Password added successfully', 'success')
        return redirect(url_for('index'))
    return render_template('add_password.html', form=form)

@app.route('/edit_password/<int:id>', methods=['GET', 'POST'])
def edit_password(id):
    password = Password.query.get_or_404(id)
    form = PasswordForm()
    if form.validate_on_submit():
        password.account = form.account.data
        password.password = form.password.data
        db.session.commit()
        flash('Password updated successfully', 'success')
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.account.data = password.account
        form.password.data = password.password
    return render_template('edit_password.html', form=form)

@app.route('/delete_password/<int:id>', methods=['GET', 'POST'])
def delete_password(id):
    password = Password.query.get_or_404(id)
    db.session.delete(password)
    db.session.commit()
    flash('Password deleted successfully', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
