import pandas as pd 

df = pd.read_csv('credit.csv')
# print(df)

# print(df['나이'].mean())
# print(df['나이'].mode())
# print(df['나이'].max())
# print(df['나이'].min())
# print(df['나이'].describe())

numeric_columns = df.select_dtypes(include=['number'])

# print(df.groupby('성별')[numeric_columns.columns].mean())

# print(df[['나이','사용금액']].corr())

print(df.query(" 나이 > 50 and 기혼 == 'Married' "))

filtered_df = df.query("성별 == 'M' and 기혼 == 'Married'")
numeric_cols = filtered_df.select_dtypes(include='number')
print(numeric_cols.mean())