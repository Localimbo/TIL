from flask import Flask, render_template
import random
import requests
import json

app = Flask(__name__)      # app 변수에 플라스크 객체 생성

# 그냥 template 소환해보기
@app.route('/')
def index():
    return render_template('index.html')         # templates directory 내에 html 파일 넣어준다. 함수가 templates 내에서 밖에 찾지 않기 때문에 !

# 로또 번호 랜덤으로 골라주기
@app.route('/pick_lotto')
def pick_lotto():
    lucky_numbers = random.sample(range(1, 46), 6)
    lucky_numbers.sort()
    return render_template('pick_lotto.html', numbers=lucky_numbers)  # numbers를 같이 넘기는거! 단순 문자열X, 변수임을 알려주는 {{}}

# sorted() 와 객체.sort()의 차이
#sorted(luck)  -  luck순서가 sort 된 채로 보여지기만 함. immutable(변경불가)
#luck.sort - luck자체의 순서를 아예 바꿔버림. 원본 자료형 바뀜  mutable

# API 사용
# Get(내놔) => Get a HTML
# Post(받아라) => Post a Data
@app.route('/lotto/<int:num>')
def find_lotto(num):
    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    res = requests.get(url).text         # 내용만 url로 가져온 typpe == string.
    data = json.loads(res)         # 딕셔너리 형태! type == dictionary

    real_numbers = []

    if data['returnValue'] == 'success':
        for key, value in data.items():
            if 'drwtNo' in key:
                real_numbers.append(value)

        real_numbers.sort()

    return render_template('get_lotto.html', numbers=real_numbers, draw_no=num)

# 제곱 구하기
@app.route('/square/<int:num>')
def square(num):
    result = num ** 2
    return f'{result}'

#  해당 피일을 직접 실행하면 main, 다른 누군가가 패카지 형식으로 import하면 다르게 나타난다.
if __name__ == '__main__':
    app.run(debug=True)

