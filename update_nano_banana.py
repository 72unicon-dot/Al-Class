import os
import re

BASE_DIR = r"c:\Users\Win\Desktop\Antigravity 실습\AI Class"

# 공통 스타일 컴포넌트 (Reused)
def get_card_style():
    return 'bg-white p-8 rounded-2xl shadow-sm border border-slate-200'

def get_section_header(icon, title):
    return f'<h2 class="text-2xl font-bold text-slate-800 mb-6 border-b pb-4"><i class="{icon} text-violet-600 mr-2"></i>{title}</h2>'

def get_tip_box(title, content):
    return f'''
    <div class="bg-amber-50 border-l-4 border-amber-400 p-6 rounded-r-xl my-6">
        <h4 class="font-bold text-amber-800 mb-2 flex items-center"><i class="fas fa-lightbulb mr-2"></i>{title}</h4>
        <p class="text-slate-700 text-sm">{content}</p>
    </div>
    '''

def get_example_box(title, prompt):
    return f'''
    <div class="bg-slate-900 text-white p-6 rounded-xl shadow-lg my-6">
        <h4 class="text-xs font-bold text-violet-300 uppercase mb-3"><i class="fas fa-terminal mr-2"></i>{title}</h4>
        <p class="font-mono text-sm leading-relaxed text-slate-300">{prompt}</p>
    </div>
    '''

