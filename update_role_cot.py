import os
import re

BASE_DIR = r"c:\Users\Win\Desktop\Antigravity 실습\AI Class"

# 공통 스타일 컴포넌트
def get_card_style():
    return 'bg-white p-8 rounded-2xl shadow-sm border border-slate-200'

def get_section_header(icon, title):
    return f'<h2 class="text-2xl font-bold text-slate-800 mb-6 border-b pb-4"><i class="{icon} text-indigo-600 mr-2"></i>{title}</h2>'

def get_equation(text):
    return f'<span class="font-mono bg-slate-100 px-2 py-0.5 rounded text-indigo-700 font-bold">{text}</span>'

# New Role & CoT Content
role_cot_content = f'''
    <!-- 1. 역할 부여 -->
    <section class="{get_card_style()}">
        {get_section_header("fas fa-user-tie", "1. 역할 부여 (Persona Prompting)")}
        
        <div class="mb-8">
            <h3 class="font-bold text-lg mb-2">개념</h3>
            <p class="text-slate-600 mb-4 leading-relaxed">
                AI에게 특정 인물, 직업, 또는 성격을 부여하는 기법입니다. 
                AI는 수조 개의 데이터를 학습했기 때문에, <em>"당신은 10년 차 마케팅 전문가입니다"</em>라고 역할을 정의해주면 그 역할에 어울리는 어조, 단어 선택, 지식 범위를 우선적으로 활성화합니다.
            </p>
            <div class="bg-indigo-50 p-4 rounded-xl border border-indigo-100">
                <h4 class="font-bold text-indigo-900 mb-2 text-sm">기대 효과</h4>
                <ul class="list-disc list-inside text-sm text-indigo-800 space-y-1">
                    <li><strong>답변의 전문성 향상:</strong> 일반적인 답변 대신 해당 분야의 실무적인 통찰이 담긴 답변을 얻을 수 있습니다.</li>
                    <li><strong>톤앤매너 조절:</strong> 청중(학생, 임원, 고객 등)에 맞는 적절한 말투를 구사합니다.</li>
                </ul>
            </div>
        </div>

        <div>
            <h3 class="font-bold text-lg mb-4 flex items-center"><i class="fas fa-search mr-2 text-slate-400"></i>사례 비교</h3>
            <div class="space-y-4">
                <div class="bg-slate-800 text-white p-4 rounded-xl shadow-md">
                    <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-2">Prompt</span>
                    <p class="font-mono text-sm break-keep">"당신은 제조 혁신 분야의 Lean 6Sigma 마스터 블랙벨트입니다. 중소기업 사장님들을 대상으로 '공장 내 7대 낭비 제거'의 중요성을 설득력 있게 설명하는 강연 개요를 작성해 주세요."</p>
                </div>
                
                <div class="grid md:grid-cols-2 gap-4">
                    <div class="bg-slate-100 p-4 rounded-xl border border-slate-200">
                        <span class="text-xs font-bold text-slate-500 uppercase block mb-2">General AI</span>
                        <p class="text-sm text-slate-600">"7대 낭비는 과잉생산, 대기, 운반 등이 있으며 이를 줄이면 효율이 좋아집니다."</p>
                    </div>
                    <div class="bg-indigo-50 p-4 rounded-xl border border-indigo-200 relative overflow-hidden">
                        <div class="absolute top-0 right-0 bg-indigo-500 text-white text-xs font-bold px-2 py-1 rounded-bl-lg">Role Playing AI</div>
                        <p class="text-sm text-indigo-900 font-medium">"현장 경영에서 가장 무서운 것은 <strong>'보이지 않는 비용'</strong>입니다. 사장님, 재고가 쌓이는 것을 자산으로 착각하고 계시진 않습니까? 불필요한 운반 동선만 줄여도 영업이익률이 X% 개선됩니다..."</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 2. CoT -->
    <section class="{get_card_style()}">
        {get_section_header("fas fa-streams", "2. 사고의 연쇄 (Chain of Thought, CoT)")}
        
        <div class="mb-8">
            <h3 class="font-bold text-lg mb-2">개념</h3>
            <p class="text-slate-600 mb-4 leading-relaxed">
                AI에게 <strong>"단계별로 생각하라"</strong>고 지시하거나, 문제 풀이의 과정을 예시로 보여주어 논리적 추론 과정을 거치게 하는 기법입니다. 
                AI가 성급하게 결론(답)을 내기 전에 중간 단계의 사고 과정을 거치도록 유도하는 것이 핵심입니다.
            </p>
            <div class="bg-purple-50 p-4 rounded-xl border border-purple-100">
                <h4 class="font-bold text-purple-900 mb-2 text-sm">기대 효과</h4>
                <ul class="list-disc list-inside text-sm text-purple-800 space-y-1">
                    <li><strong>추론 능력 극대화:</strong> 수학 문제, 논리 퍼즐, 복잡한 전략 수립에서 오답률을 획기적으로 낮춥니다.</li>
                    <li><strong>결과 도출 과정의 투명성:</strong> AI가 왜 이런 결론을 내렸는지 사용자가 검증할 수 있습니다.</li>
                </ul>
            </div>
        </div>

        <div class="bg-slate-50 p-6 rounded-xl border border-slate-200">
            <h3 class="font-bold text-lg mb-4">CoT 적용 사례: 불량률 계산</h3>
            
            <div class="mb-4">
                 <div class="bg-white p-4 rounded-lg border border-slate-200 mb-4">
                    <span class="text-xs font-bold text-purple-600 uppercase mb-1 block">Prompt</span>
                    <p class="text-sm text-slate-700">"우리 공장의 작년 불량률은 5%였고, 올해 3%로 낮추는 것이 목표입니다. 현재 월 생산량은 10,000개입니다. 목표를 달성했을 때 연간 줄일 수 있는 불량품의 총개수는 얼마인가요? <strong>단계별로 계산 과정을 보여주며 답해줘.</strong>"</p>
                 </div>
            </div>

            <div class="relative pl-6 border-l-2 border-purple-200 space-y-4">
                <div>
                    <span class="text-xs font-bold text-slate-400">Step 1</span>
                    <p class="text-sm font-medium text-slate-800">먼저 작년의 월간 불량 개수를 계산합니다:<br>{get_equation("10,000 × 0.05 = 500개")}</p>
                </div>
                <div>
                    <span class="text-xs font-bold text-slate-400">Step 2</span>
                    <p class="text-sm font-medium text-slate-800">올해 목표인 월간 불량 개수를 계산합니다:<br>{get_equation("10,000 × 0.03 = 300개")}</p>
                </div>
                <div>
                    <span class="text-xs font-bold text-slate-400">Step 3</span>
                    <p class="text-sm font-medium text-slate-800">월간 절감되는 불량 개수를 구합니다:<br>{get_equation("500 - 300 = 200개")}</p>
                </div>
                <div>
                    <span class="text-xs font-bold text-slate-400">Step 4</span>
                    <p class="text-sm font-medium text-slate-800">이를 연간으로 환산합니다:<br>{get_equation("200 × 12 = 2,400개")}</p>
                </div>
                <div class="bg-purple-100 p-3 rounded-lg inline-block">
                    <span class="text-xs font-bold text-purple-600 block">결론</span>
                    <p class="font-bold text-purple-900">연간 총 2,400개의 불량품을 줄일 수 있습니다.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 3. Power Combo -->
    <section class="bg-gradient-to-br from-indigo-900 to-purple-900 text-white p-8 rounded-2xl shadow-xl relative overflow-hidden">
        <div class="absolute top-0 right-0 p-8 opacity-10 text-9xl"><i class="fas fa-rocket"></i></div>
        <h2 class="text-2xl font-bold mb-6 border-b border-white/20 pb-4 relative z-10"><i class="fas fa-layer-group text-yellow-400 mr-2"></i>3. 두 기법의 결합 (The Power Combo)</h2>
        <p class="text-indigo-200 mb-8 relative z-10">가장 강력한 프롬프트는 이 두 가지를 섞는 것입니다.</p>
        
        <div class="flex flex-col md:flex-row gap-4 items-stretch relative z-10 mb-8">
            <div class="bg-white/10 backdrop-blur-sm p-4 rounded-xl flex-1 text-center border border-white/20">
                <div class="text-yellow-400 font-bold mb-1">역할 부여</div>
                <div class="text-xs text-indigo-200">Ex: 비즈니스 컨설턴트</div>
            </div>
            <div class="flex items-center justify-center text-yellow-400 font-bold text-xl">+</div>
            <div class="bg-white/10 backdrop-blur-sm p-4 rounded-xl flex-1 text-center border border-white/20">
                <div class="text-yellow-400 font-bold mb-1">구체적 상황</div>
                <div class="text-xs text-indigo-200">Ex: 신규 AI 시장 진출</div>
            </div>
            <div class="flex items-center justify-center text-yellow-400 font-bold text-xl">+</div>
            <div class="bg-white/10 backdrop-blur-sm p-4 rounded-xl flex-1 text-center border border-white/20">
                <div class="text-yellow-400 font-bold mb-1">CoT 지시</div>
                <div class="text-xs text-indigo-200">Ex: 단계별 논리적 근거</div>
            </div>
        </div>
        
        <div class="bg-black/30 p-6 rounded-xl border border-white/10 relative z-10">
            <span class="text-xs font-bold text-yellow-400 uppercase mb-2 block">Combo Prompt Example</span>
            <p class="font-mono text-sm leading-relaxed text-indigo-100">
                "당신은 <span class="text-yellow-300 font-bold">비즈니스 전략 컨설턴트</span>입니다. 현재 우리 회사가 <span class="text-yellow-300 font-bold">신규 AI 앱 시장에 진출</span>하려 합니다. 경쟁사 분석부터 마케팅 전략까지 <span class="text-yellow-300 font-bold">단계별로 논리적 근거를 들어</span> 전략 보고서 초안을 작성해 주세요."
            </p>
        </div>
    </section>
'''

def update_file():
    filename = "day02_role_cot.html"
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
            
            new_full_content = header_part + "\n" + role_cot_content + "\n\n    " + footer_part
            
            with open(filepath, 'w', encoding=encoding) as f:
                f.write(new_full_content)
            print(f"Successfully updated {filename}")
            
        else:
            print(f"Could not parse structure for {filename}")

    except Exception as e:
        print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    update_file()
