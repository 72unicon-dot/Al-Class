import os
import re

# List of files to update (all 12 courses + index.html if needed)
files = [
    "intro_ethics.html", "intro_basics.html", "intro_business.html",
    "master_index.html", "expert_advanced.html", 
    "special_marketing.html", "special_manufacturing.html", 
    "special_data.html", "special_video.html", 
    "management_leadership.html", "strategy_consultant.html", 
    "master_app_creator.html"
]

# Pattern to find the Enter Button logic
# In `update_registration.py`, we injected JS that sets `enterBtn.classList.remove('hidden')`.
# However, the HTML *element* usually has `onclick="window.location.href='classroom.html'"`.
# We need to find that HTML button and chang the URL.

# Search for: onclick="window.location.href='classroom.html'"
# Replace with: onclick="window.location.href='dashboard.html'"

for filename in files:
    if not os.path.exists(filename):
        continue
    
    print(f"Updating links in {filename}...")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple string replace is safer and sufficient here
    new_content = content.replace("window.location.href='classroom.html'", 
                                  "window.location.href='dashboard.html'")
    
    if content != new_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("  Updated 'Enter Classroom' link.")
    else:
        print("  No changes needed (or pattern not found).")
