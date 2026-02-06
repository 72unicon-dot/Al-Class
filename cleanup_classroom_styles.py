import os
import re

BASE_DIR = r"c:\Users\Win\Desktop\Antigravity 실습\AI Class"
FILE_PATH = os.path.join(BASE_DIR, "classroom.html")

def cleanup_styles():
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
        
        # 정규식 패턴: <span ... class="...">
        # hover:underline, hover:text-..., transition-colors 등을 제거
        
        def replace_class(match):
            full_tag = match.group(0)
            attrs = match.group(1)
            content = match.group(2)
            
            # class 속성 찾기
            class_match = re.search(r'class="([^"]*)"', attrs)
            if class_match:
                classes = class_match.group(1).split()
                # 제거할 클래스 키워드
                remove_keywords = ['hover:', 'transition', 'cursor-pointer', 'text-blue-600']
                
                new_classes = []
                for cls in classes:
                    should_remove = False
                    for keyword in remove_keywords:
                        if keyword in cls:
                            should_remove = True
                            break
                    if not should_remove:
                        new_classes.append(cls)
                
                new_class_str = ' '.join(new_classes)
                new_attrs = attrs.replace(class_match.group(0), f'class="{new_class_str}"')
                return f'<span {new_attrs}>{content}</span>'
            
            return full_tag

        # <span (속성) > (내용) </span> 패턴
        # 이미 <span>으로 변경된 태그들만 타겟팅 (커리큘럼 리스트 내)
        # <span> 태그가 중첩될 수 있으므로 주의해야 함. 하지만 현재 구조상 <li><span>...</span></li> 임.
        
        pattern = r'<span\s+([^>]*)>(.*?)</span>'
        
        new_content = re.sub(pattern, replace_class, content, flags=re.DOTALL)
        
        # 변경 확인
        if content != new_content:
            print("Successfully cleaned up styles.")
            with open(FILE_PATH, 'w', encoding=encoding) as f:
                f.write(new_content)
        else:
            print("No visible style changes needed.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    cleanup_styles()
