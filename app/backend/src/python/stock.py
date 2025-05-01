import pandas as pd
import numpy as np
import statsmodels.api as sm
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib import rc
from sklearn.linear_model import LinearRegression

# Yahoo Finance에서 데이터를 가져오기
df_apple = yf.download('AAPL', start="2023-12-29", end="2024-12-29")
df_samsung = yf.download('005930.KS', start="2023-12-29", end="2024-12-29")

# Apple 데이터 처리 및 이동평균 계산
df_apple['MA5'] = df_apple['Close'].rolling(window=5).mean()  # 5일 이동평균
df_apple['MA20'] = df_apple['Close'].rolling(window=20).mean()  # 20일 이동평균

# Samsung 데이터 처리 및 이동평균 계산
df_samsung['MA5'] = df_samsung['Close'].rolling(window=5).mean()  # 5일 이동평균
df_samsung['MA20'] = df_samsung['Close'].rolling(window=20).mean()  # 20일 이동평균

# # Apple 종가와 이동평균선 플롯
# plt.figure(figsize=(12, 6))
# plt.plot(df_apple['Close'], label="Apple Close Price (USD)", color='blue')
# plt.plot(df_apple['MA5'], label="5-Day MA", color='green', linestyle='--')
# plt.plot(df_apple['MA20'], label="20-Day MA", color='red', linestyle='--')
# plt.title("Apple Stock Close Price and Moving Averages")
# plt.xlabel("Date")
# plt.ylabel("Close Price (USD)")
# plt.legend()
# plt.grid()
# plt.show()

# # Samsung 종가와 이동평균선 플롯
# plt.figure(figsize=(12, 6))
# plt.plot(df_samsung['Close'], label="Samsung Close Price (KRW)", color='blue')
# plt.plot(df_samsung['MA5'], label="5-Day MA", color='green', linestyle='--')
# plt.plot(df_samsung['MA20'], label="20-Day MA", color='red', linestyle='--')
# plt.title("Samsung Stock Close Price and Moving Averages")
# plt.xlabel("Date")
# plt.ylabel("Close Price (KRW)")
# plt.legend()
# plt.grid()
# plt.show()



# plt.bar([1,2,3], [10,20,30])
# plt.show()

# plt.pie([50, 30, 20], labels=['ramen', 'tuna', 'snack'])
# plt.show()

# plt.hist([160,165,170,171,172,180])
# plt.show()

# plt.stackplot([1,2,3], [10,20,30], [30,20,50], [50, 30, 60])
# plt.show()


# 키 = np.array([170,180,160,165,158,176,182,172]).reshape((-1, 1))
# 몸무게 = [75,81,59,70,55,78,84,72] 

df = pd.read_csv('california_housing.csv')
print(df)

model = sm.OLS(df['price'], df[['year', 'rooms', 'bedrooms']]).fit()
print(model.summary())

a = model.predict([20, 1000, 200])
print(a)

# model = sm.OLS(몸무게, 키).fit()
# print(model.summary())

# # plt.scatter(키, 몸무게)
# # plt.show()

# # 모델 생성 및 학습
# model = LinearRegression().fit(키, 몸무게)

# # 모델 정보 출력
# print("모델 가중치(기울기):", model.coef_)
# print("모델 절편(Intercept):", model.intercept_)
# print("결정 계수(R^2):", model.score(키, 몸무게))

# # 예측 값 계산
# predicted = model.predict(키)


# # 한글 폰트 설정 (Windows의 경우 Malgun Gothic 사용)
# plt.rc('font', family='Malgun Gothic')
# plt.rc('axes', unicode_minus=False)  # 마이너스 기호 깨짐 방지

# # 시각화
# plt.scatter(키, 몸무게, color='blue', label='실제 데이터')  # 실제 데이터 점
# plt.plot(키, predicted, color='red', label='예측 선형 회귀선')  # 회귀선
# plt.title('Linear Regression: 키와 몸무게')
# plt.xlabel('키 (cm)')
# plt.ylabel('몸무게 (kg)')
# plt.legend()
# plt.grid()
# plt.show()