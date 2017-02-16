from app import app
from flask import render_template, url_for, request, flash, redirect
from .forms import ContactForm
from .utils import contact_form_email, is_safe_url

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/contact", methods=["GET","POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        print email
        textarea = form.textarea.data 
        contact_form_email(message=name + "  " + email + "  " + textarea, sender=email)
        next = request.args.get("next")
        if not is_safe_url(next):
            return flask.abort(400)
        flash("You have successfully sent Sea Turtle Web Dev a message. Please allow 24 hours for a response.", "success")
        return redirect(next or url_for("contact"))
    return render_template(
        "contact.html",
        form=form
        )

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/test")
def test():
    return render_template('test.html')

