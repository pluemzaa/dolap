log = int(input())
balls = int(input())
bag = int(input())

result = (log*balls)/bag

if result != int:
    result += 0.5
    result = int(result)
    print(result)
else:
    result = int(result)
    print(result)