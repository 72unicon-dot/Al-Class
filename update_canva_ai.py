import os
import re

BASE_DIR = r"c:\Users\Win\Desktop\Antigravity 실습\AI Class"

# 공통 스타일 컴포넌트
def get_card_style():
    return 'bg-white p-8 rounded-2xl shadow-sm border border-slate-200'

def get_section_header(icon, title):
    return f'<h2 class="text-2xl font-bold text-slate-800 mb-6 border-b pb-4"><i class="{icon} text-indigo-600 mr-2"></i>{title}</h2>'

def get_gradient_badge(text):
    return f'<span class="bg-gradient-to-r from-indigo-500 to-purple-500 text-white text-xs font-bold px-2 py-1 rounded shadow-sm">{text}</span>'

# New Canva AI Content
canva_content = f'''
    <!-- 1. 핵심 개념 -->
    <section class="{get_card_style()}">
        {get_section_header("fas fa-magic", "1. Canva AI 매직 스튜디오의 핵심 개념")}
        <div class="flex flex-col md:flex-row gap-8 items-center">
            <div class="flex-1">
                <p class="text-slate-600 mb-4 leading-relaxed">
                    매직 스튜디오는 여러 곳에 흩어져 있던 AI 기능을 한데 모은 <strong>'AI 디자인 비서'</strong>입니다. 
                    단순히 이미지를 만드는 것을 넘어, <span class="text-indigo-600 font-bold">기획(텍스트)</span>, <span class="text-purple-600 font-bold">디자인(레이아웃)</span>, <span class="text-pink-600 font-bold">편집(이미지/영상 수정)</span>의 전 과정을 AI가 보조하여 작업 시간을 획기적으로 단축해 줍니다.
                </p>
                <div class="bg-indigo-50 p-4 rounded-xl border border-indigo-100 flex items-center gap-4">
                    <div class="bg-white p-3 rounded-full shadow-sm text-2xl">✨</div>
                    <div>
                        <div class="font-bold text-indigo-900">All-in-One AI Design</div>
                        <div class="text-xs text-indigo-700">디자인의 시작부터 끝까지, AI가 함께합니다.</div>
                    </div>
                </div>
            </div>
            <div class="w-full md:w-1/3 bg-slate-100 rounded-xl p-6 text-center">
                <i class="fas fa-wand-magic-sparkles text-6xl text-transparent bg-clip-text bg-gradient-to-r from-indigo-500 to-pink-500 mb-4"></i>
                <div class="font-bold text-slate-800">Magic Studio</div>
                <div class="text-xs text-slate-500 mt-1">Powering your creativity</div>
            </div>
        </div>
    </section>

    <!-- 2. 주요 기능 소개 -->
    <section class="{get_card_style()}">
        {get_section_header("fas fa-th-large", "2. 주요 기능 소개")}
        
        <div class="grid md:grid-cols-3 gap-6">
            <!-- Creation -->
            <div class="bg-indigo-50 p-6 rounded-xl border border-indigo-100 hover:shadow-md transition-all">
                <h3 class="font-bold text-indigo-900 mb-4 flex items-center"><i class="fas fa-pen-nib mr-2"></i>① 생성형 도구</h3>
                <ul class="space-y-4 text-sm">
                    <li class="bg-white p-3 rounded-lg shadow-sm">
                        <div class="font-bold text-slate-800 mb-1">매직 디자인</div>
                        <div class="text-xs text-slate-500">프레젠테이션/SNS 초안 자동 생성</div>
                    </li>
                    <li class="bg-white p-3 rounded-lg shadow-sm">
                        <div class="font-bold text-slate-800 mb-1">매직 미디어</div>
                        <div class="text-xs text-slate-500">텍스트 → 이미지/영상 변환</div>
                    </li>
                    <li class="bg-white p-3 rounded-lg shadow-sm">
                        <div class="font-bold text-slate-800 mb-1">매직 라이트</div>
                        <div class="text-xs text-slate-500">문서 작성, 요약, 초안 생성</div>
                    </li>
                </ul>
            </div>

            <!-- Editing -->
            <div class="bg-purple-50 p-6 rounded-xl border border-purple-100 hover:shadow-md transition-all">
                <h3 class="font-bold text-purple-900 mb-4 flex items-center"><i class="fas fa-edit mr-2"></i>② 스마트 편집 도구</h3>
                <ul class="space-y-4 text-sm">
                    <li class="bg-white p-3 rounded-lg shadow-sm">
                        <div class="font-bold text-slate-800 mb-1">매직 에딧</div>
                        <div class="text-xs text-slate-500">특정 부분을 다른 물체로 변경 (사과 → 오렌지)</div>
                    </li>
                    <li class="bg-white p-3 rounded-lg shadow-sm">
                        <div class="font-bold text-slate-800 mb-1">매직 익스팬드</div>
                        <div class="text-xs text-slate-500">잘린 배경을 자연스럽게 확장</div>
                    </li>
                    <li class="bg-white p-3 rounded-lg shadow-sm">
                        <div class="font-bold text-slate-800 mb-1">매직 그랩</div>
                        <div class="text-xs text-slate-500">피사체를 스티커처럼 분리/이동</div>
                    </li>
                </ul>
            </div>

            <!-- Automation -->
            <div class="bg-pink-50 p-6 rounded-xl border border-pink-100 hover:shadow-md transition-all">
                <h3 class="font-bold text-pink-900 mb-4 flex items-center"><i class="fas fa-robot mr-2"></i>③ 변환 및 자동화</h3>
                <ul class="space-y-4 text-sm">
                    <li class="bg-white p-3 rounded-lg shadow-sm">
                        <div class="font-bold text-slate-800 mb-1">매직 스위치</div>
                        <div class="text-xs text-slate-500">문서 포맷 변환 및 다국어 번역</div>
                    </li>
                    <li class="bg-white p-3 rounded-lg shadow-sm">
                        <div class="font-bold text-slate-800 mb-1">매직 애니메이션</div>
                        <div class="text-xs text-slate-500">최적의 애니메이션 효과 자동 적용</div>
                    </li>
                </ul>
            </div>
        </div>
    </section>

    <!-- 3. 실전 활용법 -->
    <section class="{get_card_style()}">
        {get_section_header("fas fa-list-ol", "3. 실전 활용법 (Step-by-Step)")}
        
        <div class="space-y-8">
            <!-- Case 1 -->
            <div class="border border-slate-200 rounded-xl overflow-hidden">
                <div class="bg-slate-50 px-6 py-4 border-b border-slate-200 flex justify-between items-center">
                    <h3 class="font-bold text-slate-800"><span class="bg-slate-800 text-white text-xs px-2 py-1 rounded mr-2">Case 1</span> 5분 만에 발표 자료 초안 만들기</h3>
                    <i class="fas fa-presentation text-slate-400"></i>
                </div>
                <div class="p-6 relative">
                    <div class="absolute left-10 top-6 bottom-6 w-0.5 bg-slate-200"></div>
                    
                    <div class="relative pl-12 mb-6">
                        <div class="absolute left-0 w-8 h-8 rounded-full bg-indigo-600 text-white flex items-center justify-center font-bold text-sm shadow-sm z-10">1</div>
                        <h4 class="font-bold text-slate-800 text-sm mb-1">매직 디자인 선택</h4>
                        <p class="text-xs text-slate-500">캔바 홈에서 <strong>[매직 디자인]</strong> 아이콘을 클릭합니다.</p>
                    </div>
                    <div class="relative pl-12 mb-6">
                        <div class="absolute left-0 w-8 h-8 rounded-full bg-indigo-600 text-white flex items-center justify-center font-bold text-sm shadow-sm z-10">2</div>
                        <h4 class="font-bold text-slate-800 text-sm mb-1">프롬프트 입력</h4>
                        <p class="text-xs text-slate-500 bg-slate-100 p-2 rounded inline-block">"제조 혁신을 위한 Lean 방법론 도입 제안서"</p>
                        <p class="text-xs text-slate-500 mt-1">라고 주제를 입력합니다.</p>
                    </div>
                    <div class="relative pl-12">
                        <div class="absolute left-0 w-8 h-8 rounded-full bg-indigo-600 text-white flex items-center justify-center font-bold text-sm shadow-sm z-10">3</div>
                        <h4 class="font-bold text-slate-800 text-sm mb-1">템플릿 선택 및 수정</h4>
                        <p class="text-xs text-slate-500">AI가 제안한 여러 디자인 중 하나를 골라 세부 내용을 수정합니다.</p>
                    </div>
                </div>
            </div>

            <!-- Case 2 -->
            <div class="border border-slate-200 rounded-xl overflow-hidden">
                <div class="bg-slate-50 px-6 py-4 border-b border-slate-200 flex justify-between items-center">
                    <h3 class="font-bold text-slate-800"><span class="bg-slate-800 text-white text-xs px-2 py-1 rounded mr-2">Case 2</span> 제품 사진 최적화하기</h3>
                    <i class="fas fa-camera text-slate-400"></i>
                </div>
                <div class="p-6 relative">
                    <div class="absolute left-10 top-6 bottom-6 w-0.5 bg-slate-200"></div>
                    
                    <div class="relative pl-12 mb-6">
                        <div class="absolute left-0 w-8 h-8 rounded-full bg-purple-600 text-white flex items-center justify-center font-bold text-sm shadow-sm z-10">1</div>
                        <h4 class="font-bold text-slate-800 text-sm mb-1">배경 확장 (Magic Expand)</h4>
                        <p class="text-xs text-slate-500">제품 사진 업로드 > <strong>[사진 편집] > [매직 익스팬드]</strong> 선택.<br>인스타그램 비율(1:1)에 맞춰 배경을 확장합니다.</p>
                    </div>
                    <div class="relative pl-12">
                        <div class="absolute left-0 w-8 h-8 rounded-full bg-purple-600 text-white flex items-center justify-center font-bold text-sm shadow-sm z-10">2</div>
                        <h4 class="font-bold text-slate-800 text-sm mb-1">소품 추가 (Magic Edit)</h4>
                        <p class="text-xs text-slate-500"><strong>[매직 에딧]</strong>으로 제품 옆을 칠하고 <em>"커피 잔, 꽃병"</em>을 추가하여 분위기를 연출합니다.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. 활용 팁 -->
    <section class="{get_card_style()}">
        {get_section_header("fas fa-lightbulb", "4. 프로의 활용 팁 (Power Tips)")}
        <div class="grid md:grid-cols-2 gap-6">
            <div class="bg-amber-50 p-6 rounded-xl border border-amber-100">
                <h4 class="font-bold text-amber-800 mb-3 flex items-center"><i class="fas fa-comment-dots mr-2"></i>구체적인 프롬프트</h4>
                <p class="text-sm text-slate-700 mb-2">프롬프트가 구체적일수록 결과물이 좋아집니다.</p>
                <div class="bg-white p-3 rounded border border-amber-200 text-xs text-slate-500">
                    <span class="text-red-400 line-through mr-2">"공장 사진"</span>
                    <i class="fas fa-arrow-right text-amber-500 mr-2"></i>
                    <span class="text-emerald-600 font-bold">"태양이 내리쬐는 현대적인 스마트 팩토리 내부의 로봇 팔, 8k 화질"</span>
                </div>
            </div>
            <div class="bg-blue-50 p-6 rounded-xl border border-blue-100">
                <h4 class="font-bold text-blue-800 mb-3 flex items-center"><i class="fas fa-swatchbook mr-2"></i>브랜드 키트 결합</h4>
                <p class="text-sm text-slate-700">
                    기업용 계정에서는 미리 설정한 <strong>브랜드 키트(로고, 폰트, 색상)</strong>를 매직 디자인에 적용하세요.<br>
                    AI가 우리 회사의 브랜드 정체성에 딱 맞는 시안만 제안합니다.
                </p>
            </div>
        </div>
    </section>
'''

