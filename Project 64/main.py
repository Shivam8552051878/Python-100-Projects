import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dic(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/all")
def get_all_cafe():
    cafes = db.session.execute(db.select(Cafe)).scalars().fetchall()
    # print(cafes)
    # print(cafes)
    data = []
    for cafe in cafes:
        data.append(cafe.to_dic())

    return jsonify(cafes=data)


@app.route("/random")
def get_random_cafe():
    cafes = db.session.execute(db.select(Cafe)).scalars().fetchall()
    # print(cafes)
    # print(cafes)
    random_cafe = random.choice(cafes)
    print(random_cafe.to_dic())
    return jsonify(cafe=random_cafe.to_dic())


@app.route("/search", methods=["GET"])
def get_search_cafe():
    loc = request.args.get("loc")
    cafes = db.session.execute(db.select(Cafe).where(Cafe.location == loc.title())).scalars().fetchall()
    if len(cafes) != 0:
        data = []
        for cafe in cafes:
            data.append(cafe.to_dic())
        return jsonify(cafe=data)
    else:
        return jsonify(error={
            "Not Found": "We dont have cafe on that location"
        })
    # return "GE"


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_item():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record
@app.route("/update/<int:cafe_id>", methods=["PATCH"])
def update_data(cafe_id):
    update_cafes_price = db.session.query(Cafe).get(cafe_id)
    if update_cafes_price:
        update_cafes_price.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify(response={"success": "Successfully update the new cafe price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
# 7.2 5700 credit card
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
