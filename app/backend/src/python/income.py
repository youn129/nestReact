# 연습용입니다.

# from scipy.optimize import curve_fit
# import matplotlib.pyplot as plt
# import statsmodels.api as sm
# import pandas as pd
# import numpy as np

# df = pd.read_table('income.txt')
# df = df.dropna()

# # def 함수(x, a, b, c):
# #     return a*x + b*x**2 + c

# # opt, cov = curve_fit(함수, df['age'], df['income'])
# # print(opt)
# # a, b, c = opt

# # x = np.array([1,2,3,4,5,6])
# # plt.scatter(df['age'], df['income'])
# # plt.plot(x, 함수(x, a, b, c))
# # plt.show()

# x = np.column_stack([df['age'], df['age']**2])
# model = sm.OLS(df['income'], x).fit()
# print(model.summary())