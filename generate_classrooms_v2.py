import os
import re

# Configuration for 11 Courses
# Format: Filename -> { OutputFilename, Title, CurriculumData }
course_configs = {
    "intro_ethics.html": {
        "output": "classroom_ethics.html",
        "title": "AI 윤리 및 규제",
        "curriculum": [
            {"title": "Class 1: AI 윤리와 규제 트렌드", "desc": "국내외(EU AI Act) 법적 규제와 기업 리스크 분석", "details": ["생성형 AI의 저작권 이슈 사례", "기업 데이터 유출 사고 유형", "개인정보보호법과 AI 컴플라이언스"]},
            {"title": "Class 2: 실무 가이드라인 수립", "desc": "우리 회사에 맞는 AI 사용 정책 및 보안 수칙 제정", "details": ["프롬프트 입력 시 보안 주의사항", "AI 산출물의 사용 권한 및 책임", "사내 AI 윤리 강령 작성 실습"]}
        ]
    },
    "intro_basics.html": {
        "output": "classroom_basics.html",
        "title": "AI 기초 및 활용",
        "curriculum": [
            {"title": "Class 1: 생성형 AI 원리 이해 (오전)", "desc": "LLM의 작동 방식과 프롬프트 엔지니어링 기초 (4시간)", "details": ["LLM과 Transformer 구조", "Token과 Context Window 이해", "Zero-shot vs Few-shot Prompting"]},
            {"title": "Class 2: 업무 생산성 도구 (오후)", "desc": "ChatGPT, Gemini, Claude 등 주요 툴 활용법 (4시간)", "details": ["이메일 및 보고서 자동 작성", "데이터 분석 및 시각화 실습", "회의록 요약 및 할 일 추출"]}
        ]
    },
    "intro_business.html": {
        "output": "classroom_business.html",
        "title": "AI 비즈니스 전략",
        "curriculum": [
            {"title": "Day 1: AI 트렌드와 비즈니스 기회 (8시간)", "desc": "오전: 산업별 혁신 사례 / 오후: 신규 사업 모델 발굴", "details": ["(오전) 금융/제조/유통 분야 AI 도입 성공 사례 분석", "(오전) 생성형 AI 생태계와 기술 트렌드", "(오후) AI 기반 신규 비즈니스 모델 캔버스 작성", "(오후) 경쟁사 AI 전략 분석 및 차별화"]},
            {"title": "Day 2: AI 도입 로드맵 수립 (8시간)", "desc": "오전: 도입 전략 및 기획 / 오후: 구축 및 평가", "details": ["(오전) 우리 기업 AI 성숙도 진단 및 목표 설정", "(오전) PoC(개념 증명) 기획서 작성 실습", "(오후) ROI 분석 및 예산/인력 계획 수립", "(오후) AI 프로젝트 리스크 관리 및 거버넌스"]}
        ]
    },
    "expert_advanced.html": {
        "output": "classroom_advanced.html",
        "title": "AI 심화 개발",
        "curriculum": [
            {"title": "Day 1: RAG 파이프라인 구축", "desc": "LangChain을 활용한 문서 기반 질의응답 시스템", "details": ["Vector DB와 임베딩 이해", "RAG 아키텍처 설계", "Hallucination 제어 기법"]},
            {"title": "Day 2: LLM 파인튜닝 실습", "desc": "오픈소스 모델(Llama 3 등) 미세 조정하기", "details": ["데이터셋 준비 및 전처리", "LoRA/QLoRA 효율적 튜닝", "모델 평가 및 배포"]}
        ]
    },
    "special_marketing.html": {
        "output": "classroom_marketing.html",
        "title": "AI 마케팅 특화",
        "curriculum": [
            {"title": "Day 1: AI 카피라이팅 & 콘텐츠", "desc": "고객 페르소나 맞춤형 광고 문구 및 블로그 생성", "details": ["브랜드 톤앤매너 학습시키기", "SEO 최적화 콘텐츠 제작", "소셜 미디어 자동화"]},
            {"title": "Day 2: 마케팅 데이터 분석", "desc": "고객 반응 데이터 분석 및 예측", "details": ["캠페인 성과 예측 모델링", "고객 세그먼트 자동화", "개인화 마케팅 전략"]}
        ]
    },
    "special_manufacturing.html": {
        "output": "classroom_manufacturing.html",
        "title": "AI 제조/생산 특화",
        "curriculum": [
            {"title": "Day 1: 스마트 팩토리와 AI", "desc": "예지 보전 및 품질 검사 자동화", "details": ["IoT 센서 데이터 수집 및 분석", "Computer Vision 품질 관리", "설비 고장 예측 시뮬레이션"]},
            {"title": "Day 2: 공급망 최적화", "desc": "수요 예측 및 재고 관리 자동화", "details": ["시계열 데이터 기반 수요 예측", "물류 경로 최적화 알고리즘", "재고 비용 절감 전략"]}
        ]
    },
    "special_data.html": {
        "output": "classroom_data.html",
        "title": "AI 데이터 분석 특화",
        "curriculum": [
            {"title": "Day 1: Pandas AI & Code Interpreter", "desc": "대화형 데이터 분석의 세계", "details": ["자연어로 SQL 쿼리 생성", "자동 데이터 시각화 및 리포팅", "데이터 전처리 자동화"]},
            {"title": "Day 2: 머신러닝 워크플로우 자동화", "desc": "AutoML을 활용한 모델 개발", "details": ["특성 공학(Feature Engineering) 자동화", "최적 모델 탐색 및 하이퍼파라미터 튜닝", "모델 설명력(XAI) 확보"]}
        ]
    },
    "special_video.html": {
        "output": "classroom_video.html",
        "title": "AI 영상 제작 특화",
        "curriculum": [
            {"title": "Day 1: AI 영상 생성 도구 활용", "desc": "Sora, Runway, Pika 등 최신 툴 마스터", "details": ["Text-to-Video 프롬프트 기법", "이미지로 영상 애니메이션 만들기", "일관성 있는 캐릭터 영상 제작"]},
            {"title": "Day 2: 영상 편집 및 후가공", "desc": "AI 기반 컷 편집 및 특수 효과", "details": ["음성 합성 및 립싱크(Lip-sync)", "자동 자막 및 번역", "AI 배경 음악 및 효과음 생성"]}
        ]
    },
    "management_leadership.html": {
        "output": "classroom_leadership.html",
        "title": "AI 리더십",
        "curriculum": [
            {"title": "Day 1: AI 시대의 조직 관리", "desc": "AI와 협업하는 조직 문화 만들기", "details": ["AI 리터러시 교육 전략", "변화 관리 및 저항 극복", "AI 윤리 및 거버넌스 수립"]},
            {"title": "Day 2: 의사결정 지원 시스템", "desc": "데이터 기반의 합리적 경영 의사결정", "details": ["경영 대시보드 및 지표 관리", "시나리오 플래닝 시뮬레이션", "리스크 관리 및 예측"]}
        ]
    },
    "strategy_consultant.html": {
        "output": "classroom_consultant.html",
        "title": "AI 컨설턴트 양성",
        "curriculum": [
            {"title": "Day 1: AI 컨설팅 방법론", "desc": "기업의 AI 도입 니즈 발굴 및 솔루션 제안", "details": ["DT(Digital Transformation) 진단 프레임워크", "As-Is vs To-Be 분석", "RFP 작성 및 제안서 작성법"]},
            {"title": "Day 2: 프로젝트 관리 및 커뮤니케이션", "desc": "성공적인 AI 프로젝트 리딩", "details": ["Agile 방법론 적용", "이해관계자 소통 전략", "프로젝트 리스크 관리"]}
        ]
    },
    "master_app_creator.html": {
        "output": "classroom_app_creator.html",
        "title": "나만의 앱 만들기",
        "curriculum": [
            {"title": "Day 1: 노코드/로우코드 툴 활용", "desc": "코딩 없이 앱 프로토타입 만들기", "details": ["Bubble, FlutterFlow 기초", "UI/UX 디자인 원칙", "데이터베이스 연동 실습"]},
            {"title": "Day 2: 앱 배포 및 수익화", "desc": "실제 스토어 출시 및 운영", "details": ["API 연동 및 외부 서비스 활용", "앱스토어 등록 절차", "사용자 분석 및 업데이트 전략"]}
        ]
    }
}

