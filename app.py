from flask_sqlalchemy import SQLAlchemy
from flask import Flask,request,render_template,redirect,url_for
############################### security from users
from markupsafe import escape
#########################refer to intery point of application ,,,public static void main(){}
myapp = Flask(__name__)


######################################create my first route
@myapp.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"
#######################################################33333
def anotherroute():
    print(request.args.get('name'))
    return f"<h1>Another route! {escape(request.args.get('name')) } </h1>"

myapp.add_url_rule('/another',view_func=anotherroute)
#########################################################3333
@myapp.route("/profile/<name>/<int:id>")
def profile(name,id):
    return f"profile {name}{id}"
###################################################################response
@myapp.route("/response")
def test_response():
    response=myapp.make_response("this is simple response")
    response.status=200
    return response
########################################################return with template
@myapp.route("/home",endpoint='home')
def home():
    thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
    return render_template('test/home.html',name=thisdict)

#############################################################crate 404 page
@myapp.errorhandler(404)
def test_404(error):
    return render_template('test/page_not_found.html')

###################################################################add static file
@myapp.route("/static")
def inclide_static():
    return render_template('test/includestatic.html')
##################################################################macros in flask,templates

@myapp.route("/macros")
def test_macros():
    students =['youssef', 'mohamed','rady']
    courses=['youssef', 'mohamed','rady']
    return render_template('test/students.html',students=students,courses=courses)

############################################################connect to database
myapp.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///examples.sqlite"
db=SQLAlchemy(myapp)


class Posts(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100))
    description=db.Column(db.String(200))


    def __str__(self):
        return self.title
    

@myapp.route("/posts",endpoint='allposts')
def allposts():
    posts=Posts.query.all()
    return render_template('pages/listposts.html',posts=posts)


@myapp.route("/showpost/<int:id>",endpoint='show')
def showpost(id):
    post=Posts.query.get_or_404(id)
    return render_template('pages/showpost.html',post=post)

@myapp.route("/delete/<int:id>",endpoint='delete')
def deletepost(id):
    post=Posts.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('allposts'))








#############################3to apply changes int  the database
    