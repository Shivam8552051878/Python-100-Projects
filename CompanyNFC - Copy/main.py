import uuid
from io import BytesIO
import flask_login
import qrcode
import vobject
from flask import Flask, render_template, flash, redirect, url_for, request, send_file, make_response
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from Helper.forms import RegisterationForm, LoginForm, VCardFrom

from Helper.Vcard.vcard import VCardFormate

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstarp = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///company.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///company.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    vcard = relationship("VCard", back_populates="user_data")
    # comments = relationship("Comment", back_populates="comment_author")


class VCard(db.Model):
    __tablename__ = "vcard"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    organization = db.Column(db.String(20))
    title = db.Column(db.String(20))
    # photo_url = request.form['photo_url']
    work_phone = db.Column(db.String(15))
    home_phone = db.Column(db.String(15))
    cell_phone = db.Column(db.String(15))
    whatsapp_number = db.Column(db.String(15))
    work_fax = db.Column(db.String(15))
    work_email = db.Column(db.String(20))
    home_email = db.Column(db.String(20))
    website = db.Column(db.String(100))
    work_address = db.Column(db.String(255))
    home_address = db.Column(db.String(255))
    # birthday = request.form['birthday']
    # anniversary = request.form['anniversary']
    notes = db.Column(db.String(255))
    linkedin_profile = db.Column(db.String(50))
    twitter_profile = db.Column(db.String(50))
    facebook_profile = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user_data = relationship("User", back_populates="vcard")
    qrcode = relationship("QRCode", back_populates='vcard_data')


class QRCode(db.Model):
    __tablename__ = 'qrcodes'
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String, unique=True)  # Column for the link
    vcf_file = db.Column(db.Text)  # Column for the VCF file
    qr_code_img = db.Column(db.LargeBinary)
    vcard_id = db.Column(db.Integer, db.ForeignKey("vcard.id"))
    vcard_data = relationship("VCard", back_populates="qrcode")


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route("/about")
def about():
    return render_template("about.html", logged_in=current_user.is_authenticated)


@app.route("/contact")
def contact():
    return render_template("contact.html", logged_in=current_user.is_authenticated)


