import os
import re

root_dir = r"c:\Users\Win\Desktop\Antigravity_Practice\AI Class"
directories = [
    "c04_advanced", "c05_marketing", "c06_manufacturing", 
    "c07_data", "c08_video", "c10_consultant", "c11_app_creator", "c12_ethics"
]

def replace_title(match):
    day = int(match.group(1))
    time = match.group(2)
    
    if time == "오전":
        class_num = (day * 2) - 1
    elif time == "오후":
        class_num = day * 2
    else:
        return match.group(0) # Should not happen based on regex
        
    return f"Class {class_num}"

# Pattern matches: (Day 1 오전) or (Day 1 오후)
# We strictly look for exactly this format as seen in the HTML files.
# Example in file: "Class 1: ... (Day 1 오전)" -> "Class 1: ... (Class 1)" <- wait, that looks redundant.
# The user asked: "상세 거리귤럼에서 오전: 오후:을 Class1,2로 변경해 주고 강의실의 과목과 비교하여 매칭되도록 수정해줘"
# Checking file content:
# <h2 ...>Class 1: AI 마케팅 개요 및 트렌드 (Day 1 오전)</h2>
# The "Class 1" part is already there in the prefix?
# Let's check the file content again carefully.
# In `classroom_marketing.html`:
# <h2 ...>Class 1: AI 마케팅 개요 및 트렌드 (Day 1 오전)</h2>
# <h2 ...>Class 2: 고객 페르소나 ... (Day 1 오후)</h2>
# So the prefix "Class X:" is ALREADY CORRECT.
# The suffix "(Day X 오전)" is what needs to be changed OR removed?
# The user said: "오전: 오후:을 Class1,2로 변경해 주고"
# If I change "(Day 1 오전)" to "(Class 1)", then it becomes "Class 1: ... (Class 1)". Redundant.
# Maybe the user wants to remove the suffix entirely if the prefix is already Class X?
# OR maybe they want to ensure the prefix matches the calculated class number.
# Let's assume the user wants the suffix to reflect Class 1, 2. OR maybe the user wants the TEXT descriptions to change?
# "오전: 오후:을 Class1,2로 변경해 주고" -> Change Morning/Afternoon to Class 1, 2.
# "강의실의 과목과 비교하여 매칭되도록 수정해줘" -> Match with course subject.
#
# Actually, looking at `courses.ts` for marketing:
# { title: `Class 01`, file: ... }
# { title: `Class 02`, file: ... }
#
# The HTML currently says: "Class 1: ... (Day 1 오전)"
# If I change it to "Class 1: ... (Class 1)", it's weird.
# But "Class 1: ... (Day 1 Morning)" implies the schedule.
# If I simply replace "(Day X 오전)" with "" (empty), then it becomes "Class 1: ...".
# This seems cleaner and matches `courses.ts` "Class 01".
#
# HOWEVER, the user explicitly said "change Morning/Afternoon to Class 1, 2".
# Maybe they mean:
# "Day 1 오전" -> "Class 1"
# "Day 1 오후" -> "Class 2"
#
# Let's look at `c04_advanced`? 
# The `scan` script did not find matches in `c04_advanced`.
#
# Let's simple apply the transformation: "(Day X 오전)" -> "(Class Y)" first? 
# Or better, just remove the suffix if the prefix is present?
# But wait, looking at the user request again: "오전: 오후:을 Class1,2로 변경해 주고"
#
# Let's replacing "(Day \d+ (오전|오후))" with nothing? Use regex to remove it?
# OR replace with (Class X)?
#
# Let's try to remove the parenthesis part distinctively or replace it.
# "Class 1: ... (Day 1 오전)" -> "Class 1: ..."
# This seems best.
# But let's look at the generated file.
#
# Wait, maybe the user wants to RENAMING the titles in `courses.ts`?
# No, `courses.ts` already has "Class 01", "Class 02".
#
# Let's stick to modifying the HTML files.
#
# Regex strategy:
# Find: `\(Day\s*(\d+)\s*(오전|오후)\)`
# Replace with: `` (empty string)
# result: "Class 1: Title " (trailing space removal needed)
#
# Let's try to be safe. "Class \d+: (.*) \(Day \d+ (오전|오후)\)" -> "Class \d+: $1"
#
# Let's look at the file content again.
# <h2 ...>Class 1: AI 마케팅 개요 및 트렌드 (Day 1 오전)</h2>
#
# If I remove it, it becomes:
# <h2 ...>Class 1: AI 마케팅 개요 및 트렌드 </h2>
#
# This looks correct and consistent with `courses.ts`.
#
# Let's refine the script to do this.

pattern = re.compile(r"\s*\(Day\s*\d+\s*(?:오전|오후)\)")

for d in directories:
    dir_path = os.path.join(root_dir, d)
    if not os.path.exists(dir_path):
        continue
        
    for filename in os.listdir(dir_path):
        if filename.startswith("classroom_") and filename.endswith(".html"):
            filepath = os.path.join(dir_path, filename)
            
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            new_content, count = pattern.subn("", content)
            
            if count > 0:
                print(f"Updating {filename}: Removed {count} occurrences")
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
