goal = int(input())
steps = list(map(int, input().split()))

total_steps = sum(steps)
qualified_days = 0
best_streak = 0
current_streak = 0

for step in steps:
	if step >= goal:
		qualified_days += 1
		current_streak += 1
		best_streak = max(best_streak, current_streak)
	else:
		current_streak = 0

highest_steps = max(steps)
highest_days = [str(day + 1) for day in range(7) if steps[day] == highest_steps]

print(total_steps)
print(qualified_days)
print(" ".join(highest_days))
print(best_streak)

