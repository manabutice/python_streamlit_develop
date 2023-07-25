import streamlit as st
import time

st.title('streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0) # 初期値を0に設定します

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress((i+1)/100) # 0から1までの値になるように設定します
    time.sleep(0.01) # このスリープは実際の処理の代わりで、時間経過をシミュレートします

'Done!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')