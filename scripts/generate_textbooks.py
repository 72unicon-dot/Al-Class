import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

# Template for the textbook page
TEMPLATE = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>강의 교재 - {course_name}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        body {{ font-family: 'Pretendard', sans-serif; line-height: 1.7; }}
        .textbook-content h3 {{ font-size: 1.25rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.75rem; color: #1e293b; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem; }}
        .textbook-content p {{ margin-bottom: 1rem; color: #475569; }}
        .textbook-content ul {{ list-style-type: disc; padding-left: 1.5rem; margin-bottom: 1.5rem; color: #475569; }}
    </style>
</head>
<body class="bg-slate-50 min-h-screen">
    <div class="max-w-4xl mx-auto px-6 py-12">
        <div class="flex justify-between items-center mb-8">
            <a href="{back_link}" class="inline-flex items-center gap-2 text-slate-500 hover:text-slate-800 transition-colors">
                <i class="fas fa-arrow-left"></i> 강의로 돌아가기
            </a>
            <div class="flex gap-2">
                 <button onclick="window.print()" class="text-slate-400 hover:text-slate-600">
                    <i class="fas fa-print"></i>
                </button>
            </div>
        </div>

        <div class="bg-white rounded-2xl shadow-xl overflow-hidden border border-slate-100">
            <div class="bg-gradient-to-r from-indigo-600 to-indigo-800 text-white p-10 md:p-14">
                <span class="inline-block px-3 py-1 bg-white/20 rounded-full text-xs font-bold mb-4 backdrop-blur-sm tracking-wider">LECTURE NOTE</span>
                <h1 class="text-3xl md:text-4xl font-extrabold mb-2">{title}</h1>
                <p class="text-white/80 text-lg font-light">{subtitle}</p>
            </div>

            <div class="p-10 md:p-14 textbook-content">
                {content_body}
            </div>
    
            <div class="mt-12 pt-8 border-t border-slate-100 flex justify-center">
                <a href="{back_link}" class="px-6 py-3 bg-indigo-600 text-white rounded-xl font-bold hover:bg-indigo-700 transition">
                    강의 목록 보기
                </a>
            </div>
        </div>
    </div>
</body>
</html>"""

def generate_content_body(sessions):
    html = ""
    for i, session in enumerate(sessions, 1):
        html += f"<h3>{i}. {session['title']}</h3>\n"
        html += f"<p>{session['desc']}</p>\n"
        if session['details']:
            html += "<ul>\n"
            for detail in session['details']:
                html += f"<li>{detail}</li>\n"
            html += "</ul>\n"
    return html

def process_file(file_path):
    print(f"Processing {file_path}...")
    content = file_path.read_text(encoding='utf-8')
    soup = BeautifulSoup(content, 'html.parser')

    # Extract Course Info
    course_name = soup.title.string.split('-')[0].strip() if soup.title else "AI 강의"
    
    header = soup.find('header')
    if not header: return
    
    class_num_tag = header.find('span', class_='text-6xl')
    class_num = class_num_tag.text.strip() if class_num_tag else ""
    
    title_tag = header.find('h1')
    title = title_tag.text.strip() if title_tag else "강의 제목"
    
    subtitle_tag = header.find('p', class_='text-xl')
    subtitle = subtitle_tag.text.strip() if subtitle_tag else ""

    # Extract Sessions
    sessions = []
    # Sessions are usually in <div class="bg-white ..."> inside <main>
    # We look for h3 (title) and p (desc) and ul (details)
    
    # Specific logic for session cards
    session_cards = soup.find_all('div', class_=lambda x: x and 'bg-white' in x and 'rounded-2xl' in x and 'border' in x) # Approximate selector
    # Fallback if specific classes change, but based on view_file this is consistent
    
    if not session_cards:
        # Try finding group divs (Business/Basics uses slightly different structure than others)
         session_cards = soup.select('main div.bg-white')

    for card in session_cards:
        h3 = card.find('h3')
        if not h3: continue
        
        # Check if this card has "강의 보기" link
        links = card.find_all('a')
        has_view_link = any("강의 보기" in a.text for a in links)
        if not has_view_link: continue

        desc_p = h3.find_next_sibling('p')
        desc = desc_p.text.strip() if desc_p else ""
        
        details = []
        ul = card.find('ul')
        if ul:
            details = [li.text.strip() for li in ul.find_all('li')]
            
        sessions.append({
            'title': h3.text.strip(),
            'desc': desc,
            'details': details
        })

    if not sessions:
        print(f"  No sessions found in {file_path.name}")
        return

    # Generate Textbook Filename
    # lecture_marketing_class01.html -> textbook_marketing_class01.html
    new_filename = file_path.name.replace('lecture_', 'textbook_')
    if new_filename == file_path.name: # e.g. day01_lecture.html
         new_filename = "textbook_" + file_path.name

    textbook_path = file_path.parent / new_filename
    
    # Generate Content
    content_body = generate_content_body(sessions)
    new_html = TEMPLATE.format(
        course_name=course_name,
        back_link=file_path.name,
        title=title,
        subtitle=subtitle,
        content_body=content_body
    )
    
    textbook_path.write_text(new_html, encoding='utf-8')
    print(f"  Created {textbook_path.name}")
    
    # Update Links in original file
    # We replace href="#" where text contains "강의 보기"
    # Note: If there are multiple sessions, we might want to link all to the same textbook page for now,
    # OR if the user wanted granular pages, but plan said "One Textbook File per Class".
    # So we simply replace all href="#" for "강의 보기" buttons with the new filename.
    
    # Regex replacement to avoid parsing/serializing HTML which might mess up formatting
    # Looking for <a href="#" ... > ... 강의 보기 ... </a>
    # This is tricky with regex. Let's iterate manually or use soup but be careful.
    # Simple text replacement might be safer if the pattern is consistent.
    
    new_file_content = content
    # Pattern: href="#" ... 강의 보기
    # We find specific generic placeholders
    
    # Helper to replace link
    def replace_link(match):
        return match.group(0).replace('href="#"', f'href="{new_filename}"')

    # Regex for the anchor tag containing "강의 보기" and href="#"
    # flexible for attributes order
    # <a[^>]*href="#"[^>]*>.*?강의 보기.*?</a>
    # But we only want to replace the href part.
    
    # Strategy: Find the lines with "강의 보기" and href="#", replace href="#" with href="filename"
    lines = new_file_content.splitlines()
    updated_lines = []
    for line in lines:
        if "강의 보기" in line and 'href="#"' in line:
            line = line.replace('href="#"', f'href="{new_filename}"')
        updated_lines.append(line)
        
    file_path.write_text("\n".join(updated_lines), encoding='utf-8')
    print(f"  Updated links in {file_path.name}")


def main():
    base_dir = Path(r"c:\Users\Win\Desktop\Antigravity_Practice\AI Class")
    
    # List of directories to process
    dirs = [
        "c01_basics", "c02_business", "c05_marketing", "c06_manufacturing", 
        "c07_data", "c08_video", "c09_leadership", "c10_consultant", "c11_app_creator",
        "c04_advanced"
    ]
    
    # Exclude Ethics and Master Class as requested
    
    for d in dirs:
        dir_path = base_dir / d
        if not dir_path.exists(): continue
        
        print(f"Scanning {d}...")
        files = list(dir_path.glob("lecture_*.html"))
        if not files: 
            # Trying alternate naming e.g. day01_lecture.html if any
            files = list(dir_path.glob("*lecture*.html"))
            
        for f in files:
            if "textbook" in f.name: continue
            process_file(f)

if __name__ == "__main__":
    main()
