from flask import Flask # import flask module
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import redirect
from flask import jsonify
from flask import url_for
import pymysql  # 모듈 import

def addmember():
	method = request.method
	if method == 'GET':
		return render_template('addmember.html')
	else:		
		id = request.form.get('id')
		pw = request.form.get('pw')
		name = request.form.get('name')
		age = request.form.get('age')
		gender = request.form.get('gender')
		if not id or not pw:  # 아이디 또는 비밀번호가 비어 있는 경우
			return {'msg': 'ID와 PW를 확인하세요', 'code': 2}
		if not name or not name.isalpha():
			return {'msg': '이름을 확인해주세요', 'code': 2}
		if not age or not age.isdigit():
			return {'msg': '나이를 확인해주세요', 'code': 2}
		if not gender or len(gender) > 2:
			return {'msg': '성별을 확인해주세요', 'code': 2}
		
		conn = pymysql.connect(
			host='15.164.153.191', user='team2', password='team2',
			db='team2', charset='utf8'
		) # 데이터베이스 접속
		cursor = conn.cursor() # 커서 객체 생성
		sql = '''
			SELECT count(id) 
			FROM members 
			WHERE members.id = %s
		'''
		cursor.execute(sql,(id,)) # SQL 실행
		row = cursor.fetchone()

		count = row[0]

		if count != 0:
			cursor.close() # 커서 객체 종료
			conn.close() # 접속 해제	
			return {'msg': '중복된ID', 'code': 0}
		else :	
			cursor = conn.cursor()
			sql = '''
				insert into  members (id, password,member_name,gender,age) values (%s,%s,%s,%s,%s)
			'''
			cursor.execute(sql,(id,pw,name,gender,age)) # SQL 실행
			conn.commit()
			cursor.close() # 커서 객체 종료
			conn.close() # 접속 해제				
			return {'msg': '회원가입 성공', 'code': 1}