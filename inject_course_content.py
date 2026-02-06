import os
import re

# ==========================================
# 1. Course Data Definition
# ==========================================
courses_data = {
    # ------------------------------------------------------------------
    # 1. AI Ethics (1 Day)
    # ------------------------------------------------------------------
    "intro_ethics.html": {
        "stats": { "days": "1", "tools": "3", "projects": "5", "app": "0" },
        "tools": [
            {"name": "Copykiller", "icon": "fa-search", "desc": "표절/유사도 검사", "color": "blue"},
            {"name": "GPTZero", "icon": "fa-user-secret", "desc": "AI 작성 탐지", "color": "gray"},
            {"name": "Presidio", "icon": "fa-user-shield", "desc": "PII 비식별화", "color": "emerald"},
            {"name": "Fairlearn", "icon": "fa-balance-scale", "desc": "편향성 분석", "color": "purple"}
        ],
        "curriculum": [
            {"title": "오전: AI 윤리와 규제 트렌드", "desc": "국내외(EU AI Act) 법적 규제와 기업 리스크 분석", "details": ["생성형 AI의 저작권 이슈 사례", "기업 데이터 유출 사고 유형", "개인정보보호법과 AI 컴플라이언스"]},
            {"title": "오후: 실무 가이드라인 수립", "desc": "우리 회사에 맞는 AI 사용 정책 및 보안 수칙 제정", "details": ["프롬프트 입력 시 보안 주의사항", "AI 산출물의 사용 권한 및 책임", "사내 AI 윤리 강령 작성 실습"]}
        ]
    },

    # ------------------------------------------------------------------
    # 2. AI Basics (1 Day)
    # ------------------------------------------------------------------
    "intro_basics.html": {
        "stats": { "days": "1", "tools": "4", "projects": "10", "app": "0" },
        "tools": [
            {"name": "ChatGPT", "icon": "fa-comments", "desc": "OpenAI LLM", "color": "emerald"},
            {"name": "Gemini", "icon": "fa-star", "desc": "Google Multimodal", "color": "blue"},
            {"name": "Claude", "icon": "fa-brain", "desc": "Anthropic LLM", "color": "orange"},
            {"name": "Perplexity", "icon": "fa-search", "desc": "AI 검색 엔진", "color": "cyan"}
        ],
        "curriculum": [
            {"title": "오전: 생성형 AI와 친해지기", "desc": "LLM의 원리 이해와 3대 AI(ChatGPT, Gemini, Claude) 비교", "details": ["할루시네이션(환각)의 원리와 대처법", "나에게 맞는 최적의 AI 모델 찾기", "모바일 앱 설치 및 기본 세팅"]},
            {"title": "오후: 프롬프트 엔지니어링 기초", "desc": "원하는 결과를 한 번에 얻는 질문의 기술", "details": ["명확한 지시어(Persona, Context) 작성법", "자료 요약 및 이메일 초안 작성 실습", "엑셀 수식 및 번역 업무 자동화"]}
        ]
    },

    # ------------------------------------------------------------------
    # 3. AI Business (2 Days)
    # ------------------------------------------------------------------
    "intro_business.html": {
        "stats": { "days": "2", "tools": "6", "projects": "8", "app": "0" },
        "tools": [
            {"name": "ChatGPT", "icon": "fa-comments", "desc": "문서 작성", "color": "emerald"},
            {"name": "Gamma", "icon": "fa-layer-group", "desc": "PPT 자동 생성", "color": "purple"},
            {"name": "Notion AI", "icon": "fa-book", "desc": "지식 관리", "color": "gray"},
            {"name": "DeepL", "icon": "fa-language", "desc": "비즈니스 번역", "color": "blue"},
            {"name": "Midjourney", "icon": "fa-image", "desc": "이미지 소스 생성", "color": "pink"}
        ],
        "curriculum": [
            {"title": "Day 1: 문서 자동화의 기적", "desc": "회의록, 보고서, 제안서 작성 시간 90% 단축하기", "details": ["음성 녹음(Clova Note) 회의록 자동 변환", "Notion AI로 프로젝트 일정 관리하기", "ChatGPT로 시장 조사 보고서 초안 쓰기"]},
            {"title": "Day 2: 비즈니스 시각화 & 발표", "desc": "설득력 있는 프레젠테이션 자료 자동 생성", "details": ["Gamma로 텍스트를 PPT로 1분 만에 변환", "Midjourney로 저작권 걱정 없는 이미지 생성", "DeepL로 해외 바이어 이메일 및 제안서 번역"]}
        ]
    },

    # ------------------------------------------------------------------
    # 4. AI Master Class (8 Days) - EXISTING (Benchmark)
    # ------------------------------------------------------------------
    # Use existing master_index.html data, but we can verify/update stats if needed.
    # We will SKIP logic for this file or just ensure stats match.
    "master_index.html": {
         "stats": { "days": "8", "tools": "10", "projects": "20+", "app": "1" },
         # Tools and Curriculum are mostly there or handled differently (since this is the template)
         # We will inject the "Detailed Curriculum" section into it as well if missing.
         "tools": [], # Already has tools
         "curriculum": [
             {"title": "Day 1-2: AI 리터러시 & 프롬프트", "desc": "10대 AI 도구 파악 및 상황별 텍스트 출력 최적화", "details": ["LLM 원리 및 3대장 비교", "프롬프트 엔지니어링 핵심 패턴", "업무 자동화 시나리오 기획"]},
             {"title": "Day 3-4: 멀티모달 콘텐츠 제작", "desc": "이미지, 영상, 사운드를 활용한 브랜드 자산 만들기", "details": ["Midjourney/DALL-E3 이미지 워크숍", "Runway/Sora 영상 제작 실습", "ElevenLabs AI 보이스 클로닝"]},
             {"title": "Day 5-6: 노코드(Vibe) 코딩 입문", "desc": "자연어로 코딩하기, 나만의 웹 애플리케이션 개발", "details": ["Cursor 에디터 설치 및 환경 설정", "HTML/CSS/JS 기초 및 AI 페어 프로그래밍", "API 연동 및 데이터베이스 기초"]},
             {"title": "Day 7-8: 실전 프로젝트 & 배포", "desc": "직무 맞춤형 AI 앱 개발 및 클라우드 배포", "details": ["개인 프로젝트 기획 및 UI 설계", "Vercel을 통한 실제 서비스 배포", "최종 성과 발표 및 피드백"]}
         ]
    },

    # ------------------------------------------------------------------
    # 5. AI Expert Advanced (10 Days)
    # ------------------------------------------------------------------
    "expert_advanced.html": {
        "stats": { "days": "10", "tools": "8", "projects": "4", "app": "3" },
        "tools": [
            {"name": "LangChain", "icon": "fa-link", "desc": "LLM 프레임워크", "color": "orange"},
            {"name": "HuggingFace", "icon": "fa-smile", "desc": "오픈소스 모델", "color": "yellow"},
            {"name": "Pinecone", "icon": "fa-database", "desc": "벡터 DB", "color": "cyan"},
            {"name": "AutoGPT", "icon": "fa-robot", "desc": "자율 에이전트", "color": "red"}
        ],
        "curriculum": [
            {"title": "Phase 1: LLM 심층 이해 (Day 1-3)", "desc": "Transformer 아키텍처와 오픈소스 LLM 활용", "details": ["Transformer 구조와 Attention 메커니즘", "Llama 3, Mistral 등 로컬 LLM 구동", "Prompt Tuning vs Fine-tuning 비교"]},
            {"title": "Phase 2: RAG 시스템 구축 (Day 4-6)", "desc": "사내 지식 기반의 정확한 답변 시스템 구현", "details": ["텍스트 임베딩과 벡터 데이터베이스 이해", "LangChain을 이용한 문서 검색 파이프라인", "PDF/Web 데이터 연동 챗봇 실습"]},
            {"title": "Phase 3: Fine-tuning & Agent (Day 7-10)", "desc": "도메인 특화 모델 학습과 자율 에이전트 개발", "details": ["LoRA를 활용한 효율적인 파인튜닝 실습", "자율 에이전트(Agent) 설계 및 툴 사용 권한 부여", "기업용 AI 솔루션 아키텍처 설계"]}
        ]
    },

    # ------------------------------------------------------------------
    # 6. AI Marketing (5 Days)
    # ------------------------------------------------------------------
    "special_marketing.html": {
        "stats": { "days": "5", "tools": "7", "projects": "15", "app": "0" },
        "tools": [
            {"name": "Jasper", "icon": "fa-pen-alt", "desc": "카피라이팅", "color": "purple"},
            {"name": "Midjourney", "icon": "fa-paint-brush", "desc": "광고 이미지", "color": "blue"},
            {"name": "AdCreative", "icon": "fa-ad", "desc": "광고 소재 자동화", "color": "red"},
            {"name": "Canva", "icon": "fa-pencil-ruler", "desc": "소셜 콘텐츠", "color": "cyan"}
        ],
        "curriculum": [
            {"title": "Day 1: 마케팅 페르소나 & 전략", "desc": "ChatGPT로 고객 페르소나 정의 및 타겟 분석", "details": ["경쟁사 분석 및 SWOT 분석 자동화", "고객 페르소나 시뮬레이션 대화", "마케팅 캠페인 슬로건 및 메시지 도출"]},
            {"title": "Day 2-3: 콘텐츠 자동화 파이프라인", "desc": "블로그, SNS, 상세페이지 콘텐츠 대량 생산", "details": ["SEO 최적화된 블로그 포스팅 10개 1분 생성", "SNS 채널별(인스타, 링크드인) 맞춤 톤앤매너 변환", "상세페이지 세일즈 카피라이팅 자동화"]},
            {"title": "Day 4-5: 퍼포먼스 마케팅 & 광고 소재", "desc": "고효율 광고 소재 생성 및 데이터 분석", "details": ["클릭을 부르는 광고 배너 대량 제작(Midjourney)", "숏폼 광고 스크립트 및 영상 기획", "광고 성과 데이터 분석 및 리포팅 자동화"]}
        ]
    },

    # ------------------------------------------------------------------
    # 7. AI Manufacturing (5 Days)
    # ------------------------------------------------------------------
    "special_manufacturing.html": {
        "stats": { "days": "5", "tools": "5", "projects": "3", "app": "1" },
        "tools": [
            {"name": "TensorFlow", "icon": "fa-project-diagram", "desc": "딥러닝 프레임워크", "color": "orange"},
            {"name": "YOLO", "icon": "fa-eye", "desc": "객체 탐지", "color": "green"},
            {"name": "Tableau", "icon": "fa-chart-bar", "desc": "데이터 시각화", "color": "blue"},
            {"name": "PowerAutomate", "icon": "fa-cogs", "desc": "RPA", "color": "cyan"}
        ],
        "curriculum": [
            {"title": "Day 1: 제조 데이터와 AI", "desc": "스마트 팩토리 데이터 수집 및 전처리", "details": ["MES/ERP 데이터의 이해와 AI 적용 분야", "시계열 데이터(센서, 진동) 전처리 실습", "Python Pandas를 활용한 기초 데이터 분석"]},
            {"title": "Day 2-3: 예지 보전 모델링", "desc": "설비 고장 예측을 위한 이상 탐지 모델 구현", "details": ["정상 vs 비정상 데이터 분류 (Classification)", "오토인코더(Autoencoder)기반 이상 탐지", "설비 잔여 수명(RUL) 예측 기초"]},
            {"title": "Day 4-5: 비전 검사 & 공정 최적화", "desc": "이미지 기반 불량 검출 및 공정 파라미터 최적화", "details": ["YOLO 모델을 활용한 제품 결함 탐지 실습", "공정 변수 최적화를 위한 강화학습 개요", "현장 적용을 위한 AI 모델 배포 전략"]}
        ]
    },

    # ------------------------------------------------------------------
    # 8. AI Data Analyst (5 Days)
    # ------------------------------------------------------------------
    "special_data.html": {
        "stats": { "days": "5", "tools": "6", "projects": "5", "app": "0" },
        "tools": [
            {"name": "Code Interpreter", "icon": "fa-code", "desc": "노코드 분석", "color": "green"},
            {"name": "PandasAI", "icon": "fa-table", "desc": "대화형 분석", "color": "blue"},
            {"name": "Julius AI", "icon": "fa-chart-line", "desc": "고급 통계", "color": "orange"},
            {"name": "Tableau AI", "icon": "fa-chart-pie", "desc": "자동 시각화", "color": "purple"}
        ],
        "curriculum": [
            {"title": "Day 1: 데이터 리터러시 & 탐색", "desc": "코딩 없이 대화로 하는 탐색적 데이터 분석(EDA)", "details": ["ChatGPT Advanced Data Analysis 모드 활용", "데이터 구조 파악 및 결측치 처리 자동화", "기초 통계량 확인 및 데이터 요약"]},
            {"title": "Day 2-3: 인사이트 도출 & 시각화", "desc": "복잡한 데이터를 직관적인 차트로 변환", "details": ["상관관계 분석 및 핵심 지표 시각화", "고급 차트(히트맵, 산점도) 자동 생성 프롬프트", "경영진 보고용 대시보드 기획"]},
            {"title": "Day 4-5: 머신러닝 예측 모델링", "desc": "클릭 몇 번으로 만드는 수요 예측 및 분류 모델", "details": ["매출/재고 시계열 예측 모델링", "고객 이탈 예측 분류 모델 실습", "분석 결과 보고서 자동 생성 및 스토리텔링"]}
        ]
    },

    # ------------------------------------------------------------------
    # 9. AI Video Creator (5 Days)
    # ------------------------------------------------------------------
    "special_video.html": {
        "stats": { "days": "5", "tools": "8", "projects": "3", "app": "0" },
        "tools": [
            {"name": "Runway", "icon": "fa-video", "desc": "영상 생성/편집", "color": "purple"},
            {"name": "Sora/Pika", "icon": "fa-film", "desc": "텍스트-비디오", "color": "blue"},
            {"name": "ElevenLabs", "icon": "fa-microphone", "desc": "AI 성우", "color": "orange"},
            {"name": "CapCut", "icon": "fa-cut", "desc": "AI 편집 툴", "color": "black"}
        ],
        "curriculum": [
            {"title": "Day 1: 영상 기획 & 스크립트", "desc": "조회수를 부르는 킬러 콘텐츠 기획", "details": ["유튜브 트렌드 분석 및 벤치마킹 자동화", "ChatGPT로 숏폼/롱폼 대본 10초 만에 작성", "스토리보드 및 장면 묘사 프롬프트 작성"]},
            {"title": "Day 2-3: AI 영상 소스 생성", "desc": "촬영 없이 고퀄리티 영상 및 이미지 제작", "details": ["Midjourney로 일관된 캐릭터/배경 생성", "Runway Gen-2/3로 정지 이미지를 영상화", "Camera Motion 컨트롤 및 스타일 변환"]},
            {"title": "Day 4-5: 편집 & 사운드 & 발행", "desc": "AI 성우 더빙과 자동 자막, 컷 편집 완성", "details": ["ElevenLabs로 감정을 담은 AI 내레이션 생성", "CapCut/Vrew를 활용한 자동 컷 편집 및 자막", "썸네일 제작 및 유튜브 SEO 업로드 전략"]}
        ]
    },

    # ------------------------------------------------------------------
    # 10. AI Leadership (1 Day)
    # ------------------------------------------------------------------
    "management_leadership.html": {
        "stats": { "days": "1", "tools": "3", "projects": "1", "app": "0" },
        "tools": [
            {"name": "GPT-4o", "icon": "fa-brain", "desc": "전략 파트너", "color": "emerald"},
            {"name": "Perplexity", "icon": "fa-search", "desc": "시장 동향 파악", "color": "blue"},
            {"name": "Beautiful.ai", "icon": "fa-presentation", "desc": "전략 발표", "color": "purple"},
            {"name": "Gamma", "icon": "fa-layer-group", "desc": "보고서 생성", "color": "orange"}
        ],
        "curriculum": [
            {"title": "오전: AI 패러다임 시프트", "desc": "경영진이 반드시 알아야 할 AI 기술의 본질과 미래", "details": ["Gen AI가 바꿀 산업 지형도와 비즈니스 모델", "Global 기업들의 성공/실패 사례 분석", "우리 기업의 AI 성숙도 진단"]},
            {"title": "오후: AI 도입 전략 & 의사결정", "desc": "실질적인 성과를 내는 도입 로드맵 수립", "details": ["Top-down vs Bottom-up 도입 전략", "AI 도입 시 고려해야 할 비용(Capex/Opex)과 ROI", "조직 변화 관리(Change Management)와 리더십"]}
        ]
    },

    # ------------------------------------------------------------------
    # 11. AI Strategy Consultant (20 Days)
    # ------------------------------------------------------------------
    "strategy_consultant.html": {
        "stats": { "days": "20", "tools": "10", "projects": "4", "app": "0" },
        "tools": [
            {"name": "Miro AI", "icon": "fa-project-diagram", "desc": "워크숍/매핑", "color": "yellow"},
            {"name": "ChatGPT", "icon": "fa-comments", "desc": "전략 프레임워크", "color": "emerald"},
            {"name": "Excel Copilot", "icon": "fa-table", "desc": "데이터 분석", "color": "green"},
            {"name": "Notion", "icon": "fa-book", "desc": "지식 관리", "color": "gray"}
        ],
        "curriculum": [
            {"title": "Week 1: AI 기술 및 생태계 이해", "desc": "컨설턴트를 위한 심층 기술 지식", "details": ["LLM, sLLM, RAG, Agent 등 핵심 기술 심화", "AI Value Chain 및 주요 플레이어 분석", "산업별(금융, 제조, 유통) AI 유스케이스 스터디"]},
            {"title": "Week 2: 기업 진단 방법론", "desc": "AS-IS 분석 및 Pain Point 발굴", "details": ["AI 준비도 진단 툴킷 활용 실습", "데이터 인프라 및 거버넌스 진단", "임직원 인터뷰 및 프로세스 마이닝 기법"]},
            {"title": "Week 3: AI 전략 수립 & 로드맵", "desc": "TO-BE 모델 설계 및 실행 계획", "details": ["고객 여정 지도(CJM) 기반 AI 서비스 기획", "PoC 대상 과제 우선순위 도출 매트릭스", "단계별 도입 로드맵 및 예산 산정"]},
            {"title": "Week 4: 제안 및 프로젝트 관리", "desc": "설득력 있는 제안서 작성 및 PM 역량", "details": ["AI 도입 ROI 시뮬레이션 및 정량적 기대효과 산출", "발주처를 설득하는 컨설팅 제안서 작성 실습", "AI 프로젝트 리스크 관리 및 품질 보증 방안"]}
        ]
    },

    # ------------------------------------------------------------------
    # 12. Master App Creator (60 Days)
    # ------------------------------------------------------------------
    "master_app_creator.html": {
        "stats": { "days": "60", "tools": "15", "projects": "10", "app": "5" },
        "tools": [
            {"name": "VS Code", "icon": "fa-code", "desc": "IDE", "color": "blue"},
            {"name": "GitHub", "icon": "fa-github", "desc": "버전 관리", "color": "gray"},
            {"name": "AWS/Vercel", "icon": "fa-cloud", "desc": "클라우드", "color": "orange"},
            {"name": "Docker", "icon": "fa-box", "desc": "컨테이너", "color": "cyan"}
        ],
        "curriculum": [
            {"title": "Month 1: 풀스택 AI 개발 기초", "desc": "Python, JS, DB 및 기본기 다지기", "details": ["Python & JavaScript 핵심 문법 심화", "FastAPI 백엔드 & React 프론트엔드 기초", "SQL vs NoSQL 데이터베이스 설계 및 구축"]},
            {"title": "Month 2: LLM 애플리케이션 심화", "desc": "LangChain, RAG, Agent 개발", "details": ["LangChain LCEL 문법 및 Chain 설계", "Pinecone/ChromaDB 활용 RAG 파이프라인 구축", "멀티 모달 기능(이미지/음성) 연동 및 메모리 구현"]},
            {"title": "Month 3: 엔터프라이즈 배포 & 운영", "desc": "실서비스 수준의 아키텍처 및 DevOps", "details": ["Docker 컨테이너화 및 CI/CD 파이프라인", "AWS/GCP 클라우드 인프라 구축 및 오토스케일링", "시스템 모니터링, 로깅, 보안 가이드라인"]},
            {"title": "Final: 캡스톤 프로젝트", "desc": "나만의 상용화 가능한 SaaS 런칭", "details": ["아이디어 기획부터 MVP 개발, 배포까지 전 과정 수행", "실제 사용자 피드백 반영 및 기능 고도화", "투자 유치를 위한 IR 피칭 덱 작성 및 발표"]}
        ]
    }
}


