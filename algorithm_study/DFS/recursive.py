# 재귀 함수 예제

def  recursive_function () :
    print ( ‘ 재귀 함수 호출 ’ )                                                       
    recursive_function()

recursive_function()

# 종료 조건을 준 재귀 함수 예제

def  recursive_function ( i ) :
    
    if  i  ==  20 :
        return
    print ( i, ‘번째 재귀 함수에서‘, i + 1 ‘ 번째 재귀 함수 호출 ’ ) 
    recursive_function( i + 1 )
    print ( i, ‘번째 재귀 함수 호출 종료＇ )

recursive_function(1)

# 재귀 함수 활용 - 유클리드 호제법

x , y = input().split()
x = int(x)
y = int(y)
def  gcd ( x, y ) :
    if x % y == 0 :
        return y
    else :
        return gcd ( y, x % y)
