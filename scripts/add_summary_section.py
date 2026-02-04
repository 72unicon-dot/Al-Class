import os
import re

BASE_DIR = r"c:\Users\Win\Desktop\Antigravity 실습\AI Class"

# 파일별 요약 문구 매핑 (사용자 요청 반영)
SUMMARY_MESSAGES = {
    "day01_ai_concept.html": "생성형 AI의 기본 원리와 작동 방식을 이해하는 것이 혁신의 첫걸음입니다.",
    "day01_ai_ethics.html": "AI 윤리를 준수하며 책임감 있게 기술을 활용하는 자세가 중요합니다.",
    "day01_ai_trends.html": "급변하는 AI 트렌드를 파악하고 비즈니스 기회를 포착하는 안목을 길렀습니다.",
    "day01_ai_search.html": "기존 검색을 넘어선 AI 기반 리서치로 정보 수집의 효율을 극대화하세요.",
    "day01_gemini.html": "Gemini의 멀티모달 기능을 활용하여 텍스트와 이미지를 넘나드는 작업을 시도해보세요.",
    "day01_notebooklm.html": "방대한 문서를 NotebookLM으로 분석하여 인사이트를 도출하는 방법을 익혔습니다.",
    
    "day02_prompt_principles.html": "기술의 원리를 이해하는 것이 효과적인 프롬프팅의 시작입니다.",
    "day02_role_cot.html": "AI에게 역할을 부여하고 논리적 사고를 유도하여 답변의 품질을 높여보세요.",
    "day02_llm_comparison.html": "각 모델의 장단점을 파악하여 상황에 맞는 최적의 도구를 선택할 수 있습니다.",
    
    "day03_design_principles.html": "AI 기술에 디자인 원칙을 더하여 더욱 매력적이고 전문적인 결과물을 만들어보세요.",
    "day03_canva_ai.html": "Canva의 AI 도구를 활용하여 비전문가도 수준 높은 디자인을 쉽고 빠르게 제작할 수 있습니다.",
    "day03_image_params.html": "파라미터 조절을 통해 내가 상상하던 이미지를 정확하게 구현하는 능력을 갖췄습니다.",
    
    "day04_audio_synthesis.html": "텍스트를 자연스러운 음성으로 변환하여 콘텐츠의 생동감을 더해보세요.",
    "day04_video_ai.html": "AI로 영상을 생성하고 편집하여 시각적 스토리텔링의 영역을 확장했습니다.",
    "day04_runway_gen3.html": "최신 영상 생성 모델을 활용하여 상상 속의 장면을 현실감 있게 구현해보세요.",
    
    "day05_nocode_overview.html": "코딩 없이도 강력한 애플리케이션을 만들 수 있는 노코드의 잠재력을 확인했습니다.",
    "day05_automation_design.html": "반복적인 업무 흐름을 자동화하여 창의적인 일에 더 집중할 수 있는 시간을 확보하세요.",
    "day05_make_zapier.html": "다양한 도구들을 연결하여 나만의 24시간 자동화 비서 시스템을 구축했습니다.",
    
    "day06_coding_prompt.html": "자연어로 코드를 작성하며 프로그래밍의 장벽을 낮추고 논리적 사고력을 키웠습니다.",
    "day06_pair_programming.html": "AI와의 협업을 통해 더 빠르고 정확하게 코드를 작성하고 문제를 해결해보세요.",
    "day06_cursor_setup.html": "차세대 AI 에디터 Cursor를 통해 코딩 경험을 혁신하고 생산성을 극대화하세요.",
    
    "day07_web_app_structure.html": "웹 애플리케이션의 전체 구조를 이해하고 서비스를 설계할 수 있는 기반을 다졌습니다.",
    "day07_api_integration.html": "외부 API를 연동하여 우리 서비스에 강력한 기능과 데이터를 확장해보세요.",
    "day07_database_connection.html": "데이터를 체계적으로 저장하고 관리하여 사용자에게 개인화된 경험을 제공할 수 있습니다.",
    
    "day08_cloud_deployment.html": "로컬 환경을 넘어 클라우드에 서비스를 배포하여 전 세계 사용자와 만나보세요.",
    "day08_domain_https.html": "나만의 도메인을 연결하고 보안을 강화하여 신뢰받는 서비스를 완성했습니다.",
    "day08_maintenance.html": "지속적인 모니터링과 업데이트로 안정적인 서비스 운영을 시작해보세요."
}

DEFAULT_MESSAGES = {
    "day01": "AI의 기초를 다졌습니다. 이제 실무 적용을 시작해보세요.",
    "day02": "프롬프트의 원리를 이해하는 것이 AI 활용의 핵심입니다.",
    "day03": "시각적 표현력을 높여 콘텐츠의 가치를 더해보세요.",
    "day04": "멀티미디어 콘텐츠 제작의 새로운 가능성을 열었습니다.",
    "day05": "업무 자동화로 효율성을 극대화하는 방법을 익혔습니다.",
    "day06": "AI와 함께하는 프로그래밍으로 코딩의 장벽을 넘었습니다.",
    "day07": "나만의 웹 서비스를 설계하고 구현할 수 있는 능력을 갖췄습니다.",
    "day08": "서비스를 배포하고 운영하며 세상과 소통할 준비를 마쳤습니다."
}

