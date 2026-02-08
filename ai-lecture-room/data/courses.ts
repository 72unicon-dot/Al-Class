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
        lectures: Array.from({ length: 20 }, (_, i) => ({
            title: `Class ${String(i + 1).padStart(2, '0')}`,
            file: `textbook_advanced_class${String(i + 1).padStart(2, '0')}.html`
        }))
    },
    {
        id: 'c05',
        title: '05. AI 마케팅 (Marketing)',
        path: 'c05_marketing',
        lectures: Array.from({ length: 10 }, (_, i) => ({
            title: `Class ${String(i + 1).padStart(2, '0')}`,
            file: `textbook_marketing_class${String(i + 1).padStart(2, '0')}.html`
        }))
    },
    {
        id: 'c06',
        title: '06. AI 제조혁신 (Manufacturing)',
        path: 'c06_manufacturing',
        lectures: Array.from({ length: 10 }, (_, i) => ({
            title: `Class ${String(i + 1).padStart(2, '0')}`,
            file: `textbook_manufacturing_class${String(i + 1).padStart(2, '0')}.html`
        }))
    },
    {
        id: 'c07',
        title: '07. AI 데이터 분석 (Data)',
        path: 'c07_data',
        lectures: Array.from({ length: 10 }, (_, i) => ({
            title: `Class ${String(i + 1).padStart(2, '0')}`,
            file: `textbook_data_class${String(i + 1).padStart(2, '0')}.html`
        }))
    },
    {
        id: 'c08',
        title: '08. AI 영상 제작 (Video)',
        path: 'c08_video',
        lectures: Array.from({ length: 10 }, (_, i) => ({
            title: `Class ${String(i + 1).padStart(2, '0')}`,
            file: `textbook_video_class${String(i + 1).padStart(2, '0')}.html`
        }))
    },
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
        lectures: Array.from({ length: 10 }, (_, i) => ({
            title: `Class ${String(i + 1).padStart(2, '0')}`,
            file: `textbook_consultant_class${String(i + 1).padStart(2, '0')}.html`
        }))
    },
    {
        id: 'c11',
        title: '11. AI 앱 크리에이터 (App)',
        path: 'c11_app_creator',
        lectures: Array.from({ length: 10 }, (_, i) => ({
            title: `Class ${String(i + 1).padStart(2, '0')}`,
            file: `textbook_app_creator_class${String(i + 1).padStart(2, '0')}.html`
        }))
    },
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
