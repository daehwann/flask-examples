"""
Source from Pretty Printed in Youtube

"""
from flask import Flask, redirect, url_for
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
from flask_dance.contrib.github import make_github_blueprint, github

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'

twitter_blueprint = make_twitter_blueprint(api_key='TV8PbP9UFClxFbnixNgJ4T83y', api_secret='BrQLEDqebA688wh6hndXfQDegmEvtGnwpK1ZGWchVZaSdcqQtA')

github_blueprint = make_github_blueprint(client_id='1b2a54cba53d965b316c', client_secret='9d3776541fdf26319cc2c9f84e5c7c75b94d36bb')

app.register_blueprint(twitter_blueprint, url_prefix='/twitter_login')

app.register_blueprint(github_blueprint, url_prefix='/github_login')


@app.route('/twitter')
def twitter_login():
	if not twitter.authorized:
		return redirect(url_for('twitter.login'))

	#login
	account_info = twitter.get('account/settings.json')

	if account_info.ok:
		account_info_json = account_info.json()
		return '<h1>Your Twitter name is @{}'.format(account_info_json['screen_name'])

	return '<h1>Request failed!</h1>'


@app.route('/github')
def github_login():
	if not github.authorized:
		return redirect(url_for('github.login'))

	#login
	account_info = github.get('/user')

	if account_info.ok:
		account_info_json = account_info.json()
		return '<h1>Your Github name is {}'.format(account_info_json['login'])

	return '<h1>Request Failed!'

if __name__ == '__main__':
	app.run(debug=True)