# ==========================================
# 2. HTML Generation Functions
# ==========================================

def generate_tools_html(tools):
    html = ""
    # Grid adjustment based on count
    grid_cls = "grid-cols-2 md:grid-cols-4" if len(tools) <= 4 else "grid-cols-2 md:grid-cols-3 lg:grid-cols-4"
    
    for tool in tools:
        html += f"""
                <a href="#" class="tool-card bg-white rounded-2xl p-6 border-2 border-{tool.get('color', 'blue')}-500 shadow-lg text-center hover:shadow-xl hover:scale-105 transition-all cursor-pointer block">
                    <div class="w-14 h-14 bg-{tool.get('color', 'blue')}-100 rounded-xl flex items-center justify-center mb-4 mx-auto">
                        <i class="fas {tool['icon']} text-2xl text-{tool.get('color', 'blue')}-600"></i>
                    </div>
                    <h3 class="font-bold text-lg text-gray-800 mb-1">{tool['name']}</h3>
                    <p class="text-gray-500 text-xs">{tool['desc']}</p>
                </a>"""
    return html

def generate_curriculum_html(curriculum_list):
    html = """
    <!-- Detailed Curriculum Section -->
    <section id="curriculum" class="py-20 bg-gray-50">
        <div class="container mx-auto px-6">
            <div class="text-center mb-16">
                <span class="text-purple-600 font-semibold text-sm uppercase tracking-wider">Curriculum</span>
                <h2 class="text-3xl md:text-4xl font-bold mt-2 text-gray-800">
                    상세 <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-600 to-indigo-600">커리큘럼</span>
                </h2>
            </div>
            
            <div class="max-w-4xl mx-auto space-y-4">"""
    
    for idx, module in enumerate(curriculum_list):
        html += f"""
                <!-- Module {idx+1} -->
                <div class="bg-white rounded-2xl border border-gray-200 overflow-hidden hover:border-indigo-300 transition-colors shadow-sm">
                    <div class="p-6 md:p-8">
                        <div class="flex items-start gap-4">
                            <div class="flex-shrink-0 w-12 h-12 bg-indigo-50 rounded-xl flex items-center justify-center text-indigo-600 font-bold text-xl">
                                {idx+1}
                            </div>
                            <div class="flex-grow">
                                <h3 class="text-xl font-bold text-gray-800 mb-2">{module['title']}</h3>
                                <p class="text-gray-600 mb-4">{module['desc']}</p>
                                <div class="bg-gray-50 rounded-xl p-4">
                                    <ul class="space-y-2">"""
        
        for detail in module['details']:
            html += f"""
                                        <li class="flex items-start gap-2 text-sm text-gray-700">
                                            <i class="fas fa-check-circle text-indigo-500 mt-1"></i>
                                            <span>{detail}</span>
                                        </li>"""
        
        html += """
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>"""
                
    html += """
            </div>
        </div>
    </section>"""
    return html

