import os
import re

BASE_DIR = r"c:\Users\Win\Desktop\Antigravity 실습\AI Class"

# 공통 스타일 컴포넌트
def get_card_style():
    return 'bg-white p-8 rounded-2xl shadow-sm border border-slate-200'

def get_section_header(icon, title):
    return f'<h2 class="text-2xl font-bold text-slate-800 mb-6 border-b pb-4"><i class="{icon} text-indigo-600 mr-2"></i>{title}</h2>'

def get_tip_box(title, content):
    return f'''
    <div class="bg-amber-50 border-l-4 border-amber-400 p-6 rounded-r-xl my-6">
        <h4 class="font-bold text-amber-800 mb-2 flex items-center"><i class="fas fa-lightbulb mr-2"></i>{title}</h4>
        <p class="text-slate-700 text-sm">{content}</p>
    </div>
    '''

def get_example_box(bad, good):
    return f'''
    <div class="grid md:grid-cols-2 gap-4 my-6">
        <div class="bg-red-50 p-4 rounded-xl border border-red-100">
            <span class="text-xs font-bold text-red-500 uppercase block mb-2">Bad Example</span>
            <p class="text-slate-600 font-mono text-sm">{bad}</p>
        </div>
        <div class="bg-emerald-50 p-4 rounded-xl border border-emerald-100">
            <span class="text-xs font-bold text-emerald-600 uppercase block mb-2">Good Example</span>
            <p class="text-slate-800 font-bold text-sm">{good}</p>
        </div>
    </div>
    '''

