
import os
import re
import glob

# Configuration
ROOT_DIR = r"d:\AI Class"
COURSE_FOLDERS_PATTERN = "c*_*"
INTRO_FILE_PATTERN = "intro_*.html"

def update_course_header(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # Fallback for weird encodings if any
        try:
            with open(file_path, 'r', encoding='cp949') as f:
                content = f.read()
        except:
             print(f"Error reading {file_path}")
             return False

    # 1. Extract Course Name
    # Look for <h1 class="...">Course Name</h1> inside header
    # Pattern: <h1[^>]*>\s*(.*?)\s*</h1>
    # But usually it is the first h1.
    
    h1_match = re.search(r'<h1[^>]*>\s*(.*?)\s*</h1>', content, re.DOTALL)
    if not h1_match:
        print(f"Skipping {file_path}: No H1 found")
        return False
    
    course_name_raw = h1_match.group(1).strip()
    # Remove any tags inside h1 if any (like spans)
    course_name = re.sub(r'<[^>]+>', '', course_name_raw).strip()
    # Normalize spaces
    course_name = ' '.join(course_name.split())
    
    # 2. Count Tool Cards
    tool_count = content.count('class="tool-card')
    # If 0, maybe "tool-card " or similar
    if tool_count == 0:
        tool_count = content.count("tool-card")

    if tool_count == 0:
        print(f"Warning: No tools found in {file_path}")
        # Default or skip? Let's use 0 or keep original? 
        # User said "Course Name and # Tools", so "Course Name과 0대 AI 도구" might be correct but weird.
        # Let's assume there are tools if this page exists.
    
    # 3. Construct Replacement
    # Target: 8일간 마스터할 <span ...> 10대 AI 도구</span>
    # Regex to find this block.
    # It spans lines.
    
    pattern = r'(8일간 마스터할)\s*<span([^>]*)>\s*10대 AI\s*도구</span>'
    
    replacement = f'{course_name}과 <span\\2>{tool_count}대 AI 도구</span>'
    
    # Check if pattern exists
    if not re.search(pattern, content, re.DOTALL):
        print(f"Skipping {file_path}: Target string '8일간 마스터할...' not found")
        return False
        
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # 4. Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Updated {file_path}: '{course_name}' with {tool_count} tools")
    return True

def main():
    # Recursively find all HTML files in d:\AI Class\c*_*
    search_path = os.path.join(ROOT_DIR, COURSE_FOLDERS_PATTERN, "**/*.html")
    files = glob.glob(search_path, recursive=True)
    
    print(f"Found {len(files)} HTML files to scan.")
    
    count = 0
    for file_path in files:
        if update_course_header(file_path):
            count += 1
            
    print(f"Successfully updated {count} files.")

if __name__ == "__main__":
    main()
