import os
import re

root_dir = r"c:\Users\Win\Desktop\Antigravity_Practice\AI Class"
directories = [
    "c04_advanced", "c05_marketing", "c06_manufacturing", 
    "c07_data", "c08_video", "c10_consultant", "c11_app_creator", "c12_ethics"
]

pattern = re.compile(r"\(Day\s*(\d+)\s*(오전|오후)\)")

for d in directories:
    dir_path = os.path.join(root_dir, d)
    if not os.path.exists(dir_path):
        continue
        
    for filename in os.listdir(dir_path):
        if filename.startswith("classroom_") and filename.endswith(".html"):
            filepath = os.path.join(dir_path, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                matches = pattern.findall(content)
                if matches:
                    print(f"File: {d}/{filename}")
                    for m in matches:
                        print(f"  Found: Day {m[0]} {m[1]}")
