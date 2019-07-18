from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:build-a-blog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(2000))
   
    def __init__(self, title, body):
        self.title = title
        self.body = body
       
@app.route('/newpost', methods=['POST', 'GET'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        new_post = Blog(title,body)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/')
        
    return render_template('newpost.html')

@app.route('/')
def index():

    blogs = Blog.query.all()
    return render_template('blog.html',title="My Blog!", 
        blogs=blogs)


if __name__ == '__main__':
    app.run()