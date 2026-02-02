/**
 * 검색 모듈
 * 강의 및 실습 콘텐츠 검색 기능
 */

// 검색 인덱스 - 모든 강의 및 실습 데이터
const SEARCH_INDEX = {
    // Day 01
    day01_ai_concept: {
        day: 'day01',
        dayName: 'Day 01',
        type: 'lecture',
        title: 'AI 개념과 역사',
        description: '인공지능의 기본 개념과 발전 과정을 학습합니다',
        keywords: ['AI', '인공지능', '머신러닝', '딥러닝', '역사', '개념'],
        url: 'day01_ai_concept.html'
    },
    day01_ai_trends: {
        day: 'day01',
        dayName: 'Day 01',
        type: 'lecture',
        title: 'AI 트렌드',
        description: '최신 AI 기술 동향과 미래 전망',
        keywords: ['AI', '트렌드', '동향', '미래', 'GPT', 'Gemini'],
        url: 'day01_ai_trends.html'
    },
    day01_ai_search: {
        day: 'day01',
        dayName: 'Day 01',
        type: 'lecture',
        title: 'AI 검색 활용',
        description: 'AI 기반 검색 엔진 활용 방법',
        keywords: ['검색', 'Perplexity', 'AI검색', '정보탐색'],
        url: 'day01_ai_search.html'
    },
    day01_ai_ethics: {
        day: 'day01',
        dayName: 'Day 01',
        type: 'lecture',
        title: 'AI 윤리',
        description: 'AI 사용 시 고려해야 할 윤리적 문제',
        keywords: ['윤리', '책임', '편향', '프라이버시'],
        url: 'day01_ai_ethics.html'
    },
    day01_gemini: {
        day: 'day01',
        dayName: 'Day 01',
        type: 'lecture',
        title: 'Gemini 활용',
        description: 'Google Gemini 사용법과 활용 사례',
        keywords: ['Gemini', 'Google', 'AI모델', '활용'],
        url: 'day01_gemini.html'
    },
    day01_notebooklm: {
        day: 'day01',
        dayName: 'Day 01',
        type: 'lecture',
        title: 'NotebookLM',
        description: 'AI 기반 노트 정리 도구',
        keywords: ['NotebookLM', '노트', '정리', '학습'],
        url: 'day01_notebooklm.html'
    },
    day01_practice_chatbot: {
        day: 'day01',
        dayName: 'Day 01',
        type: 'practice',
        title: 'AI 챗봇 만들기',
        description: 'ChatGPT를 활용한 챗봇 실습',
        keywords: ['챗봇', 'ChatGPT', '대화형AI', '실습'],
        url: 'day01_practice_chatbot.html'
    },

    // Day 02
    day02_llm_comparison: {
        day: 'day02',
        dayName: 'Day 02',
        type: 'lecture',
        title: 'LLM 비교',
        description: 'ChatGPT vs Gemini vs Claude 비교 분석',
        keywords: ['LLM', 'ChatGPT', 'Gemini', 'Claude', '비교'],
        url: 'day02_llm_comparison.html'
    },
    day02_prompt_principles: {
        day: 'day02',
        dayName: 'Day 02',
        type: 'lecture',
        title: '프롬프트 원칙',
        description: '효과적인 프롬프트 작성 원칙',
        keywords: ['프롬프트', '원칙', '작성법', '엔지니어링'],
        url: 'day02_prompt_principles.html'
    },
    day02_role_cot: {
        day: 'day02',
        dayName: 'Day 02',
        type: 'lecture',
        title: '역할 부여 & CoT',
        description: '역할 부여와 사고의 연쇄 기법',
        keywords: ['역할', 'CoT', '사고의연쇄', '프롬프트'],
        url: 'day02_role_cot.html'
    },

    // Day 03
    day03_canva_ai: {
        day: 'day03',
        dayName: 'Day 03',
        type: 'lecture',
        title: 'Canva AI',
        description: 'Canva AI 기능 마스터',
        keywords: ['Canva', '디자인', 'AI디자인', '이미지생성'],
        url: 'day03_canva_ai.html'
    },
    day03_design_principles: {
        day: 'day03',
        dayName: 'Day 03',
        type: 'lecture',
        title: '디자인 원칙',
        description: 'AI 디자인 원칙과 실전 활용',
        keywords: ['디자인', '원칙', '비주얼', '레이아웃'],
        url: 'day03_design_principles.html'
    },
    day03_nano_banana: {
        day: 'day03',
        dayName: 'Day 03',
        type: 'lecture',
        title: 'Nano Banana',
        description: 'AI 이미지 생성 플랫폼',
        keywords: ['NanoBanana', '이미지생성', 'AI이미지'],
        url: 'day03_nano_banana.html'
    },

    // Day 04
    day04_video_ai: {
        day: 'day04',
        dayName: 'Day 04',
        type: 'lecture',
        title: 'AI 영상 생성',
        description: 'AI 영상 생성 기술과 활용',
        keywords: ['영상', '비디오', 'AI영상', 'Text-to-Video'],
        url: 'day04_video_ai.html'
    },
    day04_runway_gen3: {
        day: 'day04',
        dayName: 'Day 04',
        type: 'lecture',
        title: 'Runway Gen-3',
        description: 'Runway Gen-3 핵심 기능',
        keywords: ['Runway', 'Gen3', '영상생성', 'AI영상'],
        url: 'day04_runway_gen3.html'
    },
    day04_voice_cloning: {
        day: 'day04',
        dayName: 'Day 04',
        type: 'lecture',
        title: '음성 복제',
        description: 'AI 음성 복제 기술',
        keywords: ['음성', '복제', 'TTS', '음성합성'],
        url: 'day04_voice_cloning.html'
    },

    // Day 05
    day05_automation_design: {
        day: 'day05',
        dayName: 'Day 05',
        type: 'lecture',
        title: '자동화 설계',
        description: '업무 자동화 설계 방법론',
        keywords: ['자동화', '워크플로우', '설계', '효율화'],
        url: 'day05_automation_design.html'
    },
    day05_make_zapier: {
        day: 'day05',
        dayName: 'Day 05',
        type: 'lecture',
        title: 'Make & Zapier',
        description: 'Make와 Zapier 활용법',
        keywords: ['Make', 'Zapier', '자동화', '연동'],
        url: 'day05_make_zapier.html'
    },
    day05_nocode_overview: {
        day: 'day05',
        dayName: 'Day 05',
        type: 'lecture',
        title: '노코드 개요',
        description: '노코드 도구 소개와 활용',
        keywords: ['노코드', 'NoCode', '도구', '개발'],
        url: 'day05_nocode_overview.html'
    },

    // Day 06
    day06_coding_prompt: {
        day: 'day06',
        dayName: 'Day 06',
        type: 'lecture',
        title: '코딩 프롬프트',
        description: '효과적인 코딩 프롬프트 작성',
        keywords: ['코딩', '프롬프트', '개발', '프로그래밍'],
        url: 'day06_coding_prompt.html'
    },
    day06_cursor_setup: {
        day: 'day06',
        dayName: 'Day 06',
        type: 'lecture',
        title: 'Cursor 설정',
        description: 'Cursor AI 에디터 설정과 사용법',
        keywords: ['Cursor', 'AI에디터', '설정', 'IDE'],
        url: 'day06_cursor_setup.html'
    },
    day06_pair_programming: {
        day: 'day06',
        dayName: 'Day 06',
        type: 'lecture',
        title: 'AI 페어 프로그래밍',
        description: 'AI와 함께하는 페어 프로그래밍',
        keywords: ['페어프로그래밍', 'AI코딩', '협업'],
        url: 'day06_pair_programming.html'
    },

    // Day 07
    day07_api_integration: {
        day: 'day07',
        dayName: 'Day 07',
        type: 'lecture',
        title: 'API 연동',
        description: 'API 통합과 활용 방법',
        keywords: ['API', '연동', '통합', 'REST'],
        url: 'day07_api_integration.html'
    },
    day07_database_connection: {
        day: 'day07',
        dayName: 'Day 07',
        type: 'lecture',
        title: '데이터베이스 연결',
        description: '데이터베이스 연결과 관리',
        keywords: ['데이터베이스', 'DB', '연결', 'Firebase'],
        url: 'day07_database_connection.html'
    },
    day07_framework_overview: {
        day: 'day07',
        dayName: 'Day 07',
        type: 'lecture',
        title: '프레임워크 개요',
        description: '웹 프레임워크 소개',
        keywords: ['프레임워크', 'React', 'Vue', 'Next.js'],
        url: 'day07_framework_overview.html'
    },

    // Day 08
    day08_cloud_deployment: {
        day: 'day08',
        dayName: 'Day 08',
        type: 'lecture',
        title: '클라우드 배포',
        description: '클라우드 플랫폼 배포 방법',
        keywords: ['배포', '클라우드', 'Vercel', 'Netlify'],
        url: 'day08_cloud_deployment.html'
    },
    day08_git_github: {
        day: 'day08',
        dayName: 'Day 08',
        type: 'lecture',
        title: 'Git & GitHub',
        description: 'Git과 GitHub 활용법',
        keywords: ['Git', 'GitHub', '버전관리', '협업'],
        url: 'day08_git_github.html'
    },
    day08_domain_https: {
        day: 'day08',
        dayName: 'Day 08',
        type: 'lecture',
        title: '도메인 & HTTPS',
        description: '도메인 연결과 HTTPS 설정',
        keywords: ['도메인', 'HTTPS', 'SSL', '보안'],
        url: 'day08_domain_https.html'
    }
};

