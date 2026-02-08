import os
import re
import json

# Configuration
ROOT_DIR = os.getcwd() # c:\Users\Win\Desktop\Antigravity_Practice\AI Class
COURSES_FILE = os.path.join(ROOT_DIR, 'ai-lecture-room', 'data', 'courses.ts')
OUTPUT_FILE = os.path.join(ROOT_DIR, 'ai-lecture-room', 'data', 'searchIndex.ts')

def strip_html(content):
    # Remote script and style tags
    content = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', content, flags=re.DOTALL)
    # Remove HTML tags
    content = re.sub(r'<[^>]+>', ' ', content)
    # Decode HTML entities (basic ones)
    content = content.replace('&nbsp;', ' ').replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
    # Collapse whitespace
    content = re.sub(r'\s+', ' ', content).strip()
    return content

def parse_courses_ts():
    with open(COURSES_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    courses = []
    
    # Split content into course blocks roughly by IDs which look like "id: 'c0"
    # This matches "id: 'c01'", "id: 'c02'", etc.
    # We assume 'id:' is the start of a course object.
    
    # Find all start indices of "id: 'c"
    starts = [m.start() for m in re.finditer(r"id:\s*['\"]c\d+['\"]", content)]
    
    for i in range(len(starts)):
        start = starts[i]
        end = starts[i+1] if i+1 < len(starts) else len(content)
        block = content[start:end]
        
        # Extract metadata
        try:
            id_match = re.search(r"id:\s*['\"](.*?)['\"]", block)
            title_match = re.search(r"title:\s*['\"](.*?)['\"]", block)
            path_match = re.search(r"path:\s*['\"](.*?)['\"]", block)
            
            if not (id_match and title_match and path_match):
                continue
                
            course = {
                'id': id_match.group(1),
                'title': title_match.group(1),
                'path': path_match.group(1),
                'lectures': []
            }
            
            # Extract lectures
            # Check if it uses Array.from
            if 'Array.from' in block:
                # Dynamic generation. Scan directory.
                dir_path = os.path.join(ROOT_DIR, course['path'])
                if os.path.exists(dir_path):
                    files = sorted([f for f in os.listdir(dir_path) if f.endswith('.html')])
                    for f in files:
                        # Exclude container files if any (usually start with lecture_)
                        if f.startswith('lecture_'): continue 
                        
                        # Generate a title from filename if possible, or use filename
                        # Logic: textbook_basics_01_understanding -> Session 1...
                        # For now, just use filename or simple extraction
                        course['lectures'].append({'title': f, 'file': f})
            else:
                # Explicit list
                # Find all { title: ..., file: ... } objects
                # Regex to find title and file within this block
                l_matches = re.findall(r"title:\s*['\"](.*?)['\"],\s*file:\s*['\"](.*?)['\"]", block)
                for t, f in l_matches:
                    course['lectures'].append({'title': t, 'file': f})
            
            if course['lectures']:
                courses.append(course)
                
        except Exception as e:
            print(f"Error parsing block at {start}: {e}")

    return courses

def generate_index():
    courses = parse_courses_ts()
    search_index = []
    
    print(f"Found {len(courses)} courses.")
    
    for course in courses:
        print(f"Processing {course['title']}...")
        for lecture in course['lectures']:
            file_path = os.path.join(ROOT_DIR, course['path'], lecture['file'])
            
            if not os.path.exists(file_path):
                print(f"  [WARNING] File not found: {file_path}")
                continue
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                text_content = strip_html(content)
                # Limit content length to avoid massive file size? 
                # For now, keep it all, but maybe limit to 10k chars if it's crazy huge.
                
                item = {
                    'id': f"{course['id']}-{lecture['file']}",
                    'courseId': course['id'],
                    'courseTitle': course['title'],
                    'lectureTitle': lecture['title'],
                    'path': course['path'],
                    'file': lecture['file'],
                    'content': text_content
                }
                search_index.append(item)
            except Exception as e:
                print(f"  [ERROR] Reading {file_path}: {e}")

    # Write typescript file
    ts_content = "export interface SearchItem {\n"
    ts_content += "  id: string;\n"
    ts_content += "  courseId: string;\n"
    ts_content += "  courseTitle: string;\n"
    ts_content += "  lectureTitle: string;\n"
    ts_content += "  path: string;\n"
    ts_content += "  file: string;\n"
    ts_content += "  content: string;\n"
    ts_content += "}\n\n"
    
    ts_content += "export const SEARCH_INDEX: SearchItem[] = " + json.dumps(search_index, ensure_ascii=False, indent=2) + ";"
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(ts_content)
        
    print(f"Successfully generated search index with {len(search_index)} items at: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_index()