def get_summary_message(filename):
    if filename in SUMMARY_MESSAGES:
        return SUMMARY_MESSAGES[filename]
    day_match = re.search(r'(day\d+)', filename)
    if day_match:
        day_key = day_match.group(1)
        if day_key in DEFAULT_MESSAGES:
            return DEFAULT_MESSAGES[day_key]
    return "이번 강의의 핵심 내용을 마스터하셨습니다. 다음 단계로 나아갈 준비가 되었습니다."

def create_summary_html(message):
    return f"""
    <!-- 강의 요약 및 다음 단계 섹션 (Auto-injected) -->
    <div class="max-w-4xl mx-auto px-6 mb-8 mt-12 bg-white rounded-[32px] p-12 text-center border border-slate-100 shadow-2xl shadow-slate-100">
        <h3 class="text-3xl md:text-4xl font-black text-slate-900 mb-6 tracking-tight">강의 요약 및 다음 단계</h3>
        <p class="text-slate-500 text-lg md:text-xl font-medium mb-12 word-keep-all">{message}</p>
        <div class="flex flex-col md:flex-row justify-center gap-5">
            <button onclick="alert('교재 파일 준비 중입니다.')" class="bg-[#5c4ae3] text-white px-10 py-5 rounded-2xl font-bold text-lg flex items-center justify-center gap-3 shadow-lg shadow-indigo-100 hover:bg-[#4a3bc2] transition-colors">
                <i class="fas fa-file-pdf"></i> 교재 PDF 다운로드
            </button>
            <button onclick="location.href='classroom.html'" class="border-2 border-slate-200 text-[#5c4ae3] bg-white px-10 py-5 rounded-2xl font-bold text-lg hover:bg-indigo-50 hover:border-[#5c4ae3] transition-all">
                강의실로 돌아가기
            </button>
        </div>
    </div>
"""

def process_file(filepath, filename):
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
        
        message = get_summary_message(filename)
        summary_html = create_summary_html(message)
        
        # Case 1: 이미 "강의 요약 및 다음 단계"가 있는 경우 -> 메시지와 디자인 업데이트
        if "강의 요약 및 다음 단계" in content:
            # 기존 섹션을 통째로 교체하는 것이 깔끔함 (정규식으로 섹션 찾기)
            # <section ...> ... 강의 요약 ... </section> 패턴이나 <div ...> ... </div> 패턴
            # 하지만 태그 매칭이 어려우므로, <h3...강의 요약...</h3> 바로 뒤의 <p> 태그 내용을 교체하는 방식 사용
            
            # 메시지 교체
            pattern_msg = r'(<h3[^>]*>강의 요약 및 다음 단계</h3>\s*<p[^>]*>)(.*?)(</p>)'
            
            if re.search(pattern_msg, content, re.DOTALL):
                new_content = re.sub(pattern_msg, f'\\1{message}\\3', content, flags=re.DOTALL)
                
                # 만약 기존 섹션이 예전 디자인이라면 통째로 바꾸는게 낫지만, 여기선 메시지 업데이트에 집중
                # day02_prompt_principles.html의 경우 기존 디자인이 훌륭하므로 메시지만 바꾸면 됨.
                if content != new_content:
                    with open(filepath, 'w', encoding=encoding) as f:
                        f.write(new_content)
                    print(f"Updated message in: {filename}")
                return

        # Case 2: 없는 경우 -> 삽입
        # 삽입 위치 탐색
        insert_marker = None
        insert_pos = -1
        
        # 1순위: completeButtonContainer
        if 'id="completeButtonContainer"' in content:
            # 이미 컨테이너가 있으면 그 부모 div나 해당 div 바로 앞에 삽입
            # <div ...><div id="completeButtonContainer">...
            match = re.search(r'<div[^>]*>\s*<div id="completeButtonContainer">', content)
            if match:
                insert_pos = match.start()
            else:
                 insert_pos = content.find('<div id="completeButtonContainer"')
        
        # 2순위: Footer
        if insert_pos == -1 and '<footer' in content:
            insert_pos = content.find('<footer')
            
        # 3순위: Main 닫는 태그
        if insert_pos == -1 and '</main>' in content:
            insert_pos = content.find('</main>')
            
        # 4순위: Body 닫는 태그
        if insert_pos == -1:
            insert_pos = content.find('</body>')

        if insert_pos != -1:
            new_content = content[:insert_pos] + summary_html + "\n" + content[insert_pos:]
            
            # 만약 completeButtonContainer가 없었다면, Summary 뒤에 추가해줘야 함 (진도 추적을 위해)
            if 'id="completeButtonContainer"' not in content:
                btn_html = '\n<div class="max-w-4xl mx-auto px-6 mb-12"><div id="completeButtonContainer"></div></div>\n'
                # Summary 바로 뒤 (즉, 원래 삽입 위치 + Summary 길이)가 아니라, Summary 다음에 오도록
                # 사실 insert_pos에 Summary + BtnHTML을 넣으면 됨
                new_content = content[:insert_pos] + summary_html + btn_html + "\n" + content[insert_pos:]
            
            with open(filepath, 'w', encoding=encoding) as f:
                f.write(new_content)
            print(f"Inserted summary in: {filename}")
        else:
            print(f"Error: Could not find insertion point for {filename}")

    except Exception as e:
        print(f"Error processing {filename}: {e}")

def main():
    for filename in os.listdir(BASE_DIR):
        if filename.startswith('day') and filename.endswith('.html') and 'lecture' not in filename:
            filepath = os.path.join(BASE_DIR, filename)
            process_file(filepath, filename)

if __name__ == "__main__":
    main()
