# 딕셔너리

# 파이썬의 이터러블 객체 중 대표적인 매핑 객체로 key-value로 한 쌍인 item이라는 것을 원소로 갖는다
# (이터러블 객체를 모를 시  key-value로 한 쌍인 item이라는 것을 원소로 갖는다만 알아도 괜찮음)

# 0. 딕셔너리 특징 
# 0-1 key의 중복을 허용하지 않음, 대신 value의 중복은 허용
# 0-2 key : value의 형태로 원소를 저장
# 0-3 순서가 존재하지 않는 비시퀀스 객체(=인덱스가 존재하지 않는 객체)
# 0-4 key는 문자열,숫자를 사용 value는 어떤 객체든 가능(ex 리스트,문자열,튜플 등등)
# 0-5 웹 프로그램으로 자료를 주고 받을 때 쓰는 JSON 타입과 함께쓰기 좋음










# (!+!+ 매우 중요!+!+) 
# 밑의 예시의 key값은 어디까지나 이해를 위해 한글을 사용했을 뿐 
# 실제로 key값은 변수 네이밍과 마찬가지로 "영문"을 사용해야함








# 1. 딕셔너리의 탐색

# 1-1 in, not in을 이용한 key 탐지 방법(이터러블의 공통탐지법)
Dic = {'대책위원회':['타카나시 호시노','스나오오카미 시로코','이자요이 노노미','오쿠소라 아야네','쿠로미 세리카']}

print(f"Dic은 key로 \'대책위원회\'를 갖습니까? 답 : {'대책위원회' in Dic:}" )
print(f"Dic은 key로 \'흥신소86\'를 갖지 않습니까? 답: {'흥신소86' not in Dic:} ")




# 1-2 .get()를 이용한 value 탐지 방법(딕셔너리 고유의 탐지법)
# dict.get(key) == 해당 key의 value를 반환(해당 key가 존재하지 않을 시 None을 반환)

Dic = {'게헨나':'만마전','트리니티':'티파티','밀레니엄':'세미나','아비도스':'대책위원회',}
print(F"Dic의 value 중 \'밀레니엄\'의 value는 무엇니까? 답 : {Dic.get('밀레니엄'):}" )



# 1-3 .keys() 로 딕셔너리 객체 내 모든 key들을 확인하기(딕셔너리 고유의 탐지법)
# dict.keys() == 해당 딕셔너리 객체 내 모든 key들을 리스트 모습의 dictionary_keys 객체로 반환

Dic = {'츠카츠키 리오':'회장','하야세 유우카':'회계','우시오 노아':'서기','쿠로사키 코유키':'부원'}
print(f"{Dic.keys():}")
Dic_keys_list = [i for i in Dic.keys() ] # list comprehesion으로 dictionary keys를 리스트로 만들어 담을 수도 있음
print(f"{Dic_keys_list:}")




# 1-4 .values 로 딕셔너리 객체 내 모든 value들을 확인하기(딕셔너리 고유의 탐지법)
# dict.values() == 해당 딕셔너리 객체 내 모든 value들을 리스트 모습의 dictionary_values 객체로 반환

Dic = {'보컬':'쿄야마 카즈사','기타':'이바라기 요시미','드럼':'유토리 나츠','키보드':'쿠리무라 아이리'}
print(f"{Dic.values():}")
Dic_values_list = [i for i in Dic.values() ] # list comprehesion으로 dictionary values를 리스트로 만들어 담을 수도 있음
print(f"{Dic_values_list:}")



# 1-5 .items 로 딕셔너리 객체 내 모든 item들을 확인하기(딕셔너리 고유의 탐지법)
# dict.items() == 해당 딕셔너리 객체 내 모든 item들을 (key,value)를 원소로 갖는 리스트의 모습으로 dictionary_items 객체로 반환

Dic = {'사이바 모모이':15,'사이바 미도리':15 ,'하나오카 유즈':16,'텐도 아리스': None}
print(f"{Dic.items():}")
Dic_items_list = [i for i in Dic.items()] 
print(f"{Dic_items_list:}")









# 2. 딕셔너리에 원소 추가하기

# 2-1 .update 메서드로 추가하기
# dict.update(key = value or dictionary ) == 해당 딕셔너리 객체에 해당 key와 value를(dictionary) 추가

Dic ={'mainOS':'아로나',}
print(F"{Dic:}")
Dic.update( SubOS = '프라나') # or Dic1 = {'subOS':'프라나'}로 .update(Dic1)도 가능
print(F"{Dic:}")







 


# 3. 딕셔너리 내 원소 수정하기 

# 3-1 .update 메서드로 추가하기
# dict.update({key  :value}) == 해당 딕셔너리 객체에 이미 있는 key의 value를 ()안의 value로 수정

Dic = {'금일당번':'쿄야마 카즈사',}
print(F"{Dic:}")
Dic.update({'금일당번' : '키류 키쿄' }) 
print(F"{Dic:}")




# 4. 딕셔너리 내 원소(=key : value) 삭제하기
# dic.pop(key) == 해당 key를 가진 item(= key : value) 삭제

Dic = {'회장':'쿠치나시 유메','부회장': '타카나시 호시노',}
print(F"{Dic:}")
Dic.pop('회장')
print(F"{Dic:}")