# Template HTML used for generation
template = """<!DOCTYPE html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{COURSE_TITLE} - 나의 강의실</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        body {{
            font-family: 'Pretendard', sans-serif;
            background-color: #f8fafc;
        }}

        .gradient-text {{
            background: linear-gradient(135deg, #2563eb 0%, #4f46e5 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
    </style>
</head>

<body class="bg-slate-50">

    <!-- Navbar -->
    <header class="bg-white/80 backdrop-blur-md border-b border-slate-100 sticky top-0 z-50">
        <nav class="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <a href="index.html" class="text-slate-400 hover:text-indigo-600 transition-colors mr-2" title="메인으로 나가기">
                    <i class="fas fa-home text-xl"></i>
                </a>
                <div class="w-10 h-10 bg-indigo-600 rounded-xl flex items-center justify-center shadow-lg shadow-indigo-200">
                    <i class="fas fa-graduation-cap text-white text-lg"></i>
                </div>
                <span class="font-bold text-xl tracking-tight text-slate-800">Al Master Class <span
                        class="text-slate-400 font-normal text-sm ml-1">나의 강의실</span></span>
            </div>
            
            <div class="flex items-center gap-4">
                <div class="hidden md:flex items-center bg-slate-100 rounded-full px-4 py-1.5 border border-slate-200 focus-within:ring-2 focus-within:ring-indigo-100 transition-all">
                    <i class="fas fa-search text-slate-400 text-sm"></i>
                    <input type="text" placeholder="검색"
                        class="bg-transparent border-none focus:outline-none text-sm ml-2 w-48 text-slate-600 placeholder:text-slate-400">
                </div>
                <div class="h-8 w-[1px] bg-slate-200 mx-2"></div>
                <div class="flex items-center gap-3">
                    <span id="userEmailDisplay" class="text-sm font-medium text-slate-600"></span>
                    <button id="logoutBtn"
                        class="flex items-center gap-2 bg-slate-100 hover:bg-slate-200 text-slate-600 px-3 py-1.5 rounded-lg text-xs font-bold transition-colors">
                        <i class="fas fa-sign-out-alt"></i> 로그아웃
                    </button>
                </div>
            </div>
        </nav>
    </header>

    <main class="max-w-4xl mx-auto px-6 py-12">
        <div class="text-center mb-12">
            <span class="inline-block px-4 py-1.5 bg-indigo-50 text-indigo-600 rounded-full text-xs font-bold mb-4 tracking-wide border border-indigo-100">MY CURRICULUM</span>
            <h1 class="text-3xl md:text-4xl font-black mb-3 text-slate-900">{COURSE_TITLE}</h1>
            <p class="text-slate-500 font-medium">진도율에 맞춰 학습을 진행해 주세요</p>
        </div>

        <div class="space-y-6">
            {CURRICULUM_CARDS}
        </div>
    </main>

    <script type="module">
        import {{ auth }} from './js/firebase-config.js';
        import {{ onAuthStateChanged, signOut }} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

        onAuthStateChanged(auth, (user) => {{
            if (user) {{
                const emailDisplay = document.getElementById('userEmailDisplay');
                if (emailDisplay) emailDisplay.innerText = user.email + "님 환영합니다";
            }} else {{
                // Force redirect if not logged in
                window.location.href = 'index.html';
            }}
        }});

        const logoutBtn = document.getElementById('logoutBtn');
        if (logoutBtn) {{
            logoutBtn.addEventListener('click', () => {{
                signOut(auth).then(() => {{
                    window.location.href = 'index.html';
                }}).catch((error) => {{
                    console.error("Logout error:", error);
                }});
            }});
        }}
    </script>
</body>
</html>
"""

