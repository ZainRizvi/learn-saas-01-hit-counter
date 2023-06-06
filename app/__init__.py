from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"mysql://root:{os.getenv('MYSQL_ROOT_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB')}"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Counter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, default=0)


@app.route('/', methods=['GET', 'POST'])
def home():
    counter = Counter.query.get(1)

    if request.method == 'POST':
        if request.form['action'] == 'increment':
            counter.value += 1
        elif request.form['action'] == 'decrement':
            counter.value -= 1
        db.session.commit()

    return render_template('index.html', counter=counter.value)


if __name__ == '__main__':
    app.run(debug=True)
