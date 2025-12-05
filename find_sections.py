
file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Sections found:")
for i, line in enumerate(lines):
    if '<section' in line:
        print(f"Line {i+1}: {line.strip()}")
