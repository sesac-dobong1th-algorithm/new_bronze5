# 결과를 저장할 빈 리스트 초기화
result = []

# 무한 루프 시작
while True:
    try:
        # 사용자로부터 두 개의 정수 n과 s를 입력받음
        n, s = map(int, input().split())
        # 계산된 값을 result 리스트에 추가
        # s를 n+1로 나눈 몫을 계산하여 추가
        result.append(s // (n+1))
    except:
        # 예외 발생 시 (올바르지 않은 입력 등), 루프 종료 전에 result 리스트의 모든 값을 출력
        for x in result:
            print(x)
        break  # 무한 루프 종료
