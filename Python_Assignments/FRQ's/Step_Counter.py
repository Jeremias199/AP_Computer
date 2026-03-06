
Week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
steps = [0, 0, 0, 0, 0, 0, 0]
for i in range(len(Week)):
        User_Steps = int(input(f"How many steps did you take {Week[i]}: "))
        steps[i] += User_Steps

def evaluate_steps(step_list):
        total = 0
        for t in range(len(steps)):
                total += steps[t]

        Average = total/7

        if total >= 10000:
                return "Your goal is met! Your average is " + str(Average) + " per day."

        else:
                return "Keep on going! Your average is " + str(Average) + " per day."

print(evaluate_steps(steps))








