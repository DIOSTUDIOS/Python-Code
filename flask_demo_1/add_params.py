from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User {:s}'.format(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'POST ID {:d}'.format(post_id)
