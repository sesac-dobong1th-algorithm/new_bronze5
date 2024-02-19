import sys

total_money, num_entities = 1000, 100
money_per_entity, remaining_money = divmod(total_money, num_entities) # divmod : 내장함수
print(money_per_entity, remaining_money)
