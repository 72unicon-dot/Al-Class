import os
import re
from pathlib import Path

def check_classroom_links(base_dir):
    classroom_files = list(Path(base_dir).rglob("classroom*.html"))
    
    results = []

    for cf in classroom_files:
        if "ai-lecture-room" in str(cf): continue
        if "backups" in str(cf): continue
        
        content = cf.read_text(encoding='utf-8')
        # Find links in module cards. Heuristic: href="lecture_..." or "day..." inside main content
        # We look for <a href="..."> inside the card structure or generally in the file
        
        # Regex to find links that look like lecture pages
        links = re.findall(r'href=["\']([^"\']+\.html)["\']', content)
        
        missing_links = []
        valid_links = []
        
        for link in links:
            if link.startswith("http") or link.startswith("#"): continue
            if "index.html" in link or "curriculum" in link: continue
            
            # Resolve relative path
            target_path = cf.parent / link
            if not target_path.exists():
                missing_links.append(link)
            else:
                valid_links.append(link)
        
        if missing_links:
            results.append(f"FAIL: {cf.name} has missing links: {missing_links}")
        elif not valid_links:
             results.append(f"WARN: {cf.name} has NO lecture links found.")
        else:
            results.append(f"OK: {cf.name} links verified ({len(valid_links)} links).")

    return "\n".join(results)

if __name__ == "__main__":
    base_dir = r"c:\Users\Win\Desktop\Antigravity_Practice\AI Class"
    print(check_classroom_links(base_dir))
