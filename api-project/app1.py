from flask import Flask
app = Flask(__name__) 

@app.route('/') # 사용자에게 경로를 알려준다. / 는 루트이므로 가장 기본경로.
def hello_world():
    return '<h1>Hello World!</h1><input type="textbox"/>' # 화면에 뿌려줄 값. html  그 자체.

if __name__ == '__main__': # main 부분의  run으로 서버가 동작한다.
    app.run()