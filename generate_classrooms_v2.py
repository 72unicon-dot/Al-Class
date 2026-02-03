import os

# ==========================================
# 1. Full Course Data (Synced with injection script)
# ==========================================
courses_data = {
    "intro_ethics.html": {
        "output": "classroom_ethics.html",
        "title": "AI 윤리 및 규제",
        "curriculum": [
            {"title": "Day 1: AI 윤리와 규제 트렌드", "desc": "국내외(EU AI Act) 법적 규제와 기업 리스크 분석", "details": ["생성형 AI의 저작권 이슈 사례", "기업 데이터 유출 사고 유형", "개인정보보호법과 AI 컴플라이언스"]},
            {"title": "Day 2: 실무 가이드라인 수립", "desc": "우리 회사에 맞는 AI 사용 정책 및 보안 수칙 제정", "details": ["프롬프트 입력 시 보안 주의사항", "AI 산출물의 사용 권한 및 책임", "사내 AI 윤리 강령 작성 실습"]}
        ]
    },
    "intro_basics.html": {
        "output": "classroom_basics.html",
        "title": "AI 기초 입문",
        "curriculum": [
            {"title": "Day 1: 생성형 AI와 친해지기", "desc": "LLM의 원리 이해와 3대 AI(ChatGPT, Gemini, Claude) 비교", "details": ["할루시네이션(환각)의 원리와 대처법", "나에게 맞는 최적의 AI 모델 찾기", "모바일 앱 설치 및 기본 세팅"]},
            {"title": "Day 2: 프롬프트 엔지니어링 기초", "desc": "원하는 결과를 한 번에 얻는 질문의 기술", "details": ["명확한 지시어(Persona, Context) 작성법", "자료 요약 및 이메일 초안 작성 실습", "엑셀 수식 및 번역 업무 자동화"]}
        ]
    },
    "intro_business.html": {
        "output": "classroom_business.html",
        "title": "AI 비즈니스 활용",
        "curriculum": [
            {"title": "Day 1: 문서 자동화의 기적", "desc": "회의록, 보고서, 제안서 작성 시간 90% 단축하기", "details": ["음성 녹음(Clova Note) 회의록 자동 변환", "Notion AI로 프로젝트 일정 관리하기", "ChatGPT로 시장 조사 보고서 초안 쓰기"]},
            {"title": "Day 2: 비즈니스 시각화 & 발표", "desc": "설득력 있는 프레젠테이션 자료 자동 생성", "details": ["Gamma로 텍스트를 PPT로 1분 만에 변환", "Midjourney로 저작권 걱정 없는 이미지 생성", "DeepL로 해외 바이어 이메일 및 제안서 번역"]}
        ]
    },
    "expert_advanced.html": {
        "output": "classroom_advanced.html",
        "title": "AI 전문가 심화",
        "curriculum": [
            {"title": "Phase 1: LLM 심층 이해 (Day 1-3)", "desc": "Transformer 아키텍처와 오픈소스 LLM 활용", "details": ["Transformer 구조와 Attention 메커니즘", "Llama 3, Mistral 등 로컬 LLM 구동", "Prompt Tuning vs Fine-tuning 비교"]},
            {"title": "Phase 2: RAG 시스템 구축 (Day 4-6)", "desc": "사내 지식 기반의 정확한 답변 시스템 구현", "details": ["텍스트 임베딩과 벡터 데이터베이스 이해", "LangChain을 이용한 문서 검색 파이프라인", "PDF/Web 데이터 연동 챗봇 실습"]},
            {"title": "Phase 3: Fine-tuning & Agent (Day 7-10)", "desc": "도메인 특화 모델 학습과 자율 에이전트 개발", "details": ["LoRA를 활용한 효율적인 파인튜닝 실습", "자율 에이전트(Agent) 설계 및 툴 사용 권한 부여", "기업용 AI 솔루션 아키텍처 설계"]}
        ]
    },
    "special_marketing.html": {
        "output": "classroom_marketing.html",
        "title": "AI 마케팅 전문가",
        "curriculum": [
            {"title": "Day 1: 마케팅 페르소나 & 전략", "desc": "ChatGPT로 고객 페르소나 정의 및 타겟 분석", "details": ["경쟁사 분석 및 SWOT 분석 자동화", "고객 페르소나 시뮬레이션 대화", "마케팅 캠페인 슬로건 및 메시지 도출"]},
            {"title": "Day 2-3: 콘텐츠 자동화 파이프라인", "desc": "블로그, SNS, 상세페이지 콘텐츠 대량 생산", "details": ["SEO 최적화된 블로그 포스팅 10개 1분 생성", "SNS 채널별(인스타, 링크드인) 맞춤 톤앤매너 변환", "상세페이지 세일즈 카피라이팅 자동화"]},
            {"title": "Day 4-5: 퍼포먼스 마케팅 & 광고 소재", "desc": "고효율 광고 소재 생성 및 데이터 분석", "details": ["클릭을 부르는 광고 배너 대량 제작(Midjourney)", "숏폼 광고 스크립트 및 영상 기획", "광고 성과 데이터 분석 및 리포팅 자동화"]}
        ]
    },
    "special_manufacturing.html": {
        "output": "classroom_manufacturing.html",
        "title": "AI 제조 전문가",
        "curriculum": [
            {"title": "Day 1: 제조 데이터와 AI", "desc": "스마트 팩토리 데이터 수집 및 전처리", "details": ["MES/ERP 데이터의 이해와 AI 적용 분야", "시계열 데이터(센서, 진동) 전처리 실습", "Python Pandas를 활용한 기초 데이터 분석"]},
            {"title": "Day 2-3: 예지 보전 모델링", "desc": "설비 고장 예측을 위한 이상 탐지 모델 구현", "details": ["정상 vs 비정상 데이터 분류 (Classification)", "오토인코더(Autoencoder)기반 이상 탐지", "설비 잔여 수명(RUL) 예측 기초"]},
            {"title": "Day 4-5: 비전 검사 & 공정 최적화", "desc": "이미지 기반 불량 검출 및 공정 파라미터 최적화", "details": ["YOLO 모델을 활용한 제품 결함 탐지 실습", "공정 변수 최적화를 위한 강화학습 개요", "현장 적용을 위한 AI 모델 배포 전략"]}
        ]
    },
    "special_data.html": {
        "output": "classroom_data.html",
        "title": "AI 데이터 분석가",
        "curriculum": [
            {"title": "Day 1: 데이터 리터러시 & 탐색", "desc": "코딩 없이 대화로 하는 탐색적 데이터 분석(EDA)", "details": ["ChatGPT Advanced Data Analysis 모드 활용", "데이터 구조 파악 및 결측치 처리 자동화", "기초 통계량 확인 및 데이터 요약"]},
            {"title": "Day 2-3: 인사이트 도출 & 시각화", "desc": "복잡한 데이터를 직관적인 차트로 변환", "details": ["상관관계 분석 및 핵심 지표 시각화", "고급 차트(히트맵, 산점도) 자동 생성 프롬프트", "경영진 보고용 대시보드 기획"]},
            {"title": "Day 4-5: 머신러닝 예측 모델링", "desc": "클릭 몇 번으로 만드는 수요 예측 및 분류 모델", "details": ["매출/재고 시계열 예측 모델링", "고객 이탈 예측 분류 모델 실습", "분석 결과 보고서 자동 생성 및 스토리텔링"]}
        ]
    },
    "special_video.html": {
        "output": "classroom_video.html",
        "title": "AI 영상 크리에이터",
        "curriculum": [
            {"title": "Day 1: 영상 기획 & 스크립트", "desc": "조회수를 부르는 킬러 콘텐츠 기획", "details": ["유튜브 트렌드 분석 및 벤치마킹 자동화", "ChatGPT로 숏폼/롱폼 대본 10초 만에 작성", "스토리보드 및 장면 묘사 프롬프트 작성"]},
            {"title": "Day 2-3: AI 영상 소스 생성", "desc": "촬영 없이 고퀄리티 영상 및 이미지 제작", "details": ["Midjourney로 일관된 캐릭터/배경 생성", "Runway Gen-2/3로 정지 이미지를 영상화", "Camera Motion 컨트롤 및 스타일 변환"]},
            {"title": "Day 4-5: 편집 & 사운드 & 발행", "desc": "AI 성우 더빙과 자동 자막, 컷 편집 완성", "details": ["ElevenLabs로 감정을 담은 AI 내레이션 생성", "CapCut/Vrew를 활용한 자동 컷 편집 및 자막", "썸네일 제작 및 유튜브 SEO 업로드 전략"]}
        ]
    },
    "management_leadership.html": {
        "output": "classroom_leadership.html",
        "title": "AI시대의 리더십",
        "curriculum": [
            {"title": "Day 1 (오전): AI 패러다임 시프트", "desc": "경영진이 반드시 알아야 할 AI 기술의 본질과 미래", "details": ["Gen AI가 바꿀 산업 지형도와 비즈니스 모델", "Global 기업들의 성공/실패 사례 분석", "우리 기업의 AI 성숙도 진단"]},
            {"title": "Day 1 (오후): AI 도입 전략 & 의사결정", "desc": "실질적인 성과를 내는 도입 로드맵 수립", "details": ["Top-down vs Bottom-up 도입 전략", "AI 도입 시 고려해야 할 비용(Capex/Opex)과 ROI", "조직 변화 관리(Change Management)와 리더십"]}
        ]
    },
    "strategy_consultant.html": {
        "output": "classroom_consultant.html",
        "title": "AI 비즈니스 컨설턴트",
        "curriculum": [
            {"title": "Week 1: AI 기술 및 생태계 이해", "desc": "컨설턴트를 위한 심층 기술 지식", "details": ["LLM, sLLM, RAG, Agent 등 핵심 기술 심화", "AI Value Chain 및 주요 플레이어 분석", "산업별(금융, 제조, 유통) AI 유스케이스 스터디"]},
            {"title": "Week 2: 기업 진단 방법론", "desc": "AS-IS 분석 및 Pain Point 발굴", "details": ["AI 준비도 진단 툴킷 활용 실습", "데이터 인프라 및 거버넌스 진단", "임직원 인터뷰 및 프로세스 마이닝 기법"]},
            {"title": "Week 3: AI 전략 수립 & 로드맵", "desc": "TO-BE 모델 설계 및 실행 계획", "details": ["고객 여정 지도(CJM) 기반 AI 서비스 기획", "PoC 대상 과제 우선순위 도출 매트릭스", "단계별 도입 로드맵 및 예산 산정"]},
            {"title": "Week 4: 제안 및 프로젝트 관리", "desc": "설득력 있는 제안서 작성 및 PM 역량", "details": ["AI 도입 ROI 시뮬레이션 및 정량적 기대효과 산출", "발주처를 설득하는 컨설팅 제안서 작성 실습", "AI 프로젝트 리스크 관리 및 품질 보증 방안"]}
        ]
    },
    "master_app_creator.html": {
        "output": "classroom_app_creator.html",
        "title": "비즈니스 앱 크리에이터",
        "curriculum": [
            {"title": "Month 1: 풀스택 AI 개발 기초", "desc": "Python, JS, DB 및 기본기 다지기", "details": ["Python & JavaScript 핵심 문법 심화", "FastAPI 백엔드 & React 프론트엔드 기초", "SQL vs NoSQL 데이터베이스 설계 및 구축"]},
            {"title": "Month 2: LLM 애플리케이션 심화", "desc": "LangChain, RAG, Agent 개발", "details": ["LangChain LCEL 문법 및 Chain 설계", "Pinecone/ChromaDB 활용 RAG 파이프라인 구축", "멀티 모달 기능(이미지/음성) 연동 및 메모리 구현"]},
            {"title": "Month 3: 엔터프라이즈 배포 & 운영", "desc": "실서비스 수준의 아키텍처 및 DevOps", "details": ["Docker 컨테이너화 및 CI/CD 파이프라인", "AWS/GCP 클라우드 인프라 구축 및 오토스케일링", "시스템 모니터링, 로깅, 보안 가이드라인"]},
            {"title": "Final: 캡스톤 프로젝트", "desc": "나만의 상용화 가능한 SaaS 런칭", "details": ["아이디어 기획부터 MVP 개발, 배포까지 전 과정 수행", "실제 사용자 피드백 반영 및 기능 고도화", "투자 유치를 위한 IR 피칭 덱 작성 및 발표"]}
        ]
    }
}

