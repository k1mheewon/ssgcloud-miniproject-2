from flask import Flask, redirect, render_template, request, jsonify, url_for



app = Flask(__name__) # 초기화

@app.route('/', methods = ['GET', 'POST']) # 요청 주소
def index():
    return render_template(
        'index.html'
    )




if __name__ == '__main__':
    app.run(debug= True)