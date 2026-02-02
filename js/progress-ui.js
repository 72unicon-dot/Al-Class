/**
 * 진도 추적 UI 컴포넌트
 * 강의실 페이지 및 강의 페이지에서 사용
 */

import { getProgress, getStatistics, getNextLesson } from './progress-tracker.js';

/**
 * 전체 진도율 표시
 * @param {string} userId - 사용자 ID
 * @param {string} containerId - 컨테이너 요소 ID
 */
export async function displayTotalProgress(userId, containerId = 'progressContainer') {
    try {
        const stats = await getStatistics(userId);
        if (!stats) return;

        const container = document.getElementById(containerId);
        if (!container) return;

        container.innerHTML = `
            <div class="progress-overview-card">
                <div class="progress-header">
                    <h3 class="progress-title">
                        <i class="fas fa-chart-line"></i>
                        학습 진도
                    </h3>
                    <span class="progress-percentage">${stats.totalProgress.toFixed(1)}%</span>
                </div>
                
                <div class="progress-bar-container">
                    <div class="progress-bar-fill" style="width: ${stats.totalProgress}%"></div>
                </div>
                
                <div class="progress-stats">
                    <div class="stat-item">
                        <i class="fas fa-book text-blue-600"></i>
                        <div>
                            <p class="stat-label">강의</p>
                            <p class="stat-value">${stats.lectures.completed}/${stats.lectures.total}</p>
                        </div>
                    </div>
                    <div class="stat-item">
                        <i class="fas fa-code text-purple-600"></i>
                        <div>
                            <p class="stat-label">실습</p>
                            <p class="stat-value">${stats.practices.completed}/${stats.practices.total}</p>
                        </div>
                    </div>
                    <div class="stat-item">
                        <i class="fas fa-clock text-green-600"></i>
                        <div>
                            <p class="stat-label">학습 시간</p>
                            <p class="stat-value">${formatTime(stats.totalTimeSpent)}</p>
                        </div>
                    </div>
                </div>
            </div>
        `;
    } catch (error) {
        console.error('진도율 표시 오류:', error);
    }
}

/**
 * Day별 진도율 표시
 * @param {string} userId - 사용자 ID
 * @param {string} day - Day (예: 'day01')
 * @param {string} elementId - 표시할 요소 ID
 */
export async function displayDayProgress(userId, day, elementId) {
    try {
        const progressData = await getProgress(userId);
        const dayData = progressData.days[day];

        const element = document.getElementById(elementId);
        if (!element) return;

        const progress = dayData.progress || 0;

        element.innerHTML = `
            <div class="day-progress-badge">
                <div class="progress-circle" data-progress="${progress}">
                    <svg width="60" height="60">
                        <circle cx="30" cy="30" r="25" fill="none" stroke="#e5e7eb" stroke-width="5"/>
                        <circle cx="30" cy="30" r="25" fill="none" stroke="#3b82f6" stroke-width="5"
                                stroke-dasharray="${2 * Math.PI * 25}"
                                stroke-dashoffset="${2 * Math.PI * 25 * (1 - progress / 100)}"
                                transform="rotate(-90 30 30)"/>
                    </svg>
                    <span class="progress-text">${progress.toFixed(0)}%</span>
                </div>
            </div>
        `;
    } catch (error) {
        console.error('Day 진도율 표시 오류:', error);
    }
}

/**
 * 다음 학습 추천 표시
 * @param {string} userId - 사용자 ID
 * @param {string} containerId - 컨테이너 요소 ID
 */
export async function displayNextLesson(userId, containerId = 'nextLessonContainer') {
    try {
        const nextLesson = await getNextLesson(userId);
        const container = document.getElementById(containerId);

        if (!container) return;

        if (!nextLesson) {
            container.innerHTML = `
                <div class="next-lesson-card completed">
                    <i class="fas fa-trophy text-yellow-500 text-4xl mb-4"></i>
                    <h3 class="text-xl font-bold">축하합니다!</h3>
                    <p class="text-gray-600">모든 학습을 완료했습니다.</p>
                </div>
            `;
            return;
        }

        const icon = nextLesson.type === 'lecture' ? 'fa-book' : 'fa-code';
        const typeText = nextLesson.type === 'lecture' ? '강의' : '실습';
        const link = `${nextLesson.day}_${nextLesson.type === 'lecture' ? nextLesson.id : 'practice_' + nextLesson.id}.html`;

        container.innerHTML = `
            <div class="next-lesson-card">
                <div class="next-lesson-header">
                    <i class="fas ${icon}"></i>
                    <span>다음 학습</span>
                </div>
                <h3 class="next-lesson-title">${nextLesson.title}</h3>
                <p class="next-lesson-type">${typeText}</p>
                <a href="${link}" class="next-lesson-btn">
                    학습 시작하기
                    <i class="fas fa-arrow-right ml-2"></i>
                </a>
            </div>
        `;
    } catch (error) {
        console.error('다음 학습 표시 오류:', error);
    }
}

/**
 * 강의 완료 버튼 추가
 * @param {string} userId - 사용자 ID
 * @param {string} day - Day
 * @param {string} lectureId - 강의 ID
 * @param {string} containerId - 컨테이너 요소 ID
 */
export function addCompleteButton(userId, day, lectureId, containerId = 'completeButtonContainer') {
    const container = document.getElementById(containerId);
    if (!container) return;

    container.innerHTML = `
        <div class="complete-button-wrapper">
            <button id="markCompleteBtn" class="complete-btn">
                <i class="fas fa-check-circle"></i>
                이 강의 완료하기
            </button>
        </div>
    `;

    // 버튼 클릭 이벤트
    document.getElementById('markCompleteBtn').addEventListener('click', async () => {
        try {
            const { markLectureComplete } = await import('./progress-tracker.js');
            const { showToast } = await import('./utils.js');

            await markLectureComplete(userId, day, lectureId);

            // UI 업데이트
            const btn = document.getElementById('markCompleteBtn');
            btn.innerHTML = '<i class="fas fa-check"></i> 완료됨';
            btn.classList.add('completed');
            btn.disabled = true;

            showToast('강의를 완료했습니다!', 'success');
        } catch (error) {
            console.error('완료 처리 오류:', error);
            showToast('오류가 발생했습니다.', 'error');
        }
    });
}

/**
 * 시간 포맷팅 (초 → 시간:분)
 * @param {number} seconds - 초
 * @returns {string} 포맷된 시간
 */
function formatTime(seconds) {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);

    if (hours > 0) {
        return `${hours}시간 ${minutes}분`;
    } else if (minutes > 0) {
        return `${minutes}분`;
    } else {
        return '1분 미만';
    }
}

/**
 * 진도 데이터 실시간 업데이트 (Firestore 리스너)
 * @param {string} userId - 사용자 ID
 * @param {Function} callback - 업데이트 콜백
 */
export function listenToProgress(userId, callback) {
    import('./firebase-config.js').then(({ db }) => {
        import('https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js').then(({ doc, onSnapshot }) => {
            const progressRef = doc(db, 'progress', userId);

            return onSnapshot(progressRef, (snapshot) => {
                if (snapshot.exists()) {
                    callback(snapshot.data());
                }
            });
        });
    });
}