/**
 * 검색 실행
 * @param {string} query - 검색어
 * @param {Object} filters - 필터 옵션 {day, type}
 * @returns {Array} 검색 결과 배열
 */
export function performSearch(query, filters = {}) {
    if (!query || query.trim().length < 2) {
        return [];
    }

    const normalized = normalizeQuery(query);
    const results = [];

    Object.entries(SEARCH_INDEX).forEach(([id, item]) => {
        // 필터 적용
        if (filters.day && item.day !== filters.day) return;
        if (filters.type && item.type !== filters.type) return;

        // 매칭 점수 계산
        const score = calculateMatchScore(item, normalized);

        if (score > 0) {
            results.push({
                id,
                ...item,
                score,
                highlightedTitle: highlightKeywords(item.title, query)
            });
        }
    });

    // 점수순 정렬
    return results.sort((a, b) => b.score - a.score);
}

/**
 * 검색어 정규화
 * @param {string} query - 검색어
 * @returns {string} 정규화된 검색어
 */
function normalizeQuery(query) {
    return query.toLowerCase().trim();
}

/**
 * 매칭 점수 계산
 * @param {Object} item - 검색 대상 항목
 * @param {string} query - 정규화된 검색어
 * @returns {number} 매칭 점수
 */
function calculateMatchScore(item, query) {
    let score = 0;

    const titleLower = item.title.toLowerCase();
    const descLower = item.description.toLowerCase();

    // 제목 완전 일치: 100점
    if (titleLower === query) {
        score += 100;
    }
    // 제목 시작 일치: 50점
    else if (titleLower.startsWith(query)) {
        score += 50;
    }
    // 제목 포함: 30점
    else if (titleLower.includes(query)) {
        score += 30;
    }

    // 설명 포함: 10점
    if (descLower.includes(query)) {
        score += 10;
    }

    // 키워드 일치: 20점
    const keywordMatch = item.keywords.some(keyword =>
        keyword.toLowerCase().includes(query)
    );
    if (keywordMatch) {
        score += 20;
    }

    return score;
}

