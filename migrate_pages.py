import os
import re

# 설정
BASE_DIR = r"c:\Users\Win\Desktop\Antigravity 실습\AI Class"

def simple_replace_migration():
    """
    정규식/문자열 치환을 사용하여 HTML 파일을 일괄 업데이트하는 스크립트
    """
    for filename in os.listdir(BASE_DIR):
        # 대상 파일: dayXX_*.html 파일들 (lecture 목록 페이지 제외)
        if filename.startswith('day') and filename.endswith('.html') and 'lecture' not in filename:
            filepath = os.path.join(BASE_DIR, filename)
            
            # 인코딩 처리
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                # UTF-8 실패 시 CP949 (Windows 한글) 시도
                try:
                    with open(filepath, 'r', encoding='cp949') as f:
                        content = f.read()
                except UnicodeDecodeError:
                    # 그래도 안되면 에러 무시하고 읽기
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        print(f"Warning: Forced read with encoding errors for {filename}")
            
            # 이미 처리된 파일 건너뛰기
            if 'js/progress-ui.js' in content:
                print(f"Skipping (already migrated): {filename}")
                continue
                
            original_content = content
            
            # 1. common.css 추가
            if 'css/common.css' not in content:
                # head 닫는 태그 앞에 추가
                content = content.replace('</head>', '    <link rel="stylesheet" href="css/common.css">\n</head>')
            
            # 2. 완료 버튼 컨테이너 추가
            if 'completeButtonContainer' not in content:
                # Footer 태그 앞에 추가
                footer_tag = '<footer'
                btn_html = '\n    <div class="max-w-4xl mx-auto px-6 mb-12"><div id="completeButtonContainer"></div></div>\n'
                content = content.replace(footer_tag, btn_html + footer_tag)
            
            # 3. 스크립트 업데이트
            # 기존 Firebase Auth 스크립트 패턴 찾기
            script_pattern = r'<script type="module">.*?import { auth }.*?((?!</script>).)*</script>'
            
            # 페이지 ID 추출 (예: day01_ai_concept)
            page_id = filename.replace('.html', '')
            day_match = re.search(r'(day\d+)', filename)
            
            if day_match:
                day = day_match.group(1)
                # lectureId 추출 (예: day01 사이의 접두사 제거)
                lecture_id = page_id.replace(f"{day}_", "")
                
                new_script = f"""
    <script type="module">
        import {{ auth }} from './js/firebase-config.js';
        import {{ onAuthStateChanged }} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
        import {{ addCompleteButton }} from './js/progress-ui.js';
        import {{ initAuth }} from './js/auth-common.js';

        // 공통 인증 초기화
        initAuth();

        onAuthStateChanged(auth, (user) => {{
            if (user) {{
                // 완료 버튼 추가 (자동으로 day와 lectureId 매핑)
                addCompleteButton(user.uid, '{day}', '{lecture_id}', 'completeButtonContainer');
            }}
        }});
    </script>
"""
                # 기존 auth 스크립트를 찾아서 교체 시도
                match = re.search(script_pattern, content, re.DOTALL)
                if match:
                    content = content.replace(match.group(0), new_script)
                else:
                    # 못 찾으면 body 닫는 태그 앞에 추가
                    content = content.replace('</body>', new_script + '\n</body>')
            
            # 변경사항이 있으면 저장
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Migrated: {filename}")
            else:
                print(f"No changes needed: {filename}")

if __name__ == "__main__":
    simple_replace_migration()
