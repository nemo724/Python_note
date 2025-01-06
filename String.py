#문자열 

#기존 C는 char형의 배열 or const * char와 char * 형으로 선언하여 연속되는 메모리공간을 이용하지만 파이썬은 문자열 객체로 해결
string= "Hello World"
print(f"변수 : {string:}, 상수 : {"Hello World":}")

#문자열의 재미있는 연산
print("Hello"+"World")#+는 두 문자열 객체를 하나로 합치는 연산 
print(f"{"참 "*3:}") #*는 해당 문자열 객체를 n개 만큼 생성하는 연산

#문자열 쪼개기 
string="Hello World".split(' ')#()안에 원하는 분리 기준으로 문자열을 쪼개어 리스트형으로 반환
print(f"{string:}")



#1. 문자열 탐지

#1-1 in, not in을 이용한 탐지 방법(이터러블의 공통탐지법)

#(찾는 문자 or 문자열) in sequence(=문자열 객체 or 변수) == str객체 안에 찾고 있는 문자가 있나요? 
#(=찾는 문자 or 문자열) not in sequence(=문자열 객체 or 변수) == str객체 안에 찾고 있는 문자가 없없나요? 

string="apple"
print(f"string 안에는 a가 있나요? 답:{'a'in string:}" )
#True==네 들어 있습니다, False==아니요 들어있지 않습니다

print(f"string 안에는 k가 있나요? 답:{'k' not in string:}" )
#True==네 들어있지 않습니다, False==아니요 들어있습니다


# 1-2 .index를 이용힌 탐지 방법(이터러블의 공통탐지법)

#sequence(=문자열 객체 or 변수).index(찾는 문자 ) ==찾고 있는 문자는 해당 객체에서 몇번쨰 인덱스입니까?

string="pineapple"
print(f"string의 'a'의 인덱스의 값은 뭡니까? 답: {string.index('a'):}")



#1-3 .count를 이용한 탐지 방법(이터러블의 공통탐지법)

#sequence(=문자열 객체 or 변수).count(찾는 문자 ) ==찾고 있는 문자는 해당 객체에서 몇개가 있습니까?
string="pineapple"
print(f"string의 'p'는 총 몇개 입니까? 답: {string.count('p'):}")



# 1-4 .endswith() 메서드를 이용한 탐지 방법

#문자열 객체 or 변수.endswith(  str(=문자열 객체 or 변수)  ) == 해당 문자열 객체가 str의 내용으로 끝나나요?

string="apple"
print(f"string 끝에는 e가 있나요? 답:{string.endswith('e'):}" )
#True==네 그걸로 끝납니다, False==아니요 그걸로 끝나지 않습니다









# 2. 문자열 수정하기

#2-1 .replace() 메서드를 이용한 수정법

#sequence.replace('바뀔 곳이 될 문자열 or 문자','바꾸고 싶은 내용')

string=string.replace('pine','')
print(f"{string:}")

#2-2 .capitalize 메서드

#sequence.capitalize()==해당 문자열의 맨 앞 글자를 대문자로 변경

string="cake"
print(f"{string.capitalize():}")



