needed_experience_amount = float(input())
count_of_battles = int(input())
sum_of_experience = 0
sum_of_third_battle = 0
every_battle = 0
for battles in range(1, count_of_battles + 1):
    every_battle += 1
    experience_earned_by_bottle = float(input())

    if battles % 3 == 0:
        experience_earned_by_bottle += (experience_earned_by_bottle * 15 / 100)

    if battles % 5 == 0:
        experience_earned_by_bottle -= (experience_earned_by_bottle * 10 / 100)

    if battles % 15 == 0:
        experience_earned_by_bottle += (experience_earned_by_bottle * 5 / 100)

    sum_of_experience += experience_earned_by_bottle

    if sum_of_experience >= needed_experience_amount:
        break

if sum_of_experience >= needed_experience_amount:
    print(f"Player successfully collected his needed experience for {every_battle} battles.")
else:
    difference = abs(needed_experience_amount - sum_of_experience)
    print(f"Player was not able to collect the needed experience, {difference:.2f} more needed.")