# Nano Banana Content
nano_banana_content = f'''
    <section class="{get_card_style()}">
        {get_section_header("fas fa-layer-group", "1. 나노 바나나 프롬프트의 4단계 핵심 구조")}
        <p class="text-slate-600 mb-8">단순히 "멋진 사진"이라고 입력하기보다, 아래와 같은 구조로 상세하게 묘사할 때 모델의 성능이 극대화됩니다.</p>
        
        <div class="grid gap-4">
            <!-- Step 1 -->
            <div class="flex flex-col md:flex-row gap-4 items-start bg-violet-50 p-5 rounded-xl border border-violet-100">
                <div class="bg-violet-600 text-white font-bold py-1 px-3 rounded-md text-sm whitespace-nowrap mt-1">1단계</div>
                <div>
                    <h3 class="font-bold text-slate-800 mb-1">주체 (Subject)</h3>
                    <p class="text-sm text-slate-700 font-medium mb-1">무엇을 그릴 것인가?</p>
                    <p class="text-xs text-slate-500">예: 제조 현장의 로봇 팔, 스마트 팩토리 내부</p>
                </div>
            </div>
            
            <!-- Step 2 -->
            <div class="flex flex-col md:flex-row gap-4 items-start bg-violet-50 p-5 rounded-xl border border-violet-100">
                <div class="bg-violet-600 text-white font-bold py-1 px-3 rounded-md text-sm whitespace-nowrap mt-1">2단계</div>
                <div>
                    <h3 class="font-bold text-slate-800 mb-1">환경 (Setting)</h3>
                    <p class="text-sm text-slate-700 font-medium mb-1">배경, 조명, 날씨, 분위기</p>
                    <p class="text-xs text-slate-500">예: 사이버펑크 스타일, 밝은 대낮, 차가운 블루 톤</p>
                </div>
            </div>
            
            <!-- Step 3 -->
            <div class="flex flex-col md:flex-row gap-4 items-start bg-violet-50 p-5 rounded-xl border border-violet-100">
                <div class="bg-violet-600 text-white font-bold py-1 px-3 rounded-md text-sm whitespace-nowrap mt-1">3단계</div>
                <div>
                    <h3 class="font-bold text-slate-800 mb-1">세부 묘사 (Details)</h3>
                    <p class="text-sm text-slate-700 font-medium mb-1">재질, 색상, 특정 동작</p>
                    <p class="text-xs text-slate-500">예: 금속 질감, 투명한 유리창, 텍스트가 적힌 전광판</p>
                </div>
            </div>
            
            <!-- Step 4 -->
            <div class="flex flex-col md:flex-row gap-4 items-start bg-violet-50 p-5 rounded-xl border border-violet-100">
                <div class="bg-violet-600 text-white font-bold py-1 px-3 rounded-md text-sm whitespace-nowrap mt-1">4단계</div>
                <div>
                    <h3 class="font-bold text-slate-800 mb-1">기술적 스타일 (Style)</h3>
                    <p class="text-sm text-slate-700 font-medium mb-1">카메라 렌즈, 화풍, 렌더링 방식</p>
                    <p class="text-xs text-slate-500">예: 8k 리얼리즘, 유화풍, 광각 렌즈</p>
                </div>
            </div>
        </div>
    </section>

    <section class="{get_card_style()}">
        {get_section_header("fas fa-font", "2. 텍스트 렌더링 특화 기법")}
        <p class="text-slate-600 mb-6 font-medium">나노 바나나의 가장 큰 강점은 이미지 내에 <span class="text-violet-600 font-bold">정확한 텍스트</span>를 포함시킬 수 있다는 점입니다.</p>
        
        <div class="space-y-6">
            <div class="flex items-start gap-4 p-4 bg-slate-50 rounded-xl">
                <div class="text-violet-600 text-xl"><i class="fas fa-quote-right"></i></div>
                <div>
                    <h4 class="font-bold text-slate-800 mb-1">따옴표 사용</h4>
                    <p class="text-sm text-slate-600">이미지 안에 포함하고 싶은 글자는 반드시 <span class="bg-violet-200 text-violet-800 px-1 rounded font-mono font-bold">큰따옴표(" ")</span>로 묶어줍니다.</p>
                </div>
            </div>
            
            <div class="flex items-start gap-4 p-4 bg-slate-50 rounded-xl">
                <div class="text-violet-600 text-xl"><i class="fas fa-map-marker-alt"></i></div>
                <div>
                    <h4 class="font-bold text-slate-800 mb-1">위치 지정</h4>
                    <p class="text-sm text-slate-600"><em>"배경 전광판에 'SMART FACTORY'라고 적혀 있음"</em>과 같이 텍스트가 들어갈 구체적인 위치를 지정하세요.</p>
                </div>
            </div>
        </div>
        
        {get_example_box("예시 프롬프트", 'A futuristic manufacturing line with a large digital sign hanging from the ceiling that says "INNOVATION" in bold white neon letters, cinematic lighting, photorealistic.')}
    </section>

    <section class="{get_card_style()}">
        {get_section_header("fas fa-laptop-code", "3. 실습 가이드: 단계별 따라하기")}
        <p class="text-slate-600 mb-8">유튜브 콘텐츠 제작이나 기업 컨설팅 자료에 활용할 수 있는 고품질 이미지를 만드는 실습 과정입니다.</p>
        
        <div class="space-y-8 relative before:absolute before:inset-0 before:ml-5 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-slate-300 before:to-transparent">
            
            <!-- 실습 1 -->
            <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                <div class="flex items-center justify-center w-10 h-10 rounded-full border border-white bg-slate-300 group-[.is-active]:bg-violet-500 group-[.is-active]:text-emerald-50 shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 text-white font-bold z-10">1</div>
                <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                    <div class="flex items-center justify-between space-x-2 mb-1">
                        <div class="font-bold text-slate-900">[실습 1] 기본 이미지 생성</div>
                    </div>
                    <div class="space-y-2 mt-2 text-sm">
                        <p class="text-slate-700"><strong><i class="fas fa-pen mr-1"></i> 프롬프트 작성:</strong><br>현대적인 공장 내부에서 작업 중인 엔지니어, 고해상도 사진 스타일</p>
                        <p class="text-slate-500"><strong><i class="fas fa-eye mr-1"></i> 결과 확인:</strong><br>전체적인 구도가 맞는지 확인합니다.</p>
                    </div>
                </div>
            </div>
            
            <!-- 실습 2 -->
            <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                <div class="flex items-center justify-center w-10 h-10 rounded-full border border-white bg-slate-300 group-[.is-active]:bg-violet-500 group-[.is-active]:text-emerald-50 shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 text-white font-bold z-10">2</div>
                <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                    <div class="flex items-center justify-between space-x-2 mb-1">
                        <div class="font-bold text-slate-900">[실습 2] 텍스트 및 세부 묘사 추가</div>
                    </div>
                    <div class="space-y-2 mt-2 text-sm">
                        <p class="text-slate-700"><strong><i class="fas fa-pen mr-1"></i> 프롬프트 수정:</strong><br>현대적인 공장 내부, 엔지니어가 태블릿을 들고 있고 배경 벽면에는 큰 글씨로 <strong>"LEAN SIX SIGMA"</strong>라고 적혀 있음, 전문가용 카메라로 촬영한 듯한 선명한 화질</p>
                        <p class="text-violet-600 text-xs bg-violet-50 p-2 rounded"><strong><i class="fas fa-star mr-1"></i> 포인트:</strong> 나노 바나나는 문맥을 잘 파악하므로, '전문가용' 혹은 '시네마틱' 같은 형용사를 섞어보세요.</p>
                    </div>
                </div>
            </div>
            
            <!-- 실습 3 -->
            <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                <div class="flex items-center justify-center w-10 h-10 rounded-full border border-white bg-slate-300 group-[.is-active]:bg-violet-500 group-[.is-active]:text-emerald-50 shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 text-white font-bold z-10">3</div>
                <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                    <div class="flex items-center justify-between space-x-2 mb-1">
                        <div class="font-bold text-slate-900">[실습 3] 반복 수정 (Iterative Refinement)</div>
                    </div>
                    <div class="space-y-2 mt-2 text-sm">
                        <p class="text-slate-600 leading-relaxed">제미나이와의 대화를 통해 <em>"방금 만든 이미지에서 배경 조명을 조금 더 어둡게 해줘"</em>라거나 <em>"엔지니어의 안전모 색상을 파란색으로 바꿔줘"</em>라고 요청하며 이미지를 다듬어 나갑니다.</p>
                    </div>
                </div>
            </div>
            
        </div>
    </section>

    <section class="{get_card_style()}">
        {get_section_header("fas fa-bolt", "4. 활용 팁 (Power User Tips)")}
        <div class="grid md:grid-cols-2 gap-6">
            <div class="bg-indigo-50 p-6 rounded-xl">
                <h4 class="font-bold text-indigo-900 mb-3 flex items-center"><i class="fas fa-expand-alt mr-2"></i>화면 비율 지정</h4>
                <p class="text-sm text-indigo-800 mb-2">프롬프트 끝에 비율 파라미터를 명시하세요.</p>
                <div class="flex gap-2 text-xs">
                    <span class="bg-white border border-indigo-200 px-2 py-1 rounded shadow-sm text-indigo-600 font-mono">--ar 16:9</span>
                    <span class="text-indigo-400 self-center">가로형 (유튜브)</span>
                </div>
                <div class="flex gap-2 text-xs mt-2">
                    <span class="bg-white border border-indigo-200 px-2 py-1 rounded shadow-sm text-indigo-600 font-mono">--ar 9:16</span>
                    <span class="text-indigo-400 self-center">세로형 (쇼츠)</span>
                </div>
            </div>
            <div class="bg-emerald-50 p-6 rounded-xl">
                <h4 class="font-bold text-emerald-900 mb-3 flex items-center"><i class="fas fa-thumbs-up mr-2"></i>긍정 묘사 권장</h4>
                <p class="text-sm text-emerald-800">
                    부정적인 표현보다 긍정적인 표현을 쓰세요.<br>
                    <span class="line-through opacity-50 text-red-800 text-xs">"지저분하지 않게"</span> 
                    <i class="fas fa-arrow-right text-xs mx-1"></i> 
                    <strong>"깨끗하고 정돈된 상태"</strong><br>
                    긍정적인 단어로 묘사하는 것이 모델 이해도가 높습니다.
                </p>
            </div>
        </div>
    </section>
'''

def update_file():
    filename = "day03_nano_banana.html"
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
            
            # 새 컨텐츠 조합
            # nano_banana_content는 이미 <section> 태그들로 구성됨
            # main 안에 감싸줄 필요 없음 (이미 main_end_idx 이후니까)
            
            new_full_content = header_part + "\n" + nano_banana_content + "\n\n    " + footer_part
            
            with open(filepath, 'w', encoding=encoding) as f:
                f.write(new_full_content)
            print(f"Successfully updated {filename}")
            
        else:
            print(f"Could not parse structure for {filename}. Main or Summary marker missing.")

    except Exception as e:
        print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    update_file()
