# 1. function return
def p_plus (a,b):
    print (a + b)

def r_plus (a,b):
    return a + b

p_result = p_plus(2 , 3)
r_result = r_plus(2 , 3)

print(p_result, r_result)

def k_print(a,b):
    return a + b
    print("it isn't shown")



# it gives us back None,5
# because When p_plus ran, it automatically printed to the console value of "a + b". 
# However, the value stored in the function "p_plus" is None because that function had no return statement.
# When r_plus ran, it did not print anything to the console. 
# However, it did return a value, and that value was stored in r_plus. (CodeAcademy)

r_k_print = k_print(4,2)
print(r_k_print)

# k_print 안에 있는 print statement는 실행되지 않는다 왜냐면 return이 실행되고 난뒤에 함수가 종료되므로. 여기서 알 수 있는건 print statement 는 return으로 인해 저장된
# value 값을 우리에게 보여줄때 사용된다는 것이다.

k_print(4,2) # 따라서 이렇게 입력하면 나오는게 없음. print statement 가 없고 return 으로 인해 함수가 종료되므로.

# 2. function argument.

def say_Hello(name, age, country, fav_food):
    return f"Hello {name} you are {age} years old and you are from {country} and you like {fav_food}"

re = say_Hello(name = "young", country = "korea", fav_food = "pizza", age = "23")

print(re)

# argument 를 대입하려면 쌍따옴표 앞에 f 를 붙이고 argument를 중괄호로 감싸면 됨.
# 그리고 parameter 를 대입할때 순서가 헷갈릴 수 있으니 argument = parameter 라고 하면 순서 상관없이 argument를 입력할 수 있음.

# 3.  conditional part one

def plus (a,b):
    if type(a) is int or type(a) is float or type(b) is int or type(b) is flaot :
        return a + b
    else:
        return None

re = plus(5.4,1.2)
print(re)

# if 문안에 조건을 여러개 이어 붙일 수도 있다. 문법은 영어로 말할 때랑 매우 비슷해서 알아듣기 쉽다.

# 4. 웹사이트에서 html 코드 가져오기

import requests # requests 함수는 따로 다운받아야한다.
from bs4 import BeautifulSoup

result = requests.get('https://www.indeed.com/jobs?q=Python&l=Silicon+Valley%2C+CA')

print(result.text) # 이렇게 하면 위의 링크된 웹사이트에 있는 모든 html 코드를 가져오게 된다.



