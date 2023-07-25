from flask import Flask # import flask module
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import redirect
from flask import jsonify
from flask import url_for
import pymysql # 모듈 import
import app

def login():
	#요청방식 ( get/ post)
	method = request.method
	if method == 'GET':
		return render_template('login.html')
	else:
		id = request.form.get('id')
		pw = request.form.get('pw')
		encode = request.form.get('encode')
		if not id or not pw:  # id, pw, encode 가 비어 있는 경우
			return "<script>alert(\'ID와 PW를 확인하세요\');window.history.back();</script>"
		if not encode:  # encode 가 비어 있는 경우
			return "<script>alert(\'Entrancecode를 확인하세요\');window.history.back();</script>"
		elif encode != 'ssgcloud':
			return "<script>alert(\'Entrancecode를 확인하세요\');window.history.back();</script>"

		conn = pymysql.connect(
			host='15.164.153.191', user='team2', password='team2',
			db='team2', charset='utf8'
		) # 데이터베이스 접속
		cursor = conn.cursor() # 커서 객체 생성
		sql = '''
			SELECT count(id) 
			FROM members 
			WHERE members.id = %s AND members.password = %s
		'''
		cursor.execute(sql,(id,pw)) # SQL 실행
		row = cursor.fetchone()
		cursor.close() # 커서 객체 종료
		conn.close() # 접속 해제
		count = row[0]
		if count == 0:
			return "<script>alert(\'ID와 PW를 확인하세요\');window.history.back();</script>"	
		else:
			session['user_id'] = id
			if id == 'admin':
				session['user_role'] = 'admin'
			else:
				session['user_role'] = 'user'
			return app.domainpage()