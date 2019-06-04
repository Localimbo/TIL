from django.shortcuts import render


def index(request):
    return render(request, 'utils/index.html')

def arti(request, keyword):
    import art
    result = art.text2art(keyword, 'random')    # 'random'도 가능
    context = {
        'result' : result,
        'keyword' : keyword,
    }
    return render(request, 'utils/arti.html', context)

# 사용자가 입력 form을 제공하는 액션
def stock_input(request) :
    return render(request, 'utils/stock_input.html')

# 입력받은 data를 처리하여 결과를 제공하는 액션
def stock_output(request) :
    from iexfinance.stocks import Stock

    company_code = request.GET.get("company_code")   # post 요청으로 날라온 값 중 키 값, company_code 빼오기
    TOKEN = 'pk_0c38a77cb70e40348dd01fc20f5bfa1f'

    try:
        stock = Stock(company_code, token=TOKEN)  # 시도해서 안되면 except으로 가라
        data = stock.get_quote()                # company_code 정보 가져오기
    except:                                     # 윗 두 줄에서 문제가 없다면 그냥 pass, 에러 난다면 except로 진입?
        return render(request, 'utils/stock_output.html', {
            'is_ok' : False,                    # 잘 끝나지 않앗으면, ^^
            'message' : '검색 할 수 없습니다.',
        })
    return render(request, 'utils/stock_output.html', {
        'is_ok' :  True,                        # 잘 끝났으면 data 가져오기
        'data' : data
        })


