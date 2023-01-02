#    This is a simple webserver implemented using Python Flask library

from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def greet():
    # Get the current date and the user's birthday from the query string
    name = request.args.get('name')
    current_date_str = request.args.get('date')
    birthday_str = request.args.get('birthday')

    # Check if any of the required query string parameters are missing
    if name is None or current_date_str is None or birthday_str is None:
        return '<h1>Error: Missing query string parameter</h1>'

    # Convert the dates to datetime objects
    try:
        current_date = datetime.strptime(current_date_str, '%Y-%m-%d')
        birthday = datetime.strptime(birthday_str, '%Y-%m-%d')
    except ValueError:
        return '<h1>Error: Invalid date format</h1>'

    # Check if it is the user's birthday
    if current_date.month == birthday.month and current_date.day == birthday.day and current_date.year == birthday.year:
        return f'<h1>Happy Birthday {name}!</h1>'
    else:
        return "<h1>This is a simple Web-Server</h1>"


if __name__ == "__main__":
    app.run(debug=True)
