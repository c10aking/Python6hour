# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
#
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'갯수 + "!"로 구성

url = input()
# 규칙1
t1_str = url[7:]
print(t1_str)
# 규칙2
dot_index = t1_str.index('.')
t1_str = t1_str[:dot_index]
# 규칙3
pwd = t1_str[:3]+ str(len(t1_str)) + str(t1_str.count('e')) + '!'
print(pwd)