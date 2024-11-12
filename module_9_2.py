first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(item) for item in first_strings if len(item) < 5]
print(first_result)

second_result = [(item_1, item_2) for item_1 in first_strings for item_2 in second_strings if len(item_1) == len(item_2)]
print(second_result)

third_result = {item: len(item) for item in first_strings + second_strings if not len(item) % 2}
print(third_result)