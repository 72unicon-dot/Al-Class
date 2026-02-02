/**
 * 공통 헤더 기능 모듈
 * 모든 강의 및 실습 페이지에서 사용
 */

// Firebase 인증 상태 확인 및 사용자 이메일 표시
export function initializeHeader() {
    // Firebase가 로드되었는지 확인
    if (typeof auth === 'undefined') {
        console.error('Firebase auth is not initialized');
        return;
    }

    // 사용자 인증 상태 확인
    onAuthStateChanged(auth, (user) => {
        if (!user) {
            alert("회원 전용 강의입니다. 로그인 후 이용해주세요.");
            window.location.href = 'index.html';
        } else {
            // 사용자 이메일 표시
            displayUserEmail(user.email);
        }
    });
}

// 사용자 이메일 표시 함수
function displayUserEmail(email) {
    const emailDisplay = document.getElementById('userEmailDisplay');
    if (emailDisplay) {
        emailDisplay.innerText = email + "님 환영합니다";
    }
}

// 표준 헤더 HTML 생성 함수
export function createStandardHeader(options = {}) {
    const {
        title = '강의 제목',
        subtitle = '강의 설명',
        backLink = 'day01_lecture.html',
        backText = '강의로 돌아가기'
    } = options;

    return `
    <header class="gradient-bg text-white py-12 px-8 relative overflow-hidden">
        <!-- 사용자 정보 및 버튼 영역 -->
        <div class="absolute top-4 right-4 md:top-6 md:right-8 flex items-center gap-3 z-20">
            <span id="userEmailDisplay" class="text-sm text-white/90 font-medium hidden md:inline"></span>
            <a href="${backLink}"
                class="inline-flex items-center gap-2 px-4 py-2 bg-white/20 backdrop-blur-md text-white text-sm font-semibold rounded-full border border-white/30 hover:bg-white/30 transition-all">
                <i class="fas fa-arrow-left"></i> <span class="hidden sm:inline">${backText}</span>
            </a>
        </div>
        
        <div class="max-w-4xl mx-auto">
            <h1 class="text-3xl md:text-4xl font-bold mb-2">${title}</h1>
            <p class="text-xl opacity-90">${subtitle}</p>
        </div>
    </header>
    `;
}

// 실습 페이지 헤더 생성 함수
export function createPracticeHeader(options = {}) {
    const {
        title = '실습 제목',
        backLink = 'day01_lecture.html',
        iconClass = 'fa-code',
        iconColor = 'blue'
    } = options;

    return `
    <header class="bg-white border-b border-slate-200 sticky top-0 z-50">
        <div class="max-w-5xl mx-auto px-4 py-4 flex justify-between items-center">
            <div class="flex items-center space-x-2">
                <div class="bg-${iconColor}-600 text-white p-2 rounded-lg">
                    <i class="fas ${iconClass} text-xl"></i>
                </div>
                <h1 class="text-xl font-bold">${title}</h1>
            </div>
            <a href="${backLink}" class="text-sm font-bold text-slate-500 hover:text-${iconColor}-600">
                <i class="fas fa-arrow-left mr-1"></i> 강의로 돌아가기
            </a>
        </div>
    </header>
    `;
}

// DOM이 로드된 후 자동 초기화
if (typeof document !== 'undefined') {
    document.addEventListener('DOMContentLoaded', () => {
        // 헤더 초기화는 각 페이지에서 명시적으로 호출
        // initializeHeader();
    });
}
