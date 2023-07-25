from flask import Flask # import flask module
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import redirect
from flask import jsonify
from flask import url_for
import pymysql 

def mainpage():
	user_id = session.get('user_id')
	if user_id:
		return render_template('index.html', user_id=user_id)
	else:
		return "You are not logged in <br><a href = '/login'></b>" + \
		"click here to login</b></a>"