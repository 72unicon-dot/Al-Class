import os
import re

# Course Metadata to identify IDs
course_map = {
    "intro_ethics.html": {"id": "ethics_101", "name": "AI소개 및 윤리"},
    "intro_basics.html": {"id": "basics_101", "name": "AI 기초 입문"},
    "intro_business.html": {"id": "biz_101", "name": "AI 비즈니스 활용"},
    "master_index.html": {"id": "master_full", "name": "AI 실무 마스터"},
    "expert_advanced.html": {"id": "expert_201", "name": "AI 전문가 심화"},
    "special_marketing.html": {"id": "spec_mkt", "name": "AI 마케팅 전문가"},
    "special_manufacturing.html": {"id": "spec_mfg", "name": "AI 제조 전문가"},
    "special_data.html": {"id": "spec_data", "name": "AI 데이터 분석가"},
    "special_video.html": {"id": "spec_video", "name": "AI 영상 크리에이터"},
    "management_leadership.html": {"id": "biz_lead", "name": "AI시대의 리더십"},
    "strategy_consultant.html": {"id": "biz_consult", "name": "AI 비즈니스 컨설턴트"},
    "master_app_creator.html": {"id": "master_app", "name": "비즈니스 앱 크리에이터"}
}

# Values to inject
js_import = """
        import { initCourseApplication, checkApplicationStatus } from './js/course_application.js';
"""

# New Auth Logic Block
# We replace the existing onAuthStateChanged block with this smarter one
def get_auth_logic(course_id, course_name):
    return f"""
        // ==========================================
        // 2. Auth & Application State Logic
        // ==========================================
        // Initialize Application Logic
        initCourseApplication('{course_id}', '{course_name}');

        onAuthStateChanged(auth, async (user) => {{
            const applyBtn = document.getElementById('applyBtn');
            const enterBtn = document.getElementById('enterBtn');
            const logoutBtn = document.getElementById('heroLogoutBtn');

            if (user) {{
                // 1. Logged In
                if (logoutBtn) logoutBtn.classList.remove('hidden');
                
                // Check if already applied
                const isApplied = await checkApplicationStatus(user, '{course_id}');
                
                if (isApplied) {{
                    // Applied -> Show Enter Classroom
                    if (applyBtn) applyBtn.classList.add('hidden');
                    if (enterBtn) {{
                        enterBtn.classList.remove('hidden');
                        enterBtn.title = user.email + "님 환영합니다";
                    }}
                }} else {{
                    // Not Applied -> Show Apply Button (Logged In Mode)
                    // We modify the button to act as "Confirm Apply" instead of Login Modal
                    if (enterBtn) enterBtn.classList.add('hidden');
                    if (applyBtn) {{
                         applyBtn.classList.remove('hidden');
                         applyBtn.textContent = "수강 신청하기 (무료)";
                         // Remove onclick attribute to let JS handle it, or just rely on addEventListener in init
                         applyBtn.removeAttribute('onclick'); 
                    }}
                }}
            }} else {{
                // 2. Logged Out
                if (applyBtn) {{
                    applyBtn.classList.remove('hidden');
                    applyBtn.textContent = "교육 신청";
                    applyBtn.setAttribute('onclick', 'window.openLoginModal()'); // Restore default for guest
                }}
                if (enterBtn) enterBtn.classList.add('hidden');
                if (logoutBtn) logoutBtn.classList.add('hidden');
            }}
        }});
    """

for filename, info in course_map.items():
    if not os.path.exists(filename):
        continue
        
    print(f"Updating registration logic for {filename}...")
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Clean up the Apply Button HTML
    # We remove the hardcoded onclick="window.openLoginModal()" just in case, 
    # but strictly speaking our JS overrides it or restores it.
    # However, to be clean, let's leave it as default for guests.
    
    # 2. Inject JS Imports
    # Look for "import { db, auth }..."
    if "import { initCourseApplication" not in content:
        content = content.replace("import { db, auth } from './js/firebase-config.js';", 
                                  "import { db, auth } from './js/firebase-config.js';\n" + js_import)

    # 3. Replace Auth Logic
    # We need to find the `onAuthStateChanged(auth, (user) => { ... });` block.
    # It ends before `// Global Functions`.
    
    # regex for the block
    # Matches: onAuthStateChanged(auth, (user) => { [content] });
    # This is risky with regex due to nested braces. Consuming until Global Functions comment is safer.
    
    start_marker = "onAuthStateChanged(auth, (user) => {"
    end_marker = "// Global Functions"
    
    s_idx = content.find(start_marker)
    e_idx = content.find(end_marker)
    
    if s_idx != -1 and e_idx != -1:
        # Extract the old block to ensure we are replacing the right thing
        # but just replacing the range is easier.
        
        # We need to backtrack from end_idx to find the closing `});` or `    });`
        # actually the previous logic usually ends with `        });`
        
        new_logic = get_auth_logic(info['id'], info['name'])
        
        # We replace everything from start_marker to the line before Global Functions
        # Assuming there is a closing }); right before Global Functions
        
        # Let's try to match the exact block in the template if possible.
        # Template block:
        #         onAuthStateChanged(auth, (user) => {
        #             const applyBtn = ...
        #             ...
        #             } else {
        #                 ...
        #             }
        #         });
        
        # We will simply cut from s_idx to e_idx and insert new logic.
        # But we must be careful not to delete extra code.
        
        content = content[:s_idx] + new_logic + "\n\n        " + content[e_idx:]
        print("  Updated Auth Logic")
        
    else:
        print("  Warning: Could not find Auth Logic block")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("\nRegistration logic updated for all courses.")
