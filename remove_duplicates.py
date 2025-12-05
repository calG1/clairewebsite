
file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# We want to keep lines 0 to 918 (index 0 to 918)
# And lines 1113 to end (index 1113 to end)
# Note: line numbers are 1-based, indices are 0-based.
# Line 919 is index 918.
# Line 1114 is index 1113.

# So we want lines[:918] + lines[1113:]

start_delete_index = 918 # Line 919
end_delete_index = 1113 # Line 1114 (start of next section)

# Verify the lines we are keeping/deleting
print(f"Last kept line (918): {lines[start_delete_index-1].strip()}")
print(f"First deleted line (919): {lines[start_delete_index].strip()}")
print(f"Last deleted line (1113): {lines[end_delete_index-1].strip()}")
print(f"First kept line (1114): {lines[end_delete_index].strip()}")

new_lines = lines[:start_delete_index] + lines[end_delete_index:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Successfully removed duplicate sections.")
