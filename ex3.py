from ex2 import logger

@logger('example.log')
def flat_generator(list_of_lists):
    for item in list_of_lists:
        for i in item:
            yield i

for item in flat_generator([
 ['a', 'b', 'c'],
 ['d', 'e', 'f', 'h', False],
[1, 2, None]
 ]):
    print(item)