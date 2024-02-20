
total_money, num_entities = 1000, 100 
money_per_entity, remaining_money = divmod(total_money, num_entities) # divmod : 내장함수
print(money_per_entity, remaining_money) # 1000원을 100원씩 10명에게 나눠주고 0이 남음
# 출력 - 전체돈,남은돈