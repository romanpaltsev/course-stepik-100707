subscribers = list(map(int, input().split()))
subscribers = sorted(subscribers, reverse=True)
print(*subscribers)