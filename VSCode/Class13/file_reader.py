from pathlib import Path

path = Path('data.txt')
contents = path.read_text()
print(type(contents))
print(contents)

lines = contents.splitlines()
line_num = 1
for line in lines:
    print(f'{line_num:03d}: {line}')
    line_num += 1

out_file = Path('output.txt')
out_file.write_text("here's my output")
                