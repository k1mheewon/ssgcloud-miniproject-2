from flask import Flask # import flask module
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import redirect
from flask import jsonify
from flask import url_for
import pymysql 

def logout():
    session.pop('user_id', None)  # 세션에서 user_id 제거
    return redirect('/login')