# 파일별 콘텐츠 데이터 (HTML Fragment)
CONTENT_MAP = {
    # --- Day 03: 디자인 ---
    "day03_design_principles.html": f'''
        <section class="{get_card_style()}">
            {get_section_header("fas fa-shapes", "시각적 계층 구조 (Visual Hierarchy)")}
            <p class="text-slate-600 mb-4 leading-relaxed">
                디자인의 가장 중요한 목적은 <strong>'정보의 전달'</strong>입니다. 사용자가 무엇을 먼저 봐야 할지 모른다면 실패한 디자인입니다.
                크기, 색상, 위치를 통해 정보의 중요도를 시각적으로 구별하세요.
            </p>
            <ul class="space-y-4 text-slate-700 list-disc list-inside ml-2">
                <li><strong>크기(Scale):</strong> 제목은 본문보다 최소 2배 이상 커야 합니다.</li>
                <li><strong>색상(Color):</strong> 강조하고 싶은 핵심 키워드에만 포인트 컬러를 사용하세요.</li>
                <li><strong>공백(Whitespace):</strong> 여백은 비어있는 공간이 아니라 <strong>'숨 쉴 공간'</strong>입니다.</li>
            </ul>
        </section>

        <section class="{get_card_style()}">
            {get_section_header("fas fa-palette", "실무 배색 60-30-10 법칙")}
            <p class="text-slate-600 mb-4">
                색상 조합이 어렵다면 이 황금 비율을 따르세요. 인테리어 디자인에서 유래했지만 UI/UX에서도 완벽하게 작동합니다.
            </p>
            <div class="flex h-24 rounded-xl overflow-hidden shadow-lg my-6">
                <div class="w-[60%] bg-slate-100 flex items-center justify-center text-slate-500 font-bold">Base (60%)<br>배경/여백</div>
                <div class="w-[30%] bg-indigo-100 flex items-center justify-center text-indigo-600 font-bold">Secondary (30%)<br>본문/카드</div>
                <div class="w-[10%] bg-indigo-600 flex items-center justify-center text-white font-bold">Accent (10%)<br>버튼/강조</div>
            </div>
            {get_tip_box("색상 선택 팁", "초보자는 회색조(Grayscale)로 먼저 디자인을 완성한 후, 마지막에 브랜드 컬러 1가지만 더하는 것이 가장 안전합니다.")}
        </section>
        
        <section class="{get_card_style()}">
             {get_section_header("fas fa-font", "타이포그래피 가독성 가이드")}
             <div class="grid md:grid-cols-2 gap-8">
                <div>
                    <h4 class="font-bold mb-2">자간 (Letter Spacing)</h4>
                    <p class="text-sm text-slate-600 mb-2">글자 사이의 간격입니다. 한글은 자간을 좁혀야 읽기 편합니다.</p>
                    <div class="bg-slate-50 p-3 rounded text-lg font-bold tracking-widest text-slate-400 mb-1">프레젠테이션 (자간 0)</div>
                    <div class="bg-slate-50 p-3 rounded text-lg font-bold tracking-tighter text-slate-800">프레젠테이션 (자간 -0.05em)</div>
                </div>
                <div>
                    <h4 class="font-bold mb-2">행간 (Line Height)</h4>
                    <p class="text-sm text-slate-600 mb-2">글줄 사이의 간격입니다. 본문은 글자 크기의 1.5~1.6배가 적당합니다.</p>
                    <p class="bg-slate-50 p-3 rounded text-sm leading-tight text-slate-400 mb-1">행간이 너무 좁으면<br>읽기가 답답하고<br>눈이 피로합니다.</p>
                    <p class="bg-slate-50 p-3 rounded text-sm leading-relaxed text-slate-800">행간이 적당하면<br>눈이 자연스럽게<br>다음 줄로 이동합니다.</p>
                </div>
             </div>
        </section>
    ''',

    "day03_canva_ai.html": f'''
        <section class="{get_card_style()}">
            {get_section_header("fas fa-magic", "Magic Edit: 부분 수정의 혁명")}
            <p class="text-slate-600 mb-4">
                이미지 전체를 다시 만들 필요 없이, 원하는 부분만 브러시로 칠하고 프롬프트를 입력하면 감쪽같이 수정됩니다.
            </p>
            <div class="bg-slate-50 p-6 rounded-xl border border-slate-200">
                <h4 class="font-bold mb-4">Step-by-Step 가이드</h4>
                <ol class="list-decimal list-inside space-y-3 text-slate-700">
                    <li>Canva 에디터에서 이미지 선택 > <strong>[사진 편집]</strong> 클릭</li>
                    <li><strong>[Magic Edit]</strong> 도구 선택</li>
                    <li>바꾸고 싶은 영역(예: 손에 든 꽃)을 브러시로 칠하기</li>
                    <li>프롬프트 입력: <em>"스마트폰을 들고 있는 모습으로 변경해줘"</em></li>
                    <li>생성 버튼 클릭 후 마음에 드는 결과 선택</li>
                </ol>
            </div>
        </section>

        <section class="{get_card_style()}">
            {get_section_header("fas fa-expand-arrows-alt", "Magic Expand: 상상력의 확장")}
            <p class="text-slate-600 mb-4">
                사진의 비율이 맞지 않아 여백이 남나요? Magic Expand를 사용하면 AI가 잘린 배경을 상상하여 자연스럽게 채워줍니다.
            </p>
            {get_tip_box("언제 사용하나요?", "가로형 배너를 만들어야 하는데 세로로 찍은 인물 사진밖에 없을 때, 배경을 양옆으로 늘려서 텍스트 공간을 확보할 수 있습니다.")}
        </section>
    ''',

    # --- Day 04: 비디오/오디오 ---
    "day04_audio_synthesis.html": f'''
        <section class="{get_card_style()}">
            {get_section_header("fas fa-wave-square", "Text-to-Speech (TTS)의 진화")}
            <p class="text-slate-600 mb-4 leading-relaxed">
                초기 TTS는 단순히 사전에 녹음된 음절을 이어 붙이는 방식(Concatenative)이라 기계음처럼 들렸습니다. 
                최신 <strong>Neural TTS</strong>는 딥러닝 모델이 전체 문맥을 이해하고 성우의 호흡, 억양, 감정선까지 예측하여 생성합니다.
            </p>
            <div class="grid grid-cols-2 gap-4 text-center mt-6">
                 <div class="bg-slate-100 p-4 rounded-xl">
                    <div class="font-bold text-slate-500 mb-2">기존 방식</div>
                    <div class="text-xs text-slate-400">"안.녕.하.세.요. 반.갑.습.니.다."</div>
                 </div>
                 <div class="bg-amber-100 p-4 rounded-xl border border-amber-200">
                    <div class="font-bold text-amber-700 mb-2">AI Neural TTS</div>
                    <div class="text-xs text-amber-600">"안녕하세요~! (밝게) 만나서 반가워요."</div>
                 </div>
            </div>
        </section>

        <section class="{get_card_style()}">
            {get_section_header("fas fa-sliders-h", "음성 합성 파라미터 튜닝")}
            <ul class="space-y-6">
                <li>
                    <div class="flex justify-between font-bold mb-1">
                        <span>Stability (안정성)</span>
                        <span class="text-indigo-600">0.5 ~ 0.8 추천</span>
                    </div>
                    <div class="w-full bg-slate-200 rounded-full h-2">
                        <div class="bg-indigo-600 h-2 rounded-full" style="width: 70%"></div>
                    </div>
                    <p class="text-xs text-slate-500 mt-2">너무 높으면 단조롭고, 너무 낮으면 목소리가 떨리거나 튈 수 있습니다.</p>
                </li>
                <li>
                    <div class="flex justify-between font-bold mb-1">
                        <span>Similarity (유사성)</span>
                        <span class="text-indigo-600">0.7 ~ 0.9 추천</span>
                    </div>
                    <div class="w-full bg-slate-200 rounded-full h-2">
                        <div class="bg-indigo-600 h-2 rounded-full" style="width: 85%"></div>
                    </div>
                    <p class="text-xs text-slate-500 mt-2">원본 목소리와의 일치도입니다. 너무 높으면 원본의 잡음까지 따라 할 수 있습니다.</p>
                </li>
            </ul>
        </section>
    ''',

    "day04_video_ai.html": f'''
        <section class="{get_card_style()}">
            {get_section_header("fas fa-video", "생성형 비디오의 3가지 모드")}
            <div class="grid md:grid-cols-3 gap-6">
                <div class="text-center p-4">
                    <div class="bg-indigo-50 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4 text-indigo-600 text-2xl"><i class="fas fa-font"></i></div>
                    <h3 class="font-bold mb-2">Text to Video</h3>
                    <p class="text-sm text-slate-600">텍스트 프롬프트만으로 무에서 유를 창조. 상상 속 장면 구현에 적합.</p>
                </div>
                <div class="text-center p-4">
                    <div class="bg-pink-50 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4 text-pink-600 text-2xl"><i class="fas fa-image"></i></div>
                    <h3 class="font-bold mb-2">Image to Video</h3>
                    <p class="text-sm text-slate-600">이미지를 움직이게 만듦. 캐릭터나 제품의 일관성 유지에 유리.</p>
                </div>
                <div class="text-center p-4">
                    <div class="bg-emerald-50 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4 text-emerald-600 text-2xl"><i class="fas fa-film"></i></div>
                    <h3 class="font-bold mb-2">Video to Video</h3>
                    <p class="text-sm text-slate-600">기존 영상을 다른 스타일(예: 실사 → 애니메이션)로 변환.</p>
                </div>
            </div>
        </section>

        <section class="{get_card_style()}">
            {get_section_header("fas fa-camera", "프롬프트로 카메라 워킹 제어하기")}
            <p class="text-slate-600 mb-6">영상 생성 AI에게는 전문적인 촬영 용어를 써야 정확하게 알아듣습니다.</p>
            <div class="space-y-4">
                <div class="flex items-start gap-4 p-4 bg-slate-50 rounded-lg">
                    <span class="bg-slate-800 text-white text-xs font-bold px-2 py-1 rounded">Zoom In/Out</span>
                    <p class="text-sm text-slate-700">피사체에 가까워지거나 멀어짐. <em>"Slow zoom in on the character's eye"</em></p>
                </div>
                <div class="flex items-start gap-4 p-4 bg-slate-50 rounded-lg">
                    <span class="bg-slate-800 text-white text-xs font-bold px-2 py-1 rounded">Pan Left/Right</span>
                    <p class="text-sm text-slate-700">카메라가 고정된 상태로 좌우로 회전. <em>"Pan right to reveal the landscape"</em></p>
                </div>
                 <div class="flex items-start gap-4 p-4 bg-slate-50 rounded-lg">
                    <span class="bg-slate-800 text-white text-xs font-bold px-2 py-1 rounded">Tracking Shot</span>
                    <p class="text-sm text-slate-700">피사체의 움직임을 따라 같이 이동. <em>"Tracking shot following the running car"</em></p>
                </div>
            </div>
             {get_example_box("A man walking", "Cinematic tracking shot of a mysterious man walking in neon rain, cyberpunk style, highly detailed, 4k")}
        </section>
    ''',
    
    # --- Day 05: 업무 자동화 ---
    "day05_nocode_overview.html": f'''
        <section class="{get_card_style()}">
            {get_section_header("fas fa-code-branch", "No-Code vs Low-Code")}
            <p class="text-slate-600 mb-6">
                코딩을 몰라도 앱을 만들 수 있는 시대입니다. 하지만 두 용어는 약간의 차이가 있습니다.
            </p>
            <table class="w-full text-sm text-left text-slate-600">
                <thead class="text-xs text-slate-700 uppercase bg-slate-100">
                    <tr>
                        <th class="px-6 py-3 rounded-tl-lg">구분</th>
                        <th class="px-6 py-3">No-Code (노코드)</th>
                        <th class="px-6 py-3 rounded-tr-lg">Low-Code (로우코드)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="bg-white border-b hover:bg-slate-50">
                        <td class="px-6 py-4 font-bold">주 사용자</td>
                        <td class="px-6 py-4">기획자, 마케터, 일반인</td>
                        <td class="px-6 py-4">개발자, 데이터 과학자</td>
                    </tr>
                    <tr class="bg-white border-b hover:bg-slate-50">
                        <td class="px-6 py-4 font-bold">자유도</td>
                        <td class="px-6 py-4">정해진 템플릿 내에서</td>
                        <td class="px-6 py-4">높음 (코드 개입 가능)</td>
                    </tr>
                    <tr class="bg-white border-b hover:bg-slate-50">
                        <td class="px-6 py-4 font-bold">학습 곡선</td>
                        <td class="px-6 py-4">매우 낮음 (하루 만에 가능)</td>
                        <td class="px-6 py-4">중간 (기초 로직 이해 필요)</td>
                    </tr>
                </tbody>
            </table>
        </section>

        <section class="{get_card_style()}">
             {get_section_header("fas fa-project-diagram", "자동화의 핵심: Trigger와 Action")}
             <p class="text-slate-600 mb-6">모든 자동화 툴(Zapier, Make 등)은 <strong>"이 일이 생기면(If this), 저 일을 해라(Then that)"</strong>라는 논리로 작동합니다.</p>
             
             <div class="flex items-center justify-center gap-4 my-8">
                <div class="text-center p-6 bg-blue-50 rounded-xl border-2 border-dashed border-blue-200 w-1/3">
                    <div class="text-blue-600 font-bold mb-2">Trigger (방아쇠)</div>
                    <div class="text-xs text-slate-500">새로운 이메일 도착,<br>설문지 제출 완료</div>
                </div>
                <div class="text-2xl text-slate-300"><i class="fas fa-arrow-right"></i></div>
                <div class="text-center p-6 bg-emerald-50 rounded-xl border-2 border-dashed border-emerald-200 w-1/3">
                    <div class="text-emerald-600 font-bold mb-2">Action (행동)</div>
                    <div class="text-xs text-slate-500">슬랙으로 알림 발송,<br>스프레드시트에 행 추가</div>
                </div>
             </div>
             {get_tip_box("자동화 설계 팁", "처음부터 복잡한 워크플로우를 짜지 마세요. '매일 아침 뉴스 크롤링해서 메일로 받기' 같은 아주 작은 반복 업무부터 시작하는 것이 성공의 지름길입니다.")}
        </section>
    ''',
    
     # --- Day 06: 코딩 ---
    "day06_coding_prompt.html": f'''
        <section class="{get_card_style()}">
             {get_section_header("fas fa-laptop-code", "개발자를 위한 프롬프트 엔지니어링")}
             <p class="text-slate-600 mb-6">
                코딩을 위한 AI 대화는 일반적인 대화와 다릅니다. AI에게 <strong>명확한 스펙(Spec)</strong>을 주는 것이 핵심입니다.
             </p>
             <ul class="space-y-3 bg-slate-50 p-6 rounded-xl border border-slate-200 text-sm text-slate-700">
                <li class="flex items-start gap-2"><i class="fas fa-check text-green-500 mt-1"></i> <strong>기술 스택 명시:</strong> "Python 3.10과 Pandas 라이브러리를 사용해줘."</li>
                <li class="flex items-start gap-2"><i class="fas fa-check text-green-500 mt-1"></i> <strong>입출력 예시 제공:</strong> "입력 리스트가 [1, 2, 3]일 때, 출력은 6이 되어야 해."</li>
                <li class="flex items-start gap-2"><i class="fas fa-check text-green-500 mt-1"></i> <strong>에러 처리 요구:</strong> "빈 리스트가 들어왔을 때 예외 처리 코드를 포함해줘."</li>
             </ul>
             
             {get_example_box("피보나치 수열 함수 짜줘", "Python으로 피보나치 수열을 구하는 함수를 작성해줘. 재귀(Recursion) 방식 말고 메모이제이션(Memoization)을 사용해서 성능을 최적화해줘. 주석으로 각 라인을 설명해줘.")}
        </section>
    ''',
}

