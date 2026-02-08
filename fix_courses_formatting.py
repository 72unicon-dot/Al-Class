import re
import os

root_dir = r"c:\Users\Win\Desktop\Antigravity_Practice\AI Class"
courses_file = os.path.join(root_dir, "ai-lecture-room", "data", "courses.ts")

with open(courses_file, "r", encoding="utf-8") as f:
    content = f.read()

# The error is "Unterminated string literal" caused by newlines in the title string.
# Example: 
# { title: 'Class 7: Function 
#                                 Calling &
#                                 Tools', file: ... }
#
# We need to find these patterns and join them into a single line.
# Regex: search for `'[^']*'` but handling newlines? Python re defaults don't match newline with . 
# Actually, the file has actual newline characters inside the quotes.
# We can use a regex that matches the line structure: `{ title: '...', file: '...' }`
# but the title part spans multiple lines.

# Strategy:
# Read line by line? No, better to use regex on full content.
# Match: `title:\s*'([^']*)'` where the group can contain newlines.
# Then replace newlines and multiple spaces within that group.

def fix_title(match):
    full_str = match.group(0) # title: '...'
    inner_str = match.group(1) # content inside quotes
    
    # Replace newlines and excessive whitespace with single space
    clean_inner = re.sub(r'\s+', ' ', inner_str).strip()
    
    return f"title: '{clean_inner}'"

# Pattern: `title:\s*'((?:[^']|\n)*)'`
# Note: This might be dangerous if there are escaped quotes, but simple titles shouldn't have them.
pattern = re.compile(r"title:\s*'([^']*)'", re.DOTALL)

new_content = pattern.sub(fix_title, content)

with open(courses_file, "w", encoding="utf-8") as f:
    f.write(new_content)
    
print("Fixed courses.ts formatting.")
