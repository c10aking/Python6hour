sentence = '나는 소년입니다'
print(sentence)
sentence2 = '파이썬은 쉬워요'
print(sentence2)
sentence3 = """
나는 소년이고, 
파이썬은 쉬워요
"""
print(sentence3)
##########################################
# 문자열 슬라이싱
jumin = "990120-1234567"

print("성별 : " +jumin[7])
print("연 : " + jumin[0:2]) # 0부터 2 직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[0:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:14]) #뒤를 비우면 끝까지 출력함
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:])

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # 대문자여부 체크
print(len(python)) # 길이 반환
print(python.replace("Python","Java"))

index = python.index("A")# 특정 문자 위치 찾기
print(index)
index = python.index("n", index + 1) # 시작지점을 index위치 + 1로 지정
print(index)

print(python.find("Java")) # 찾고자하는 단어가 없을 경우 -1로 출력하고 계속 진행
print(python.index("Java")) # 에러 출력
print(python.count("n")) # 등장 횟수 카운팅

