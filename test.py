import os
import re

folder_path = 'saves'

# Pattern: matches files like 'save#1', 'save#23', etc.
pattern = re.compile(r'^save#(\d+)$')

save_files = []
for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        match = pattern.match(filename)
        if match:
            save_files.append((int(match.group(1)), filename))  # (number, filename)

# Sort by save number
save_files.sort()

# Print all matching save files
for number, name in save_files:
    print(f"Found save file: {name} (number {number})")
    