# ==========================================
# 2. Template Logic
# ==========================================

def generate_card(index, module):
    # Colors for rotation
    colors = ["indigo", "emerald", "blue", "purple", "rose", "amber", "teal", "cyan"]
    color = colors[index % len(colors)]
    
    details_html = ""
    for detail in module['details']:
        details_html += f"""
                                    <li class="flex items-start gap-2"><i
                                            class="fas fa-check-circle text-{color}-600 mt-1"></i><span>{detail}</span></li>"""

    # Always link to day01_lecture.html
    link = "day01_lecture.html"

    # Use a number formatted like 01, 02
    day_num = str(index + 1).zfill(2)
    
    return f"""
                    <!-- Module {index+1} -->
                    <div class="day-card bg-white rounded-3xl shadow-xl overflow-hidden border border-gray-100 ring-4 ring-transparent hover:ring-{color}-50 transition-all">
                        <div class="bg-gradient-to-r from-{color}-600 to-{color}-800 text-white px-8 py-6">
                            <div class="flex items-center justify-between flex-wrap gap-4">
                                <div class="flex items-center gap-4">
                                    <span class="text-4xl font-black opacity-30">{day_num}</span>
                                    <div>
                                        <h3 class="text-2xl font-bold">{module['title']}</h3>
                                        <p class="opacity-80">{module['desc']}</p>
                                    </div>
                                </div>
                                <div class="flex items-center gap-4 flex-wrap">
                                    <a href="{link}"
                                        class="px-6 py-2.5 bg-white text-{color}-700 rounded-full text-sm font-bold hover:bg-{color}-50 transition-all shadow-lg flex items-center gap-2 transform hover:-translate-y-0.5">
                                        <i class="fas fa-play"></i> 학습하기
                                    </a>
                                </div>
                            </div>
                        </div>
                        <div class="p-8">
                            <div class="bg-{color}-50 rounded-2xl p-6">
                                <ul class="space-y-3 text-gray-700">
                                    {details_html}
                                </ul>
                            </div>
                        </div>
                    </div>"""

