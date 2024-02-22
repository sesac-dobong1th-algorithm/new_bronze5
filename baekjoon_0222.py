n, a, b= map(int, input().split())
if a>b:
    print("Subway")
elif a<b:
    print("Bus")
elif a==b:
    print("Anything")