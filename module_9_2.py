first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(s) for s in first_strings if len(s) >= 5]
second_result = [(i, j) for i in first_strings for j in second_strings if
                 len(i) == len(j)]
third_result = {s: len(s) for s in first_strings + second_strings if not
len(s) % 2}


print(first_result)
print(second_result)
print(third_result)