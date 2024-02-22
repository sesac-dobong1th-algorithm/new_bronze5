def calculate_sums_and_cubes(N):        # 함수 정의, N에 입력 받는다.
    sum_of_numbers = sum(range(1, N+1)) # (range~ 는 1부터 N까지의 연속된 숫자(정수) 생성
    square_of_sum = sum_of_numbers ** 2 # 1부터 N까지의 합의 제곱
    sum_of_cubes = sum(i**3 for i in range(1, N+1))  # 1부터 N까지의 세제곱의 합
                                                        
    return sum_of_numbers, square_of_sum, sum_of_cubes  # 이 세가지를 전부 계산 및 출력하여 반환한다.

                            # 예시 입력에 대해 함수를 호출하여 결과 출력
N = 5   # N 예시입력 5
sum_of_numbers, square_of_sum, sum_of_cubes = calculate_sums_and_cubes(N)   # 이 함수에 집어넣는다.

print(sum_of_numbers)
print(square_of_sum)
print(sum_of_cubes)
# 세개의 결과를 모두 출력한다.


#########################################################################################################


def calculate_sums_and_cubes(N):    # 함수 정의, N에 입력 받는다.
    sum_of_numbers = sum(range(1, N+1))  # 1부터 N까지의 합
    square_of_sum = sum_of_numbers ** 2  # 1부터 N까지의 합의 제곱
    sum_of_cubes = sum(i**3 for i in range(1, N+1)) # 리스트 컴프리헨션(list comprehension)을 사용하지 않고, 
                                                    # 제너레이터(generator) 표현식을 사용하여 1부터 N까지 각 수의 세제곱을 계산하고, 그 결과들의 합을 계산한다
                                                    # i**3는 i의 세제곱을 의미함, for i in range(1, N+1)은 1부터 N까지 각 i에 대해 세제곱을 계산
                                                    # sum() 함수는 이 세제곱들의 합을 계산한다

    return sum_of_numbers, square_of_sum, sum_of_cubes # 위 세가지를 전부 계산하여 반환한다.

            
N = 100 # N 예시입력 100
sum_of_numbers, square_of_sum, sum_of_cubes = calculate_sums_and_cubes(N) # 이 함수에 세가지 값을 모두 집어넣는다.
print(sum_of_numbers)
print(square_of_sum)
print(sum_of_cubes)

# 세가지의 값을 모두 출력한다.