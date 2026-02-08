import os
from pathlib import Path
from bs4 import BeautifulSoup

def fix_links_in_file(file_path):
    content = file_path.read_text(encoding='utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    
    # Determine expected textbook filename
    # lecture_marketing_class01.html -> textbook_marketing_class01.html
    textbook_filename = file_path.name.replace('lecture_', 'textbook_')
    if textbook_filename == file_path.name: 
         textbook_filename = "textbook_" + file_path.name
         
    # Check if target textbook exists
    target_path = file_path.parent / textbook_filename
    if not target_path.exists():
        print(f"Skipping {file_path.name}: Target textbook {textbook_filename} not found.")
        return False

    updated = False
    # Find all 'a' tags
    for a in soup.find_all('a'):
        # Check if text contains "강의 보기" (handling nested tags like <i>)
        if "강의 보기" in a.get_text():
            current_href = a.get('href')
            if current_href == "#" or current_href is None:
                a['href'] = textbook_filename
                updated = True
                print(f"  Fixed link in {file_path.name} -> {textbook_filename}")

    if updated:
        file_path.write_text(str(soup), encoding='utf-8')
        return True
    return False

def main():
    base_dir = Path(r"c:\Users\Win\Desktop\Antigravity_Practice\AI Class")
    
    dirs = [
        "c01_basics", "c02_business", "c05_marketing", "c06_manufacturing", 
        "c07_data", "c08_video", "c09_leadership", "c10_consultant", "c11_app_creator",
        "c04_advanced"
    ]
    
    count = 0
    for d in dirs:
        dir_path = base_dir / d
        if not dir_path.exists(): continue
        
        files = list(dir_path.glob("lecture_*.html"))
        if not files: 
            files = list(dir_path.glob("*lecture*.html"))
            
        for f in files:
            if "textbook" in f.name: continue
            if fix_links_in_file(f):
                count += 1
                
    print(f"Total files updated: {count}")

if __name__ == "__main__":
    main()
