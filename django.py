# 1. multiple argument
## 1-1 positional argument

def plus (*args):
    result = 0
    for number in args:
        result += number
    print(result)

plus(1,2,3,4,5,1,1,1)


## 1-2 keyword argument

def kplus(**kwargs):
    
    print(kwargs)

kplus(a = 1, b = 2 ,c = 3)

# 둘다 무한대로 인자를 대입할 수 있다.

# 2. class

class Car1(): 
    wheels = 4
    windows = 4
    handle = 2
    color = "Red"
    def start(self):
        print(self.wheels)
        print("I started")
# car class 안에 있는 기능,정의를 property 라고 한다
# 안에 있는 함수를 method 라고 한다.
# 여기 argument self 는 default argument이다. 그냥 빈칸이라고 생각해도 무방하다.

porche = Car1() 
#porche 를 instance라고 하고 이 과정을 instantiation이라고 한다.


porche.owner = "Yeong" 
# 새로운 property를 추가할 수 도 있다.

mini = Car1()
# instance를 바꿀 수도 있다.

mini.start()
# 이때 start method는 default 로 mini class를 함수로 가진다.


# 3. property 재정의

class car2():

    def __init__(self, **kwargs):
        self.wheels = 4
        self.windows = 4
        self.handle = 2
        self.color = kwargs.get("color", "black") # default key, value 를 정함
        self.price = kwargs.get("price", "$20") # 마찬가지
    
    def __str__(self):
        return f"Car with {self.wheels} wheels"

# 이미 갖고있는 built-in method가 있다. print(Dir(car2))를 하면 나온다 
# 그중에 __str__(원래는 변수 porche를 스트링으로 바꾸어 print에 넣었을때 해석 가능하게 한다) , __init__ 이 있다. 
# 이건 call하지 않아도 python이 자동적으로 invoke 한다.

porche = car2(color = "green", price = "$60") # property 를 새로 지정했다
print(porche.color, porche.price)
# 터미널을 보면 init, str이 자동으로 실행되는걸 알 수 있다.

mini = car2()
print(mini.color,mini.price)
# property를 새로 지정하지 않았기 때문에 default property가 출력될 것이다.

# 4. inherit(extend), replace, super

class convertible(car2):
    def take_off(self):
        return "taking off"

    def __str__(self):
        return "Car with no roof"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time = kwargs.get("time", 10)

porche = convertible(color = "green", price = "$80")

print(porche.color, porche.time)
# coursera에서도 배운 기능이다. car2를 convertible class의 인자로 쓰면 car2안에 있는 모든 기능이 convertible로 옮겨가고 convertible 안에 있는 기능도 사용가능해진다.
# 말그대로 car2 class를 확장시킨것이다. (take_off 함수추가됨) 그리고 str 함수는 교체되었다. 
# 또한 car2 에 있던 init 함수를 super 함수를 이용하여 그대로 불러온다. method 또한 확장시킬수있다. 
# init함수에 time property를 추가하면된다. 위에 처럼.