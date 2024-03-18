# # 리스트 []
# # 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30
#
# subway = [10, 20, 30]
# print(subway)
#
# subway = ["유재석", "조세호", "박명수"]
# print(subway)
# # 조세호씨가 몇번째 칸에 타고 있는가
# print(subway.index("유재석")) # 위치 찾기
#
# # 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("노홍철")
# print(subway)
#
# # 정형돈씨를 유재석/ 조세호 사이에 태워봄
# subway.insert(1, "정형돈") # 맨 뒤에 추가가 아닌 중간에 끼워넣기
# print(subway)
#
# # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)
#
# # 같은 이름의 사람이 몇명있는지 확인
# subway.append("유재석")
# print(subway.count("유재석"))

# # 정렬도 가능
# num_list = [3,2,9,4,6,7]
# num_list.sort()
# print(num_list)
#
# # 순서 뒤집기
# num_list.reverse()
# print(num_list)
#
# # 모두 지우기
# num_list.clear()
# print(num_list)

# # 다양한 자료형 함께 사용
# mix_list = ["유재석", 20, False]
# num_list = [3, 6, 7, 8, 9]
# print(mix_list)
#
# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)

# dictionary
cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet)
# print(cabinet[100])
#
# print(cabinet.get(3))
# print(cabinet[5]) # 값이 없으면 에러를 출력 후 종료
# print(cabinet.get(5)) # 값이 없으면 None 출력 후 진행
# print(cabinet.get(5, "사용 가능"))
# print("hi")

print(3 in cabinet) # 있으면 true 없으면 false

cabinet = {"A-3":"유재석", "B-100":"김태호"} # 문자열도 가능
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-30"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"] # 키 삭제
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear() # 요소값들 모두 삭제
print(cabinet)

# 튜플

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") 튜플이라 값 추가, 변경, 삭제, 수정 불가
# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)