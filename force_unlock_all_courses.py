import os
import re

# Mapping Landing Page -> Classroom File
course_map = {
    "intro_ethics.html": "classroom_ethics.html",
    "intro_basics.html": "classroom_basics.html",
    "intro_business.html": "classroom_business.html",
    "master_index.html": "classroom.html", 
    "expert_advanced.html": "classroom_advanced.html",
    "special_marketing.html": "classroom_marketing.html",
    "special_manufacturing.html": "classroom_manufacturing.html",
    "special_data.html": "classroom_data.html",
    "special_video.html": "classroom_video.html",
    "management_leadership.html": "classroom_leadership.html",
    "strategy_consultant.html": "classroom_consultant.html",
    "master_app_creator.html": "classroom_app_creator.html"
}

# The new simplified auth logic template
# We inject the specific classroom link dynamically
def get_new_auth_logic(classroom_file):
    return f"""
        onAuthStateChanged(auth, async (user) => {{
            const applyBtn = document.getElementById('applyBtn');
            const enterBtn = document.getElementById('enterBtn');
            const logoutBtn = document.getElementById('heroLogoutBtn');

            if (user) {{
                // 1. Logged In -> Force Show Enter Button (Bypass Application Check)
                if (logoutBtn) logoutBtn.classList.remove('hidden');
                
                if (applyBtn) applyBtn.classList.add('hidden');
                if (enterBtn) {{
                    enterBtn.classList.remove('hidden');
                    enterBtn.title = user.email + "님 환영합니다";
                    // Direct Link to Classroom
                    enterBtn.onclick = () => window.location.href = '{classroom_file}';
                }}
            }} else {{
                // 2. Logged Out
                if (applyBtn) {{
                    applyBtn.classList.remove('hidden');
                    applyBtn.textContent = "교육 신청";
                    // Restore login modal trigger
                    applyBtn.onclick = () => window.openLoginModal();
                }}
                if (enterBtn) enterBtn.classList.add('hidden');
                if (logoutBtn) logoutBtn.classList.add('hidden');
            }}
        }});
    """

for filename, classroom_file in course_map.items():
    if not os.path.exists(filename):
        print(f"Skipping {filename} - not found")
        continue

    print(f"Unlocking {filename} -> {classroom_file}...")
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the Enter Button HTML (static fallback)
    # Search for id="enterBtn" and replace its onclick
    # pattern: <button id="enterBtn" onclick="..."
    # We want to replace whatever is in onclick with `window.location.href='{classroom_file}'`
    
    # Check if we can find the button roughly
    if 'id="enterBtn"' in content:
        # We'll use regex to be safe about attributes order
        # But simple string replace might work if format is consistent.
        # Let's try to set the onclick attribute in HTML first.
        
        # Regex to find onclick content for enterBtn
        # <button id="enterBtn" onclick="[^"]*"
        
        # Actually, let's just make sure the Javascript logic (below) overrides it.
        # But changing HTML is good for static analysis.
        pass

    # 2. Replace Auth Logic
    # We need to find the `onAuthStateChanged` block.
    # It starts with `onAuthStateChanged(auth, async (user) => {` and ends before `window.openLoginModal = ...` or similar.
    # The block is quite large.
    
    # Strategy: Find start of onAuthStateChanged and find the matching closing brace? Hard.
    # Use Regex with specific markers.
    
    # Marker 1: onAuthStateChanged(auth, async (user) => {
    # Marker 2: // Global Functions (or close to it)
    
    start_marker = "onAuthStateChanged(auth, async (user) => {"
    end_marker = "// Global Functions"
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        # Find the last closing brace and parenthesis before end_marker
        block_end = content.rfind("});", start_idx, end_idx) + 3
        
        if block_end > start_idx:
            # Replace the block
            new_logic = get_new_auth_logic(classroom_file)
            content = content[:start_idx] + new_logic + content[end_idx:]
            print("  Replaced Auth Logic")
        else:
             print("  Could not find end of auth block safely")
    else:
        print("  Could not find auth block markers")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("\nAll courses unlocked.")
