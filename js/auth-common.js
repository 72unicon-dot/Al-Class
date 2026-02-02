/**
 * AI Class 공통 인증 모듈
 * 모든 강의 및 실습 페이지에서 사용하는 Firebase 인증 로직
 */

import { auth } from './firebase-config.js';
import { onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

/**
 * 페이지 접근 권한 확인 및 사용자 이메일 표시
 * @param {Object} options - 설정 옵션
 * @param {boolean} options.requireAuth - 인증 필수 여부 (기본: true)
 * @param {string} options.redirectUrl - 미인증 시 리다이렉트 URL (기본: 'index.html')
 * @param {string} options.emailDisplayId - 이메일 표시 요소 ID (기본: 'userEmailDisplay')
 * @param {boolean} options.showWelcomeMessage - 환영 메시지 표시 여부 (기본: true)
 */
export function initAuth(options = {}) {
    const {
        requireAuth = true,
        redirectUrl = 'index.html',
        emailDisplayId = 'userEmailDisplay',
        showWelcomeMessage = true
    } = options;

    onAuthStateChanged(auth, (user) => {
        if (!user && requireAuth) {
            alert("회원 전용 강의입니다. 로그인 후 이용해주세요.");
            window.location.href = redirectUrl;
        } else if (user) {
            displayUserEmail(user.email, emailDisplayId, showWelcomeMessage);
        }
    });
}

/**
 * 사용자 이메일 표시
 * @param {string} email - 사용자 이메일
 * @param {string} elementId - 표시할 요소 ID
 * @param {boolean} showWelcome - 환영 메시지 표시 여부
 */
function displayUserEmail(email, elementId, showWelcome) {
    const emailDisplay = document.getElementById(elementId);
    if (emailDisplay) {
        emailDisplay.innerText = showWelcome ? `${email}님 환영합니다` : email;
    }
}

/**
 * 현재 로그인한 사용자 정보 가져오기
 * @returns {Promise<Object|null>} 사용자 객체 또는 null
 */
export function getCurrentUser() {
    return new Promise((resolve) => {
        const unsubscribe = onAuthStateChanged(auth, (user) => {
            unsubscribe();
            resolve(user);
        });
    });
}

/**
 * 로그아웃
 */
export async function logout() {
    try {
        await auth.signOut();
        window.location.href = 'index.html';
    } catch (error) {
        console.error('로그아웃 오류:', error);
        alert('로그아웃 중 오류가 발생했습니다.');
    }
}

// 자동 초기화 (기본 설정)
if (typeof document !== 'undefined') {
    document.addEventListener('DOMContentLoaded', () => {
        // 페이지에서 data-auth-required 속성 확인
        const body = document.body;
        if (body.dataset.authRequired !== 'false') {
            initAuth();
        }
    });
}
