from flask import Flask, render_template, request, redirect, send_file
from so import get_jobs
from save import save_to_file
app = Flask(__name__)

db = {} 
# database를 만들어준 이유: 한번 검색하면 여기에 저장되어 나중에 똑같은걸 검색할때 여기서 바로 꺼내서 시간을 줄일 수 있도록
# db를 제일 상위에 위치한 이유: 새로고침해도 안에 저장된 data가 그대로 있어야 하므로.

@app.route('/') # 웹사이트 제일 첫번째 화면 url 이 된다.
def home():
    return render_template("flower.html")
# 이런식으로 render_temlplate 함수를 import 하여, html 파일을 home 함수안에서 불러와 웹상에 그 파일을 띄울 수 있게 된다. 
# 반드시 'templates' 라는 폴더를 만들고 그 안에 파일을 넣어야 작동이 되는구나!!

@app.route('/contact')
def contact():    
    return "come back to me"


# @app.route('/<username>')
# def username(username):
#     return f"Hello your name is {username}"
# url 입력란에다가 '/<username>' 요렇게 해주고 밑에 인자를 받는 함수를 입력하면 url에 입력하는 글자가 인자가 되어 username 함수에 대입된다. 
# 이런걸 dynamic url 이라고 한다.


@app.route('/report')
def report():
    word = request.args.get('word').lower() # url을 보면 a = b 처럼 dict 형태가 보임 그중에서 word= $$ 해당하는 $$를 뽑아내는거임. 
    # 그리고 대문자를 입력했을 경우를 대비해 소문자로 바꾸어줬음.    
    if word: #If word has value
        fromDb = db.get(word) # db 안에 저장된 jobs data를 꺼내오기. 
        if fromDb: # 만약 그게 있다면 그걸 jobs라고 다시 지정함. jobs 라고 지정했기 때문에 형태가 생겼고 ,report.html 같은 다른곳에서 사용가능해짐.
            jobs = fromDb
        else: # db에 저장되게 없으면 저장해라. {key = word, value =  get_jobs(word)}
            jobs = get_jobs(word) # word 가 so.py에서 url 로 바뀌었고 필요한곳에 사용되도록 수정했다.(기존 URL 은 python만 search 가능하도록 했지만 지금은 입력하는 족족 search 되도록 해야하므로.)
            db[word] = jobs 
    else: #If word is None
        return redirect("/") # word가 None 이면 홈으로 경로를 재설정한다.(redirect 를 import 해줌.)
    return render_template("report.html",
    searchingword = word, 
    searchingrResult = len(jobs), 
    jobs = jobs[:10] # 이렇게 하면 최초로딩시간이 조금 더 줄어든다
    ) 
    # 그럼 report.html 상에서 {{searchingword}}를 word 로 치환한다.
    # 이러한 과정을 'rendering' 이라고 한다.
    # 그리고 대박!! 버그 발생했을때, 논리를 공책에 적고 라인에 번호를 매긴다음, 번호가 지나갈때마다 어떤일이 일어나는지 적으면서 눈으로 확인하자! ​
    # 왼쪽페이지 에는 코드를, 오른쪽 페이지에는 번호를 적고, 각 번호에 어떤일이 일어나는지 적자. 그렇게 해서 오늘 버그가 왜 발생했는지 알아냈다.
    # internal server error 가 발생했었는데 알고보니 if word: jobs = get_jobs(word)를 추가했기 때문이었다. 


@app.route('/export')
def export():
    try:
        word = request.args.get('word').lower()
        if not word:
            raise Exception()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv", mimetype='application/x-csv', attachment_filename='summary_report.csv', as_attachment=True) # 이렇게 하면 이름 적은대로 저장됨.
    except:
        return redirect("/")
# word 없으면 홈으로 다시 보냄. 그리고 word, jobs 가 없으면 exception() 함수 작동. 즉, except로 바로 보낸다는 뜻.     
# save_to_file(save.py에 있는 함수) 이랑 send_file(파일을 다운받는 함수) import 함


app.run(host="0.0.0.0")

# 계속 /contact 했을때 not found 가 떠서 뭐지 했는데 알고보니, 새로고침이 안되서 그런것이었다.
# ctrl + c 해주거나 superscrap.py를 나갔다가 다시 들어가면 될것이다.

