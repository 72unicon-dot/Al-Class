import os
import re

root_dir = r"c:\Users\Win\Desktop\Antigravity_Practice\AI Class"
courses_file = os.path.join(root_dir, "ai-lecture-room", "data", "courses.ts")

# Mapping course ID to directory
course_map = {
    "c04": "c04_advanced",
    "c05": "c05_marketing",
    "c06": "c06_manufacturing",
    "c07": "c07_data",
    "c08": "c08_video",
    "c10": "c10_consultant",
    "c11": "c11_app_creator"
}

# Regex to find titles in HTML based on the specific Tailwind class used
# <h2 class="text-xl md:text-2xl font-bold mb-2 pl-2 md:pl-0 relative">Title</h2>
title_pattern = re.compile(r'class="text-xl md:text-2xl font-bold mb-2 pl-2 md:pl-0 relative">\s*([^<]+)\s*</h2>', re.IGNORECASE)

def extract_lectures(course_dir):
    lectures = []
    dir_path = os.path.join(root_dir, course_dir)
    if not os.path.exists(dir_path):
        print(f"Directory not found: {dir_path}")
        return []

    # Find the main classroom file
    classroom_file = None
    for f in os.listdir(dir_path):
        if f.startswith("classroom_") and f.endswith(".html"):
            classroom_file = os.path.join(dir_path, f)
            break
    
    if not classroom_file:
        print(f"Classroom file not found in {dir_path}")
        return []

    with open(classroom_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    matches = title_pattern.findall(content)
    
    # matches will be a list of strings like "Class 1: ...", OR "Title Name"
    # We assume they are in order 1..N
    
    # Extract suffix from directory name? c05_marketing -> marketing
    suffix = course_dir.split("_")[1]
    if course_dir == "c11_app_creator": suffix = "app_creator"
    if course_dir == "c03_master_class": suffix = "master_class" 
    
    for i, title in enumerate(matches):
        clean_title = title.strip()
        class_num = i + 1
        num_str = f"{class_num:02d}"
        
        # If title doesn't start with Class, prepend it
        if not re.match(r"^Class\s*\d+", clean_title, re.IGNORECASE):
            clean_title = f"Class {class_num}: {clean_title}"
            
        filename = f"textbook_{suffix}_class{num_str}.html"
        lectures.append({"title": clean_title, "file": filename})
        
    return lectures

def generate_ts_block(lectures):
    lines = ["        lectures: ["]
    for l in lectures:
        lines.append(f"            {{ title: '{l['title']}', file: '{l['file']}' }},")
    lines.append("        ]")
    return "\n".join(lines)

# Read courses.ts
with open(courses_file, "r", encoding="utf-8") as f:
    ts_content = f.read()

# Update loop
for cid, cdir in course_map.items():
    print(f"Processing {cid} ({cdir})...")
    lectures = extract_lectures(cdir)
    if not lectures:
        print(f"  No lectures found for {cid}")
        continue
        
    print(f"  Found {len(lectures)} lectures.")
    new_block = generate_ts_block(lectures)
    
    # Find the block for this course
    start_marker = f"id: '{cid}'"
    start_idx = ts_content.find(start_marker)
    if start_idx == -1:
        print(f"  Could not find {cid} in courses.ts")
        continue
        
    # Find "lectures:"
    lectures_idx = ts_content.find("lectures:", start_idx)
    
    # Check if it matches Array.from pattern OR already updated list
    # We want to replace whatever is there until the next object closure
    
    # Identify the end of the current 'lectures' value.
    # It can be `Array.from(...))` OR `[` ... `]`
    
    # Look at the next few characters
    next_chars = ts_content[lectures_idx+9:lectures_idx+50].strip()
    
    replace_start = lectures_idx
    replace_end = -1
    
    if next_chars.startswith("Array.from"):
        # Find closing ))
        end_match = re.search(r"\)\)\s*", ts_content[lectures_idx:])
        if end_match:
            replace_end = lectures_idx + end_match.end()
    elif next_chars.startswith("["):
        # Find closing ]
        # Simplistic approach: find matching bracket? 
        # Or just find the `]` indented correctly?
        # Since we generated it with indentation, let's look for `        ]`
        end_match = ts_content.find("        ]", lectures_idx)
        if end_match != -1:
            replace_end = end_match + 9 # length of "        ]"
    
    if replace_end == -1:
        # Fallback: Find the "}," that closes the course object
        # The course object property list usually ends with lectures.
        # But lectures is the last property. So we can look for `    },` at the start of a line?
        end_match = ts_content.find("\n    },", lectures_idx)
        if end_match != -1:
             replace_end = end_match # Don't include the closing brace
        else:
             print("  Could not determine end of `lectures` block.")
             continue

    # Apply replacement
    # print(f"Replacing from {replace_start} to {replace_end}")
    ts_content = ts_content[:replace_start] + new_block + ts_content[replace_end:]

# Write back
with open(courses_file, "w", encoding="utf-8") as f:
    f.write(ts_content)
    
print("courses.ts updated.")
