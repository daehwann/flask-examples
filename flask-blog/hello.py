from flask import Flask, url_for, render_template, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!!!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

with app.test_request_context():
    print url_for('hello')
    print url_for('hello_world')
    print url_for('show_user_profile', username='John Doe')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)



