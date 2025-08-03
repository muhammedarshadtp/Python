
# num=[1,2,3]  # This is an iterable

# it=iter(num) # Get an iterator object

# print(next(it))  # Output: 1
# print(next(it))  # Output: 2
# print(next(it))  # Output: 3
# # print(next(it))       # ❌ Raises StopIteration (no more items)


class CountDown:

    def __init__(self,start):
        self.num=start

    def __iter__(self):
        return self
    def __next__(self):
        if self.num <=0:
            raise StopIteration
        current=self.num
        self.num -= 1
        return current


d1=CountDown(4)

for i in d1:
    print(i)