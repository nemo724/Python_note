# 집합

# 수학에서의 집합과 마찬가지로 중복을 허용하지 않고, 순서가 존재하지 않는 자료형
# 대부분 공학을 위해 사용하는 자료형

# 0. 집합의 특징
# 0-1 중복을 허용하지 않음 
# 0-2 순서가 존재하지 않는 비시퀀스객체임
# 0-3 대부분 원소 구성 탐지 및 파악을 위해 사용
# 0-4 {}를 사용시 key:value는 딕셔너리, value만 존재시 집합으로 선언됨
# 0-5 원소로 모든 자료형이 들어갈 수 있는 이터러블 객체임









# 1. 집합 탐지 

# 1-1 in, not in을 이용한 원소 탐지 방법(이터러블의 공통탐지법)

Set = {1,2,3,4,5}

print(f"Set 안에 3이 들어 있습니까? 답 : {3 in Set:}")
print(f"Set 안에 6이 들어 있습니까? 답 : {6 not in Set:}")


# 1-2 .union 메서드를 이용한 합집합 탐지(집합의 고유탐지법)
# set.union(집합 객체) == set과 ()안 집합 객체의 합집합을 보여줌 (=원소는 set v 집합객체가 True인 객체들)

Set = {1,2,3,4,5}
Set2 = {0,9,8,7,6}
print(F"Set 과 Set2의 합집합 : {Set.union(Set2):}")# 논리 연산자로는 {Set | Set2:}

# 1-3 .intersection 메서드를 이용한 교집합 탐지(집합의 고유탐지법)
# set.intersection(집합객체) == set과 ()안에 집합객체의 교집합을 보여줌 (=원소는 Set ^ 집합객체가 True인 객체들)

Set = {1,2,3,4}
Set2 = {3,4,5,6}
print(F"Set 과 Set2의 교집합 : {Set.intersection(Set2):}")# 논리 연산자로는 {Set & Set2:}

# 1-4 .difference 메서드를 이용한 차집합 탐지(집합의 고유 탐지법)
# set.difference(집합객체) == set과 ()안에 집합객체와 차집합인 원소를 보여줌 
# (원소는 set,집합객체에 속하고 ㄱset v ㄱ집합객체가 True인 객체들)

Set ={2,3,4,5}
Set2={3,4,5,6,7}
print(F"Set내 set2와 차집합인 원소 : {Set.difference(Set2):}")

# 1-5 .isdisjoint 메서드를 이용한 서로소 탐지(집합의 고유 탐지법)
# set.isdisjoint(집합객체) == set과 집합객체는 서로소인가?(=True: 교집합이 없음, Flase : 교집합이 존재)

Set = {1,3,5,7}
Set2 = {2,4,6,8}
print(f"Set과 Set2는 서로소집합입니까? 답:{Set.isdisjoint(Set2):}")

# 1-6 .issubset 메서드를 이용한 부분집합 탐지(집합의 고유 탐지법)
# set.issubset(집합객체) == set은 집합객체의 부분집합입니까?

Set = {1,2,3}
Set2 ={1,2,3,4}
print(f"Set은 Set2의 부분집합입니까? 답: {Set.issubset(Set2):}")

# 1-6 .issuperset 메서드를 이용한 모집합 탐지(집합의 고유 탐지법)
# set.issuperset(집합객체) == set은 집합객체의 모집합입니까?

Set = {9,8,7,6,5,4,3,2,1}
Set2 = {1,2,4,6}
print(f"Set은 Set2의 모집합입니까? 답: {Set.issuperset(Set2):}")











# 2 집합의 원소 추가 

# 2-1 .add 메서드를 이용한 원소 추가(집합 고유 추가법)
# set.add(추가할 원소) == 해당 set 객체 내에 ()안의 원소가 추가됨

Set = {1,2}
print(f"{Set:}")
Set.add(3)#집합 객체도 가능
print(f"{Set:}")



# 2-2 .update 메서드를 이용한 원소 추가
Set = {1,3,5,7}
print(f"{Set:}")
Set.update({9,11,13})
print(f"{Set:}")










# 3. 집합의 원소 삭제

# 3-1 .discard 메서드를 이용한 원소 삭제

Set = {1,2,3,4,5,6,7,102}
print(f"{Set:}")
Set.discard(102)
print(f"{Set:}")

#.remove는 지우려는 원소가 없으면 오류를 일으키지만 .discards는 오류를 발생시키지 않음



# 3-2 .clear 메서드를 이용한 모든 원소 삭제
Set.clear()
print(f"{Set:}")
