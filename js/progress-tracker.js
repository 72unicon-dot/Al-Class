/**
 * 학습 진도 추적 모듈
 * Firestore를 사용하여 사용자별 학습 진도 저장 및 조회
 */

import { db } from './firebase-config.js';
import {
    doc,
    getDoc,
    setDoc,
    updateDoc,
    serverTimestamp
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

// 커리큘럼 구조 정의
const CURRICULUM = {
    day01: {
        lectures: ['ai_concept', 'ai_trends', 'ai_search', 'ai_ethics', 'ai_caution', 'gemini', 'notebooklm', 'research_method'],
        practices: ['chatbot', 'notebooklm', 'report']
    },
    day02: {
        lectures: ['gems_ai', 'llm_comparison', 'prompt_principles', 'role_cot'],
        practices: ['automation', 'claude', 'gems']
    },
    day03: {
        lectures: ['canva_ai', 'design_principles', 'image_params', 'nano_banana'],
        practices: ['detail', 'branding', 'cardnews', 'sns']
    },
    day04: {
        lectures: ['video_ai', 'runway_gen3', 'audio_synthesis', 'voice_cloning'],
        practices: ['video', 'voice', 'convert']
    },
    day05: {
        lectures: ['automation_design', 'make_zapier', 'nocode_overview', 'trigger_action'],
        practices: ['customer', 'email', 'news']
    },
    day06: {
        lectures: ['coding_prompt', 'cursor_setup', 'pair_programming', 'vibe_coding'],
        practices: ['cursor', 'html', 'python']
    },
    day07: {
        lectures: ['api_integration', 'database_connection', 'framework_overview', 'web_app_structure'],
        practices: ['chatbot_app', 'todo', 'ui']
    },
    day08: {
        lectures: ['cloud_deployment', 'domain_https', 'git_github', 'maintenance'],
        practices: ['deploy', 'final', 'project']
    }
};

/**
 * 사용자 진도 데이터 초기화
 * @param {string} userId - 사용자 ID
 * @returns {Promise<Object>} 초기화된 진도 데이터
 */
export async function initializeProgress(userId) {
    const initialData = {
        userId: userId,
        lastUpdated: serverTimestamp(),
        totalProgress: 0,
        days: {}
    };

    // 각 Day 초기화
    for (const [day, content] of Object.entries(CURRICULUM)) {
        initialData.days[day] = {
            progress: 0,
            lectures: {},
            practices: {}
        };

        // 강의 초기화
        content.lectures.forEach(lectureId => {
            initialData.days[day].lectures[lectureId] = {
                completed: false,
                completedAt: null,
                timeSpent: 0
            };
        });

        // 실습 초기화
        content.practices.forEach(practiceId => {
            initialData.days[day].practices[practiceId] = {
                completed: false,
                completedAt: null
            };
        });
    }

    // Firestore에 저장
    await setDoc(doc(db, 'progress', userId), initialData);
    return initialData;
}

/**
 * 사용자 진도 데이터 가져오기
 * @param {string} userId - 사용자 ID
 * @returns {Promise<Object>} 진도 데이터
 */
export async function getProgress(userId) {
    try {
        const progressRef = doc(db, 'progress', userId);
        const progressSnap = await getDoc(progressRef);

        if (progressSnap.exists()) {
            return progressSnap.data();
        } else {
            // 데이터가 없으면 초기화
            return await initializeProgress(userId);
        }
    } catch (error) {
        console.error('진도 데이터 가져오기 오류:', error);
        throw error;
    }
}

/**
 * 강의 완료 표시
 * @param {string} userId - 사용자 ID
 * @param {string} day - Day (예: 'day01')
 * @param {string} lectureId - 강의 ID
 * @param {number} timeSpent - 학습 시간 (초, 선택사항)
 */
export async function markLectureComplete(userId, day, lectureId, timeSpent = 0) {
    try {
        const progressRef = doc(db, 'progress', userId);

        await updateDoc(progressRef, {
            [`days.${day}.lectures.${lectureId}.completed`]: true,
            [`days.${day}.lectures.${lectureId}.completedAt`]: serverTimestamp(),
            [`days.${day}.lectures.${lectureId}.timeSpent`]: timeSpent,
            lastUpdated: serverTimestamp()
        });

        // 진도율 재계산
        await updateDayProgress(userId, day);
    } catch (error) {
        console.error('강의 완료 표시 오류:', error);
        throw error;
    }
}

/**
 * 실습 완료 표시
 * @param {string} userId - 사용자 ID
 * @param {string} day - Day
 * @param {string} practiceId - 실습 ID
 */
export async function markPracticeComplete(userId, day, practiceId) {
    try {
        const progressRef = doc(db, 'progress', userId);

        await updateDoc(progressRef, {
            [`days.${day}.practices.${practiceId}.completed`]: true,
            [`days.${day}.practices.${practiceId}.completedAt`]: serverTimestamp(),
            lastUpdated: serverTimestamp()
        });

        // 진도율 재계산
        await updateDayProgress(userId, day);
    } catch (error) {
        console.error('실습 완료 표시 오류:', error);
        throw error;
    }
}

/**
 * Day별 진도율 업데이트
 * @param {string} userId - 사용자 ID
 * @param {string} day - Day
 */
async function updateDayProgress(userId, day) {
    try {
        const progressData = await getProgress(userId);
        const dayData = progressData.days[day];

        // 완료된 항목 수 계산
        const completedLectures = Object.values(dayData.lectures)
            .filter(l => l.completed).length;
        const completedPractices = Object.values(dayData.practices)
            .filter(p => p.completed).length;

        const totalCompleted = completedLectures + completedPractices;
        const totalItems = Object.keys(dayData.lectures).length +
            Object.keys(dayData.practices).length;

        // Day별 진도율
        const dayProgress = (totalCompleted / totalItems) * 100;

        // 전체 진도율 계산
        const totalProgress = calculateTotalProgress(progressData);

        // Firestore 업데이트
        await updateDoc(doc(db, 'progress', userId), {
            [`days.${day}.progress`]: dayProgress,
            totalProgress: totalProgress,
            lastUpdated: serverTimestamp()
        });
    } catch (error) {
        console.error('진도율 업데이트 오류:', error);
        throw error;
    }
}

/**
 * 전체 진도율 계산
 * @param {Object} progressData - 진도 데이터
 * @returns {number} 전체 진도율 (0-100)
 */
function calculateTotalProgress(progressData) {
    let totalCompleted = 0;
    let totalItems = 0;

    for (const [day, dayData] of Object.entries(progressData.days)) {
        const completedLectures = Object.values(dayData.lectures)
            .filter(l => l.completed).length;
        const completedPractices = Object.values(dayData.practices)
            .filter(p => p.completed).length;

        totalCompleted += completedLectures + completedPractices;
        totalItems += Object.keys(dayData.lectures).length +
            Object.keys(dayData.practices).length;
    }

    return totalItems > 0 ? (totalCompleted / totalItems) * 100 : 0;
}

/**
 * 다음 학습할 항목 추천
 * @param {string} userId - 사용자 ID
 * @returns {Promise<Object>} 추천 항목 {day, type, id}
 */
export async function getNextLesson(userId) {
    try {
        const progressData = await getProgress(userId);

        for (const [day, dayData] of Object.entries(progressData.days)) {
            // 미완료 강의 찾기
            for (const [lectureId, lecture] of Object.entries(dayData.lectures)) {
                if (!lecture.completed) {
                    return {
                        day: day,
                        type: 'lecture',
                        id: lectureId,
                        title: getLectureTitle(day, lectureId)
                    };
                }
            }

            // 미완료 실습 찾기
            for (const [practiceId, practice] of Object.entries(dayData.practices)) {
                if (!practice.completed) {
                    return {
                        day: day,
                        type: 'practice',
                        id: practiceId,
                        title: getPracticeTitle(day, practiceId)
                    };
                }
            }
        }

        // 모든 학습 완료
        return null;
    } catch (error) {
        console.error('다음 학습 추천 오류:', error);
        return null;
    }
}

/**
 * 강의 제목 가져오기 (임시 - 실제로는 데이터베이스에서)
 */
function getLectureTitle(day, lectureId) {
    // 실제 구현에서는 강의 제목 매핑 필요
    return `${day} - ${lectureId}`;
}

/**
 * 실습 제목 가져오기 (임시)
 */
function getPracticeTitle(day, practiceId) {
    return `${day} 실습 - ${practiceId}`;
}

/**
 * 학습 통계 가져오기
 * @param {string} userId - 사용자 ID
 * @returns {Promise<Object>} 통계 데이터
 */
export async function getStatistics(userId) {
    try {
        const progressData = await getProgress(userId);

        let totalLectures = 0;
        let completedLectures = 0;
        let totalPractices = 0;
        let completedPractices = 0;
        let totalTimeSpent = 0;

        for (const dayData of Object.values(progressData.days)) {
            totalLectures += Object.keys(dayData.lectures).length;
            completedLectures += Object.values(dayData.lectures)
                .filter(l => l.completed).length;

            totalPractices += Object.keys(dayData.practices).length;
            completedPractices += Object.values(dayData.practices)
                .filter(p => p.completed).length;

            totalTimeSpent += Object.values(dayData.lectures)
                .reduce((sum, l) => sum + (l.timeSpent || 0), 0);
        }

        return {
            totalProgress: progressData.totalProgress,
            lectures: {
                total: totalLectures,
                completed: completedLectures,
                remaining: totalLectures - completedLectures
            },
            practices: {
                total: totalPractices,
                completed: completedPractices,
                remaining: totalPractices - completedPractices
            },
            totalTimeSpent: totalTimeSpent,
            lastUpdated: progressData.lastUpdated
        };
    } catch (error) {
        console.error('통계 가져오기 오류:', error);
        return null;
    }
}
