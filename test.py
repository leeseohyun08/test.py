import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 앱 제목
st.title("수학 함수 그래프 그리기")

# 함수 입력받기
st.subheader("그릴 함수 입력:")
user_function = st.text_input("함수 입력 (예: x**2, np.sin(x), np.cos(x), x**3 - 2*x + 1)")

# 함수가 비어 있지 않으면 그래프를 그립니다.
if user_function:
    try:
        # x 값 범위 설정
        x = np.linspace(-10, 10, 400)
        
        # 사용자가 입력한 함수를 실행할 수 있도록 하기
        y = eval(user_function)  # 입력한 수식 계산
        
        # 그래프 그리기
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=f'y = {user_function}')
        plt.title(f'그래프: y = {user_function}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.legend(loc="best")
        
        # Streamlit에서 그래프 표시
        st.pyplot(plt)

    except Exception as e:
        st.error(f"함수 계산 중 오류가 발생했습니다: {e}")
else:
    st.write("위에 함수 수식을 입력하면 해당 함수의 그래프를 그릴 수 있습니다.")
