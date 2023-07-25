from flask import Flask # import flask module
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import redirect
from flask import jsonify
from flask import url_for
import pymysql 

import login, logout, addmember,mainpage

app = Flask(__name__) # 초기화
app.secret_key = 'your_secret_key'

@app.route('/', methods = ['GET', 'POST']) # 요청 주소
def index():
   user_id = session.get('user_id')
   if user_id:
    return render_template('index.html', user_id=user_id)
   else:
    return redirect('/login')

#login
@app.route('/login', methods=['get', 'post'])
def dologin():
    return login.login()

#logout
@app.route('/logout')
def dologout():
	return logout.logout()

#회원가입
@app.route('/addmember', methods=['get', 'post'])
def doaddmember():
	return addmember.addmember()

#메인페이지
@app.route('/mainpage', methods=['get', 'post'])
def domainpage():
	return mainpage.mainpage()

#관리자페이지


if __name__ == '__main__':
    app.run(debug= True)