

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

def count_80_up(students):
    count=0
    for student in students:
        if student['평균'] >= 80:
            count+=1
    return count

def ins_student(students):
    new_student = add_info()
    students.append(new_student)

def del_student(students, student_id):
    for student in students:
        if student['학번'] == student_id:
            students.remove(student)
            print(f"학생 {student['이름']}의 정보 삭제")

students = []
for i in range(5):
  students.append(add_info())


sort(students)
show(students)
print("80점 이상인 학생 수: ", count_80_up(students))

while True:
    print("\n1. 학생 정보 추가")
    print("2. 학생 정보 삭제")
    print("3. 개인 정보 출력")
    print("4. 전체 정보 출력")
    print("다른 숫자: 종료")
    choice = int(input("원하는 작업을 선택하세요: "))

    if choice == 1:
        ins_student(students)
    elif choice == 2:
        student_id = int(input("삭제할 학생의 학번을 입력하세요: "))
        del_student(students, student_id)
    elif choice == 3:
        sort(students)
        search_key = input("학번 또는 이름을 입력하세요: ")
        found = False
        for student in students:
            if str(student['학번']) == search_key or student['이름'] == search_key:
                print("학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
                print("===================================================================")
                print(f"{student['학번']}\t{student['이름']}\t{student['영어']}\t{student['C언어']}\t{student['파이썬']}\t{student['총점']}\t{student['평균']:.2f}\t{student['학점']}\t{student['등수']}")
                found = True
        if not found:
            print(f"학번 또는 이름 '{search_key}'에 해당하는 학생 정보가 없습니다.")
    elif choice == 4:
        sort(students)
        show(students)
        print("80점 이상인 학생 수: ", count_80_up(students))
    else:
        print("프로그램을 종료합니다.")
        break