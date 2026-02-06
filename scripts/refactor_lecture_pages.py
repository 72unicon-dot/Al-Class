import os
import re

ROOT_DIR = r"d:\AI Class"
EXCLUDE_FILES = ["index.html", "intro_ethics.html", "intro_business.html", "intro_basics.html"]

def refactor_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # match the entire module script block that contains initAuth and addCompleteButton
    # We use non-greedy matching .*? inside the script tag, ensuring we find the one with our target function
    
    # Pattern designed to be flexible with whitespace and comments
    # 1. Start with script module
    # 2. Look for initAuth (optional check to ensure it's the right script)
    # 3. Look for addCompleteButton and capture args
    # 4. End script
    
    # We will just search for the addCompleteButton call to get IDs, 
    # and then find the enclosing script block to replace.
    
    button_pattern = r"addCompleteButton\(user\.uid,\s*['\"]([^'\"]+)['\"],\s*['\"]([^'\"]+)['\"],\s*['\"]([^'\"]+)['\"]\);"
    button_match = re.search(button_pattern, content)
    
    if button_match:
        day_id = button_match.group(1)
        lecture_id = button_match.group(2)
        container_id = button_match.group(3)
        
        # Now finding the script block that contains this match
        # We assume there's only one such block per file for these pages
        
        # Regex to match the whole script block containing initAuth and the button call
        # <script type="module">...initAuth...addCompleteButton...</script>
        
        script_block_pattern = r'(<script type="module">[\s\S]*?initAuth[\s\S]*?addCompleteButton[\s\S]*?</script>)'
        script_match = re.search(script_block_pattern, content)
        
        if script_match:
            print(f"Match found in {file_path}: {day_id}, {lecture_id}")
            
            new_script = f'''<script type="module">
        import {{ initApp }} from '../js/app-core.js';
        import {{ addCompleteButton }} from '../js/progress-ui.js';

        initApp({{
            requireAuth: true,
            onLogin: (user) => {{
                addCompleteButton(user.uid, '{day_id}', '{lecture_id}', '{container_id}');
            }}
        }});
    </script>'''
            
            new_content = content.replace(script_match.group(1), new_script)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        else:
            print(f"Found button call but couldn't match script block in {file_path}")
            
    return False

def main():
    count = 0
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".html") and file not in EXCLUDE_FILES:
                file_path = os.path.join(root, file)
                try:
                    if refactor_file(file_path):
                        count += 1
                        print(f"Updated: {file}")
                except Exception as e:
                    print(f"Error processing {file}: {e}")
    
    print(f"Total files updated: {count}")

if __name__ == "__main__":
    main()
