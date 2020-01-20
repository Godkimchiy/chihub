from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test():
    return render_template('post.html') # templates 폴덩 안의 html을 불러와 리턴.

@app.route('/post', methods=['POST'])
def post():
    value = request.form['test']
    return value

if __name__ == '__main__':
    app.run()