def enhance_content():
    for filename, new_content in CONTENT_MAP.items():
        filepath = os.path.join(BASE_DIR, filename)
        if not os.path.exists(filepath):
            print(f"File not found: {filename}")
            continue

        try:
            # 파일 읽기
            content = ""
            encoding = 'utf-8'
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                encoding = 'cp949'
                with open(filepath, 'r', encoding='cp949') as f:
                    content = f.read()

            # 메인 콘텐츠 영역 교체
            # 전략: <main ...> 태그 시작부터 ... <div id="completeButtonContainer" (또는 Summary 섹션) 전까지의 내용을 교체
            # 하지만 안전하게 <main> 내부를 파싱하는 것이 좋음.
            # 기존 파일 구조: <main ...> ... [Old Content] ... [Summary Section] ... </main>
            # 우리가 원하는 구조: <main ...> ... [New Content] ... [Summary Section] ... </main>
            
            # Summary Section이 있는 부분 찾기 (이전 단계에서 추가함)
            summary_marker = '<!-- 강의 요약 및 다음 단계 섹션'
            summary_start = content.find(summary_marker)
            
            main_start_tag_end = content.find('<main') 
            if main_start_tag_end != -1:
                main_start_tag_end = content.find('>', main_start_tag_end) + 1
            
            if main_start_tag_end != -1 and summary_start != -1:
                # Header(강의 제목 등)는 main 밖에 있거나 main 안에 있을 수 있음.
                # 파일 구조상 Header는 <body> 직후에 있고 <main>은 그 뒤에 있음.
                # 따라서 <main> 시작부터 Summary 전까지를 다 날리고 새 콘텐츠로 채우면 됨.
                # 단, <main> 안에 헤더성 타이틀이 또 있는지 확인 필요. (보통은 <header> 태그가 main 밖에 있음)
                
                # 기존 컨텐츠의 앞부분(혹시 모를 타이틀 등)을 보존해야 할 수도 있음.
                # 하지만, CONTENT_MAP에 전체 섹션을 다 넣었으므로 과감하게 교체.
                
                # 새 콘텐츠 래퍼 (간격 등 스타일링)
                wrapped_content = f'{{new_content}}'
                
                final_content = content[:main_start_tag_end] + "\n" + new_content + "\n\n    " + content[summary_start:]
                
                with open(filepath, 'w', encoding=encoding) as f:
                    f.write(final_content)
                print(f"Enhanced content for: {filename}")
                
            else:
                print(f"Could not parse structure for {filename}. Main or Summary missing.")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    enhance_content()
