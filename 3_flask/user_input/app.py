from flask import Flask, render_template, request
from iexfinance.stocks import Stock

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search_stock')
def stock():
    return render_template('search_stock.html', is_first_search = True)


@app.route('/search_result')
def result():

    TOKEN = 'pk_0c38a77cb70e40348dd01fc20f5bfa1f'

    user_input = request.args.get('keyword')    # *** 핵심 코드! 사용자가 이전에 제출한 데이터 받아오기

    try:
        stock = Stock(user_input, token=TOKEN)    # 시도해서 안되면 except으로 가라
        data = stock.get_quote()
    except:
         return render_template(      # 에러나면은 탈출해라
            'search_stock.html',
            is_success = False,)

    return render_template(
        'search_stock.html',
        is_success = True,
        c_name = data['companyName'],      # 변수에 데이터 담아서 html에 실어서 보냄
        l_price = data['latestPrice'], )


if __name__ == '__main__' :
    app.run(debug=True)

