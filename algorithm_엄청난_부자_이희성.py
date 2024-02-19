a = input()  # .input()으로 첫째 줄의 n과 m의 입력을 받음
b = a.split()  # .split()으로 입력받은 n과 m을 공백을 기준으로 나눠, b = ['n', 'm'] 리스트 형태로 변환
print(int(b[0]) // int(b[1]))  # b에 있는 'n'과 'm'을 인덱싱한 후 str에서 int로 형변환해서 //로 몫을 출력
print(int(b[0]) % int(b[1]))  # b에 있는 'n'과 'm'을 인덱싱한 후 str에서 int로 형변환해서 %로 나머지를 출력