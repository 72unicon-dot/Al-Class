import json
import os

# Configuration Paths - Assumes script is run from project root, or we need to adjust
# If script is in scripts/ folder, paths should be relative to project root or use absolute paths.
# Let's assume we run this from project root for now, or handle paths dynamically.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Assuming script will be moved to scripts/ folder
DATA_PATH = os.path.join(BASE_DIR, 'data', 'curriculum.json')
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates', 'classroom_template.html')

# If running from root (during refactor transition)
if not os.path.exists(DATA_PATH):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, 'data', 'curriculum.json')
    TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates', 'classroom_template.html')

def load_data():
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_template():
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        return f.read()

def get_curriculum_card(index, module, course_output_filename):
    colors = ["indigo", "emerald", "blue", "purple"]
    color = colors[index % len(colors)]
    
    details_html = ""
    for detail in module['details']:
        details_html += f"""
                                    <li class="flex items-start gap-2"><i
                                            class="fas fa-check-circle text-{color}-600 mt-1"></i><span>{detail}</span></li>"""

    # Link Logic
    link = "day01_lecture.html" # fallback

    if "classroom_ethics.html" in course_output_filename:
        if index == 0: link = "lecture_ethics_class1.html"
        elif index == 1: link = "lecture_ethics_class2.html"
    elif "classroom_basics.html" in course_output_filename:
        if index == 0: link = "lecture_basics_class1.html"
        elif index == 1: link = "lecture_basics_class2.html"
    elif "classroom_business.html" in course_output_filename:
        if index == 0: link = "lecture_business_class1.html"
        elif index == 1: link = "lecture_business_class2.html"
        elif index == 2: link = "lecture_business_class3.html"
        elif index == 3: link = "lecture_business_class4.html"
    else:
        day_num = str(index + 1).zfill(2)
        link = "day01_lecture.html"
    
    return f"""
            <!-- Module {index+1} -->
            <div class="bg-white rounded-3xl p-1 shadow-xl shadow-slate-200/50 border border-white hover:border-{color}-100 transition-all duration-300 group">
                <div class="bg-gradient-to-r from-{color}-600 to-{color}-800 rounded-[20px] p-6 md:p-8 text-white relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-64 h-64 bg-white opacity-5 rounded-full blur-3xl -mr-16 -mt-16 pointer-events-none"></div>
                    
                    <div class="flex flex-col md:flex-row md:items-center justify-between gap-6 relative z-10">
                        <div>
                            <span class="text-{color}-200 font-bold text-5xl md:text-6xl opacity-20 absolute -left-4 -top-4 select-none">{str(index+1).zfill(2)}</span>
                            <h2 class="text-xl md:text-2xl font-bold mb-2 pl-2 md:pl-0 relative">{module['title']}</h2>
                            <p class="text-{color}-100 text-sm md:text-base pl-2 md:pl-0 opacity-90">{module['desc']}</p>
                        </div>
                        <a href="{link}" class="bg-white text-{color}-700 px-6 py-2.5 rounded-full text-sm font-bold shadow-lg hover:shadow-xl hover:scale-105 active:scale-95 transition-all flex items-center gap-2 whitespace-nowrap self-start md:self-auto">
                            <i class="fas fa-play"></i> 학습하기
                        </a>
                    </div>
                </div>
                
                <div class="p-6 md:p-8 bg-indigo-50/30 rounded-b-[20px]">
                    <ul class="space-y-3 text-sm text-slate-600 font-medium">
                        {details_html}
                    </ul>
                </div>
            </div>
    """

def generate_classroom_html(config, template):
    cards_html = ""
    for i, module in enumerate(config['curriculum']):
        cards_html += get_curriculum_card(i, module, config['output'])
    
    html = template.replace("{COURSE_TITLE}", config['title']) \
                   .replace("{CURRICULUM_CARDS}", cards_html)
    
    # Check if we need to adjust output path if script is moved
    # currently writing to current working directory or relative path in config['output']
    output_path = os.path.join(BASE_DIR, config['output']) if 'scripts' in BASE_DIR else config['output']

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Regenerated {output_path}")

# Execution
if __name__ == "__main__":
    print(f"Loading data from {DATA_PATH}...")
    try:
        course_configs = load_data()
        template = load_template()
        
        print("Starting regeneration...")
        for key, config in course_configs.items():
            generate_classroom_html(config, template)
        print("All classrooms regenerated.")
    except Exception as e:
        print(f"Error: {e}")
