import random
import requests
import json

# 랜덤한 거 뽑기
def get_random_numbers():
    numbers = random.sample(range(1, 46), 6)
    return sorted(numbers)

#진짜 정보 가져오기
def get_lotto_numbers(num):
    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    res = requests.get(url).text  # type == String
    data = json.loads(res)  # type == dict
    bonus_number = data['bnusNo']
    # winning = data['firstAccumamnt']

    real_numbers = []


    if data['returnValue'] == 'success':
        for key, value in data.items():
            if 'drwtNo' in key:
                real_numbers.append(value)

        real_numbers.sort()
    return {'real' : real_numbers, 'bonus': bonus_number}

# 등수 매기기 함수
def get_result(real_list, random_list, bonus) :
    lucky = set(real_list)
    real = set(random_list)

    match_count = len(real.intersection(lucky))

    result = '꽝'
    if match_count == 6:
        result = 1
    elif match_count == 5 and bonus in random_list:
        result = 2
    elif match_count == 5:
        result = 3
    elif match_count == 4:
        result = 4
    elif match_count == 3:
        result = 5

    return result

# 하이라이트!
print(__name__)

