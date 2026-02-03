import re
import os

# Data: Unique 3 Strengths for each course
# Format: filename: [ {title, text, benefit_title, benefit_text, icon, color} * 3 ]
# Colors: blue, violet, amber (default gradient themes) - can vary if needed but keeping structure simple for now.

courses_data = {
    "intro_ethics.html": [
        {
            "icon": "fa-shield-alt",
            "title": "필수 규제 완벽 대비",
            "desc": "EU AI Act, 국내 AI 기본법 등 급변하는 국내외 AI 규제 환경을 분석하여, <b class='text-blue-300'>법적 리스크를 최소화</b>하는 가이드를 제공합니다.",
            "benefit_title": "리스크 관리",
            "benefit_text": "기업 도입 시 발생할 수 있는 저작권 침해 및 데이터 유출 사고를 <b class='text-emerald-300'>사전에 100% 예방</b>하는 체크리스트를 확보합니다."
        },
        {
            "icon": "fa-balance-scale",
            "title": "윤리적 의사결정 프레임워크",
            "desc": "AI 편향성, 할루시네이션 등 실무에서 마주칠 윤리적 딜레마 상황에서 <b class='text-purple-300'>올바른 판단을 내리는 기준</b>을 학습합니다.",
            "benefit_title": "신뢰성 확보",
            "benefit_text": "고객과 주주에게 신뢰받는 <b class='text-emerald-300'>'책임감 있는 AI(Responsible AI)'</b> 브랜드 이미지를 구축합니다."
        },
        {
            "icon": "fa-users-cog",
            "title": "조직 AI 거버넌스 수립",
            "desc": "단순 이론이 아닌, 실제 기업에 바로 적용 가능한 <b class='text-orange-300'>AI 사용 가이드라인 및 사내 정책</b> 표준안을 제공합니다.",
            "benefit_title": "표준 정책 수립",
            "benefit_text": "수강 후 즉시 우리 회사에 맞는 <b class='text-emerald-300'>AI 윤리 강령 및 보안 지침서</b>를 완성하여 배포할 수 있습니다."
        }
    ],
    "intro_basics.html": [
        {
            "icon": "fa-magic",
            "title": "누구나 가능한 프롬프트",
            "desc": "개발 지식 없이도 자연어만으로 AI를 제어하는 <b class='text-blue-300'>핵심 프롬프트 패턴 5가지</b>를 집중 훈련합니다.",
            "benefit_title": "즉시 활용",
            "benefit_text": "검색보다 빠른 해답 도출! 업무 처리 속도가 <b class='text-emerald-300'>기존 대비 3배 이상</b> 빨라지는 경험을 하게 됩니다."
        },
        {
            "icon": "fa-sync",
            "title": "업무 자동화 첫걸음",
            "desc": "반복되는 이메일 작성, 회의록 요약, 일정 관리 등 <b class='text-purple-300'>귀찮은 단순 업무</b>를 AI에게 맡기는 법을 배웁니다.",
            "benefit_title": "워라밸 실현",
            "benefit_text": "하루 1시간 이상의 <b class='text-emerald-300'>여유 시간</b>을 확보하여 더 중요하고 창의적인 일에 집중할 수 있습니다."
        },
        {
            "icon": "fa-laptop-house",
            "title": "실습 위주 기초 훈련",
            "desc": "이론은 최소화하고, 직접 ChatGPT와 Gemini를 켜두고 따라 하는 <b class='text-orange-300'>100% 실습 중심</b> 강의입니다.",
            "benefit_title": "자신감 상승",
            "benefit_text": "AI에 대한 막연한 두려움을 없애고, <b class='text-emerald-300'>'나도 할 수 있다'</b>는 디지털 자신감을 완전히 회복합니다."
        }
    ],
    "intro_business.html": [
        {
            "icon": "fa-file-signature",
            "title": "문서 작성 시간 단축",
            "desc": "기획안, 보고서, 보도자료 등 직장인의 숙명인 <b class='text-blue-300'>글쓰기 업무</b>를 AI와 함께 초고속으로 처리합니다.",
            "benefit_title": "생산성 혁명",
            "benefit_text": "3시간 걸리던 보고서 작성이 <b class='text-emerald-300'>30분으로 단축</b>되는 놀라운 생산성 향상을 체감합니다."
        },
        {
            "icon": "fa-brain",
            "title": "창의적 아이디어 발상",
            "desc": "혼자 고민하지 마세요. AI를 브레인스토밍 파트너로 활용하여 <b class='text-purple-300'>참신한 기획 아이디어</b>를 무한히 도출합니다.",
            "benefit_title": "기획력 강화",
            "benefit_text": "막막했던 기획 회의가 즐거워지며, <b class='text-emerald-300'>남들과 다른 관점</b>의 제안으로 인정받는 인재가 됩니다."
        },
        {
            "icon": "fa-chart-pie",
            "title": "직무별 맞춤 실습",
            "desc": "인사, 총무, 영업, 마케팅 등 <b class='text-orange-300'>내 직무에 딱 맞는 AI 활용법</b>을 케이스 스터디로 배웁니다.",
            "benefit_title": "현업 적용",
            "benefit_text": "내일 당장 출근해서 써먹을 수 있는 <b class='text-emerald-300'>실무 밀착형 스킬</b>을 내 것으로 만듭니다."
        }
    ],
    "master_index.html": [ # AI 실무 마스터 (Original)
        {
            "icon": "fa-chart-line",
            "title": "데이터 기반 의사결정",
            "desc": "6개월간의 매출, 마케팅 비용 등 복잡한 수치를 AI로 분석하여 <b class='text-blue-300'>'경영진 보고서' 초안</b>을 뽑아냅니다.",
            "benefit_title": "통찰력 확보",
            "benefit_text": "데이터 요약 및 인사이트 도출을 <b class='text-emerald-300'>단 몇 분 만에 해결</b>하는 업무 생산성 혁명을 체험합니다."
        },
        {
            "icon": "fa-layer-group",
            "title": "올인원 멀티모달",
            "desc": "텍스트(Text), 이미지(Image), 영상(Video)까지 <b class='text-purple-300'>10대 AI 도구</b>를 체계적으로 연결하여 사용합니다.",
            "benefit_title": "1인 기업 역량",
            "benefit_text": "기획부터 제작까지 혼자 수행 가능한 <b class='text-emerald-300'>'슈퍼 제너럴리스트'</b> 수준의 역량을 갖춥니다."
        },
        {
            "icon": "fa-trophy",
            "title": "성과 중심 프로젝트",
            "desc": "단순 기능 학습이 아닌, 구체적인 <b class='text-orange-300'>내 비즈니스 KPI</b>를 달성하는 프로젝트를 수행합니다.",
            "benefit_title": "결과물 도출",
            "benefit_text": "교육 종료 시 <b class='text-emerald-300'>'AI 기반 비즈니스 기획안'</b>과 프로토타입 앱을 손에 쥐게 됩니다."
        }
    ],
    "expert_advanced.html": [
        {
            "icon": "fa-cogs",
            "title": "Fine-tuning 실전",
            "desc": "범용 AI가 아닌, 우리 회사의 데이터와 톤앤매너를 학습시킨 <b class='text-blue-300'>맞춤형 LLM 모델</b>을 직접 튜닝해봅니다.",
            "benefit_title": "도메인 특화",
            "benefit_text": "업계 용어와 사내 규정을 완벽히 이해하는 <b class='text-emerald-300'>우리 회사 전용 AI</b>를 구축할 수 있습니다."
        },
        {
            "icon": "fa-database",
            "title": "RAG 시스템 구축",
            "desc": "AI의 환각 현상을 없애고, 정확한 사내 문서 기반 답변을 제공하는 <b class='text-purple-300'>검색 증강 생성(RAG)</b> 기술을 마스터합니다.",
            "benefit_title": "정확도 향상",
            "benefit_text": "수천 페이지의 매뉴얼에서도 <b class='text-emerald-300'>정확한 정답만 찾아주는</b> 고성능 지식 봇을 설계합니다."
        },
        {
            "icon": "fa-robot",
            "title": "AI 에이전트 개발",
            "desc": "사람의 개입 없이 스스로 계획하고 도구를 사용하여 임무를 완수하는 <b class='text-orange-300'>자율 AI 에이전트</b>를 구현합니다.",
            "benefit_title": "완전 자동화",
            "benefit_text": "24시간 365일 쉬지 않고 일하는 <b class='text-emerald-300'>디지털 직원</b>을 채용하는 효과를 얻습니다."
        }
    ],
    "special_marketing.html": [
        {
            "icon": "fa-pen-nib",
            "title": "무한 콘텐츠 생성",
            "desc": "블로그, 인스타, 유튜브 대본 등 채널별 최적화된 마케팅 콘텐츠를 <b class='text-blue-300'>AI로 무제한 생성</b>하는 파이프라인을 구축합니다.",
            "benefit_title": "비용 절감",
            "benefit_text": "콘텐츠 제작 대행 비용을 <b class='text-emerald-300'>0원으로 절감</b>하고, 업로드 빈도는 5배 늘립니다."
        },
        {
            "icon": "fa-bullseye",
            "title": "초정밀 타겟팅",
            "desc": "고객 리뷰와 행동 데이터를 AI로 분석하여, 구매 전환율이 높은 <b class='text-purple-300'>핵심 타겟 페르소나</b>를 발굴합니다.",
            "benefit_title": "ROAS 극대화",
            "benefit_text": "광고 효율이 떨어지는 원인을 찾아내고, <b class='text-emerald-300'>구매 전환율(CVR)</b>을 획기적으로 개선합니다."
        },
        {
            "icon": "fa-rocket",
            "title": "마케팅 자동화",
            "desc": "고객 유입부터 구매 유도 이메일 발송까지, 잠자고 있을 때도 돌아가는 <b class='text-orange-300'>세일즈 오토메이션</b>을 완성합니다.",
            "benefit_title": "매출 증대",
            "benefit_text": "수동 관리에 들이던 시간을 없애고, <b class='text-emerald-300'>자동화된 수익 창출 시스템</b>을 소유하게 됩니다."
        }
    ],
    "special_manufacturing.html": [
        {
            "icon": "fa-exclamation-triangle",
            "title": "설비 이상 사전 감지",
            "desc": "진동, 소음 데이터를 AI가 학습하여 고장 징후를 <b class='text-blue-300'>사전에 포착하고 경고</b>하는 예지 보전 기술을 배웁니다.",
            "benefit_title": "가동률 향상",
            "benefit_text": "돌발 고장으로 인한 라인 중단을 막아, <b class='text-emerald-300'>설비 가동 효율(OEE)</b>을 극대화합니다."
        },
        {
            "icon": "fa-search-plus",
            "title": "AI 기반 품질 검사",
            "desc": "사람의 눈으로 놓치기 쉬운 미세한 불량을 <b class='text-purple-300'>컴퓨터 비전 AI</b>로 0.1초 만에 판별하는 시스템을 이해합니다.",
            "benefit_title": "불량률 감소",
            "benefit_text": "전수 검사 체계를 구축하여 고객에게 나가는 <b class='text-emerald-300'>불량 유출을 제로화(0%)</b> 합니다."
        },
        {
            "icon": "fa-network-wired",
            "title": "스마트 팩토리 최적화",
            "desc": "공정 데이터 분석을 통해 병목 구간을 찾고, 생산 계획을 최적화하는 <b class='text-orange-300'>데이터 기반 공장 운영</b> 노하우를 습득합니다.",
            "benefit_title": "원가 절감",
            "benefit_text": "불필요한 대기 시간과 재고 비용을 줄여 <b class='text-emerald-300'>제조 원가를 획기적으로 절감</b>합니다."
        }
    ],
    "special_data.html": [
        {
            "icon": "fa-code",
            "title": "No-Code 데이터 분석",
            "desc": "복잡한 코딩 없이도 자연어 대화만으로 데이터를 추출하고 분석하는 <b class='text-blue-300'>Code Interpreter</b> 활용법을 마스터합니다.",
            "benefit_title": "장벽 제거",
            "benefit_text": "비전공자도 당장 오늘부터 <b class='text-emerald-300'>데이터 분석가처럼</b> 데이터를 자유자재로 다루게 됩니다."
        },
        {
            "icon": "fa-chart-area",
            "title": "고품질 시각화",
            "desc": "AI에게 엑셀 파일만 던져주면, 경영진 보고용 <b class='text-purple-300'>프로페셔널한 차트와 그래프</b>를 즉시 그려냅니다.",
            "benefit_title": "설득력 강화",
            "benefit_text": "데이터 뒤에 숨겨진 의미를 한눈에 보여주어, <b class='text-emerald-300'>의사결정권자를 단번에 설득</b>하는 보고서를 만듭니다."
        },
        {
            "icon": "fa-crystal-ball",
            "title": "AI 미래 예측",
            "desc": "과거 데이터 패턴을 학습하여 다음 달 매출, 재고 수요 등을 <b class='text-orange-300'>정교하게 예측하는 모델</b>을 만들어봅니다.",
            "benefit_title": "전략적 대비",
            "benefit_text": "감 이 아닌 데이터에 기반한 예측으로 <b class='text-emerald-300'>비즈니스 불확실성</b>을 최소화합니다."
        }
    ],
    "special_video.html": [
        {
            "icon": "fa-video",
            "title": "촬영 없는 영상 제작",
            "desc": "카메라, 조명, 마이크 없이 오직 <b class='text-blue-300'>AI 툴(Runway, Sora 등)</b>만으로 고퀄리티 영상을 생성합니다.",
            "benefit_title": "제작 혁신",
            "benefit_text": "영상 한 편 제작에 들던 수일의 시간과 비용을 <b class='text-emerald-300'>1/10 수준으로 압축</b>합니다."
        },
        {
            "icon": "fa-globe",
            "title": "글로벌 콘텐츠화",
            "desc": "AI 더빙과 자막 번역 기술로, 한국어 영상 하나를 순식간에 <b class='text-purple-300'>10개국어 버전</b>으로 확산시킵니다.",
            "benefit_title": "시장 확장",
            "benefit_text": "언어 장벽 없이 전 세계 시청자를 나의 <b class='text-emerald-300'>잠재 고객으로 확보</b>합니다."
        },
        {
            "icon": "fa-bolt",
            "title": "숏폼 대량 생산",
            "desc": "긴 영상을 하이라이트 쇼츠(Shorts)로 자동 편집하고 대량 생산하는 <b class='text-orange-300'>바이럴 공장 시스템</b>을 구축합니다.",
            "benefit_title": "채널 성장",
            "benefit_text": "압도적인 콘텐츠 물량 공세로 유튜브/인스타 채널을 <b class='text-emerald-300'>가장 빠르게 급성장</b>시킵니다."
        }
    ],
    "management_leadership.html": [
        {
            "icon": "fa-chess-king",
            "title": "AI 경영 통찰력",
            "desc": "기술적 디테일보다, AI가 가져올 산업의 판도 변화와 <b class='text-blue-300'>새로운 비즈니스 기회</b>를 포착하는 눈을 키웁니다.",
            "benefit_title": "비전 수립",
            "benefit_text": "불확실한 미래 속에서 조직이 나아가야 할 <b class='text-emerald-300'>명확한 AI 북극성(North Star)</b>을 제시합니다."
        },
        {
            "icon": "fa-sitemap",
            "title": "조직 혁신 전략",
            "desc": "AI 도입 시 필연적인 조직 저항을 관리하고, 구성원들을 AI 협업 인재로 변화시키는 <b class='text-purple-300'>체인지 매니지먼트</b>를 배웁니다.",
            "benefit_title": "성공적 안착",
            "benefit_text": "도입 실패 없이 AI가 조직 문화에 <b class='text-emerald-300'>성공적으로 뿌리내리게</b> 리딩합니다."
        },
        {
            "icon": "fa-hand-holding-usd",
            "title": "투자 대비 효과(ROI)",
            "desc": "막대한 AI 투자 비용, 과연 타당한가? 냉철하게 비용과 효용을 분석하여 <b class='text-orange-300'>최적의 투자 의사결정</b>을 내립니다.",
            "benefit_title": "재무적 성과",
            "benefit_text": "무분별한 도입을 막고, <b class='text-emerald-300'>실질적인 이익</b>을 가져다주는 프로젝트만 선별합니다."
        }
    ],
    "strategy_consultant.html": [
        {
            "icon": "fa-stethoscope",
            "title": "AI 기업 진단",
            "desc": "기업의 데이터 준비 상태, 인프라, 조직 역량을 객관적으로 평가하는 <b class='text-blue-300'>AI 준비도 진단 프레임워크</b>를 익힙니다.",
            "benefit_title": "현황 파악",
            "benefit_text": "막연했던 기업의 상태를 수치화하여 <b class='text-emerald-300'>정확한 처방과 솔루션</b>을 제시합니다."
        },
        {
            "icon": "fa-project-diagram",
            "title": "로드맵 설계",
            "desc": "단기적 도입부터 중장기적 전환까지, 단계별로 실행 가능한 <b class='text-purple-300'>AI 트랜스포메이션 마스터플랜</b>을 수립합니다.",
            "benefit_title": "실행력 확보",
            "benefit_text": "이상적인 그림이 아닌, <b class='text-emerald-300'>현실적이고 구체적인 실행 계획</b>으로 고객을 리드합니다."
        },
        {
            "icon": "fa-comments-dollar",
            "title": "컨설팅 설득 화법",
            "desc": "기술 용어를 비즈니스 언어로 통역하여, C-Level 경영진을 설득하고 <b class='text-orange-300'>프로젝트 수주를 이끌어내는</b> 커뮤니케이션 스킬을 배웁니다.",
            "benefit_title": "수주 성공",
            "benefit_text": "고객의 페인 포인트를 정확히 찌르는 제안으로 <b class='text-emerald-300'>컨설팅 계약 성사율</b>을 높입니다."
        }
    ],
    "master_app_creator.html": [
        {
            "icon": "fa-cubes",
            "title": "엔터프라이즈 아키텍처",
            "desc": "장난감 같은 앱이 아닌, 대규모 트래픽과 보안을 고려한 <b class='text-blue-300'>현업 수준의 시스템 설계</b> 능력을 배양합니다.",
            "benefit_title": "전문가 도약",
            "benefit_text": "단순 코더를 넘어, 시스템 전체를 조망하고 설계하는 <b class='text-emerald-300'>스페셜리스트 아키텍트</b>로 성장합니다."
        },
        {
            "icon": "fa-link",
            "title": "LangChain 심화",
            "desc": "LLM과 외부 데이터를 정교하게 연결하는 LangChain의 고급 기능을 마스터하여 <b class='text-purple-300'>복합적인 추론이 가능한 AI</b>를 만듭니다.",
            "benefit_title": "문제 해결",
            "benefit_text": "기존 챗봇으로는 불가능했던 <b class='text-emerald-300'>고난이도 복합 업무</b>를 AI로 자동화 구현합니다."
        },
        {
            "icon": "fa-upload",
            "title": "실전 배포 및 운영",
            "desc": "AWS, Vercel 등 클라우드 환경에 실제 서비스를 배포하고, 로그 모니터링 및 유지보수하는 <b class='text-orange-300'>DevOps 기초</b>까지 다룹니다.",
            "benefit_title": "서비스 런칭",
            "benefit_text": "내 아이디어를 세상에 내놓고 <b class='text-emerald-300'>실제 수익을 창출</b>하는 나만의 SaaS 서비스를 갖게 됩니다."
        }
    ]
}

