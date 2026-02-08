export interface Lecture {
    title: string;
    file: string;
}

export interface Course {
    id: string;
    title: string;
    path: string;
    lectures: Lecture[];
}

export const COURSES: Course[] = [
    {
        id: 'c01',
        title: '01. AI 기초 (Basics)',
        path: 'c01_basics',
        lectures: [
            { title: 'Session 1: AI의 이해와 도구 세팅', file: 'textbook_basics_01_understanding.html' },
            { title: 'Session 2: 프롬프트 엔지니어링', file: 'textbook_basics_02_prompt.html' },
            { title: 'Session 3: 업무 시간 단축', file: 'textbook_basics_03_productivity.html' },
            { title: 'Session 4: 검색과 데이터 분석', file: 'textbook_basics_04_analysis.html' },
            { title: 'Session 5: 나만의 AI 비서 & 마무리', file: 'textbook_basics_05_assistant.html' }
        ]
    },
    {
        id: 'c02',
        title: '02. AI 비즈니스 전략 (Business)',
        path: 'c02_business',
        lectures: [
            // Day 1
            { title: 'Day 1-1: 글로벌 AI 트렌드', file: 'textbook_business_01_01_trends.html' },
            { title: 'Day 1-2: 비즈니스 AI 구조', file: 'textbook_business_01_02_structure.html' },
            { title: 'Day 1-3: 주요 AI 기술 (Vision)', file: 'textbook_business_01_03_tech.html' },
            { title: 'Day 1-4: 고성능 문서 제작', file: 'textbook_business_01_04_docs.html' },
            { title: 'Day 1-5: Vibe Coding 기초', file: 'textbook_business_01_05_vibe.html' },
            // Day 2
            { title: 'Day 2-1: 프롬프트 엔지니어링', file: 'textbook_business_02_01_prompt.html' },
            { title: 'Day 2-2: 주요 AI 기술 (NLP)', file: 'textbook_business_02_02_nlp.html' },
            { title: 'Day 2-3: Vibe Coding & API', file: 'textbook_business_02_03_api.html' },
            { title: 'Day 2-4: 프로젝트 기획 & 웹앱', file: 'textbook_business_02_04_project.html' },
            { title: 'Day 2-5: AI 윤리 & 마무리', file: 'textbook_business_02_05_ethics.html' }
        ]
    },
    {
        id: 'c03',
        title: '03. 마스터 클래스 (Master)',
        path: 'c03_master_class',
        lectures: [
            { title: 'Day 1: 생성형 AI 입문', file: 'day01_lecture.html' },
            { title: 'Day 2: 프롬프트 고급', file: 'day02_lecture.html' },
            { title: 'Day 3: 이미지 생성', file: 'day03_lecture.html' },
            { title: 'Day 4: 비디오/오디오', file: 'day04_lecture.html' },
            { title: 'Day 5: 업무 자동화', file: 'day05_lecture.html' },
            { title: 'Day 6: 코딩과 개발', file: 'day06_lecture.html' },
            { title: 'Day 7: 웹 앱 개발', file: 'day07_lecture.html' },
            { title: 'Day 8: 배포 및 운영', file: 'day08_lecture.html' }
        ]
    },
    {
        id: 'c04',
        title: '04. AI 심화 (Advanced)',
        path: 'c04_advanced',
                lectures: [
            { title: 'Class 1: RAG 아키텍처 & Vector DB', file: 'textbook_advanced_class01.html' },
            { title: 'Class 2: LangChain 핵심 컴포넌트', file: 'textbook_advanced_class02.html' },
            { title: 'Class 3: 문서 로딩 및 분할 전략', file: 'textbook_advanced_class03.html' },
            { title: 'Class 4: Retriever 최적화', file: 'textbook_advanced_class04.html' },
            { title: 'Class 5: RAG 성능 평가', file: 'textbook_advanced_class05.html' },
            { title: 'Class 6: AI 에이전트 기초', file: 'textbook_advanced_class06.html' },
            { title: 'Class 7: Function Calling & Tools', file: 'textbook_advanced_class07.html' },
            { title: 'Class 8: Multi-Agent Systems', file: 'textbook_advanced_class08.html' },
            { title: 'Class 9: Memory & State', file: 'textbook_advanced_class09.html' },
            { title: 'Class 10: Autonomous Agents 구축', file: 'textbook_advanced_class10.html' },
            { title: 'Class 11: LLM 아키텍처 이해', file: 'textbook_advanced_class11.html' },
            { title: 'Class 12: 데이터셋 준비 및 전처리', file: 'textbook_advanced_class12.html' },
            { title: 'Class 13: PEFT & LoRA', file: 'textbook_advanced_class13.html' },
            { title: 'Class 14: Quantization & QLoRA', file: 'textbook_advanced_class14.html' },
            { title: 'Class 15: 모델 평가 및 벤치마크', file: 'textbook_advanced_class15.html' },
            { title: 'Class 16: LLM 서빙 및 최적화', file: 'textbook_advanced_class16.html' },
            { title: 'Class 17: Prompt Engineering at Scale', file: 'textbook_advanced_class17.html' },
            { title: 'Class 18: Security & Guardrails', file: 'textbook_advanced_class18.html' },
            { title: 'Class 19: Enterprise AI Strategy', file: 'textbook_advanced_class19.html' },
            { title: 'Class 20: Final Capstone Project', file: 'textbook_advanced_class20.html' },
        ]},
    {
        id: 'c05',
        title: '05. AI 마케팅 (Marketing)',
        path: 'c05_marketing',
                        lectures: [
            { title: 'Class 1: AI 마케팅 개요 및 트렌드', file: 'textbook_marketing_class01.html' },
            { title: 'Class 2: 고객 페르소나 및 타겟팅 전략', file: 'textbook_marketing_class02.html' },
            { title: 'Class 3: AI 카피라이팅 기초', file: 'textbook_marketing_class03.html' },
            { title: 'Class 4: 채널별 맞춤 텍스트 콘텐츠 실습', file: 'textbook_marketing_class04.html' },
            { title: 'Class 5: AI 이미지 생성 프롬프트', file: 'textbook_marketing_class05.html' },
            { title: 'Class 6: 디자인 자동화', file: 'textbook_marketing_class06.html' },
            { title: 'Class 7: 숏폼 영상 기획 및 생성', file: 'textbook_marketing_class07.html' },
            { title: 'Class 8: 퍼포먼스 마케팅 데이터 분석', file: 'textbook_marketing_class08.html' },
            { title: 'Class 9: 마케팅 자동화 파이프라인', file: 'textbook_marketing_class09.html' },
            { title: 'Class 10: 실전 캠페인 기획 및 발표', file: 'textbook_marketing_class10.html' },
        ]},
    {
        id: 'c06',
        title: '06. AI 제조혁신 (Manufacturing)',
        path: 'c06_manufacturing',
                        lectures: [
            { title: 'Class 1: 제조업의 AI 혁신', file: 'textbook_manufacturing_class01.html' },
            { title: 'Class 2: IoT 센서 데이터 수집', file: 'textbook_manufacturing_class02.html' },
            { title: 'Class 3: 컴퓨터 비전 품질 검사', file: 'textbook_manufacturing_class03.html' },
            { title: 'Class 4: 딥러닝 불량 탐지 실습', file: 'textbook_manufacturing_class04.html' },
            { title: 'Class 5: 예지 보전(PdM)의 이해', file: 'textbook_manufacturing_class05.html' },
            { title: 'Class 6: 고장 예측 모델링', file: 'textbook_manufacturing_class06.html' },
            { title: 'Class 7: 수요 예측 및 재고 최적화', file: 'textbook_manufacturing_class07.html' },
            { title: 'Class 8: 공정 최적화 및 Digital Twin', file: 'textbook_manufacturing_class08.html' },
            { title: 'Class 9: 생성형 AI와 제조업', file: 'textbook_manufacturing_class09.html' },
            { title: 'Class 10: 제조 AI 프로젝트', file: 'textbook_manufacturing_class10.html' },
        ]},
    {
        id: 'c07',
        title: '07. AI 데이터 분석 (Data)',
        path: 'c07_data',
                lectures: [
            { title: 'Class 1: Day 1: Pandas AI & Code Interpreter', file: 'textbook_data_class01.html' },
            { title: 'Class 2: Day 1: 데이터 전처리 및 정제', file: 'textbook_data_class02.html' },
            { title: 'Class 3: Day 2: 머신러닝 기초 및 분류', file: 'textbook_data_class03.html' },
            { title: 'Class 4: Day 2: 회귀 분석 및 예측', file: 'textbook_data_class04.html' },
            { title: 'Class 5: Day 3: 데이터 시각화 기초', file: 'textbook_data_class05.html' },
            { title: 'Class 6: Day 3: 인터랙티브 대시보드', file: 'textbook_data_class06.html' },
            { title: 'Class 7: Day 4: 텍스트 데이터 분석', file: 'textbook_data_class07.html' },
            { title: 'Class 8: Day 4: 시계열 데이터 분석', file: 'textbook_data_class08.html' },
            { title: 'Class 9: Day 5: 딥러닝 입문', file: 'textbook_data_class09.html' },
            { title: 'Class 10: Day 5: 종합 데이터 프로젝트', file: 'textbook_data_class10.html' },
        ]},
    {
        id: 'c08',
        title: '08. AI 영상 제작 (Video)',
        path: 'c08_video',
                lectures: [
            { title: 'Class 1: Day 1: AI 영상 기획 & 스토리보드', file: 'textbook_video_class01.html' },
            { title: 'Class 2: Day 1: AI 이미지 생성 심화', file: 'textbook_video_class02.html' },
            { title: 'Class 3: Day 2: 영상 생성 AI 기초', file: 'textbook_video_class03.html' },
            { title: 'Class 4: Day 2: 영상 생성 AI 심화', file: 'textbook_video_class04.html' },
            { title: 'Class 5: Day 3: AI 캐릭터 & 가상 인간', file: 'textbook_video_class05.html' },
            { title: 'Class 6: Day 3: AI 음성 합성 & 더빙', file: 'textbook_video_class06.html' },
            { title: 'Class 7: Day 4: 영상 편집 & 효과', file: 'textbook_video_class07.html' },
            { title: 'Class 8: Day 4: 자막 및 번역 자동화', file: 'textbook_video_class08.html' },
            { title: 'Class 9: Day 5: 숏폼 콘텐츠 제작', file: 'textbook_video_class09.html' },
            { title: 'Class 10: Day 5: 종합 영상 프로젝트', file: 'textbook_video_class10.html' },
        ]},
    {
        id: 'c09',
        title: '09. AI 리더십 (Leadership)',
        path: 'c09_leadership',
        lectures: [
            { title: 'Class 01: AI 경영 전략', file: 'textbook_leadership_class01.html' },
            { title: 'Class 02: 조직 혁신', file: 'textbook_leadership_class02.html' }
        ]
    },
    {
        id: 'c10',
        title: '10. AI 컨설턴트 (Consultant)',
        path: 'c10_consultant',
                lectures: [
            { title: 'Class 1: AI 컨설팅 기초', file: 'textbook_consultant_class01.html' },
            { title: 'Class 2: As-Is vs To-Be 분석', file: 'textbook_consultant_class02.html' },
            { title: 'Class 3: AI 도입 타당성 분석', file: 'textbook_consultant_class03.html' },
            { title: 'Class 4: RFP 및 제안서 작성', file: 'textbook_consultant_class04.html' },
            { title: 'Class 5: 프로젝트 관리 (PM)', file: 'textbook_consultant_class05.html' },
            { title: 'Class 6: 커뮤니케이션 & 협상', file: 'textbook_consultant_class06.html' },
            { title: 'Class 7: 프로세스 혁신 (PI)', file: 'textbook_consultant_class07.html' },
            { title: 'Class 8: AI 전략 로드맵 수립', file: 'textbook_consultant_class08.html' },
            { title: 'Class 9: AI 윤리 및 리스크 관리', file: 'textbook_consultant_class09.html' },
            { title: 'Class 10: 캡스톤 프로젝트: 전략 컨설팅', file: 'textbook_consultant_class10.html' },
        ]},
    {
        id: 'c11',
        title: '11. AI 앱 크리에이터 (App)',
        path: 'c11_app_creator',
                lectures: [
            { title: 'Class 1: 노코드/로우코드 기초', file: 'textbook_app_creator_class01.html' },
            { title: 'Class 2: UI/UX 디자인 & DB 설계', file: 'textbook_app_creator_class02.html' },
            { title: 'Class 3: 앱 배포 및 수익화', file: 'textbook_app_creator_class03.html' },
            { title: 'Class 4: LangChain 기초', file: 'textbook_app_creator_class04.html' },
            { title: 'Class 5: Vector DB & RAG', file: 'textbook_app_creator_class05.html' },
            { title: 'Class 6: 챗봇 개발 I: 프롬프트 엔지니어링', file: 'textbook_app_creator_class06.html' },
            { title: 'Class 7: 챗봇 개발 II: Advanced', file: 'textbook_app_creator_class07.html' },
            { title: 'Class 8: 멀티채널 연동', file: 'textbook_app_creator_class08.html' },
            { title: 'Class 9: 성능 최적화 및 운영', file: 'textbook_app_creator_class09.html' },
            { title: 'Class 10: 캡스톤 프로젝트: 상용 앱 출시', file: 'textbook_app_creator_class10.html' },
        ]},
    {
        id: 'c12',
        title: '12. AI 윤리 (Ethics)',
        path: 'c12_ethics',
        lectures: [
            { title: '저작권 분쟁', file: 'textbook_ethics_copyright.html' },
            { title: '프롬프트 보안', file: 'textbook_ethics_prompt.html' },
            { title: 'AI 산출물 책임', file: 'textbook_ethics_accountability.html' },
            { title: '할루시네이션', file: 'textbook_ethics_hallucination.html' },
            { title: 'EU AI Act', file: 'textbook_ethics_eu_act.html' },
            { title: '개인정보보호', file: 'textbook_ethics_privacy.html' },
            { title: '정보유출 대응', file: 'textbook_ethics_leak.html' }
        ]
    }
];
