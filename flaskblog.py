from flask import Flask, render_template, redirect, flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__, template_folder="Templates")
app.config['SECRET_KEY'] = "XYZ"

posts = [
  {
    "title":"Blog 1",
    "content": "This is some shitty content of blog 1",
    "author": "aman",
    "date_posted":"2018-04-10"
  },
    {
    "title":"Blog 2",
    "content": "This is some shitty content of blog 2",
    "author": "dummy",
    "date_posted":"2018-04-12"
  },
  ]
  
@app.route("/")
def home():
  return render_template("home.html", posts=posts)


@app.route("/about")
def about():
  return render_template("about.html")
  

@app.route("/register", methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash('Account Created Sucessfully')
    return redirect("login")
  return render_template("register.html", form=form)
 


@app.route("/login", methods=['GET', 'POST'])
def login():
  form = LoginForm()
  return render_template("login.html", form=form)
  
if __name__ == "__main__":
  app.run(debug=True)