def generate_summary_stats_html(stats):
    return f"""
                <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
                    <div class="p-6">
                        <div class="text-4xl font-black text-purple-600 mb-2">{stats['days']}</div>
                        <div class="text-gray-600">일 과정</div>
                    </div>
                    <div class="p-6">
                        <div class="text-4xl font-black text-purple-600 mb-2">{stats['tools']}</div>
                        <div class="text-gray-600">핵심 도구</div>
                    </div>
                    <div class="p-6">
                        <div class="text-4xl font-black text-purple-600 mb-2">{stats['projects']}</div>
                        <div class="text-gray-600">실습/프로젝트</div>
                    </div>
                    <div class="p-6">
                        <div class="text-4xl font-black text-purple-600 mb-2">{stats['app']}</div>
                        <div class="text-gray-600">앱 배포</div>
                    </div>
                </div>"""

# ==========================================
# 3. Main Injection Logic
# ==========================================

for filename, data in courses_data.items():
    if not os.path.exists(filename):
        print(f"Skipping {filename} - file not found")
        continue
    
    print(f"Processing {filename}...")
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Tools Section
    # Find the tools grid container. 
    # master_index.html has <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-6">
    # We'll replace the *entire contents* of this div until the closing div.
    
    tools_html = generate_tools_html(data['tools'])
    # Need to verify grid structure in template to replace correctly.
    # Pattern: <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-6"> ... </div> (before </section>)
    
    # Let's target the SECTION containing tools to be safer.
    # <section class="py-20 bg-white" id="tools">
    # ...
    # <div class="grid ..."> .... </div>
    # ...
    # </section>
    
    tool_section_regex = r'(<section class="py-20 bg-white" id="tools">)(.*?)(<h2.*?10대 AI.*?</h2>)(.*?)(<div class="grid.*?gap-6">)(.*?)(</div>\s*</div>\s*</section>)'
    # This is getting complicated.
    # Simple approach: Replace the inner HTML of the grid container.
    
    # Find grid start
    tools_grid_start = '<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-6">'
    tools_grid_end_marker = '<!-- Course Summary -->'
    
    start_idx = content.find(tools_grid_start)
    if start_idx != -1:
        # Find closing div before Course Summary
        end_idx = content.find(tools_grid_end_marker)
        
        # Backtrack from end_idx to find the closing div of the grid
        # The structure is: </div> (grid) </div> (container) </section> (tools)
        # So look for last </div> before section end
        section_end = content.rfind('</section>', 0, end_idx)
        container_end = content.rfind('</div>', 0, section_end)
        grid_end = content.rfind('</div>', 0, container_end)
        
        # Now replace content[start_idx + len(tools_grid_start) : grid_end]
        # But wait, we also want to change the grid columns class if needed
        # So let's replace the whole DIV line too.
        
        # New grid class
        new_grid_class = "grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6" # max 4 cols for 4-8 tools
        
        new_tools_section_content = f'<div class="{new_grid_class}">' + tools_html
        
        content = content[:start_idx] + new_tools_section_content + content[grid_end:]
        print("  Updated Tools Section")
        
        # Also update the Title "10대 AI 도구" to "핵심 AI 도구" or similar count
        content = content.replace("10대 AI 도구", f"{data['stats']['tools']}대 핵심 도구")


    # 2. Update Stats Section
    # Find <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
    stats_start = '<div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">'
    s_start_idx = content.find(stats_start)
    if s_start_idx != -1:
         # Find closing div
         # Looks safe to scan for next </div> that closes this. 
         # It contains 4 divs inside.
         # Let's just find the next </div></div></div> (imprecise).
         
         # Better: Look for "<!-- Footer -->"
         footer_marker = '<!-- Footer -->'
         footer_idx = content.find(footer_marker)
         
         # Find </section> before footer
         stat_sect_end = content.rfind('</section>', 0, footer_idx)
         stat_container_end = content.rfind('</div>', 0, stat_sect_end)
         stat_grid_end = content.rfind('</div>', 0, stat_container_end) # Closing of max-w-4xl
         s_end_idx = content.rfind('</div>', 0, stat_container_end) # Actually the grid closes before max-w-4xl closes
         
         # The structure:
         # <section> <div container> <div max-w> <div YEAR GRID> ... </div> </div> </div> </section>
         
         # Let's use regex for the stats grid content
         # Pattern: <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center"> ... </div>
         
         new_stats_html = generate_summary_stats_html(data['stats'])
         # Replace the whole div
         content = re.sub(r'<div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">.*?</div>\s*</div>', 
                          new_stats_html + "\n            </div>", 
                          content, flags=re.DOTALL)
         print("  Updated Stats Section")


    # 3. Insert Curriculum Section
    # Location: After "Why This Course" (Strengths) section and Before "Tools" section.
    # Marker: <section class="py-20 bg-white" id="tools">
    
    curriculum_html = generate_curriculum_html(data['curriculum'])
    
    tools_section_marker = '<section class="py-20 bg-white" id="tools">'
    if tools_section_marker in content:
        content = content.replace(tools_section_marker, curriculum_html + "\n\n    " + tools_section_marker)
        print("  Inserted Curriculum Section")
    
    
    # 4. Update Hero Button
    # Old: href="curriculum.html"
    # New: href="#curriculum"
    content = content.replace('href="curriculum.html"', 'href="#curriculum"')
    
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("\nAll files processed.")