/**
 * 키워드 하이라이팅
 * @param {string} text - 원본 텍스트
 * @param {string} query - 검색어
 * @returns {string} 하이라이팅된 HTML
 */
function highlightKeywords(text, query) {
    if (!query) return text;

    const regex = new RegExp(`(${escapeRegex(query)})`, 'gi');
    return text.replace(regex, '<mark>$1</mark>');
}

/**
 * 정규식 특수문자 이스케이프
 * @param {string} str - 문자열
 * @returns {string} 이스케이프된 문자열
 */
function escapeRegex(str) {
    return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

/**
 * 자동완성 제안
 * @param {string} query - 검색어
 * @param {number} limit - 최대 제안 수
 * @returns {Array} 제안 목록
 */
export function getSuggestions(query, limit = 5) {
    if (!query || query.trim().length < 2) {
        return [];
    }

    const normalized = normalizeQuery(query);
    const suggestions = new Set();

    Object.values(SEARCH_INDEX).forEach(item => {
        // 제목에서 제안
        if (item.title.toLowerCase().includes(normalized)) {
            suggestions.add(item.title);
        }

        // 키워드에서 제안
        item.keywords.forEach(keyword => {
            if (keyword.toLowerCase().includes(normalized)) {
                suggestions.add(keyword);
            }
        });
    });

    return Array.from(suggestions).slice(0, limit);
}

/**
 * 인기 검색어 (임시 - 실제로는 분석 데이터 활용)
 * @returns {Array} 인기 검색어 목록
 */
export function getPopularSearches() {
    return [
        'AI',
        '프롬프트',
        'ChatGPT',
        'Canva',
        '자동화',
        'Cursor',
        '배포'
    ];
}
