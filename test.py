import streamlit as st
import math

# 앱 제목
st.title("간단한 수학 계산기")

# 사용자로부터 숫자 입력 받기
number = st.number_input("숫자를 입력하세요:", min_value=0.0)

# 입력된 숫자에 대해 계산
if number >= 0:
    square = number ** 2  # 제곱
    square_root = math.sqrt(number)  # 제곱근

    # 결과 출력
    st.write(f"{number}의 제곱은 {square:.2f}입니다.")
    st.write(f"{number}의 제곱근은 {square_root:.2f}입니다.")
else:
    st.write("숫자는 0 이상의 값을 입력하세요.")
