numbers: list[int] = [1,2,3,4,5,6]
print(*list(map(lambda x: x + 5, numbers)))

numbers: list[int] = [1,2,3,4,5,6]
numbers2: list[int] = [3,9,1,2,3,4]
print(*list(map(lambda x, y: x*y, numbers, numbers2)))

lst: list[str] = ['connect', 'ctrl', 'save', 'go', 'live', 'spell']
print(*list(map(list, lst)))

def even(number: int) -> int:
    if number % 2 != 0:
        return number + 2
    return number + 10

numbers: list[int] = [1,2,3,4,5,6,7]
print(*list(map(even, numbers)))

numbers: list[int] = [1,2,3,4,5,6,7]
def square(number: int) -> int:
    return number ** 2
print(*list(map(square, numbers)))

lst: list[str] = ['connect', 'ctrl', 'save', 'go', 'live', 'spell']
print(*list(map(lambda x: len(x), lst)))

lst1: tuple[str] = ('apple', 'banana', 'cherry')
lst2: tuple[str] = ('orange', 'lemon', 'pineapple')
print(*list(map(lambda x, y: y+x+y, lst1, lst2)))

lst: list[str] = ['connect', 'ctrl', 'save', 'go', 'live', 'spell']
itr: str = "|"
print(*list(map(lambda x: itr+x+itr , lst)))
print(*list(map(lambda x: f"{itr}{x}{itr}" , lst)))

lst: list[str] = ['connect', 'ctrl', 'save', 'go', 'live', 'spell']
print(*list(map(ord, *list(map(list, lst)))))
