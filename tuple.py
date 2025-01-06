#튜플

#대표적인 불변객체로 수정이 불가능한 읽기 전용 시퀀스객체이다

# 0. 튜플의 특징
# 0-1 불변객체로 수정(=추가,삭제)가 불가능하여 변경되면 안되는 값들을 담아두는 객체다다
# 0-2 순서가 존재
# 0-3 ()에서 ,로 구분되기에 꼭 한 개 일 때는 원소 뒤에는 ,를 찍어준다











# 1. 튜플 탐지방법

# 1-1 in, not in을 사용한 탐지 방법(이터러블의 공통탐지법)
tup = (1,2,3,4,5,)
print(F"tup 안에 5가 들어 있나요? 답:{5 in tup:}")
print(F"tup 안에 7가 들어 있지 않나요? 답:{7 not in tup:}")



# 1-2 .index를 이용한 탐지 방법(이터러블의 공통탐지법)
tup = tuple(i for i in "Hello World")#언팩킹과 함수 없이 튜플을 생성하는 tuple comprehension 
print(F"tup 내에서 \'W\'는 몇 번 입니까? 답 : {tup.index('W'):}")

# 1-3 .count를 이용한 탐지 방법(이터러블의 공통탐지법)
tup = tuple(i for i in " 전력절대 come*true ")
print(f"tup 내에서 \' \'는 몇 개가 있습니까? 답 : {tup.count(' '):}")


# + Q:저는 튜플을 수정하고 싶은데요?
# A:원래 그런거 하는 자료형이 아닌데 해야한다면 리스트 생성자 함수로 변환하시고 수정 후 다시 튜플로 만드세요

tup=list(tup)
print(f"{tup:}")
del tup[0],tup[-1] #del은 인덱스로 지우는 예약어



tup=tuple(tup)
print(f"{tup:}")
