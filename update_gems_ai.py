import os
import re

BASE_DIR = r"c:\Users\Win\Desktop\Antigravity 실습\AI Class"

# 공통 스타일 컴포넌트
def get_card_style():
    return 'bg-white p-8 rounded-2xl shadow-sm border border-slate-200'

def get_section_header(icon, title):
    return f'<h2 class="text-2xl font-bold text-slate-800 mb-6 border-b pb-4"><i class="{icon} text-emerald-600 mr-2"></i>{title}</h2>'

# New Gems Content
gems_content = f'''
    <!-- 1. Gems 핵심 개념 -->
    <section class="{get_card_style()}">
        {get_section_header("fas fa-gem", "1. Gems의 핵심 개념")}
        <div class="flex flex-col md:flex-row gap-8 items-center">
            <div class="flex-1">
                <p class="text-slate-600 mb-4 leading-relaxed">
                    Gems는 사용자가 <strong class="text-emerald-700">특정 역할(Persona)</strong>과 <strong class="text-emerald-700">지침(Instruction)</strong>을 미리 설정해 둔 <strong>맞춤형 제미나이 버전</strong>입니다. 
                    매번 긴 프롬프트를 입력할 필요 없이, 한 번 만들어 두면 해당 Gem을 클릭하는 것만으로 즉시 전문적인 답변을 얻을 수 있습니다.
                </p>
                <div class="grid grid-cols-2 gap-4 mt-6">
                    <div class="bg-emerald-50 p-4 rounded-xl border border-emerald-100 text-center">
                        <div class="text-2xl mb-2">🎭</div>
                        <div class="font-bold text-emerald-900 text-sm">Persona</div>
                        <div class="text-xs text-emerald-700">나만의 전문가 역할 부여</div>
                    </div>
                    <div class="bg-emerald-50 p-4 rounded-xl border border-emerald-100 text-center">
                        <div class="text-2xl mb-2">⚡</div>
                        <div class="font-bold text-emerald-900 text-sm">Instruction</div>
                        <div class="text-xs text-emerald-700">반복 업무 즉시 실행</div>
                    </div>
                </div>
            </div>
            <div class="w-full md:w-1/3 flex justify-center">
                 <div class="relative w-48 h-48 bg-gradient-to-tr from-emerald-100 to-teal-100 rounded-full flex items-center justify-center animate-pulse">
                    <i class="fas fa-diamond text-6xl text-emerald-500"></i>
                    <div class="absolute -bottom-4 bg-white px-4 py-2 rounded-full shadow-lg text-emerald-800 font-bold text-sm">My Custom AI</div>
                 </div>
            </div>
        </div>
    </section>

    <!-- 2. 주요 특징 -->
    <section class="{get_card_style()}">
        {get_section_header("fas fa-star", "2. 주요 특징")}
        <div class="grid md:grid-cols-2 gap-6">
            <div class="bg-slate-50 p-6 rounded-xl border border-slate-100">
                <h3 class="font-bold text-slate-800 mb-2 flex items-center"><i class="fas fa-pen-fancy text-emerald-500 mr-2"></i>맞춤형 지시 (Custom Instructions)</h3>
                <p class="text-sm text-slate-600">말투, 전문 지식 수준, 답변 형식(표, 코드, 리스트 등)을 자유롭게 설정할 수 있습니다.</p>
            </div>
            <div class="bg-slate-50 p-6 rounded-xl border border-slate-100">
                <h3 class="font-bold text-slate-800 mb-2 flex items-center"><i class="fab fa-google text-emerald-500 mr-2"></i>구글 생태계 연동 (Native Integration)</h3>
                <p class="text-sm text-slate-600">Gmail, Google Drive, Docs의 데이터를 직접 참조하거나 작업 결과를 해당 앱으로 바로 보낼 수 있습니다.</p>
                <div class="text-xs text-slate-500 mt-2 bg-white p-2 rounded border border-slate-200">Ex: "내 드라이브의 강의안을 바탕으로 퀴즈 Gem 만들기"</div>
            </div>
            <div class="bg-slate-50 p-6 rounded-xl border border-slate-100">
                <h3 class="font-bold text-slate-800 mb-2 flex items-center"><i class="fas fa-book-reader text-emerald-500 mr-2"></i>지식 학습 (Knowledge Base)</h3>
                <p class="text-sm text-slate-600">PDF, 텍스트 파일 등을 업로드하여 특정 문서를 학습한 전문가 Gem을 만들 수 있습니다.</p>
            </div>
            <div class="bg-slate-50 p-6 rounded-xl border border-slate-100">
                <h3 class="font-bold text-slate-800 mb-2 flex items-center"><i class="fas fa-cubes text-emerald-500 mr-2"></i>사전 제작된 Gems 제공</h3>
                <p class="text-sm text-slate-600">구글에서 미리 만든 '학습 코치', '코딩 파트너', '글쓰기 편집기', '브레인스토머' 등을 바로 사용하거나 복사해서 수정할 수 있습니다.</p>
            </div>
        </div>
    </section>

    <!-- 3. 활용 방법 및 실무 사례 -->
    <section class="{get_card_style()}">
        {get_section_header("fas fa-tools", "3. 활용 방법 및 실무 사례")}
        
        <!-- 만드는 법 -->
        <div class="mb-8">
            <h3 class="font-bold text-lg text-slate-800 mb-4 bg-emerald-50 inline-block px-3 py-1 rounded-lg">🛠️ 만드는 법</h3>
            <ol class="space-y-4 relative border-l-2 border-emerald-100 ml-3 pl-6">
                <li class="relative">
                    <span class="absolute -left-[2.2rem] top-0 w-8 h-8 bg-emerald-500 text-white rounded-full flex items-center justify-center font-bold text-sm">1</span>
                    <strong class="text-slate-900 block mb-1">탐색 및 시작</strong>
                    <span class="text-sm text-slate-600">제미나이 왼쪽 사이드바에서 <strong>[Gems 탐색하기]</strong> 또는 <strong>[새로운 Gem]</strong> 클릭</span>
                </li>
                <li class="relative">
                    <span class="absolute -left-[2.2rem] top-0 w-8 h-8 bg-emerald-500 text-white rounded-full flex items-center justify-center font-bold text-sm">2</span>
                    <strong class="text-slate-900 block mb-1">이름 및 지침 설정</strong>
                    <div class="bg-slate-800 text-white p-3 rounded-lg text-xs font-mono mt-1">
                        <div class="text-emerald-400 mb-1"># 이름: 제조혁신 컨설팅 비서</div>
                        <div>"너는 20년 경력의 Lean 6Sigma 전문가야. 항상 현장 중심의 사례를 들어 설명하고, 답변 마지막엔 반드시 3가지 핵심 요약을 제공해."</div>
                    </div>
                </li>
                <li class="relative">
                    <span class="absolute -left-[2.2rem] top-0 w-8 h-8 bg-emerald-500 text-white rounded-full flex items-center justify-center font-bold text-sm">3</span>
                    <strong class="text-slate-900 block mb-1">저장 및 실행</strong>
                    <span class="text-sm text-slate-600">저장 후 해당 Gem을 클릭해 대화 시작</span>
                </li>
            </ol>
        </div>

        <!-- 실무 활용 시나리오 -->
        <div>
            <h3 class="font-bold text-lg text-slate-800 mb-4 bg-emerald-50 inline-block px-3 py-1 rounded-lg">💼 실무 활용 시나리오</h3>
            <div class="overflow-x-auto">
                <table class="w-full text-sm text-left text-slate-600 border rounded-xl overflow-hidden shadow-sm">
                    <thead class="text-xs text-slate-700 uppercase bg-slate-100 border-b">
                        <tr>
                            <th class="px-4 py-3 font-bold w-1/4">활용 분야</th>
                            <th class="px-4 py-3 font-bold w-1/2">Gem 설정 아이디어</th>
                            <th class="px-4 py-3 font-bold w-1/4">기대 효과</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100">
                        <tr class="bg-white hover:bg-slate-50">
                            <td class="px-4 py-3 font-bold text-slate-800">유튜브 채널 관리</td>
                            <td class="px-4 py-3">"구독자 유입을 극대화하는 썸네일 제목 및 해시태그 생성기"</td>
                            <td class="px-4 py-3 text-emerald-600">클릭률(CTR) 개선 및 제작 시간 단축</td>
                        </tr>
                        <tr class="bg-white hover:bg-slate-50">
                            <td class="px-4 py-3 font-bold text-slate-800">강의 자료 제작</td>
                            <td class="px-4 py-3">"업로드한 전문 서적 PDF를 기반으로 시험 문제와 해설을 만드는 교육 조교"</td>
                            <td class="px-4 py-3 text-emerald-600">교안 제작 및 테스트 자동화</td>
                        </tr>
                        <tr class="bg-white hover:bg-slate-50">
                            <td class="px-4 py-3 font-bold text-slate-800">비즈니스 메일</td>
                            <td class="px-4 py-3">"상황별(제안, 거절, 감사) 비즈니스 매너를 갖춘 다국어 메일 작성기"</td>
                            <td class="px-4 py-3 text-emerald-600">실수 방지 및 전문성 강화</td>
                        </tr>
                        <tr class="bg-white hover:bg-slate-50">
                            <td class="px-4 py-3 font-bold text-slate-800">데이터 분석</td>
                            <td class="px-4 py-3">"CSV 파일을 분석해 제조 현장의 병목 구간(Bottleneck)을 찾아주는 분석가"</td>
                            <td class="px-4 py-3 text-emerald-600">신속한 인사이트 도출</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>

    <!-- 4. Gems 활용 팁 -->
    <section class="{get_card_style()}">
        {get_section_header("fas fa-lightbulb", "4. Gems 활용 팁 (Pro Tips)")}
        <div class="grid md:grid-cols-3 gap-6">
            <div class="bg-amber-50 p-6 rounded-xl border border-amber-200">
                <h4 class="font-bold text-amber-800 mb-3 text-sm flex items-center"><i class="fas fa-magic mr-2"></i>Gem 안에서 Gem 만들기</h4>
                <p class="text-xs text-slate-700 leading-relaxed">
                    "내가 Gem을 더 잘 만들 수 있도록 돕는 '프롬프트 엔지니어 Gem'을 만들어줘"라고 요청해 보세요.
                </p>
            </div>
            <div class="bg-blue-50 p-6 rounded-xl border border-blue-200">
                <h4 class="font-bold text-blue-800 mb-3 text-sm flex items-center"><i class="fas fa-layer-group mr-2"></i>단계별 지침(CoT) 활용</h4>
                <p class="text-xs text-slate-700 leading-relaxed">
                    지침 칸에 "결론을 내기 전, 먼저 상황을 분석하고(1단계), 대안을 제시한 뒤(2단계), 최종안을 확정해라"와 같이 논리적 흐름을 입력하면 훨씬 정교한 답변을 얻습니다.
                </p>
            </div>
            <div class="bg-purple-50 p-6 rounded-xl border border-purple-200">
                <h4 class="font-bold text-purple-800 mb-3 text-sm flex items-center"><i class="fas fa-sync-alt mr-2"></i>반복 수정 (Iterative)</h4>
                <p class="text-xs text-slate-700 leading-relaxed">
                    한 번에 완벽한 Gem을 만들려 하기보다, 대화를 나누며 "이 말투는 너무 딱딱하니 조금 더 친근하게 바꿔줘"라고 업데이트해 나가는 것이 좋습니다.
                </p>
            </div>
        </div>
    </section>
'''

def update_file():
    filename = "day02_gems_ai.html"
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

        # 삽입 위치 전략
        summary_marker = '<!-- 강의 요약 및 다음 단계 섹션'
        summary_start = content.find(summary_marker)
        
        main_start_pattern = r'<main[^>]*>'
        main_match = re.search(main_start_pattern, content)
        
        if main_match and summary_start != -1:
            main_end_idx = main_match.end()
            
            header_part = content[:main_end_idx]
            footer_part = content[summary_start:]
            
            new_full_content = header_part + "\n" + gems_content + "\n\n    " + footer_part
            
            with open(filepath, 'w', encoding=encoding) as f:
                f.write(new_full_content)
            print(f"Successfully updated {filename}")
            
        else:
            print(f"Could not parse structure for {filename}")

    except Exception as e:
        print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    update_file()
