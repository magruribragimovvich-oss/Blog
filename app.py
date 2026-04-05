import os
from flask import Flask, render_template
from slugify import slugify
from flask import jsonify

app = Flask(__name__)

def read_articles():
    articles = os.listdir('articles')
    slug_articles = {}
    for article in articles:
        slug = slugify(article)
        slug_articles[slug] = article
    return slug_articles

articles = read_articles()


@app.route('/')
def index():
    return render_template('blog.html', articles=articles)


@app.route('/blog/<slug>')
def blog(slug: str):
    title = articles[slug]
    with open(f'articles/{title}') as file:
        content = file.read()
        
    return jsonify({
        "title": title,
        "content": content
    })
if __name__ == '__main__':
    app.run(debug=True)