# Template pattern to match the strengths section cards
# We look for the 3 columns in the grid.
# The template has: <!-- Strength 1 --> ... <!-- Strength 2 --> ... <!-- Strength 3 -->
# We will regenerate the HTML for the 3 cards.

def generate_strength_card(data, index):
    # Colors for the 3 cards (based on template design)
    gradients = [
        "from-blue-600 to-cyan-600",
        "from-violet-600 to-purple-600",
        "from-amber-600 to-orange-600"
    ]
    icon_bgs = [
        "from-blue-500 to-cyan-500",
        "from-violet-500 to-purple-500",
        "from-amber-500 to-orange-500"
    ]
    texts = ["blue", "violet", "amber"]
    
    g = gradients[index]
    ib = icon_bgs[index]
    t = texts[index]
    
    # Using data from dictionary
    title = data['title']
    desc = data['desc']
    benefit_title = data['benefit_title']
    benefit_text = data['benefit_text']
    icon = data['icon']
    
    return f"""                <!-- Strength {index+1} -->
                <div class="relative group">
                    <div
                        class="absolute inset-0 bg-gradient-to-r {g} rounded-3xl blur-xl opacity-50 group-hover:opacity-75 transition">
                    </div>
                    <div class="relative bg-white/10 backdrop-blur-lg rounded-3xl p-8 border border-white/20 h-full">
                        <div
                            class="w-16 h-16 bg-gradient-to-br {ib} rounded-2xl flex items-center justify-center mb-6">
                            <i class="fas {icon} text-3xl text-white"></i>
                        </div>
                        <span class="text-{t}-300 text-sm font-semibold">STRENGTH 0{index+1}</span>
                        <h3 class="text-xl font-bold mt-2 mb-4">{title}</h3>
                        <div class="space-y-4 text-gray-300 text-sm">
                            <div class="bg-white/5 rounded-xl p-4">
                                <p class="font-semibold text-white mb-2"><i
                                        class="fas fa-star text-yellow-400 mr-2"></i>강점</p>
                                <p>{desc}</p>
                            </div>
                            <div class="bg-white/5 rounded-xl p-4">
                                <p class="font-semibold text-white mb-2"><i
                                        class="fas fa-rocket text-emerald-400 mr-2"></i>기대효과</p>
                                <p>{benefit_text}</p>
                            </div>
                        </div>
                    </div>
                </div>"""

