from app import app
from flask import render_template
from app.models import Post

@app.route('/')
def index():
    # Fetch from db
    posts = Post.query.all()

    # posts = []
    return render_template('index.html', posts=posts)


@app.route('/blogposts')
def blogs():

     # Fetch from db
    posts = Post.query.all()

    return render_template('blogs.html', posts=posts)

@app.route('/blogsposts/<int:id>')
def single_blog(id):

    #Fetch single post from DB
    post = Post.query.get(id)

    return render_template('blog.html', post=post)