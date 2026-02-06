import os
import re

BASE_DIR = r"c:\Users\Win\Desktop\Antigravity 실습\AI Class"
FILE_PATH = os.path.join(BASE_DIR, "classroom.html")

def remove_links_regex():
    try:
        # 인코딩 처리하며 파일 읽기
        content = ""
        encoding = 'utf-8'
        try:
            with open(FILE_PATH, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            encoding = 'cp949'
            with open(FILE_PATH, 'r', encoding='cp949') as f:
                content = f.read()
        
        # 1. 대상 식별: "학습하기" 버튼이 아닌 모든 링크
        # 학습하기 버튼은 보통 "학습하기" 텍스트를 포함하거나, 특정 버튼 스타일을 가짐.
        # 강의 목록의 링크는 hover:underline 등을 포함할 수 있음.
        
        # 정규식 패턴: <a ...>내용</a>
        # DOTALL 플래그를 사용하여 줄바꿈 포함 매칭
        
        def replace_tag(match):
            full_tag = match.group(0)
            attrs = match.group(1)
            inner_text = match.group(2)
            
            # "학습하기" 버튼은 건너뛰기
            if "학습하기" in inner_text or "fa-play" in inner_text:
                return full_tag
            
            # 그 외의 링크는 span으로 변경
            # href 속성 제거
            new_attrs = re.sub(r'\s*href="[^"]*"', '', attrs)
            
            # hover 관련 클래스 제거 (선택사항)
            # new_attrs = re.sub(r'hover:[\w-]+', '', new_attrs)
            
            return f'<span {new_attrs}>{inner_text}</span>'

        # <a (속성) > (내용) </a> 패턴
        pattern = r'<a\s+([^>]*)>(.*?)</a>'
        
        new_content = re.sub(pattern, replace_tag, content, flags=re.DOTALL)
        
        # 변경된 갯수 확인 (대략적으로)
        diff_count = len(re.findall(pattern, content, flags=re.DOTALL)) - len(re.findall(pattern, new_content, flags=re.DOTALL))
        
        if content == new_content:
            print("No links were changed. Please check the logic.")
        else:
            print(f"Successfully processed file. (Note: Count is approximate)")
            
            with open(FILE_PATH, 'w', encoding=encoding) as f:
                f.write(new_content)
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    remove_links_regex()
