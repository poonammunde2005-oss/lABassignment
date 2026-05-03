n=int(input())
marks= list(map(int, input().split()))
if any(mark <40 for mark in marks):
    print("Fail")
else:
    aggregate_percentage = sum(marks)/n
    print(f"Aggregate Percentage: {aggregate_percentage:.2f}")
    if aggregate_percentage > 75:
        print("Grade: Distinction")
    elif aggregate_percentage >=60:
        print("Grade: First Division")
    elif aggregate_percentage >=50:
        print("Grade: Second Division")
    elif aggregate_percentage >=40:
        print("Grade: Third Division")