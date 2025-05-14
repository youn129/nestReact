# 연습용입니다.

# import pandas as pd
# import re

# raw = pd.read_excel('product.xlsx', engine = "openpyxl")

# def 함수(a):
#     return a * 1.1

# raw['부가세 포함'] = raw['판매가'].apply(함수)



# def 함수2(a):
#     if re.search('Chair', str(a)):
#         return '의자'
#     if re.search('Table', str(a)):
#         return '테이블'
    
# raw['카테고리'] = raw['상품목록'].apply(함수2)
# print(raw)


# a = re.findall('ㅋ+', 'ab안c녕d&eㅋㅋㅋㅋㅋf^gㅋ')
# print(a)


# print(re.sub('\D','','ab안c녕d&eㅋ5ㅋㅋㅋ1234ㅋf^gㅋ'))