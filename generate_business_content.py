
# Script to generate Lecture Pages and Textbooks for AI Business Strategy Course (Expanded)
import os

# ==========================================
# 1. TEXTBOOKS DATA (Expanded Content)
# ==========================================
textbooks = [
    {
        "filename": "textbook_business_cases.html",
        "title": "산업별 AI 혁신 사례 심층 분석",
        "subtitle": "Deep Dive into Global AI Transformation Stories",
        "color": "blue",
        "content": """
            <h3>1. 금융 산업의 AI 혁신 (Finance)</h3>
            <p>금융 산업은 방대한 데이터를 보유하고 있어 AI 도입 효과가 가장 즉각적으로 나타나는 분야입니다. 단순 챗봇 상담을 넘어 자산 관리, 리스크 분석, 사기 탐지 등 핵심 업무로 확산되고 있습니다.</p>

            <h4 class="text-lg font-bold text-slate-800 mt-4">Case 1: JP Morgan의 'IndexGPT' & 'LLM Suite'</h4>
            <ul class="list-disc pl-6 space-y-2 mb-4">
                <li><strong>배경:</strong> 고객들은 개인화된 투자 조언을 원하지만, 프라이빗 뱅커(PB)의 수는 한정적입니다.</li>
                <li><strong>솔루션:</strong> 금융 데이터에 특화된 LLM인 IndexGPT를 개발하여 고객의 투자 성향에 맞는 ETF 및 금융 상품을 분석하고 추천합니다.</li>
                <li><strong>성과:</strong> 자산 관리 서비스의 대중화를 이끌었으며, 직원들의 리서치 업무 시간을 40% 이상 단축했습니다.</li>
            </ul>

            <h4 class="text-lg font-bold text-slate-800 mt-4">Case 2: BloombergGPT</h4>
            <ul class="list-disc pl-6 space-y-2 mb-4">
                <li><strong>특징:</strong> 40년 이상의 금융 데이터(3630억 토큰)와 일반 데이터(3450억 토큰)를 결합하여 자체 구축한 모델입니다.</li>
                <li><strong>차별점:</strong> 일반적인 GPT-4보다 금융 용어 이해도와 복잡한 금융 수식 처리 능력이 월등히 뛰어납니다.</li>
            </ul>

            <hr class="my-8 border-slate-200">

            <h3>2. 제조 산업의 스마트 팩토리 (Manufacturing)</h3>
            <p>제조업에서는 '효율성 극대화'와 '다운타임(가동 중단) 최소화'가 핵심입니다. 생성형 AI는 설계부터 유지보수까지 전 과정을 혁신하고 있습니다.</p>

            <h4 class="text-lg font-bold text-slate-800 mt-4">Case: Mitsubishi Electric & Siemens</h4>
            <div class="bg-blue-50 p-4 rounded-xl border border-blue-100 my-4">
                <strong>🔧 기존 방식:</strong> 엔지니어가 PLC(Programmable Logic Controller) 장비를 제어하기 위해 복잡한 특수 코드를 직접 작성해야 함.<br>
                <strong>🚀 AI 도입 후:</strong> 엔지니어가 "컨베이어 벨트 속도를 10% 늦춰줘"라고 자연어로 입력하면, AI가 자동으로 PLC 코드를 생성하여 장비에 입력.
            </div>
            <p>이로 인해 신입 엔지니어도 숙련자처럼 장비를 제어할 수 있게 되었으며, 프로그래밍 오류로 인한 사고가 획기적으로 감소했습니다.</p>

            <hr class="my-8 border-slate-200">

            <h3>3. 유통 및 소비재 (Retail & CPG)</h3>
            <p>유통업의 핵심은 '초개인화(Hyper-personalization)'입니다. 고객 한 명 한 명에게 딱 맞는 경험을 제공하는 데 AI가 활용됩니다.</p>
            
            <h4 class="text-lg font-bold text-slate-800 mt-4">Case: Coca-Cola 'Create Real Magic'</h4>
            <p>코카콜라는 OpenAI의 DALL-E와 협업하여 소비자가 직접 코카콜라의 에셋(로고, 병 이미지 등)을 활용해 예술 작품을 만들 수 있는 캠페인을 진행했습니다.</p>
            <ul class="list-disc pl-6 space-y-2 mt-2">
                <li>소비자가 브랜드 경험의 주체가 되는 '참여형 마케팅'의 정점.</li>
                <li>생성된 수만 장의 이미지는 코카콜라의 전광판 광고로 활용되어 마케팅 비용 절감 및 바이럴 효과 극대화.</li>
            </ul>
        """
    },
    {
        "filename": "textbook_business_trends.html",
        "title": "생성형 AI 생태계와 기술 트렌드",
        "subtitle": "Understanding the Gen-AI Ecosystem",
        "color": "indigo",
        "content": """
            <h3>1. 생성형 AI 기술 스택 (The Tech Stack)</h3>
            <p>AI 비즈니스를 이해하려면 기술의 층위(Layer)를 파악해야 합니다. 어디에 기회가 있는지 알 수 있기 때문입니다.</p>
            
            <table class="w-full text-sm border mt-4 mb-6">
                <tr class="bg-indigo-900 text-white">
                    <th class="p-3">Layer</th>
                    <th class="p-3">설명</th>
                    <th class="p-3">주요 플레이어</th>
                </tr>
                <tr>
                    <td class="p-3 font-bold border-b">Application (앱)</td>
                    <td class="p-3 border-b">실제 최종 사용자가 쓰는 서비스</td>
                    <td class="p-3 border-b">Jasper, Notion AI, Character.ai</td>
                </tr>
                 <tr>
                    <td class="p-3 font-bold border-b">Model (모델)</td>
                    <td class="p-3 border-b">지능을 제공하는 LLM 엔진</td>
                    <td class="p-3 border-b">GPT-4, Claude 3, Gemini, Llama 3</td>
                </tr>
                 <tr>
                    <td class="p-3 font-bold border-b">Infra (인프라)</td>
                    <td class="p-3 border-b">모델을 돌리기 위한 하드웨어/클라우드</td>
                    <td class="p-3 border-b">NVIDIA, AWS, Azure, Google Cloud</td>
                </tr>
            </table>

            <h3>2. 2026년 주요 기술 트렌드</h3>
            
            <h4 class="font-bold text-indigo-700 mt-4">1) 멀티모달(Multimodal)의 일상화</h4>
            <p>이제 텍스트뿐만 아니라, 이미지, 오디오, 비디오를 동시에 이해하고 생성하는 것이 기본이 되었습니다. '보고 듣고 말하는' AI가 비즈니스의 접점을 넓힙니다.</p>

            <h4 class="font-bold text-indigo-700 mt-4">2) 온디바이스 AI (On-device AI)</h4>
            <p>인터넷 연결 없이 노트북이나 스마트폰 자체 칩(NPU)에서 AI가 구동됩니다. 개인정보 보안이 중요한 금융, 의료, 법률 분야에서 폭발적 성장이 예상됩니다.</p>
            
            <h4 class="font-bold text-indigo-700 mt-4">3) AI 에이전트 (Autonomous Agents)</h4>
            <p>시켜서 하는 AI가 아니라, 스스로 목표를 달성하기 위해 계획을 세우고 도구를 사용하는 '자율 주행' AI가 등장했습니다. (예: "다음 주 출장 준비해줘"라고 하면 항공권 예매, 호텔 예약, 미팅 일정 조율을 알아서 수행)</p>
        """
    },
    {
        "filename": "textbook_business_bmc.html",
        "title": "AI 기반 비즈니스 모델 캔버스 (BMC)",
        "subtitle": "Business Model Innovation with AI",
        "color": "violet",
        "content": """
            <h3>1. AI 도입으로 변화하는 9 Block</h3>
            <p>기존 비즈니스 모델 캔버스(BMC)의 각 요소가 AI로 인해 어떻게 바뀌는지 분석합니다.</p>

            <div class="grid md:grid-cols-2 gap-6 mt-6">
                <div class="border p-4 rounded-lg shadow-sm">
                    <h4 class="font-bold text-violet-700 mb-2">💰 Cost Structure (비용 구조)</h4>
                    <p class="text-sm text-slate-600">인건비 비중은 줄어들지만, <strong>API 사용료, 클라우드 서버 비용, 데이터 관리 비용</strong>이라는 새로운 비용 항목이 생깁니다. 변동비(Token usage) 관리가 핵심입니다.</p>
                </div>
                <div class="border p-4 rounded-lg shadow-sm">
                    <h4 class="font-bold text-violet-700 mb-2">🎁 Value Proposition (가치 제안)</h4>
                    <p class="text-sm text-slate-600">'빠른 속도', '저렴한 가격'을 넘어 <strong>'개인 맞춤형 결과물', '창의적 보조'</strong>가 새로운 가치가 됩니다.</p>
                </div>
                <div class="border p-4 rounded-lg shadow-sm">
                    <h4 class="font-bold text-violet-700 mb-2">🔑 Key Resources (핵심 자원)</h4>
                    <p class="text-sm text-slate-600">공장, 설비보다 <strong>'독자적인 데이터셋(Proprietary Data)'</strong>과 <strong>'프롬프트 엔지니어링 노하우'</strong>가 핵심 자산이 됩니다.</p>
                </div>
                <div class="border p-4 rounded-lg shadow-sm">
                    <h4 class="font-bold text-violet-700 mb-2">🤝 Customer Relationship (고객 관계)</h4>
                    <p class="text-sm text-slate-600">일방적 정보 전달에서 <strong>'24/365 실시간 대화형 상호작용'</strong>으로 관계의 질이 바뀝니다.</p>
                </div>
            </div>

            <h3>2. 실습: AI 서비스 기획하기</h3>
            <p>가상의 'AI 여행 가이드' 서비스를 기획한다고 가정해봅시다.</p>
            <ul class="list-disc pl-6 space-y-2 mt-2 bg-slate-50 p-4 rounded">
                <li><strong>Target:</strong> 계획 짜기 귀찮아하는 P형 여행자</li>
                <li><strong>Value:</strong> 취향만 말하면 1분 만에 동선, 맛집, 예약까지 끝내줌</li>
                <li><strong>Revenue:</strong> 식당/호텔 예약 수수료 + 프리미엄 구독 (광고 제거)</li>
            </ul>
        """
    },
    {
        "filename": "textbook_business_gap.html",
        "title": "경쟁사 분석 및 차별화 전략",
        "subtitle": "Competitive Analysis & Differentiation",
        "color": "purple",
        "content": """
            <h3>1. AI 시대의 경쟁 우위 요소 (Moat)</h3>
            <p>누구나 똑같은 GPT-4를 쓰는 시대에, 우리 기업만의 해자(Moat)는 무엇일까요?</p>
            
            <h4 class="font-bold text-purple-800 mt-4">1) 데이터 해자 (Data Moat)</h4>
            <p>경쟁사가 접근할 수 없는 <strong>우리만의 데이터</strong>가 있는가? (예: 10년간 축적된 고객 상담 로그, 독점 계약된 이미지 DB)</p>

            <h4 class="font-bold text-purple-800 mt-4">2) 워크플로우 해자 (Workflow Moat)</h4>
            <p>AI를 기존 업무 시스템(ERP, CRM)에 얼마나 매끄럽게 녹여냈는가? 사용자가 AI를 쓰고 있다는 사실조차 모르게 편해야 합니다.</p>

            <h3>2. Gap 분석 프레임워크</h3>
            <p>현재(As-Is)와 목표(To-Be) 사이의 격차를 분석하여 AI 도입 전략을 짭니다.</p>
            <table class="w-full text-sm border mt-4">
                <tr class="bg-gray-100"><th class="p-2 border">구분</th><th class="p-2 border">현재 (As-Is)</th><th class="p-2 border">미래 (To-Be)</th><th class="p-2 border">AI의 역할 (Action)</th></tr>
                <tr><td class="p-2 border">고객 응대</td><td class="p-2 border">상담원 연결 대기 10분</td><td class="p-2 border">대기 시간 0초</td><td class="p-2 border">FAQ 자동 응답 챗봇 도입</td></tr>
                <tr><td class="p-2 border">마케팅</td><td class="p-2 border">불특정 다수 스팸 발송</td><td class="p-2 border">1:1 초개인화 메시지</td><td class="p-2 border">고객 구매 이력 기반 카피라이팅 생성</td></tr>
            </table>
        """
    },
    {
        "filename": "textbook_business_maturity.html",
        "title": "AI 성숙도 진단 모델 (Maturity Model)",
        "subtitle": "Assessing Organizational Readiness",
        "color": "green",
        "content": """
            <h3>1. 조직의 AI 준비 상태 진단</h3>
            <p>무턱대고 도입하기 전에 우리 회사의 체력을 측정해야 합니다. Gartner의 성숙도 모델을 기반으로 재구성했습니다.</p>
            
            <div class="space-y-4 mt-4">
                <div class="border-l-4 border-slate-300 pl-4 py-2">
                    <strong class="text-lg">Level 1: 인식 (Awareness)</strong>
                    <p class="text-sm text-slate-500">경영진이 AI의 중요성은 알지만, 구체적 계획이나 전담 조직 없음. 파편적인 개인 활용 단계.</p>
                </div>
                <div class="border-l-4 border-green-300 pl-4 py-2">
                    <strong class="text-lg">Level 2: 활성화 (Active)</strong>
                    <p class="text-sm text-slate-500">초기 실험(PoC)이 진행됨. 데이터가 모이기 시작하지만 품질이 낮음. 특정 부서(IT) 주도.</p>
                </div>
                <div class="border-l-4 border-green-500 pl-4 py-2">
                    <strong class="text-lg">Level 3: 운영 (Operational)</strong>
                    <p class="text-sm text-slate-500">성공한 PoC가 실제 업무 시스템에 적용됨. AI 예산이 정규 편성됨. 데이터 거버넌스 수립 시작.</p>
                </div>
                <div class="border-l-4 border-green-700 pl-4 py-2">
                    <strong class="text-lg">Level 4: 시스템화 (Systemic)</strong>
                    <p class="text-sm text-slate-500">전사적으로 AI가 내재화됨. 신규 프로젝트 기획 시 AI 검토가 기본(Default). 데이터 선순환 구조 완성.</p>
                </div>
            </div>

            <h3>2. 단계별 액션 플랜</h3>
            <ul class="list-disc pl-6 space-y-2 mt-4">
                <li><strong>Lv 1 → Lv 2:</strong> 성공 사례(Quick Win)를 빨리 만들어 내부 공감대 형성.</li>
                <li><strong>Lv 2 → Lv 3:</strong> MLOps(운영 파이프라인) 구축 및 데이터 표준화 투자.</li>
                <li><strong>Lv 3 → Lv 4:</strong> 비즈니스 모델 혁신 및 전 직원 AI 리터러시 교육 강화.</li>
            </ul>
        """
    },
    {
        "filename": "textbook_business_poc_matrix.html",
        "title": "PoC 과제 선정 매트릭스",
        "subtitle": "Prioritizing AI Projects",
        "color": "teal",
        "content": """
            <h3>1. 어떤 과제부터 해야 할까?</h3>
            <p>하고 싶은 것(Desirability), 할 수 있는 것(Feasibility), 돈이 되는 것(Viability)의 교집합을 찾아야 합니다.</p>

            <h4 class="font-bold text-teal-800 mt-4">우선순위 선정 매트릭스 (2x2)</h4>
            <div class="relative w-full h-64 bg-slate-50 border-2 border-slate-300 rounded-lg mt-4 mb-8">
                <!-- X, Y Axis -->
                <div class="absolute bottom-0 left-0 w-full h-[2px] bg-slate-400"></div>
                <div class="absolute bottom-0 left-0 w-[2px] h-full bg-slate-400"></div>
                <div class="absolute bottom-2 right-2 text-xs font-bold">실현 가능성 (기술/데이터) ▶</div>
                <div class="absolute top-2 left-2 text-xs font-bold">▲ 비즈니스 임팩트 (매출/비용)</div>

                <!-- Zones -->
                <div class="absolute top-4 right-4 bg-teal-100 text-teal-800 p-2 rounded text-center text-xs font-bold border border-teal-300 shadow-sm w-24">
                    1순위: Quick Win<br>(하기 쉽고 효과 큼)
                </div>
                <div class="absolute top-4 left-12 bg-amber-100 text-amber-800 p-2 rounded text-center text-xs font-bold border border-amber-300 shadow-sm w-24">
                    2순위: Big Bet<br>(어렵지만 효과 큼)
                </div>
                 <div class="absolute bottom-12 right-4 bg-blue-100 text-blue-800 p-2 rounded text-center text-xs font-bold border border-blue-300 shadow-sm w-24">
                    3순위: Low Hanging<br>(소소한 개선)
                </div>
            </div>

            <h3>2. PoC 수행 계획서 핵심 항목 (Project Charter)</h3>
            <ul class="list-disc pl-6 space-y-2">
                <li><strong>문제 정의 (Problem Statement):</strong> 무엇이 문제인가? (예: 고객 문의가 폭주하여 응대율이 70%로 떨어짐)</li>
                <li><strong>가설 (Hypothesis):</strong> AI 챗봇을 도입하면 단순 문의 50%를 자동 처리할 수 있을 것이다.</li>
                <li><strong>성공 지표 (Metrics):</strong> 단순 문의 처리율 50% 달성, 상담원 만족도 4.0 이상.</li>
                <li><strong>필요 자원 (Resources):</strong> 지난 1년치 상담 로그 데이터(QA set), 개발자 2명, 2개월.</li>
            </ul>
        """
    },
    {
        "filename": "textbook_business_tco.html",
        "title": "ROI & TCO 시뮬레이션",
        "subtitle": "Financial Analysis for AI Projects",
        "color": "amber",
        "content": """
            <h3>1. AI 도입 비용의 진실 (TCO: Total Cost of Ownership)</h3>
            <p>눈에 보이는 모델 구독료는 빙산의 일각입니다.</p>
            
            <h4 class="font-bold text-amber-800 mt-4">숨겨진 비용 체크리스트</h4>
            <ul class="space-y-2 mt-2 bg-amber-50 p-4 rounded text-sm">
                <li>✅ <strong>데이터 준비 비용:</strong> 라벨링, 정제, 개인정보 마스킹 (전체 비용의 60% 차지)</li>
                <li>✅ <strong>운영 및 모니터링:</strong> 답변 품질 검수자(Human in the loop) 인건비</li>
                <li>✅ <strong>리스크 비용:</strong> 환각 현상으로 인한 법적 분쟁, 기업 이미지 손실 잠재 비용</li>
            </ul>

            <h3>2. ROI 시뮬레이션 예시</h3>
            <p>월 300만원 비용으로 월 1,000만원의 인건비 절감 효과를 낸다면?</p>
            <div class="overflow-x-auto">
                <table class="w-full text-sm text-center border mt-4">
                    <tr class="bg-slate-100 font-bold">
                        <td class="p-2 border">구분</td>
                        <td class="p-2 border">1개월 차</td>
                        <td class="p-2 border">6개월 차</td>
                        <td class="p-2 border">12개월 차</td>
                    </tr>
                    <tr>
                        <td class="bg-slate-50 font-bold p-2 border">누적 투자비</td>
                        <td class="p-2 border">-1,000만 (구축비)</td>
                        <td class="p-2 border">-2,500만</td>
                        <td class="p-2 border">-4,300만</td>
                    </tr>
                    <tr>
                        <td class="bg-slate-50 font-bold p-2 border">누적 이익</td>
                        <td class="p-2 border">0원 (안정화)</td>
                        <td class="p-2 border">+5,000만</td>
                        <td class="p-2 border">+1억 1천만</td>
                    </tr>
                    <tr class="text-red-600 font-bold bg-red-50">
                        <td class="p-2 border">Net Profit</td>
                        <td class="p-2 border">-1,000만</td>
                        <td class="p-2 border text-green-600">+2,500만 (BEP 달성)</td>
                        <td class="p-2 border text-green-600">+6,700만</td>
                    </tr>
                </table>
            </div>
        """
    },
    {
        "filename": "textbook_business_governance.html",
        "title": "AI 프로젝트 인력 및 거버넌스",
        "subtitle": "Building the Right Team & Policy",
        "color": "red",
        "content": """
            <h3>1. AI 드림팀 구성하기</h3>
            <p>개발자만 있다고 되는 것이 아닙니다. 도메인 전문가의 역할이 더 중요해지고 있습니다.</p>
            <div class="grid md:grid-cols-2 gap-4 mt-4">
                <div class="border p-3 rounded">
                    <strong class="text-red-700 block mb-1">💻 AI 엔지니어</strong>
                    <span class="text-xs text-slate-500">모델 튜닝, RAG 파이프라인 구축, 인프라 최적화</span>
                </div>
                <div class="border p-3 rounded">
                    <strong class="text-red-700 block mb-1">🗣️ 프롬프트 엔지니어</strong>
                    <span class="text-xs text-slate-500">LLM에게 질문을 잘 던져서 최적의 답변을 이끌어냄</span>
                </div>
                <div class="border p-3 rounded">
                    <strong class="text-red-700 block mb-1">👔 도메인 전문가 (SME)</strong>
                    <span class="text-xs text-slate-500">AI가 내놓은 답이 맞는지 검증하고, 비즈니스 룰 정의</span>
                </div>
                <div class="border p-3 rounded">
                    <strong class="text-red-700 block mb-1">⚖️ AI 윤리 담당자</strong>
                    <span class="text-xs text-slate-500">저작권, 개인정보, 편향성 이슈 등 법적 리스크 관리</span>
                </div>
            </div>

            <h3>2. AI 거버넌스 체크리스트</h3>
            <ul class="list-disc pl-6 space-y-2 mt-4">
                <li><strong>데이터 보안:</strong> 고객 정보를 퍼블릭 GPT에 입력하지 않도록 차단/마스킹 정책 수립.</li>
                <li><strong>책임 소재:</strong> AI가 실수했을 때 누가 책임질 것인가? (최종 승인권자는 항상 사람이어야 함)</li>
                <li><strong>투명성:</strong> 이 결과물이 AI가 만든 것임을 사용자에게 명시했는가? (Watermarking 등)</li>
            </ul>
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
        body {{ font-family: 'Pretendard', sans-serif; line-height: 1.8; }}
        .textbook-content h3 {{ font-size: 1.4rem; font-weight: 800; margin-top: 2.5rem; margin-bottom: 1rem; color: #1e293b; border-left: 5px solid #3b82f6; padding-left: 1rem; }}
        .textbook-content h4 {{ font-size: 1.15rem; font-weight: 700; margin-top: 1.5rem; margin-bottom: 0.8rem; color: #334155; }}
        .textbook-content p {{ margin-bottom: 1.2rem; color: #475569; font-size: 1.05rem; }}
        .textbook-content ul, .textbook-content ol {{ list-style-position: outside; margin-left: 1.5rem; margin-bottom: 1.5rem; color: #475569; }}
        .textbook-content li {{ margin-bottom: 0.5rem; }}
        .textbook-content table {{ width: 100%; border-collapse: collapse; margin-top: 1.5rem; margin-bottom: 1.5rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); border-radius: 0.5rem; overflow: hidden; }}
        .textbook-content th, .textbook-content td {{ padding: 1rem; border: 1px solid #e2e8f0; }}
        .textbook-content th {{ background-color: #f1f5f9; font-weight: 700; color: #1e293b; }}
        .textbook-content td {{ background-color: #ffffff; }}
        .textbook-content strong {{ color: #0f172a; font-weight: 700; background: linear-gradient(120deg, #e0f2fe 0%, #e0f2fe 100%); background-repeat: no-repeat; background-size: 100% 40%; background-position: 0 88%; }}
    </style>
</head>
<body class="bg-slate-50 min-h-screen">
    <div class="max-w-4xl mx-auto px-6 py-12">
        <div class="flex justify-between items-center mb-8">
            <a href="classroom_business.html" class="inline-flex items-center gap-2 text-slate-500 hover:text-slate-800 transition-colors">
                <i class="fas fa-arrow-left"></i> 강의실로 돌아가기
            </a>
            <div class="flex gap-2">
                 <button onclick="window.print()" class="text-slate-400 hover:text-slate-600 p-2"><i class="fas fa-print"></i></button>
            </div>
        </div>
        <div class="bg-white rounded-2xl shadow-2xl overflow-hidden border border-slate-100 print:shadow-none print:border-none">
            <div class="bg-gradient-to-r from-{color}-700 to-{color}-900 text-white p-10 md:p-16 relative overflow-hidden">
                <div class="absolute top-0 right-0 w-64 h-64 bg-white opacity-5 rounded-full blur-3xl -mr-16 -mt-16 pointer-events-none"></div>
                <span class="inline-block px-4 py-1.5 bg-white/10 rounded-full text-sm font-bold mb-6 backdrop-blur-md tracking-widest border border-white/20">LECTURE NOTE</span>
                <h1 class="text-3xl md:text-5xl font-extrabold mb-4 leading-tight">{title}</h1>
                <p class="text-white/80 text-xl font-light">{subtitle}</p>
            </div>
            <div class="p-10 md:p-16 textbook-content">
                {content}
                
                <div class="bg-slate-50 border border-slate-200 rounded-xl p-6 mt-12">
                    <h4 style="margin-top:0; border:none; color:#334155"><i class="fas fa-lightbulb text-yellow-500 mr-2"></i> 핵심 요약 (Takeaway)</h4>
                    <ul class="mb-0 mt-2 space-y-1 text-sm">
                        <li>AI 도입은 기술 문제가 아니라 <strong>비즈니스 모델의 변화</strong>입니다.</li>
                        <li>모든 것을 다 하려 하지 말고, <strong>확실한 성과(Quick Win)</strong>를 낼 수 있는 작은 과제부터 시작하세요.</li>
                        <li><strong>데이터 보안과 거버넌스</strong>는 선택이 아닌 필수 생존 요건입니다.</li>
                    </ul>
                </div>
            </div>
            <div class="bg-slate-50 p-8 border-t border-slate-200 flex justify-center print:hidden">
                <button onclick="history.back()" class="px-8 py-4 bg-white border border-slate-200 text-slate-700 rounded-xl font-bold hover:bg-slate-100 hover:border-slate-300 transition-all shadow-sm">
                    목록으로 돌아가기
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
# 3. GENERATE LECTURE PAGES (Class 1~4)
# ==========================================
def get_lecture_header(title, subtitle, day_label):
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
                <span class="text-6xl font-black opacity-20 block mb-[-10px]">{day_label}</span>
                <h1 class="text-3xl md:text-5xl font-extrabold tracking-tight">{title}</h1>
                <p class="text-xl opacity-90 font-light">{subtitle}</p>
            </div>
        </div>
    </header>
    """

def get_card(icon, color, title, desc, tags, view_link):
    tag_html = ""
    for tag in tags:
        tag_html += f'<span class="bg-{color}-50 text-{color}-700 px-3 py-1 rounded-md text-xs font-semibold">{tag}</span>'
    listen_link = "https://al-class.vercel.app/ai-lecture-room/dist/index.html"
    return f"""
                <div class="bg-white p-8 rounded-3xl border border-slate-100 card-shadow hover:border-{color}-200 transition-all group relative overflow-hidden">
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
        .gradient-bg { background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); }
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

# Class 1 (Day 1 AM)
c1 = base_html_start + get_lecture_header("산업별 AI 혁신 사례", "Day 1 (오전): 금융, 제조, 유통 분야 성공 사례 분석 (4시간)", "Class 01")
c1 += """<main class="max-w-5xl mx-auto px-6 py-12 space-y-12">
        <section class="space-y-6">
            <h2 class="text-2xl font-bold border-l-4 border-blue-600 pl-4">PART 1: 산업별 혁신 트렌드</h2>
            <div class="grid gap-6">"""
c1 += get_card("chart-line", "blue", "Global AI Innovation Cases", "금융(JP Morgan), 제조(Siemens), 유통(Nike) 등 산업별 Top-tier 기업들의 AI 도입 배경과 성과를 상세히 분석합니다.", ["Case Study", "Industry"], "textbook_business_cases.html")
c1 += get_card("microchip", "indigo", "AI Ecosystem & Tech Trends", "생성형 AI 기술 스택(앱-모델-인프라)을 이해하고, 멀티모달 및 온디바이스 AI 등 최신 기술 트렌드를 학습합니다.", ["Tech Trend", "GenAI"], "textbook_business_trends.html")
c1 += """</div></section></main>""" + base_html_end
with open("lecture_business_class1.html", "w", encoding="utf-8") as f: f.write(c1)

# Class 2 (Day 1 PM)
c2 = base_html_start + get_lecture_header("신규 사업 모델 발굴", "Day 1 (오후): AI 기반 비즈니스 모델(BM) 설계 및 전략 (4시간)", "Class 02")
c2 += """<main class="max-w-5xl mx-auto px-6 py-12 space-y-12">
        <section class="space-y-6">
             <h2 class="text-2xl font-bold border-l-4 border-violet-600 pl-4">PART 2: 비즈니스 모델 혁신</h2>
            <div class="grid gap-6">"""
c2 += get_card("lightbulb", "violet", "AI-Native Business Model", "기존 BM 캔버스 9 Block이 AI로 인해 어떻게 변화하는지 학습하고, 새로운 가치 제안(Value Proposition)을 도출합니다.", ["BM Canvas", "Innovation"], "textbook_business_bmc.html")
c2 += get_card("chess", "purple", "Competitive Analysis", "우리 기업만의 데이터 해자(Data Moat)를 구축하고, 경쟁사 대비 차별화된 AI 도입 전략을 수립합니다.", ["Strategy", "Moat"], "textbook_business_gap.html")
c2 += """</div></section></main>""" + base_html_end
with open("lecture_business_class2.html", "w", encoding="utf-8") as f: f.write(c2)

# Class 3 (Day 2 AM)
c3 = base_html_start + get_lecture_header("도입 로드맵 및 기획", "Day 2 (오전): 성숙도 진단 및 PoC 프로젝트 기획 실습 (4시간)", "Class 03")
c3 += """<main class="max-w-5xl mx-auto px-6 py-12 space-y-12">
        <section class="space-y-6">
             <h2 class="text-2xl font-bold border-l-4 border-green-600 pl-4">PART 3: 기획 및 로드맵</h2>
            <div class="grid gap-6">"""
c3 += get_card("clipboard-check", "green", "AI Maturity Assessment", "Gartner 모델을 기반으로 우리 조직의 AI 도입 준비 상태(성숙도)를 진단하고 단계별 성장 목표를 설정합니다.", ["Diagnosis", "Roadmap"], "textbook_business_maturity.html")
c3 += get_card("flask", "teal", "PoC Planning & Matrix", "실현 가능성과 비즈니스 임팩트를 고려한 우선순위 선정 매트릭스를 활용하여 성공적인 PoC 프로젝트를 기획합니다.", ["PoC", "Planning"], "textbook_business_poc_matrix.html")
c3 += """</div></section></main>""" + base_html_end
with open("lecture_business_class3.html", "w", encoding="utf-8") as f: f.write(c3)

# Class 4 (Day 2 PM)
c4 = base_html_start + get_lecture_header("실행 전략 및 거버넌스", "Day 2 (오후): ROI 분석 및 리스크 관리 전략 (4시간)", "Class 04")
c4 += """<main class="max-w-5xl mx-auto px-6 py-12 space-y-12">
        <section class="space-y-6">
             <h2 class="text-2xl font-bold border-l-4 border-amber-600 pl-4">PART 4: 실행 및 관리</h2>
            <div class="grid gap-6">"""
c4 += get_card("calculator", "amber", "TCO & ROI Analysis", "단순 구독료 외에 숨겨진 데이터 관리, 인력 비용 등을 포함한 총 소유 비용(TCO)과 투자 대비 수익(ROI)을 시뮬레이션합니다.", ["Financial", "ROI"], "textbook_business_tco.html")
c4 += get_card("shield-alt", "red", "AI Governance & Ethics", "AI 프로젝트를 위한 조직 구성(R&R)과 데이터 보안, 윤리적 리스크를 관리하는 거버넌스 체계를 수립합니다.", ["Risk", "Team"], "textbook_business_governance.html")
c4 += """</div></section></main>""" + base_html_end
with open("lecture_business_class4.html", "w", encoding="utf-8") as f: f.write(c4)

print("Generated all 4 separte lecture classes and 8 expanded textbooks.")
