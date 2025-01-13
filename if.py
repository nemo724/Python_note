# if문 

# 모든 프로그래밍 언어의 공통적인 3요소인 자료형, 조건문, 반복문 중 if는 조건문에 해당하는 개념임
# 조건문은 기본적으로 참, 거짓 이란 Boolean이라는 자료형이 갖는 값에 따라 특정 명령어를 실행 or 중단 시킬 수 있음

# 0. if의 특징
# 0-1 Python에서는 정수 0은 False(=거짓) 1은 True(=참)이라는 값을 가짐
# 0-2 Python에서는 if : 후 개행 후 꼭 반드시 4칸씩 들여쓰기를 한 후 명령문을 작성해야 함  















# 1. if의 실행

# 1-1 참일때만 실행 시키기
# if 조건문 :
    # (해당 조건문이 참일 경우 실행시킬 명령문)


student1 = {'name':'스나오오카미 시로코','age':16,} 

print("student1은 16살이 맞나요?")
# 해당 질문의 명제는 student1의 key 중 하나인 age의 value값은 16과 같나?
# 명제란 답으로 참 or 거짓을 가질 수 있는 문장  

if student1.get('age') == 16: # ==은 등위 연산자 (= 두 값이 같은지를 참과 거짓으로 판단할 수 있는 연산자)
    print("네, 그 학생은 16살이 맞습니다") # 참일 경우




# 1-2 참이 아닌 경우 특정 명령문을 실행 시키기(= 거짓일 때 실행시키기)
# else :
    # (if문의 조건이 거짓이 될 경우 실행시킬 명령문)

student2 = { 'name' : '타카나시 호시노', 'age' : 17,}

print("student2의 이름이 스나오오카미 시로코입니까?")
# 해당 질문의 명제는 student2의 key 중 하나인 name의 value값은 '스나오오카미 시로코'와 같나?

if student2.get('name') == '스나오오카미 시로코':# student2.get('name') 반환값과 '스나오오카미 시로코'가 같은 경우(=참)
    print("네, 스나오오카미 시로코가 맞습니다") # 해당 명령문을 실행

else : # 그러나 student2.get('name') 반환값이 '스나오오카미 시로코'가 아닌 경우(=거짓)
    print(f"아니요, 그 학생의 이름은 {student2.get('name'):}입니다") # 해당 명령문을 실행















# 2. 관계 연산자

# 2-1 초과 미만을 나타내는 <,>
student3 = {'name':"하야세 유우카", 'height': 156}
student4 = {'name': '우시오 노아','height': 161}

print("student3가 student 4보다 작습니까?")


if student3.get('height')<student4.get('height'):# 156 < 161이 맞습니까?(답 : 참)
    print(f"답 :{student3.get('height')< student4.get('height'):}")

student5 = {'name':"사이바 모모이", 'height': 143}
student6 = {'name':"사이바 미도리", 'height': 143}

print("student5가 student 6보다 작습니까?")

if student5.get('height')<student6.get('height'):# 143 < 143이 맞습니까?(답 : 거짓) 
    print(f"답 : {student5.get('height')<student6.get('height'):}") # 조건식이 거짓으로 실행되지 않음

# <와 >는 오로지 두 값의 비교를 크거나 작거나로만 보기에 
# 두 값이 같은 경우는 무조건 거짓으로 판단




# 2-2 이상, 이하를 나타내는 >=,<=
student7 = {'name':'텐도 아리스', 'height':152}
student8 = {'name':'하나오카 유즈', 'height':150}

print('student7의 키는 150이상입니까?')

if student7.get('height')>= 150:# 152 >= 150 (답 : 참)
    print("네 150 이상입니다")

print('student8의 키는 150이상입니까?')# 150 >= 150 (답 : 참)

if student8.get('height')>= 150:
    print("네 150 이상입니다")

# 이상과 이하는 두 값의 크거나 작거나 외에 같은지도 보기에 <,>보다 더 유연하게 쓸 수 있음




# 2-3 같음과 같지 않음을 나타내는 ==, !=
student9 = {'name':'키류 키쿄','species':'고양이'}
student10 = {'name':'쿄야마 카즈사', 'species':'고양이'}

