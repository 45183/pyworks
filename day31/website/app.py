from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/season/')
def season():
    season = "겨울"
    seasons = ['봄', '여름', '가을', '겨울']
    return render_template(
        'season.html',
        season = season,
        seasons = seasons
    )    # 키 = 값

@app.route('/loop_index/', methods = ['GET'])       #methods = ['GET'] 생략가능
def loop_index():
    items = ['a', 'b', 'c', 'd']
    return render_template('loop_index.html', items = items)

@app.route('/register/', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 데이터 전닯 받음(가져오기)
        mid = request.form['mid']
        pwd = request.form['passwd']
        name = request.form['name']
        gender = request.form['gender']
        return render_template(
            'memberlist.html',
            mid=mid, pwd=pwd,
            name=name,
            gender=gender)                          # 데이터를 memberlist.html에 보냄
    else:                                           # request.method == 'GET'
        return render_template('register.html')

@app.route('/even_odd/', methods=['GET', 'POST'])
def even_odd():
    if request.method == "POST":
        try:
            # 데이터 수집
            num = int(request.form['num'])              # 정수 입력받을경우 앞에 int붙여야함
        except ValueError:
            error = "숫자를 입력하세요"
            return render_template('even_odd.html', error_msg = error)
        else:
            # 데이터 연산
            if num % 2 == 0:
                result = "짝수입니다."
            else:
                result = "홀수입니다."

            return render_template('calc_result.html', num = num, result=result)
    else:
        return render_template('even_odd.html')

app.run()