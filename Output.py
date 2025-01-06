#파이썬의 출력 방식

# 1. %를 이용한 출력방식

# 1-1 %d(정수의 출력 방식)
i=3
print("변수 i = %d, 상수 %d" %(i,3))

# 1-2 %f(실수의 출력방식)
from math import pi
print("pi = %.2f, 원주율 = %.2f" %(pi,3.141592))

# 1-3 %s(문자열의 출력 방식)
s="Hello World"
print("%s" %(s))
print("%s" %('Goodbye World'))

# 1-4 %에서의 고급출력 기술
# % (3.출력방향: + 오른쪽, - 왼쪽) (1.출력에 사용할 칸) (2.절삭범위) 형식지정자
print("%20.3s" %("Hello World"))
print("%20d" %(1000000))
#디폴트는 -로 왼쪽부터 출력 그러나 출력에 칸을 사용시 +설정으로 바뀌어 오른쪽부터 출력 



#2. .format

#2-1 정수의 출력
i=5
print("변수 i = {0:}, 상수 = {1:}".format(i,5))

#2-2 실수의 출력
print("pi = {0:.2f}, 원주율 ={1:.2f}".format(pi,3.141592))

#2-3 문자열의 출력
h="Hello World"
print("{0:} and {1:}".format(h, "Goodbye World"))



#3 f-string

#3-1 정수의 출력
i = 7
print(F"변수 i = {i:}, 상수 = {7:}")

#3-2 실수의 출력
print(F"pi = {pi:.2f}, 원주율 = {3.141592:.2f}")

#3-3 문자열의 출력
h="Hello World"
print(F"{h:} and {"Goodbye World":}")


#2,3-4 고급출력
#{변수 or 인덱스 : (4.공백을 채울 기호) (1.출력방향 : <,>,^) (2.출력에 사용할 칸) (3.절삭범위) 형식지정자 }
print('{0:0<10.3f}'.format(pi))
print(f"{pi:0<10.3f}")





#출력에 사용하는 옵션 

#seperator 옵션
#출력에서 복수의 문자열 객체끼리의 공백 발생 시 해당 공백을 지정한 문자로 바꿔 구분함
print(f"{"Hello":}",f"{"World":}","",sep='!')

#end 옵션
#복수의 print() 사용시 자동 개행처리되는 것을 개행대신 지정문자로 바꿔 줄바꿈 없이 출력
print(f"{"Hello":}",end=' ')
print(f"{"World":}") 