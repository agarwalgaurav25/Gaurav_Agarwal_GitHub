print("Who is the President of India?")
print("A - Draupadi Murmu")
print("B - Ram Nath Kovind")
ans1 = str(input("ENter Your answer A or B "))
score = 0
if ans1 == "A":
    print("answer correct")
    score = score + 10
else:
    print("answer wrong")
    score = score - 10
print("Gaurav, your score is ", score)

