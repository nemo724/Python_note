#리스트 

#C에서의 리스트는 사용할 자료형인 변수 + 자신의 뒤 원소가 위치한 메모리주소를 담은 포인터 변수를 
#멤버로 가지는 구조체로 직접 구현하였지만 파이썬은 리스트 객체로 이를 구현함

# 0. 리스트의 특징
# 0-1 리스트 또한 시퀀스 객체로 슬라이싱 + 언패킹 가능 (시퀀스객체란 해당 객체 내 원소들이 순서를 갖는 객체를 의미)
# 0-2 가변적인 크기를 갖는 자료형 + 원소로 시퀀스 객체를 가짐
# 0-3 중복 원소를 허용 + 순서가 존재
# 0-4 가변객체로 수정이 가능한 자료형













# 1. 리스트 탐지 방법

# 1-1 in, not in을 이용한 탐지 방법(이터러블의 공통탐지법)
List =[1,2,3,4,5]

print(F"List 안에 5가 들어 있나요? 답:{5 in List:}")
print(F"List 안에 7가 들어 있지 않나요? 답:{7 not in List:}")

# 1-2 .index()를 이용한 탐지 방법(이터러블의 공통탐지법)

List = [i for i in "Hello World"]#언팩킹과 함수 없이 리스트를 생성하는 list comprehension 
print(F"List 내에서 \'W\'는 몇 번 입니까? 답 : {List.index('W'):}")

# 1-3 .count를 이용한 탐지 방법(이터러블의 공통탐지법)

List = [i for i in "Goodbye World"] 
print(f"List 내에서 \'o\'는 총 몇개를 사용하였습니까? 답 : {List.count('o'):}")






# 2. 리스트에 원소 추가하기

# 2-1 .append 메서드를 이용한 원소추가 (리스트의 매서드)
# list.append(추가를 원하는 객체) == 가장 마지막 인덱스의 원소로 추가함

List = [i for i in "상냥함의 " ]
print(f"{List:}")
List.append('기억')
print(f"{List:}")

# 2-2 .insert 메서드를 이용한 원소추가 (리스트의 메서드)
# list.insert(위치하기 원하는 인덱스, 추가를 원하는 객체) == 원하는 곳에 원하는 value를 추가한 리스트 객체가 됨

List = [i for i in "Aoharu" ]
print(F"{List:}",end =" ") ; print(f"List가 바라 보고 있는 객체의 주소: {id(List):}")
List.insert(0,"RE")
print(f"{List:}",end =" ") ; print(f"List가 바라 보고 있는 객체의 주소: {id(List):}")

#2-3 .extend 메서드를 이용한 원소추가 (리스트의 메서드)
#리스트객체.extend(이어 붙이고 싶은 리스트 객체) == 기존 리스트 객체를 다른 리스트 객체를 이어붙인 객체로 만듬 

List = [i for i in "irdori"] ; List2 =[i for i in "canvas"]
print(F"{List:} {List2:}") ; print(id(List))
List.extend(List2)
print(f"{List:}") ; print(id(List))





# 3. 리스트 원소 삭제

# 3-1 .remove 메서드를 이용한 삭제(리스트의 메서드)
#list.remove(삭제하고 싶은 value )

List = [i for i in "Thanks   to"]
print(F"{List:}")
List.remove(' '); List.remove(List[-3])
print(F"{List:}")

# 3-2 .pop() 메서드로 이용한 삭제(이터러블의 공통메서드)
# seq.pop() == 후입선출 방식으로 원소를 제거

List = [i for i in range(1,5,1)]
print(F"{List:}")
List.pop()
print(F"{List:}")










# 4. 리스트 정렬
# 순서가 존재하는 리스트는 C에서는 직접 정렬 알고리즘으로 정렬함수를 구현해야 했지만
# 파이썬은 정렬함수를 기본제공

import random as r
List =[r.randrange(1,11) for i in range(1,10)]
print(f"{List:}")

# 4-1 .sort() 메서드를 이용(리스트의 메서드)

#list.sort(reverse = 허용 or 거부) == 내림차순을 허용,거부에 따라 올림,내림차순으로 원소를 정리(디폴트는 올림차순) 

List.sort(reverse=False)#내림차순 거부(=올림차순 정렬)
print(f"{List:}")

List.sort(reverse=True)#내림차순 허용(=내림차순 정렬)
print(f"{List:}")


#sorted()는 .sort와 달리 정렬된 상태의 리스트 객체를 반환(새 객체를 생성하기 위해서 사용)



# 4-2 .reverse() 메서드를 이용(리스트의 메서드)
#list.reverse() == 현재상태를 역으로 변경(=[::-1]로 만듬)
List = [i for i in "그 꿈이 남기고 간 흔적들"]
List.reverse()
print(f"{List:}")

#reversed()는 순서가 존재하는 시퀀스객체를 이터러블 객체로 반환하기에 
#할당 받을 변수 = reversed(시퀀스객체) 후 
# 변수를 순서가 존재하는 시퀀스 객체로 변환해야함