# Main Update Loop
for filename, strengths in courses_data.items():
    if not os.path.exists(filename):
        print(f"Skipping {filename} - not found")
        continue
        
    print(f"Updating {filename}...")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Construct new HTML for the grid content
    new_cards_html = ""
    for i in range(3):
        new_cards_html += generate_strength_card(strengths[i], i)
        if i < 2:
            new_cards_html += "\n\n"
            
    # Regex to find the content between <!-- Strength 1 --> and the end of Strength 3 div
    # Pattern: Look for the grid container, then replace its valid children.
    # To be safer, we can try to locate the container: <div class="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto">
    
    start_marker = '<div class="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto">'
    end_marker = '</div>\n        </div>\n    </section>' # Assuming standard indentation
    
    # A robust way: Find start marker, then find the closing div of that container.
    # Since regex on HTML structure is risky, we will use the exact previous content structure if possible
    # Or just replace everything between the start marker and the "Top 10 AI Tools" section start if strictly structured.
    
    # Let's try finding the start marker
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print(f"  Error: Could not find grid container in {filename}")
        continue
        
    # Move pointer to after the marker
    content_start = start_idx + len(start_marker)
    
    # Find the end of this section (container closing div)
    # Since we have nested divs, we need to be careful.
    # However, in our template, the closing `</div>` for this grid is followed by `</div>` (container) and `</section>`.
    # Let's look for `<!-- Strength 1 -->`
    
    strength1_idx = content.find('<!-- Strength 1 -->', start_idx)
    if strength1_idx == -1:
        print("  Error: Could not find Strength 1 marker")
        continue

    # We need to find where Strength 3 ends.
    # Strength 3 starts...
    strength3_idx = content.find('<!-- Strength 3 -->', strength1_idx)
    
    # After Strength 3 div, there are 3 closing divs: 
    # 1. Strength 3 card closing
    # 2. Strength 3 wrapper closing
    # 3. Strength 3 transition wrapper closing
    # Actually, let's look at the template structure again.
    
    # Template:
    # <div class="grid ...">
    #    <!-- S1 --> ... </div>
    #    <!-- S2 --> ... </div>
    #    <!-- S3 --> ... </div>
    # </div>
    
    # So we replace from <!-- Strength 1 --> until the closing </div> of the grid.
    # We can find the grid closing div by looking for the next occurrence of `</div>` that is followed by `</div>` and `<section`.
    # Or we can just build the regex for <!-- Strength 1 -->.*<!-- Strength 3 -->.*?(match the closing div of strength 3)
    
    # Let's construct a RegEx that captures from Strength 1 to the end of Strength 3 card.
    
    pattern = re.compile(r'<!-- Strength 1 -->.*?<!-- Strength 3 -->.*?</div>\s*</div>\s*</div>', re.DOTALL)
    # The ending of Strength 3 in template:
    #                 <div class="relative group"> ... </div>
    # Needs to match properly.
    
    # Simplified approach: We know the template structure exactly because we just wrote it.
    # We can use the start of Strength 1 and strictly look for the closing of the section container
    # "            </div>\n        </div>\n    </section>\n\n\n    <!-- Top 10 AI Tools"
    
    section_end_idx = content.find('<!-- Top 10 AI Tools Section -->')
    if section_end_idx == -1:
        # Fallback for files that might differ (e.g. Master which might have different next section?)
        # Master template has Top 10 too.
        print("  Warning: Top 10 tools section not found, looking for alternative end")
        section_end_idx = content.find('</section>', start_idx)
    
    # Now work backwards from section_end to find the grid closing div
    # ... </div> (grid) </div> (container) </section>
    
    # Let's replace the innerHTML of the grid directly
    # We will replace everything between `start_marker` + newline and the detected end of the grid.
    
    # Let's just create the full content to replace
    replacement = f"""
{new_cards_html}
            """
    
    # Find the range to replace
    # From: start_marker (end of it)
    # To: The matching closing div.
    # Since counting divs is hard, let's assume valid indentation from the template creation.
    # The grid closing div usually aligns with <div class="grid...
    # In template: 
    #             </div>
    #         </div>
    #     </section>
    
    # We will assume everything between start_marker and the last `</div>` before `</div>` before `</section>` IS the content.
    
    # Regex for standard template replacement
    # Matches: start_marker + any content + closing div of grid
    regex = r'(<div class="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto">)(.*?)(</div>\s*</div>\s*</section>)'
    
    new_content = re.sub(regex, f'\\1\\n{new_cards_html}\\n            \\3', content, flags=re.DOTALL)
    
    if len(new_content) == len(content):
        # Replacement didn't happen - probably regex mismatch due to whitespace
        print("  Regex mismatch - trying fallback search")
        # Direct string find
        s_idx = content.find(start_marker) + len(start_marker)
        
        # Look for the section end
        sect_end = content.find('</section>', s_idx)
        # Find the last </div> before sect_end
        grid_end = content.rfind('</div>', 0, sect_end) # Container div
        grid_inner_end = content.rfind('</div>', 0, grid_end) # Grid div
        
        if s_idx > 0 and grid_inner_end > 0:
            new_content = content[:s_idx] + "\n" + new_cards_html + "\n            " + content[grid_inner_end:]
            print("  Fallback replacement applied")
        else:
            print("  FAILED to update strengths.")
            continue

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("  Success.")

print("\\nAll files updated.")
