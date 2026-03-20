try:
	clever_students = 0
	fallen = 0
	for i in range(5):
		score = float(input(f"How many points did student {i+1} get? "))
		if score >= 90:
			clever_students += 1
		elif score < 90:
			fallen += 1
	print(f"{clever_students} student/s have/has managed to pass the exam with a high point")

	print(f"{fallen} student/s have/has passed the exam with a low point")
except ValueError:
	print("please enter only numbers")