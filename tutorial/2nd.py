import numpy

a = numpy.arange(20)
b = a.reshape((4, 5))
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
arr = numpy.array(lst)

print(a)
print(b)

print(arr[0:2, 0:2])
print(arr[1:, 1:])

'''
NOTE 파이썬의 slice 관련 내용
튜플이란 특이한 개념이 존재한다.
(y x) 형식이며 x 혹은 y가 숫자면 그거에 맞는 값을 불러온다.

일단 `:` 형식이면 0 ~ 끝 값까지의 값을 갖고 온다.
다음으로 `n1:n2` 형식이면 n1 ~ n2 - 1까지의 값을 갖고 온다.
다음으로 `n1:` 형식이면  n1 ~ 끝 값까지의 값을 갖고 온다.
마지막으로 `:n2` 형식이면 0 ~ n2 - 1까지의 값을 갖고 온다.
'''
