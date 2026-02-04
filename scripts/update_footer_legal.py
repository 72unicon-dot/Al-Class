import os
import re

files_to_update = [
    "index.html", "dashboard.html",
    "intro_ethics.html", "intro_basics.html", "intro_business.html",
    "master_index.html", "expert_advanced.html", 
    "special_marketing.html", "special_manufacturing.html", 
    "special_data.html", "special_video.html", 
    "management_leadership.html", "strategy_consultant.html", 
    "master_app_creator.html"
]

# HTML to insert
legal_links = """
            <div class="flex justify-center gap-6 mb-4 text-xs opacity-70">
                <a href="terms.html" class="hover:underline">이용약관</a>
                <span class="opacity-50">|</span>
                <a href="privacy.html" class="hover:underline">개인정보처리방침</a>
            </div>
"""

# Pattern: Insert BEFORE the copyright line
# <p class="text-sm opacity-60">© 2026 ...</p>

for filename in files_to_update:
    if not os.path.exists(filename):
        continue
    
    print(f"Updating footer in {filename}...")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already updated
    if "terms.html" in content:
        print("  Already has legal links.")
        continue
        
    # Find copyright line
    # Matches: <p class="text-sm opacity-60">© ...
    # We want to insert legal_links BEFORE this paragraph.
    
    pattern = r'(<p class="text-sm opacity-60">© 2026)'
    
    if re.search(pattern, content):
        content = re.sub(pattern, legal_links + r'\1', content)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print("  Updated footer.")
    else:
        print("  Could not find copyright line pattern.")
