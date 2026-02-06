
import os
import re

def fix_merge_conflicts(root_dir):
    conflict_pattern = re.compile(
        r'<<<<<<< HEAD\s*(.*?)\s*=======\s*(.*?)\s*>>>>>>>[^\n]*',
        re.DOTALL
    )

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if not filename.endswith('.html'):
                continue
                
            filepath = os.path.join(dirpath, filename)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                continue

            if '<<<<<<< HEAD' in content:
                print(f"Fixing {filepath}...")
                
                # Replace with HEAD content
                new_content = conflict_pattern.sub(r'\1', content)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"  Fixed.")
                else:
                    print(f"  Warning: Pattern did not match even though marker exists.")

if __name__ == "__main__":
    target_dir = r"c:\Users\Win\Desktop\Antigravity 실습\AI Class"
    fix_merge_conflicts(target_dir)
