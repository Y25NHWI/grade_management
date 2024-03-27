
def add_info():
  stn = int(input("학번: "))
  name = input("이름: ")
  eng = int(input("영어 점수: "))
  c = int(input("C언어 점수: "))
  py = int(input("파이썬 점수: "))
  total, avg = cal_sumavg(eng, c, py)
  grade = cal_grade(avg)

  return {'학번': stn, '이름': name, '영어': eng, 'C언어': c, '파이썬': py, '총점': total, '평균': avg, '학점': grade}

def cal_sumavg(a, b, c):
  sum = a + b + c
  avg = sum / 3
  return sum, avg

def cal_grade(avg):
  if avg >= 90:
      return "A"
  elif avg >= 80:
      return "B"
  elif avg >= 70:
      return "C"
  elif avg >= 60:
      return "D"
  else:
      return "F"

def sort(students):
  students.sort(key=lambda x: x['총점'], reverse=True)
  for i, student in enumerate(students, start=1):
      student['등수'] = i

def show(students):
  print("\t\t\t성적관리 프로그램")
  print("===================================================================")
  print("학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
  print("===================================================================")
  for student in students:
      print((f"{student['학번']}\t{student['이름']}\t{student['영어']}\t{student['C언어']}\t{student['파이썬']}\t{student['총점']}\t{student['평균']:.2f}\t{student['학점']}\t{student['등수']}"))


students = []
for i in range(5):
  students.append(add_info())

sort(students)
show(students)
