def createCounter():
    def f():
        x = 0
        while True:
            x += 1
            yield x
    it = f()
    def number():
        return next(it)
    return number
 
createA = createCounter()
print(createA(),createA(),createA())
