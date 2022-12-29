def binary_search(array, n, left, right):
    middle = (left + right) // 2

    if left > right:
        return f"Индекс числа меньше введенного: {middle}.\nИндекс числа больше введенного: {middle + 1}."
    if n < seq[0]:
        return f"Числа меньше введенного нет.\nИндекс числа больше введеного или равного ему: {seq.index(min(seq))}."
    if middle + 1 > seq.index(max(seq)):
        return f"Числа больше введенного нет.\nИндекс числа меньше введеного или равного ему: {len(seq)-1}."

    if array[middle] == n:
        if middle - 1 < 0:
            return f"Числа меньше введенного нет.\nИндекс числа, равного введенному: {middle}."
        else:
            return f"Индекс числа меньше введенного: {middle - 1}.\nИндекс числа, равного введенному: {middle}."
    elif n < array[middle]:
        return binary_search(array, n, left, middle - 1)
    else:
        return binary_search(array, n, middle + 1, right)


seq = input("Введите последовательность чисел через пробел: ")
seq_ = seq.replace(" ", "")

while seq_.isdigit() is not True:
    print("Введены недопустимые символы.\nИспользуйте только цифры и пробел.")
    seq = input("Введите последовательность чисел через пробел: ")
    seq_ = seq.replace(" ", "")

num = int(input("Введите любое число: "))

seq = list(map(int, seq.split()))
seq.sort()
print(seq)

index = binary_search(seq, num, 0, len(seq)-1)
print(index)