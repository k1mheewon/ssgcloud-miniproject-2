from flask import Flask # import flask module
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import redirect
from flask import jsonify
from flask import url_for
import pymysql  # 모듈 import


def adminpage():
    # 데이터베이스에서 요청 목록 조회
    conn = pymysql.connect(
        host='15.164.153.191',
        user='team2',
        password='team2',
        db='team2',
        charset='utf8'
    )
    cursor = conn.cursor()
    sql = '''
        SELECT * FROM register WHERE approval = "n" ORDER BY menu_num ASC;
    '''
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('adminpage.html', data=data)

# 요청 처리 API

def handle_approval():
    try:
        data = request.json['data']
        action = request.json['action']

        # 데이터베이스 업데이트 또는 삭제 처리
        conn = pymysql.connect(
            host='15.164.153.191',
            user='team2',
            password='team2',
            db='team2',
            charset='utf8'
        )
        cursor = conn.cursor()
        for item in data:
            name = item['name']
            type = item['type']
            address = item['address']
            
            if action == 'approved':
                # 승인 처리
                sql = '''
                    UPDATE register SET approval = "y" WHERE restaurant_name = %s AND food_type = %s AND address = %s;
                '''
                cursor.execute(sql, (name, type, address))
            elif action == 'notapproved':
                # 거절 처리
                sql = '''
                    UPDATE register SET approval = "x" WHERE restaurant_name = %s AND food_type = %s AND address = %s;
                '''
                cursor.execute(sql, (name, type, address))

        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'msg': '처리되었습니다.', 'code': 1})
    except Exception as e:
        return jsonify({'msg': str(e), 'code': 0})