def update_file():
    filename = "day03_canva_ai.html"
    filepath = os.path.join(BASE_DIR, filename)
    
    if not os.path.exists(filepath):
        print(f"File not found: {filename}")
        return

    try:
        content = ""
        encoding = 'utf-8'
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            encoding = 'cp949'
            with open(filepath, 'r', encoding='cp949') as f:
                content = f.read()

        # 삽입 위치 전략: 
        # <main> 태그 시작 후 ~ '강의 요약' 섹션 전까지의 내용을 교체
        
        summary_marker = '<!-- 강의 요약 및 다음 단계 섹션'
        summary_start = content.find(summary_marker)
        
        main_start_pattern = r'<main[^>]*>'
        main_match = re.search(main_start_pattern, content)
        
        if main_match and summary_start != -1:
            main_end_idx = main_match.end()
            
            # 기존 main 내부 컨텐츠
            header_part = content[:main_end_idx]
            footer_part = content[summary_start:]
            
            new_full_content = header_part + "\n" + canva_content + "\n\n    " + footer_part
            
            with open(filepath, 'w', encoding=encoding) as f:
                f.write(new_full_content)
            print(f"Successfully updated {filename}")
            
        else:
            print(f"Could not parse structure for {filename}. Main or Summary marker missing.")

    except Exception as e:
        print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    update_file()
