
# Script to generate Lecture Pages and Textbooks for AI Business Strategy Course
import os

# ==========================================
# 1. TEXTBOOKS DATA (Business Course)
# ==========================================
textbooks = [
    {
        "filename": "textbook_business_cases.html",
        "title": "산업별 AI 혁신 사례 (Case Study)",
        "subtitle": "Finance, Manufacturing, Retail AI Transformation",
        "color": "blue",
        "content": """
            <h3>1. 금융 (Finance)</h3>
            <ul class="list-disc pl-6 space-y-2">
                <li><strong>JP Morgan:</strong> 'IndexGPT'를 통해 고객 맞춤형 투자 포트폴리오를 AI가 분석하고 추천.</li>
                <li><strong>Bloomberg:</strong> 'BloombergGPT'를 자체 구축하여 40년치 금융 데이터를 학습, 시장 분석 속도 단축.</li>
            </ul>

            <h3>2. 제조 (Manufacturing)</h3>
            <ul class="list-disc pl-6 space-y-2">
                <li><strong>Siemens:</strong> 공장 자동화에 생성형 AI를 도입하여, 엔지니어가 자연어로 코딩하면 PLC 코드를 생성.</li>
                <li><strong>Hyundai:</strong> 로봇 개 '스팟'에 AI를 탑재하여 공장 내 위험 요소를 실시간 감지 및 보고.</li>
            </ul>

            <h3>3. 유통 (Retail)</h3>
            <ul class="list-disc pl-6 space-y-2">
                <li><strong>Nike:</strong> 고객의 발 모양과 취향 데이터를 분석하여 맞춤형 디자인을 생성 및 제공 (C2M).</li>
                <li><strong>Coca-Cola:</strong> 'Create Real Magic' 캠페인을 통해 소비자가 AI로 광고 이미지를 만들게 하고 이를 마케팅에 활용.</li>
            </ul>
        """
    },
    {
        "filename": "textbook_business_bm.html",
        "title": "AI 기반 신규 비즈니스 모델 발굴",
        "subtitle": "Business Model Canvas with AI",
        "color": "indigo",
        "content": """
            <h3>1. 생성형 AI가 바꾸는 BM의 핵심</h3>
            <p>기존 서비스에 AI 채팅만 붙이는 것이 아니라, <strong>가치 제안(Value Proposition)</strong> 자체가 AI로 인해 어떻게 변하는지 고민해야 합니다.</p>
            
            <h3>2. AI 비즈니스 유형 3가지</h3>
            <div class="grid md:grid-cols-3 gap-4 mt-4 text-sm">
                <div class="bg-indigo-50 p-3 rounded border border-indigo-200">
                    <strong class="block text-indigo-700 mb-2">1. Co-pilot (부조종사)</strong>
                    <p>전문가의 업무를 보조. (예: Github Copilot, Jasper)</p>
                </div>
                 <div class="bg-blue-50 p-3 rounded border border-blue-200">
                    <strong class="block text-blue-700 mb-2">2. Creator (창작자)</strong>
                    <p>새로운 콘텐츠나 데이터를 생성. (예: Midjourney, Suno AI)</p>
                </div>
                 <div class="bg-purple-50 p-3 rounded border border-purple-200">
                    <strong class="block text-purple-700 mb-2">3. Agent (대리인)</strong>
                    <p>인간 대신 복잡한 작업을 자율 수행. (예: AutoGPT, AI 비서)</p>
                </div>
            </div>

            <h3>3. BM 캔버스 실습 가이드</h3>
            <p>'비용 구조(Cost Structure)'에서 AI API 비용을 고려하고, '핵심 자원(Key Resources)'에 데이터 파이프라인을 추가하는 것이 중요합니다.</p>
        """
    },
    {
        "filename": "textbook_business_roadmap.html",
        "title": "AI 성숙도 진단 및 목표 설정",
        "subtitle": "AI Maturity Model & Goal Setting",
        "color": "green",
        "content": """
            <h3>1. AI 도입 5단계 성숙도 모델</h3>
            <ol class="list-decimal pl-6 space-y-2">
                <li><strong>탐색기 (Exploring):</strong> 개인적 관심으로 툴을 써보는 단계.</li>
                <li><strong>실험기 (Experimenting):</strong> 소규모 파일럿 프로젝트(PoC)를 진행해보는 단계.</li>
                <li><strong>공식화 (Formalizing):</strong> 전사적 도입을 위한 예산과 조직이 생기는 단계.</li>
                <li><strong>확장기 (Scaling):</strong> 여러 부서로 AI 활용이 확산되고 데이터가 통합되는 단계.</li>
                <li><strong>변혁기 (Transforming):</strong> AI가 비즈니스의 핵심 경쟁력이 되는 단계 (AI First).</li>
            </ol>

            <h3>2. 목표 설정 (KPI) 예시</h3>
            <ul>
                <li><strong>단기:</strong> 직원 1인당 업무 시간 일 30분 단축 (생산성)</li>
                <li><strong>중기:</strong> 고객 응대 자동화율 50% 달성 (비용 절감)</li>
                <li><strong>장기:</strong> AI 기반 신규 매출 비중 10% 달성 (매출 증대)</li>
            </ul>
        """
    },
    {
        "filename": "textbook_business_poc.html",
        "title": "PoC(개념 증명) 기획서 작성 실습",
        "subtitle": "Planning a Proof of Concept",
        "color": "teal",
        "content": """
            <h3>1. 실패하지 않는 PoC의 조건</h3>
            <p>AI 프로젝트의 80%는 PoC에서 멈춥니다. 성공 확률을 높이려면?</p>
            <ul class="list-disc pl-6 space-y-2 mt-2">
                <li><strong>작게 시작하라 (Start Small):</strong> 너무 거창한 문제보다, 해결 가능한 구체적 문제(Pain Point)에 집중하세요.</li>
                <li><strong>데이터 확인:</strong> AI 모델보다 중요한 것은 '학습시킬 깨끗한 데이터가 있는가'입니다.</li>
                <li><strong>User Feedback:</strong> 현업 사용자를 기획 초기부터 참여시켜야 합니다.</li>
            </ul>

            <h3>2. PoC 기획서 템플릿 항목</h3>
            <table class="w-full text-sm border mt-4">
                <tr class="bg-gray-100"><th class="p-2 border">항목</th><th class="p-2 border">내용</th></tr>
                <tr><td class="p-2 border">Problem</td><td class="p-2 border">분석 리포트 작성에 3일 소요됨</td></tr>
                <tr><td class="p-2 border">Solution</td><td class="p-2 border">LLM을 활용한 초안 자동 생성</td></tr>
                <tr><td class="p-2 border">Success Metric</td><td class="p-2 border">작성 시간 3일 -> 4시간 단축</td></tr>
            </table>
        """
    },
    {
        "filename": "textbook_business_roi.html",
        "title": "ROI 분석 및 투자 전략",
        "subtitle": "Return on Investment Analysis",
        "color": "amber",
        "content": """
            <h3>1. AI 도입 비용 (TCO) 계산</h3>
            <p>단순 솔루션 구독료 외에 숨겨진 비용을 파악해야 합니다.</p>
            <ul>
                <li><strong>API 사용료:</strong> 토큰당 과금 (사용량 증가 시 급증)</li>
                <li><strong>인프라 비용:</strong> 클라우드 GPU 서버 비용, 벡터 DB 비용</li>
                <li><strong>인건비:</strong> 프롬프트 엔지니어링, 데이터 전처리 인력</li>
            </ul>

            <h3>2. 정량적 vs 정성적 효과</h3>
            <div class="grid md:grid-cols-2 gap-4 mt-4">
                <div class="bg-amber-50 p-4 border border-amber-200 rounded">
                    <strong>💰 정량적 (Hard ROI)</strong>
                    <ul class="text-sm pl-4 list-disc mt-2">
                        <li>인건비 절감액</li>
                        <li>매출 증가액</li>
                        <li>오류 예방 비용</li>
                    </ul>
                </div>
                 <div class="bg-orange-50 p-4 border border-orange-200 rounded">
                    <strong>✨ 정성적 (Soft ROI)</strong>
                     <ul class="text-sm pl-4 list-disc mt-2">
                        <li>직원 만족도(단순 반복 업무 제거)</li>
                        <li>브랜드 혁신 이미지</li>
                        <li>의사결정 속도 향상</li>
                    </ul>
                </div>
            </div>
        """
    },
    {
        "filename": "textbook_business_risk.html",
        "title": "AI 프로젝트 리스크 관리",
        "subtitle": "Risk Management & Governance",
        "color": "red",
        "content": """
            <h3>1. 주요 리스크 요인</h3>
            <ul>
                <li><strong>환각(Hallucination):</strong> AI가 잘못된 정보를 생성하여 의사결정을 그르칠 위험.</li>
                <li><strong>편향(Bias):</strong> 학습 데이터의 편향으로 인해 차별적 결과가 나올 위험 (채용, 대출 심사 등).</li>
                <li><strong>의존성(Dependency):</strong> 특정 AI 모델(OpenAI 등)에 지나치게 의존하여 가격 인상/정책 변경에 취약해짐.</li>
            </ul>

            <h3>2. AI 거버넌스 구축</h3>
            <p>전사적인 AI 관리 체계를 만들어야 합니다. 'AI 윤리 위원회'를 설치하거나, AI 산출물에 대한 '인간 검수 프로세스'를 의무화하는 것이 그 시작입니다.</p>
        """
    }
]

