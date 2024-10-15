minutes = []
days = int(input('Days to calculate > '))

[minutes.append(int(input('Enter daily minute value > '))) for _ in range(days)]
mean = sum(minutes) / len(minutes)

print(f"Your average screentime is {mean:.0f} minutes")
