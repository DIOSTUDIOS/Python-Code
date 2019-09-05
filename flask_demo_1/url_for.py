from flask import Flask, url_for

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User {:s}'.format(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'POST ID {:d}'.format(post_id)


@app.route('/url/')
def get_url():
    return url_for('show_post', post_id=2)


if __name__ == '__main__':
    app.run(debug=True)