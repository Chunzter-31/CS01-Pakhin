keep = int(input("กรุณาใส่คะแนนเก็บ :"))
mid = int(input("กรุณาใส่คะแนนกลางภาค :"))
final = int(input("กรุณาใส่คะแนนปลายภาค :"))
score = keep+mid+final
if score >= 80:
  grade = "A"
elif score >= 75:
  grade = "B+"
elif score >= 70:
  grade = "B"
elif score >= 65:
  grade = "C+"
elif score >= 60:
  grade = "C"
elif score >= 55:
  grade = "D+"
elif score >= 50:
  grade = "D"
else :
  grade = "F"
if score > 100 :
  print("คะแนนไม่ถูกต้อง")
if score <= 100 :
  print("เกรดของคุณคือ :", grade)
