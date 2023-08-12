from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired,URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = StringField('Location URL', validators=[DataRequired(), URL()])
    open_time = StringField('Open Time 8AM', validators=[DataRequired()])
    close_time = StringField('Close Time 9PM', validators=[DataRequired()])
    coffee_rating = SelectField("Coffe Rating", choices=["☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕☕️☕️☕️️"], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Rating", choices=["💪", "💪💪", "💪💪💪", "💪💪💪️💪", "💪💪💪💪💪️"], validators=[DataRequired()])
    power_outlet_rating_filed = SelectField("power outlet rating fields".title(), choices=["🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    if form.validate_on_submit():
        with open('cafe-data.csv','a',encoding="utf8") as file:
            dt = f"\n{form.cafe.data},{form.location_url.data},{form.open_time.data}, " \
                 f"{form.close_time.data},{form.coffee_rating.data},{form.wifi_rating.data},{form.power_outlet_rating_filed.data}"
            file.write(dt)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows, length=len(list_of_rows))


if __name__ == '__main__':
    app.run(debug=True)
