from pathlib import Path
import json

numbers = [2, 5, 8, 13.6]

dictionary = {'a': 123, 'b': 446}

#file = Path('numbers.json')
#contents = json.dumps(numbers)
#file.write_text(contents)

file = Path('dictionary.json')
contents = json.dumps(dictionary)
file.write_text(contents)

numbers = 123
dictionary = "ned"
print(numbers)
print(dictionary)

file = Path('numbers.json')
contents = file.read_text()
numbers = json.loads(contents)
print(numbers)
