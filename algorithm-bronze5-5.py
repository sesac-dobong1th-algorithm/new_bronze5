# 1
hongjuns_id = "appa" # 홍준의 아이디를 appa로 정의한다.
fan = ":fan:"  # 선풍기는 :fan: 으로 정한다.

print(f"{fan}{fan}{fan}")   # f-string 사용 / 첫째줄 선풍기3개
print(f"{fan}:{hongjuns_id}:{fan}")   # 둘째줄 선풍기1, 홍준아이디, 선풍기1
print(f"{fan}{fan}{fan}")   # 첫번째 줄과 동일





# 2
hongjuns_id = "h0ngjun7"    # 홍준의 아이디를 h0ngjun7로 정의한다.
fan = ":fan:"     # 선풍기는 :fan: 으로 지정한다.

# .format() 메소드를 사용하여 위와 같이 출력
print("{}{}{}".format(fan, fan, fan))
print("{}:{}:{}".format(fan, hongjuns_id, fan))
print("{}{}{}".format(fan, fan, fan))