def get_curriculum_card(index, module, course_output_filename):
    colors = ["indigo", "emerald", "blue", "purple"]
    color = colors[index % len(colors)]
    
    details_html = ""
    for detail in module['details']:
        details_html += f"""
                                    <li class="flex items-start gap-2"><i
                                            class="fas fa-check-circle text-{color}-600 mt-1"></i><span>{detail}</span></li>"""

    # Link Logic
    # Default: day01_lecture.html
    # Ethics Special: lecture_ethics_class1.html / lecture_ethics_class2.html
    link = "day01_lecture.html" # fallback

    if "classroom_ethics.html" in course_output_filename:
        # Ethics Special Logic
        if index == 0:
            link = "lecture_ethics_class1.html"
        elif index == 1:
            link = "lecture_ethics_class2.html"
    elif "classroom_basics.html" in course_output_filename:
        # Basics Special Logic
        if index == 0:
            link = "lecture_basics_class1.html"
        elif index == 1:
            link = "lecture_basics_class2.html"
    elif "classroom_business.html" in course_output_filename:
        # Business Special Logic
        if index == 0:
            link = "lecture_business_day1.html"
        elif index == 1:
            link = "lecture_business_day2.html"
    else:
        # Generic Logic for others
        day_num = str(index + 1).zfill(2)
        # Future: If we have specific files for other courses, map them here.
        # For now, all point to day01_lecture.html as placeholder
        link = "day01_lecture.html"
    
    return f"""
            <!-- Module {index+1} -->
            <div class="bg-white rounded-3xl p-1 shadow-xl shadow-slate-200/50 border border-white hover:border-{color}-100 transition-all duration-300 group">
                <div class="bg-gradient-to-r from-{color}-600 to-{color}-800 rounded-[20px] p-6 md:p-8 text-white relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-64 h-64 bg-white opacity-5 rounded-full blur-3xl -mr-16 -mt-16 pointer-events-none"></div>
                    
                    <div class="flex flex-col md:flex-row md:items-center justify-between gap-6 relative z-10">
                        <div>
                            <span class="text-{color}-200 font-bold text-5xl md:text-6xl opacity-20 absolute -left-4 -top-4 select-none">{str(index+1).zfill(2)}</span>
                            <h2 class="text-xl md:text-2xl font-bold mb-2 pl-2 md:pl-0 relative">{module['title']}</h2>
                            <p class="text-{color}-100 text-sm md:text-base pl-2 md:pl-0 opacity-90">{module['desc']}</p>
                        </div>
                        <a href="{link}" class="bg-white text-{color}-700 px-6 py-2.5 rounded-full text-sm font-bold shadow-lg hover:shadow-xl hover:scale-105 active:scale-95 transition-all flex items-center gap-2 whitespace-nowrap self-start md:self-auto">
                            <i class="fas fa-play"></i> 학습하기
                        </a>
                    </div>
                </div>
                
                <div class="p-6 md:p-8 bg-indigo-50/30 rounded-b-[20px]">
                    <ul class="space-y-3 text-sm text-slate-600 font-medium">
                        {details_html}
                    </ul>
                </div>
            </div>
    """

def generate_classroom_html(config):
    cards_html = ""
    for i, module in enumerate(config['curriculum']):
        cards_html += get_curriculum_card(i, module, config['output'])
    
    html = template.replace("{COURSE_TITLE}", config['title']) \
                   .replace("{CURRICULUM_CARDS}", cards_html)
    
    with open(config['output'], 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Regenerated {config['output']} with Home button & Smart Links.")


# Execution
print("Starting regeneration of classroom files...")
for key, config in course_configs.items():
    generate_classroom_html(config)
print("All classrooms regenerated.")
