import re

# Map titles (or distinctive substrings) to filenames and button colors for matching
link_map = [
    {
        "marker": "AI소개 및 윤리",
        "file": "intro_ethics.html",
        "color": "blue"
    },
    {
        "marker": "AI 기초 입문",
        "file": "intro_basics.html",
        "color": "blue"
    },
    {
        "marker": "AI 비즈니스 활용",
        "file": "intro_business.html",
        "color": "blue"
    },
    # Skip Master Class (already done)
    {
        "marker": "AI 전문가 심화",
        "file": "expert_advanced.html",
        "color": "orange"
    },
    {
        "marker": "AI 마케팅 전문가",
        "file": "special_marketing.html",
        "color": "pink"
    },
    {
        "marker": "AI 제조 전문가",
        "file": "special_manufacturing.html",
        "color": "gray"
    },
    {
        "marker": "AI 데이터 분석가",
        "file": "special_data.html",
        "color": "cyan"
    },
    {
        "marker": "AI 영상 크리에이터",
        "file": "special_video.html",
        "color": "red"
    },
    {
        "marker": "AI시대의 리더십",
        "file": "management_leadership.html",
        "color": "yellow"
    },
    {
        "marker": "AI 비즈니스 컨설턴트",
        "file": "strategy_consultant.html",
        "color": "emerald"
    },
    {
        "marker": "비즈니스 앱 크리에이터",
        "file": "master_app_creator.html",
        "color": "indigo"
    }
]

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Strategy: Split by course cards (roughly) or use simpler regex
# Since we know the structure:
# <!-- Title Comment --> ... <h3 ...>Title</h3> ... <button ...>...</button>
# We can find the button AFTER the Title.

for item in link_map:
    # 1. Find the position of the title
    title_match = re.search(re.escape(item['marker']), content)
    if not title_match:
        print(f"Warning: Could not find title '{item['marker']}'")
        continue
    
    start_pos = title_match.end()
    
    # 2. Find the next button tag after this title
    # Look for <button ... ref-color ...>
    # We use a non-greedy search for the next button
    button_pattern = r'<button\s+class="[^"]*bg-' + item['color'] + r'-[0-9]{3}[^"]*"\s*>\s*자세히 보기\s*</button>'
    
    match = re.search(button_pattern, content[start_pos:])
    
    if match:
        original_button = match.group(0)
        
        # Construct new link
        # Extract class from original button but add 'block text-center' and remove w-full if needed (w-full is usually there)
        class_match = re.search(r'class="([^"]*)"', original_button)
        if class_match:
            classes = class_match.group(1)
            # Ensure block and text-center are present for <a> tag to behave like a button
            if 'block' not in classes:
                classes = 'block text-center ' + classes
            
            new_link = f'<a href="{item["file"]}" class="{classes}">자세히 보기</a>'
            
            # Replace ONLY this instance
            # We need to calculate absolute position to replace correctly
            abs_start = start_pos + match.start()
            abs_end = start_pos + match.end()
            
            content = content[:abs_start] + new_link + content[abs_end:]
            print(f"Updated link for {item['marker']} -> {item['file']}")
        else:
            print(f"Could not extract classes for {item['marker']}")
    else:
        print(f"Warning: Could not find matching button for '{item['marker']}' with color {item['color']}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Index.html updated successfully.")