@app.route("/Sign-Up", methods=["GET", "POST"])
def registration():
    form = RegisterationForm()
    if form.validate_on_submit():
        password = generate_password_hash(form.password.data, method="pbkdf2", salt_length=8)
        new_user = User(
            email=form.email.data,
            name=form.name.data,
            password=password,

        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template("register.html", form=form, logged_in=current_user.is_authenticated)


@app.route("/Sign-In", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email == form.data.get("email"))).scalar()
        if not user:
            flash("This email id dose not exit.Try another.")
            return redirect(url_for("login"))
        elif not check_password_hash(user.password, form.data.get("password")):
            flash("Incorrect password.Try again.")
            return redirect(url_for("login"))
        else:
            login_user(user)
            return redirect(url_for("home"))
    return render_template("login.html", form=form, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect(url_for("home"))


@app.route('/create-vcard', methods=["POST", "GET"])
@login_required
def vcard():
    form = VCardFrom()
    if form.validate_on_submit():
        card = VCard(first_name=form.first_name.data,
                     last_name=form.last_name.data,
                     organization=form.organization.data or None,
                     title=form.title.data or None,
                     # photo_url = request.form['photo_url'],
                     work_phone=form.work_phone.data or None,
                     home_phone=form.home_phone.data or None,
                     cell_phone=form.cell_phone.data or None,
                     work_fax=form.work_fax.data or None,
                     work_email=form.work_email.data or None,
                     home_email=form.home_email.data or None,
                     website=form.website.data or None,
                     notes=form.notes.data or None,
                     linkedin_profile=form.linkedin_profile.data or None,
                     twitter_profile=form.twitter_profile.data or None,
                     facebook_profile=form.facebook_profile.data or None,
                     whatsapp_number=form.whatsapp_number.data or None,
                     work_address=form.work_address.data or None,
                     home_address=form.home_address.data or None,
                     user_id=current_user.id
                     )
        db.session.add(card)
        db.session.commit()
        print(card.id)
        return redirect(url_for("insertdata", card_id=card.id))
    return render_template("create-Vcard.html", form=form, logged_in=True)


@app.route("/show-vcards", methods=["GET", "POST"])
@login_required
def show_vcard():
    # print(current_user.id)
    vcards = db.session.execute(db.select(VCard).where(VCard.user_id == current_user.id)).scalars().fetchall()
    # print(uuid.uuid4().hex)
    return render_template("showvcard.html", vcards=vcards, logged_in=True)


@app.route("/generate-file-qqrcode/<int:card_id>", methods=["POST", "GET"])
@login_required
def insertdata(card_id):
    print(card_id)
    vcard = VCardFormate()
    vcard_data = db.session.execute(db.select(VCard).where(VCard.id == card_id)).scalar()
    data = []
    name = data.append(vcard.name(vcard_data.first_name) if vcard_data.first_name != None else "")
    formated_name = data.append(
        vcard.formated_name(vcard_data.first_name, vcard_data.last_name) if vcard_data.first_name != None else "")
    organization = data.append(vcard.organization(vcard_data.organization) if vcard_data.organization != None else "")
    title = data.append(vcard.title(vcard_data.title) if vcard_data.title != None else "")
    work_phone = data.append(vcard.phone(vcard_data.work_phone) if vcard_data.work_phone != None else "")
    home_phone = data.append(vcard.phone(vcard_data.home_phone, type="home") if vcard_data.home_phone != None else "")
    cell_phone = data.append(vcard.phone(vcard_data.cell_phone, type="cell") if vcard_data.cell_phone != None else "")
    work_fax = data.append(
        vcard.phone(vcard_data.work_fax, type="work", phone_num_type="fax") if vcard_data.work_fax != None else "")
    work_email = data.append(vcard.email(email_id=vcard_data.work_email) if vcard_data.work_email != None else "")
    home_email = data.append(
        vcard.email(email_id=vcard_data.home_email, type="home") if vcard_data.home_email != None else "")
    website = data.append(vcard.website(vcard_data.website) if vcard_data.website != None else "")
    notes = data.append(vcard.website(vcard_data.notes) if vcard_data.notes != None else "")
    linkedin_profile = data.append(vcard.social_profile(url=vcard_data.linkedin_profile,
                                                        type="linkedin") if vcard_data.linkedin_profile != None else "")
    twitter_profile = data.append(vcard.social_profile(url=vcard_data.twitter_profile,
                                                       type="twitter") if vcard_data.twitter_profile != None else "")
    facebook_profile = data.append(vcard.social_profile(url=vcard_data.facebook_profile,
                                                        type="facebook") if vcard_data.facebook_profile != None else "")
    whatsapp_number = data.append(
        vcard.social_profile(url=vcard_data.whatsapp_number) if vcard_data.whatsapp_number != None else "")
    work_address = data.append(
        vcard.address(address_main=vcard_data.home_address, type="work") if vcard_data.home_address != None else "")
    home_address = data.append(
        vcard.address(address_main=vcard_data.home_address, type="home") if vcard_data.home_address != None else "")
    str_data = ""
    print(data)
    print(facebook_profile)
    for d in data:
        if d == "":
            pass
        else:
            str_data += "\n" + d
    vcffile_str = vcard.format_vcard(str_data)
    # binary_vcffile_str = ''.join(format(ord(i), '08b') for i in vcffile_str)
    unik_link = uuid.uuid4().hex
    # qr = qrcode.QRCode(
    #     version=1,
    #     error_correction=qrcode.constants.ERROR_CORRECT_H,
    #     box_size=10,
    #     border=4,
    # )
    # qr.add_data(f"http://127.0.0.1:4444/{unik_link}")
    # qr.make(fit=True)
    # qr_img = qr.make_image(fill_color="black", back_color="white")
    qrcode_data = QRCode(
        link=str(uuid.uuid4()),
        vcf_file=vcffile_str,
        qr_code_img=None,
        vcard_id=card_id
    )
    db.session.add(qrcode_data)
    db.session.commit()
    return redirect(url_for("show_vcard"))


@app.route("/<int:post_id>")
def result(post_id):
    return render_template("result.html", post_id=post_id)


@app.route("/download/<int:post_id>")
def download_file(post_id):
    print(post_id)
    file_entry = db.session.execute(db.select(QRCode).where(QRCode.id == post_id)).scalar()
    name = db.session.execute(db.select(VCard).where(VCard.id == file_entry.vcard_id)).scalar()
    print(name)
    print(file_entry)
    if file_entry:
        response = make_response(file_entry.vcf_file)
        response.headers['Content-Disposition'] = 'attachment; filename=' + (name.first_name + ".vcf")
        return response
        # return send_file(
        #     file_entry.vcf_file,
            # attachment_filename="shivam.vcf",
        #     as_attachment=True,
        #     download_name="shivam.vcf"
        # )

    return "File not found."

@app.route('/download-file')
def download_file_():
    # file_record = File.query.filter_by(id=1).first()  # Replace 'id=1' with your desired file identifier

    response = make_response("shivam this side")
    response.headers['Content-Disposition'] = 'attachment; filename=' + "file_record.txt"

    return response

@app.route('/generate', methods=['POST', 'GET'])
def generate_qr_code():
    if request.method == 'POST':
        link = request.form.get('link')
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')

        # Create a vCard (VCF) object
        vcard = vobject.vCard()
        vcard.add('fn').value = "shivam"
        vcard.add('n').value = vobject.vcard.Name(family=name)
        vcard.add('tel').value = phone
        vcard.add('email').value = email

        # Save the vCard to a VCF file
        vcf_file = BytesIO()
        vcard.serialize(vcf_file)
        vcf_file.seek(0)

        # Generate the QR code image
        # qr = qrcode.QRCode(
        #     version=1,
        #     error_correction=qrcode.constants.ERROR_CORRECT_H,
        #     box_size=10,
        #     border=4,
        # )
        # qr.add_data(link)
        # qr.make(fit=True)
        # qr_img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image and VCF file to the database
        qr_code = QRCode(link=link, vcf_file=vcf_file.read())
        db.session.add(qr_code)
        db.session.commit()

    return render_template("qrcode.html")


@app.route('/download/<int:image_id>')
def download_qr_code(image_id):
    qr_code = db.session.query(QRCode).filter_by(id=image_id).first()
    print(qr_code)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_code.link)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    # Send the QR code image
    # qr_img = BytesIO(qr_img)
    # qr_img.seek(0)
    qr_img.save("./static/qr/qrcode.png")

    # Send the VCF file
    # vcf_file = BytesIO(qr_code.vcf)
    # vcf_file.seek(0)
    with open("./static/vcf/contact.vcf", 'w') as f:
        vcf_file = f.write(qr_code.vcf_file.decode())
    return send_file('static/qr/qrcode.png', as_attachment=True) and send_file('static/vcf/contact.vcf',
                                                                               as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4444, debug=True)
