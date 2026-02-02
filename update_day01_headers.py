"""
강의 페이지 헤더 스타일 통일 스크립트
Day01 상세 페이지의 헤더를 표준 형식으로 변경
"""

import re
import os
from pathlib import Path

# 작업 디렉토리
BASE_DIR = r"c:\Users\Win\Desktop\Antigravity 실습\AI Class"

# Day01 상세 페이지 목록 (완전히 다른 구조)
DAY01_DETAIL_PAGES = [
    "day01_ai_concept.html",
    "day01_ai_caution.html",
    "day01_ai_ethics.html",
    "day01_ai_search.html",
    "day01_ai_trends.html",
    "day01_gemini.html",
    "day01_notebooklm.html",
    "day01_research_method.html"
]

# 표준 헤더 템플릿
STANDARD_HEADER = '''    <header class="gradient-bg text-white py-12 px-8 relative overflow-hidden">
        <!-- 사용자 정보 및 버튼 영역 -->
        <div class="absolute top-4 right-4 md:top-6 md:right-8 flex items-center gap-3 z-20">
            <span id="userEmailDisplay" class="text-sm text-white/90 font-medium hidden md:inline"></span>
            <a href="day01_lecture.html"
                class="inline-flex items-center gap-2 px-4 py-2 bg-white/20 backdrop-blur-md text-white text-sm font-semibold rounded-full border border-white/30 hover:bg-white/30 transition-all">
                <i class="fas fa-arrow-left"></i> <span class="hidden sm:inline">강의로 돌아가기</span>
            </a>
        </div>
        
        <div class="max-w-4xl mx-auto">
            <h1 class="text-3xl md:text-4xl font-bold mb-2">{title}</h1>
            <p class="text-xl opacity-90">{subtitle}</p>
        </div>
    </header>'''

# 사용자 이메일 표시 JavaScript
EMAIL_DISPLAY_SCRIPT = '''        } else {
            const emailDisplay = document.getElementById('userEmailDisplay');
            if (emailDisplay) emailDisplay.innerText = user.email + "님 환영합니다";
        }'''

def extract_title_from_content(content):
    """기존 콘텐츠에서 제목 추출"""
    # h1 태그에서 제목 추출
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
    if h1_match:
        title = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()
        return title
    return "강의 제목"

def extract_subtitle_from_content(content):
    """기존 콘텐츠에서 부제목 추출"""
    # p 태그에서 부제목 추출 (h1 다음)
    subtitle_match = re.search(r'<h1[^>]*>.*?</h1>\s*<p[^>]*>(.*?)</p>', content, re.DOTALL)
    if subtitle_match:
        subtitle = re.sub(r'<[^>]+>', '', subtitle_match.group(1)).strip()
        return subtitle
    return "강의 설명"

def update_day01_page(filepath):
    """Day01 상세 페이지 헤더 업데이트"""
    print(f"Processing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 제목과 부제목 추출
    title = extract_title_from_content(content)
    subtitle = extract_subtitle_from_content(content)
    
    # 헤더 생성
    new_header = STANDARD_HEADER.format(title=title, subtitle=subtitle)
    
    # 기존 헤더 찾기 및 교체
    # 패턴 1: <header class="bg-slate-50...">...</header>
    pattern1 = r'<header class="bg-slate-50[^"]*">.*?</header>'
    # 패턴 2: <header class="max-w-4xl...">...</header>
    pattern2 = r'<header class="max-w-4xl[^"]*">.*?</header>'
    
    if re.search(pattern1, content, re.DOTALL):
        content = re.sub(pattern1, new_header, content, flags=re.DOTALL)
    elif re.search(pattern2, content, re.DOTALL):
        content = re.sub(pattern2, new_header, content, flags=re.DOTALL)
    
    # JavaScript에 이메일 표시 로직 추가
    # onAuthStateChanged 내부의 } 찾기
    auth_pattern = r'(onAuthStateChanged\(auth, \(user\) => \{[\s\S]*?window\.location\.href = [\'"]index\.html[\'"];)\s*\}'
    if re.search(auth_pattern, content):
        content = re.sub(
            auth_pattern,
            r'\1' + EMAIL_DISPLAY_SCRIPT + '\n        }',
            content
        )
    
    # 파일 저장
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Updated: {filepath}")

def main():
    """메인 실행 함수"""
    print("=" * 60)
    print("Day01 상세 페이지 헤더 스타일 통일 시작")
    print("=" * 60)
    
    updated_count = 0
    
    for filename in DAY01_DETAIL_PAGES:
        filepath = os.path.join(BASE_DIR, filename)
        if os.path.exists(filepath):
            try:
                update_day01_page(filepath)
                updated_count += 1
            except Exception as e:
                print(f"✗ Error processing {filename}: {e}")
        else:
            print(f"✗ File not found: {filename}")
    
    print("=" * 60)
    print(f"완료: {updated_count}/{len(DAY01_DETAIL_PAGES)} 파일 업데이트")
    print("=" * 60)

if __name__ == "__main__":
    main()
