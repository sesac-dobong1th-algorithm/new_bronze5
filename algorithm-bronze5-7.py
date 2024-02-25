import tkinter as tk    # 파이썬 GUI 기본 라이브러리 tk(GUI)inter(INTERFACE) 사용, tk라고 줄여서 불러온다.
from tkinter import simpledialog    # tkinter 라는 모듈에서 simpledialog를 불러온다.

root = tk.Tk()  # 대화창 객체 생성
root.withdraw()     # tkinter 기본 껍데기 숨기기

N = simpledialog.askinteger("입력", "N 값을 입력하세요 (0 또는 1):")  
# 유저에게 0이나 1을 입력 받는다. 입력창, 안내창 글귀 생성

# 입력 값에 따라 조건부 출력을 실행합니다.
if N == 0:      # 만약 입력값이 0을 입력 한다면
    print("YONSEI")     # 대문자 영문 YOUNSEI를 출력한다.
elif N == 1:       # 만약 입력값이 1을 입력한다면
    print("Leading the Way to the Future")  # 연세대학교 슬로건을 출력
else:       # 위 조건 이외의 정수를 입력한다면
    print("0 또는 1이어야 합니다.")     # 이러한 오류안내문구를 출력한다.