print('student9 과 student10은 같은 종족인 학생입니까?')

if student9.get('species') == student10.get('species'):
    print("네 해당 두 학생은 같은 종족입니다")

print('student9 과 student10은 그럼 이름은 다릅니까?')

if student9.get('name') != student10.get('name'):
    print(f"네 두 학생은 각각 {student9.get('name'):},{student10.get('name'):} 로 이름이 다릅니다")

# ==은 두 값이 같을때만 참, !=은 두 값이 다를때만 참












# 3. 다중 if문
# Q. 만일 if의 조건문의 참은 아니지만 else의 문장을 실행시키는 것이 아닌 특정 다른 명령문을 실행시켜야 할 때 어떻게 해야 하는가?
# A. 다른 조건식을 추가하여 해당 조건식이 참일 때 실행시키게 한다

# 3-1 elif를 이용한 조건문
# C에서는 else if문이라 작성 하지만 Python은 이를 축약하여 elif라 작성
# elif 조건식 :
#     (해당 elif의 조건문이 참일 때 실행시키고 싶은 명령문)

student1.update(school='아비도스')

print("student1는 어느 학교입니까?")

if student1.get('school') == '게헨나': # 아비도스 == 게헨나는 거짓이기에 실행되지 않음
    print(f'{student1.get('name'):}은 게헨나의 학생입니다')

elif student1.get('school') == '아비도스': # elif의 아비도스 == 아비도스는 참이기에 해당 elif의 조건문이 실행됨 
    print(f'{student1.get('name'):}은 아비도스의 학생입니다')

else : # 위의 elif가 참으로 실행되었기에 해당 조건문은 실행되지 않음음
    print('해당 학생의 학교는 등록되어 있지 않습니다')

# 다중 if문들은 if -> elif -> else 순서대로 내려가며 조건식을 계산하기에 해당 순서를 지키며 다중 if문을 작성해야함
# 내려가면서 참인 조건문이 있으면 해당 조건문만 실행 하여 그 뒤의 elif문들, else문은 무시함















# 4. 중첩 if문 
# Q. 특정 조건문에서 참인 것들 중에서 그 안에서도 어떠한 기준에 따라 참, 거짓 또는 특정 값으로 나누고 싶을 때는 어떻게 해야 하는가?
# A. if문 안에  또 다른 if문을 넣어 참, 거짓, 특정 기준을 조건식으로 분류하게 만든다

import random as r
Students =\
[ {'name': '소라사키 히나','age':17,'school':'게헨나'},
  {'name':'류우게 키사키','age':17,'school':'산해경'},
  {'name': '이오치 마리','age': 15,'school':'트리니티'},
  {'name' : '쿠다 이즈나','age':15,'school':'백귀야행'},
]

num = r.randrange(0,3)
if Students[num].get('age') == 17: # 학생의 나이가 17살인 경우
    if Students[num].get('school') == '게헨나':# 학생의 나이가 17살이고 학교가 게헨나인 경우
        print(f"{Students[num].get('name'):} 은(는) 게헨나 3학년입니다")

    elif Students[num].get('school') == '산해경':# 학생의 나이가 17살이고 학교가 산해경인 경우
        print(f"{Students[num].get('name'):} 은(는) 산해경 3학년입니다")

elif Students[num].get('age') == 15: # 학생의 나이가 15살인 경우
    if Students[num].get('school') == '트리니티': # 학생의 나이가 15살이고 학교가 트리니티인 경우
        print(f"{Students[num].get('name'):} 은(는) 트리니티 1학년입니다")

    elif Students[num].get('school') == '백귀야행': # 학생의 나이가 15살이고 학교가 백귀야행인 경우
        print(f"{Students[num].get('name'):} 은(는) 백귀야행 1학년입니다")

# 이렇게 다중 if문을 쓰면 같은 값을 가지는 경우여도 
# 특정 조건을 더 걸어 분리할 수 있기에 특정 명령문을 실행하거나 or 특정 값을 갖게 할 수도도 있다