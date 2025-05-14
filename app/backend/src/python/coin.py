# 연습용입니다

# import sys
# import traceback

# try:
#     import requests
#     import json
#     import time

#     # 현재 시간 기준 epoch time
#     current_epoch_time = int(time.time() * 1000)

#     # API 요청
#     url = f'https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/XRP?lastDt={current_epoch_time}&interval=1H&1734337133423'
#     response = requests.get(url)
#     # JSON 파싱
#     딕셔너리 = response.json()

#     # 결과 가공
#     result = []
#     for i in 딕셔너리['body']['candles']:
#         formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i['dt'] / 1000))
#         result.append({
#             "datetime": formatted_time,
#             "close": i['close'],
#             "volume": i['volume']
#         })

#     # JSON 출력 (stdout에만 JSON 출력)
#     print(json.dumps(result[:10]))

#     # url2 = [
#     #     "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1609524000000",
#     #     "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608811200000",
#     #     "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608098400000",
#     #     "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1606672800000",
#     #     "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605960000000",
#     #     "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605242700000",
#     #     "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1604534400000",
#     #     "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603821600000",
#     #     "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603108800000",
#     #     "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1602396000000",
#     # ]

#     # def 함수(구멍):
#     #     data = requests.get(구멍)
#     #     딕셔너리 = json.loads(data.content)
#     #     return 딕셔너리['data'][0]['Close']

#     # from multiprocessing.dummy import Pool as ThreadPool

#     # pool = ThreadPool(4)
#     # result = pool.map(함수, url2)
#     # pool.close()
#     # pool.join()

#     # print(result)


# except Exception as e:
#     # 오류만 stderr로 출력
#     print(f"Python script error: {traceback.format_exc()}", file=sys.stderr)
#     sys.exit(1)

