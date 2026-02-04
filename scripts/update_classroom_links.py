import os

# Mapping Landing Page -> Course Name -> Classroom File
link_map = {
    "intro_ethics.html": "classroom_ethics.html",
    "intro_basics.html": "classroom_basics.html",
    "intro_business.html": "classroom_business.html",
    "master_index.html": "classroom.html", # Keep original for master
    "expert_advanced.html": "classroom_advanced.html",
    "special_marketing.html": "classroom_marketing.html",
    "special_manufacturing.html": "classroom_manufacturing.html",
    "special_data.html": "classroom_data.html",
    "special_video.html": "classroom_video.html",
    "management_leadership.html": "classroom_leadership.html",
    "strategy_consultant.html": "classroom_consultant.html",
    "master_app_creator.html": "classroom_app_creator.html"
}

for filename, target_link in link_map.items():
    if not os.path.exists(filename):
        continue
        
    print(f"Linking {filename} -> {target_link}...")
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace window.location.href='dashboard.html' with specific link
    # Note: master_index.html had 'day01_lecture.html' from previous fix. We should change it to 'classroom.html' for consistency?
    # Actually user wanted separation. Let's point master_index to 'classroom.html' (which is the master class room).
    
    if filename == "master_index.html":
        # It might be day01_lecture.html or dashboard.html
        if "day01_lecture.html" in content:
             content = content.replace("day01_lecture.html", target_link)
        elif "dashboard.html" in content:
             content = content.replace("dashboard.html", target_link)
    else:
        # Others point to dashboard.html currently
        content = content.replace("dashboard.html", target_link)
        content = content.replace("classroom.html", target_link) # Just in case
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("All landing pages updated to point to specific classrooms.")
