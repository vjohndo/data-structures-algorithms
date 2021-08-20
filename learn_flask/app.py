from flask import Flask, render_template, url_for
from markupsafe import Markup

app = Flask(__name__)

app.config['SECRET']


# This posts will be a list of dictionaries, representing blog posts
posts = [
    {
        'author':'John Do',
        'title':'Blog Post 1',
        'content':'First post concent',
        'date_posted':'April 21, 2012'
    },
    {
        'author':'John Do2',
        'title':'Blog Post 12',
        'content':'First post concent2',
        'date_posted':'April 21, 20122'
    }
]

# Routes are waht you type in to the brower to go into different pages
# Decorators are just ways to add additional fuctionailty to existing functions
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.jinja', posts=posts)


    # return '''
    #         multiline string
    # '''

@app.route("/about")
def about():
    return render_template('about.jinja', title='About Flask')

# Debug mode allows you reload changes without having to restart variables
# if you run this python script direciton script, __name__ will be '__main__'
if __name__ == '__main__':
    app.run(debug=True)