# ==========================================
# 2. GENERATE TEXTBOOK FILES
# ==========================================
textbook_template = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>강의 교재 - AI 비즈니스 전략</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        body {{ font-family: 'Pretendard', sans-serif; line-height: 1.7; }}
        .textbook-content h3 {{ font-size: 1.25rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.75rem; color: #1e293b; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem; }}
        .textbook-content p {{ margin-bottom: 1rem; color: #475569; }}
        .textbook-content ul, .textbook-content ol {{ list-style-position: inside; margin-bottom: 1.5rem; color: #475569; }}
        .textbook-content table {{ width: 100%; border-collapse: collapse; margin-top: 1rem; }}
        .textbook-content th, .textbook-content td {{ padding: 0.75rem; border: 1px solid #e2e8f0; }}
        .textbook-content th {{ background-color: #f8fafc; font-weight: 600; }}
    </style>
</head>
<body class="bg-slate-50 min-h-screen">
    <div class="max-w-4xl mx-auto px-6 py-12">
        <div class="flex justify-between items-center mb-8">
            <a href="classroom_business.html" class="inline-flex items-center gap-2 text-slate-500 hover:text-slate-800 transition-colors">
                <i class="fas fa-arrow-left"></i> 강의실로 돌아가기
            </a>
            <button onclick="window.print()" class="text-slate-400 hover:text-slate-600"><i class="fas fa-print"></i></button>
        </div>
        <div class="bg-white rounded-2xl shadow-xl overflow-hidden border border-slate-100">
            <div class="bg-gradient-to-r from-{color}-600 to-{color}-800 text-white p-10 md:p-14">
                <span class="inline-block px-3 py-1 bg-white/20 rounded-full text-xs font-bold mb-4 backdrop-blur-sm tracking-wider">LECTURE NOTE</span>
                <h1 class="text-3xl md:text-4xl font-extrabold mb-2">{title}</h1>
                <p class="text-white/80 text-lg font-light">{subtitle}</p>
            </div>
            <div class="p-10 md:p-14 textbook-content">
                {content}
            </div>
            <div class="mt-12 pt-8 border-t border-slate-100 flex justify-center">
                <button onclick="history.back()" class="px-6 py-3 bg-slate-100 text-slate-700 rounded-xl font-bold hover:bg-slate-200 transition">
                    목록으로
                </button>
            </div>
        </div>
    </div>
</body>
</html>
"""

for item in textbooks:
    html = textbook_template.format(**item)
    with open(item['filename'], 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {item['filename']}")

# ==========================================
# 3. GENERATE LECTURE PAGES (Day 1 & 2)
# ==========================================
def get_lecture_header(title, subtitle, day_num):
    return f"""
    <header class="gradient-bg text-white py-12 px-8 relative overflow-hidden">
        <div class="absolute top-4 right-4 md:top-6 md:right-8 flex items-center gap-3 z-20">
            <span id="userEmailDisplay" class="text-sm text-white/90 font-medium hidden md:inline"></span>
            <a href="classroom_business.html"
                class="inline-flex items-center gap-2 px-4 py-2 bg-white/20 backdrop-blur-md text-white text-sm font-semibold rounded-full border border-white/30 hover:bg-white/30 transition-all">
                <i class="fas fa-arrow-left"></i>
                <span class="hidden sm:inline">강의실 홈으로</span>
            </a>
        </div>
        <div class="max-w-6xl mx-auto flex flex-col md:flex-row justify-between items-end relative z-10">
            <div class="space-y-2">
                <span class="text-6xl font-black opacity-20 block mb-[-10px]">Day {day_num}</span>
                <h1 class="text-3xl md:text-5xl font-extrabold tracking-tight">{title}</h1>
                <p class="text-xl opacity-90 font-light">{subtitle}</p>
            </div>
        </div>
    </header>
    """

def get_card(am_pm, icon, color, title, desc, tags, view_link):
    tag_html = ""
    for tag in tags:
        tag_html += f'<span class="bg-{color}-50 text-{color}-700 px-3 py-1 rounded-md text-xs font-semibold">{tag}</span>'
    listen_link = "https://al-class.vercel.app/ai-lecture-room/dist/index.html"
    return f"""
                <div class="bg-white p-8 rounded-3xl border border-slate-100 card-shadow hover:border-{color}-200 transition-all group relative overflow-hidden">
                    <div class="absolute top-0 right-0 bg-{color}-100 text-{color}-700 text-xs font-bold px-3 py-1 rounded-bl-xl">{am_pm}</div>
                    <div class="flex items-start gap-4">
                        <div class="bg-{color}-50 text-{color}-600 p-3 rounded-2xl group-hover:bg-{color}-600 group-hover:text-white transition-colors">
                            <i class="fas fa-{icon} text-2xl"></i>
                        </div>
                        <div class="flex-1">
                            <h3 class="text-xl font-bold mb-2">{title}</h3>
                            <p class="text-slate-500 text-sm mb-4 leading-relaxed">{desc}</p>
                            <div class="flex flex-wrap gap-2 mb-4">
                                {tag_html}
                            </div>
                            <div class="flex gap-2">
                                <a href="{view_link}" class="inline-flex items-center gap-2 px-4 py-2 bg-slate-100 text-slate-700 text-sm font-bold rounded-lg hover:bg-slate-200 transition-colors">
                                    <i class="fas fa-book-reader"></i> 강의 보기
                                </a>
                                <a href="{listen_link}" target="_blank" class="inline-flex items-center gap-2 px-4 py-2 bg-{color}-600 text-white text-sm font-bold rounded-lg hover:bg-{color}-700 transition-colors">
                                    <i class="fas fa-play-circle"></i> 강의 듣기
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
    """

base_html_start = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI 비즈니스 전략 - 강의 시청</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        body { font-family: 'Pretendard', sans-serif; scroll-behavior: smooth; }
        .gradient-bg { background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); } /* Dark Blue for Business */
        .card-shadow { box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05); }
    </style>
</head>
<body class="bg-slate-50 text-slate-900">
"""

base_html_end = """
    <script type="module">
        import { auth } from './js/firebase-config.js';
        import { onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
        onAuthStateChanged(auth, (user) => {
            if (!user) { alert("로그인이 필요합니다."); window.location.href='index.html'; }
            else { document.getElementById('userEmailDisplay').innerText = user.email + "님 환영합니다"; }
        });
    </script>
</body>
</html>
"""

# Day 1
d1 = base_html_start + get_lecture_header("AI 트렌드와 비즈니스 기회 (8시간)", "오전: 산업별 혁신 사례 / 오후: 신규 사업 모델 발굴", "01")
d1 += """<main class="max-w-6xl mx-auto px-6 py-12 space-y-12">
        <section class="space-y-6">
            <div class="inline-flex items-center gap-3 bg-blue-900 text-white px-5 py-2 rounded-full shadow-lg">
                <span class="font-bold text-xs tracking-widest">Day 1</span>
                <h2 class="text-lg font-bold">비즈니스 혁신과 기회</h2>
            </div>
            <div class="grid md:grid-cols-2 gap-6">"""
d1 += get_card("오전", "chart-line", "blue", "산업별 AI 혁신 사례 (Case Study)", "금융, 제조, 유통 등 주요 산업군의 성공적인 AI 도입 사례를 심층 분석합니다.", ["Finance", "Retail", "Mfg"], "textbook_business_cases.html")
d1 += get_card("오후", "lightbulb", "indigo", "AI 기반 신규 비즈니스 모델 발굴", "AI를 통해 기존 가치 사슬을 재정의하고 새로운 수익 모델을 설계합니다. (BM Canvas)", ["Biz Model", "Innovation"], "textbook_business_bm.html")
d1 += """</div></section></main>""" + base_html_end

with open("lecture_business_day1.html", "w", encoding="utf-8") as f:
    f.write(d1)
    print("Generated lecture_business_day1.html")

# Day 2
d2 = base_html_start + get_lecture_header("AI 도입 로드맵 수립 (8시간)", "오전: 도입 전략 및 기획 / 오후: 구축 및 평가 (8시간)", "02")
d2 += """<main class="max-w-6xl mx-auto px-6 py-12 space-y-12">
        <section class="space-y-6">
             <div class="inline-flex items-center gap-3 bg-teal-800 text-white px-5 py-2 rounded-full shadow-lg">
                <span class="font-bold text-xs tracking-widest">Day 2</span>
                <h2 class="text-lg font-bold">전략 수립 및 실행</h2>
            </div>
            <div class="grid md:grid-cols-2 gap-6">"""
d2 += get_card("오전", "clipboard-list", "green", "AI 성숙도 진단 및 목표 설정", "우리 조직의 AI 준비 수준을 진단하고 단계별 도입 목표를 수립합니다.", ["Strategy", "KPI"], "textbook_business_roadmap.html")
d2 += get_card("오전", "flask", "teal", "PoC(개념 증명) 기획서 작성", "실패하지 않는 AI 프로젝트를 위한 PoC 기획 및 검증 방법을 실습합니다.", ["PoC", "Planning"], "textbook_business_poc.html")
d2 += get_card("오후", "coins", "amber", "ROI 분석 및 투자 전략", "AI 도입에 따른 비용(TCO)과 정량적/정성적 기대 효과를 분석합니다.", ["ROI", "Cost"], "textbook_business_roi.html")
d2 += get_card("오후", "shield-alt", "red", "AI 리스크 관리 및 거버넌스", "환각, 편향성, 보안 등 AI 도입 시 발생할 수 있는 리스크 대응 방안을 마련합니다.", ["Risk", "Governance"], "textbook_business_risk.html")
d2 += """</div></section></main>""" + base_html_end

with open("lecture_business_day2.html", "w", encoding="utf-8") as f:
    f.write(d2)
    print("Generated lecture_business_day2.html")
