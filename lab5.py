def repeat(n):
    def my_decorator(genuine_function):
        def my_fake(arg):
            result=arg
            for i in range(n):
                result=genuine_function(result)
            return result
        return my_fake
    return my_decorator
            

@repeat(2)
def plus_1(x):
    return x+1

@repeat(0)
def mul_2(x):
    return x*2

print(plus_1(3))
print(mul_2(4))
