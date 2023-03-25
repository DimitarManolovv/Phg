skorost=float(input())
if skorost <= 10:
	print("slow")
elif 10 <= skorost <= 50:
	print("average")
elif 50 <= skorost <= 150:
	print("fast")
elif 150 <= skorost <= 1000:
	print("ultra fast")
else:
	print("extremely fast")