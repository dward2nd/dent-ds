credit1 = int(input())
grade1 = float(input())

credit2 = int(input())
grade2 = float(input())

credit3 = int(input())
grade3 = float(input())

sum_score = credit1 * grade1 + credit2 * grade2 + credit3 * grade3
sum_weight = credit1 + credit2 + credit3

gpa = sum_score / sum_weight
print("%.2f" % gpa)
# or
# print("{:.2f}".format(gpa))
# or
# print(f"{gpa:.2f}")
