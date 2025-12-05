
import os

file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# We are looking for:
# </section>
# <h2 ... Tournament Schedule

for i in range(len(lines) - 1):
    line = lines[i]
    next_line = lines[i+1]
    
    if '</section>' in line and 'Tournament Schedule' in next_line:
        print(f"Found the spot at line {i+1}")
        # Insert the missing tags
        # <section id="schedule" class="py-16 bg-gray-50">
        #     <div class="container mx-auto px-6">
        
        insert_lines = [
            '        <section id="schedule" class="py-16 bg-gray-50">\n',
            '            <div class="container mx-auto px-6">\n'
        ]
        
        # We need to insert these AFTER line i (the </section>)
        # So at index i+1
        
        new_lines = lines[:i+1] + insert_lines + lines[i+1:]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print("Fixed Schedule section.")
        break
else:
    print("Could not find the pattern.")
