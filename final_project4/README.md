# EXPENSE TRACKER

## Video Demo:  <https://youtu.be/VN68SX_E2MI>

### Description: Building an Expense Tracker Web Application with Flask: A Comprehensive Overview

#### Overview

The Expense Tracker web application is a robust tool for managing expenses, developed using Flask, a web framework for Python. Leveraging the power of Flask, SQLAlchemy, and other essential modules, this application enables users to efficiently handle their financial transactions. From user registration to login, expense addition, and management, the application provides a seamless experience.

## Code Explanation

### `app.py`

In the heart of the application, `app.py` orchestrates the functionalities. Two crucial models, `User` and `Expense`, are defined using SQLAlchemy. The `User` model stores user information, while the `Expense` model handles details about each expense. Flask forms, `ExpenseForm` and `UserRegistrationForm`, facilitate user input for adding expenses and registering users.

The routing logic is encapsulated in this file. Key routes include registration (`/register`), login (`/login`), home (`/`), and actions related to expenses. The home route ensures that only authenticated users can view their expenses, fetched from the database and displayed in descending order based on the amount. This sorting is accomplished in the `home.html` template.

### `layout.html`

This file defines the foundational structure for all HTML pages within the application. It acts as the base layout and includes links to essential external resources, such as the Bootstrap library and custom CSS styles. The footer of the layout incorporates contact links represented by icons for popular social media platforms.

### `register.html`

Building on the base layout, `register.html` is a template that provides a user registration form. Utilizing the `UserRegistrationForm`, users can input their username, email, password and also prompts for confirmation of password. Upon successful registration, the user is redirected to the login page.

### `login.html`

Extending the layout, the `login.html` template offers a user-friendly login form. Users can enter either their username or email for identification. Successful logins result in redirection to the home page.

### `home.html`

This template is a pivotal component, rendering the user's welcome message and displaying their expenses in an interactive table. The table is sorted in descending order based on the expense amount, enhancing user experience. Each row presents expense details and a delete button.

### `add_expense.html`

Dovetailing with the layout, `add_expense.html` facilitates the addition of new expenses. The `ExpenseForm` captures the description and amount of the expense. Upon submission, the expense is added to the database, and users are redirected to the home page.

### `styles.css`

Aesthetic appeal and user experience are enhanced through `styles.css`, a stylesheet that defines the visual aspects of various elements in the application. From form styling to button appearances and social media icons in the footer, this CSS file contributes to the overall coherence of the application.

## Running the Application

1. Ensure you have Python installed.
2. Install the required packages using the following command:

    ```bash
    pip install Flask Flask-SQLAlchemy Flask-WTF Flask-Migrate validate_email_address Werkzeug
    ```

3. Run the application using:

    ```bash
    python app.py
    ```

4. Open your browser and navigate to [http://localhost:5000](http://localhost:5000) to use the Expense Tracker.

## Application Features

- **User Registration**: Users can register with a unique username, email, and password.
- **User Login**: Registered users can log in using their username or email and password.
- **Expense Tracking**: Users can add, view, and delete their expenses. Expenses are displayed in a table sorted by the highest amount.
- **Logout**: Users can log out of their accounts.

## Technologies Used

- Flask: Web framework for building the application.
- SQLAlchemy: Database ORM (Object-Relational Mapping) for interacting with the SQLite database.
- WTForms: Library for handling forms and form validation.
- Flask-Migrate: Extension for handling database migrations.

## Contact Us

For any inquiries or assistance, feel free to contact us through the provided social media channels:

- [WhatsApp](https://wa.link/jwlows)
- [Instagram](https://www.instagram.com/chris_4lyf?igsh=MTFpdjRjcnZnYnZqaQ==)
- [Twitter](https://x.com/Chris_4lyf?t=DdRa5uuD9h-NoPPs0BTpHA&s=09)
- [Telegram](https://t.me/Chris_4lyf)
- [Facebook](https://www.facebook.com/itz.drsmart.3)

## Conclusion

In conclusion, the Expense Tracker web application offers users a comprehensive solution for managing their financial  activities. Built with Flask, it demonstrates the prowess of web development using Python. SQLAlchemy streamlines database interactions, ensuring data integrity. The modular structure, coupled with templates and styles, makes the application easily maintainable and extensible. This Expense Tracker serves as a testament to the flexibility and power of Flask in developing practical and user-friendly web applications.
