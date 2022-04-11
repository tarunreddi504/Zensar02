
l = [1, 2, 3, 4, 5]
print(f"list :{l}")
print(type(l))

print("-" * 40)
# print(dir(l))
itrObj = l.__iter__()
# print(dir(itrObj))                  # __iter__(), __next__() protocols of iteration
print(itrObj.__next__())            # print the elements from the list
print(itrObj.__next__())            # print the elements from the list
print(itrObj.__next__())            # print the elements from the list
print(itrObj.__next__())            # print the elements from the list
print(itrObj.__next__())            # print the elements from the list
# print(itrObj.__next__())            # StopIteration exception

print("-" * 40)
for i in l:
    print(i)
