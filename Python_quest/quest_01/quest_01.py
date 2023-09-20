# Quest 01. 회문인지 아닌지 확인하는 프로그램

# 조건: 단어(string)를 입력받을 수 있게 한다. 자료형에 대한 이해가 부족하다면? 검색 혹은 노드 확인!!  
# 입력된 단어를 뒤집어서 출력할 수 있게 한다. 입력된 단어가 회문이 맞는지 확인하여 출력할 수 있게 한다.  
# 자료형, 제어문, 함수를 활용한다.  


####### 답안 #######


# 사용자로부터 문자열을 받음
txt = input("input: ")

# a라는 변수에 사용자로부터 입력받은 문자열을 거꾸로 해서 저장함
a = txt[::-1]

# a(거꾸로 저장된 사용자가 입력한 문자열)를 출력
print("뒤집힌 단어는", str(a), "입니다.")

# 사용자가 입력한 문자열과 그 문자열의 거꾸로 저장된 문자열이 같은 지 비교
if txt == a:
    # 사용자가 입력한 문자열과 그 문자열의 거꾸로 저장된 문자열이 같으면 "회문입니다" 출력
    print("회문입니다")
else:
    # 사용자가 입력한 문자열과 그 문자열의 거꾸로 저장된 문자열이 다르면 "회문이 아닙니다" 출력
    print("회문이 아닙니다")


####### 회고 #######


# 배운 점 - 함수를 활용해서 문제를 풀이하는 방식을 새롭게 알 수 있었습니다.

# 아쉬운 점 - 파이썬 신텍스 작성이 익숙하지 않아서 답을 도출하기 위한 코드를 디자인하는 것이 어려웠습니다.

# 느낀 점 - 그루 분들과 문제에 대해 의논하고 답을 찾기 위해 노력하는 과정이 즐겁고 유익했습니다.