# Load Template
with open("classroom.html", "r", encoding="utf-8") as f:
    template_content = f.read()

# Find Injection Points
start_marker = '<div class="space-y-8 max-w-5xl mx-auto">'
# Identify end of the container
section_curriculum = template_content.find('id="curriculum"')
section_end = template_content.find('</section>', section_curriculum)
container_end = template_content.rfind('</div>', 0, section_end) # Closing of container
grid_end = template_content.rfind('</div>', 0, container_end) # Closing of grid (max-w-5xl) - wait

# Let's split strictly by the start marker
parts = template_content.split(start_marker)
header_part = parts[0] + start_marker

# The footer part needs to be extracted carefully.
# We skip everything after start_marker until the "My Curriculum" section ends.
# The structure is: <section> ... <div space-y-8 ...> [CARDS] </div> ... </section>
# So we need to look for the matching </div> for space-y-8.
# Since it is hard to parse HTML with regex, let's assume the template is standard.
# We will use the footer part from:
footer_start_idx = template_content.find('            </div>\n        </div>\n    </section>', section_curriculum)
# Just hardcode the footer part if needed or use previous method
footer_part = """
            </div>
        </div>
    </section>
    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-gray-200 py-8 mt-12">
        <div class="container mx-auto px-6 text-center text-gray-500 text-sm">
            &copy; 2026 AI Class Management System. All rights reserved.
        </div>
    </footer>

    <!-- Firebase Scripts -->
    <script type="module">
        import { auth } from './js/firebase-config.js';
        import { onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
        import { displayTotalProgress, displayNextLesson } from './js/progress-ui.js';

        onAuthStateChanged(auth, async (user) => {
            if (!user) {
                alert("로그인이 필요합니다.");
                window.location.href = 'index.html';
            } else {
                const emailDisplay = document.getElementById('userEmailDisplay');
                if (emailDisplay) emailDisplay.innerText = user.email + "님 환영합니다";

                // 진도 추적 UI 초기화
                // Course ID mapping logic could be added here later
            }
        });

        window.logout = () => {
            if (confirm('로그아웃 하시겠습니까?')) {
                signOut(auth).then(() => window.location.href = 'index.html');
            }
        }
    </script>

</body>

</html>
"""

# Generate
for key, data in courses_data.items():
    print(f"Refining {data['output']}...")
    
    cards_html = ""
    for idx, item in enumerate(data['curriculum']):
        cards_html += generate_card(idx, item)
    
    # Replace Header Title
    current_header = header_part.replace("AI 실무 마스터 클래스", data['title'])
    
    # Also update "My Curriculum" subtitle if needed
    # (It says "나의 AI 강의실" in template, which is generic enough)
    
    full_html = current_header + cards_html + footer_part
    
    with open(data['output'], "w", encoding="utf-8") as f:
        f.write(full_html)

print("All classrooms regenerated with full curriculum details.")
