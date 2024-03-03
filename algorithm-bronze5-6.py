def check_password_validity(passwords):     # def 함수 정의 한다. 
    results = []       # 검사 결과 저장리스트 생성
       # 조건 : 비밀번호 길이가 6자리 이상 9자리 이하
    for pwd in passwords:   # for 반복문 사용
        if 6 <= len(pwd) <= 9: # 만약 길이가 6개자리 이상 9자리 이하면 
            results.append("yes")   # 조건에 해당하면 yes 출력
        else:   # 그 이외의 결과
            results.append("no")    # 조건에 해당하지 않으면 no 출력
    return results      # 모든 결과를 반환한다.

N = 3   # 입력 예제 3개 문자열 갯수로 이해하였음
passwords = ["1245125", "asdij", "120318739721"]   # 이 세개의 문자열 입력예제

# 비밀번호 유효성 검사를 수행하고 결과를 출력합니다.
check_results = check_password_validity(passwords)
for result in check_results:    # for 반복문 사용 , check password validity 함수 호출
    print(result)   # 순서대로 결과 출력
