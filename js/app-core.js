/**
 * AI Class Core Application Logic
 * Consolidates Authentication, Login Modal, and Common UI functions.
 */

import { auth } from './firebase-config.js';
import {
    onAuthStateChanged,
    signInWithEmailAndPassword,
    signOut,
    GoogleAuthProvider,
    signInWithPopup
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

// ==========================================
// 1. Login Modal UI & Logic
// ==========================================

const LOGIN_MODAL_ID = 'userLoginModal';

/**
 * Injects the Login Modal HTML into the document body if it doesn't exist.
 */
function injectLoginModal() {
    if (document.getElementById(LOGIN_MODAL_ID)) return;

    const modalHTML = `
    <div id="${LOGIN_MODAL_ID}" class="fixed inset-0 z-[100] hidden">
        <div class="absolute inset-0 bg-black/60 backdrop-blur-sm" onclick="window.closeLoginModal()"></div>
        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-white w-full max-w-sm rounded-2xl shadow-2xl p-8 transform transition-all">
            <div class="text-center mb-6">
                <div class="w-12 h-12 bg-indigo-100 text-indigo-600 rounded-full flex items-center justify-center mx-auto mb-3 text-xl">
                    <i class="fas fa-user-graduate"></i>
                </div>
                <h3 class="text-2xl font-bold text-gray-800">수강생 로그인</h3>
                <p class="text-gray-500 text-sm mt-1">강의실 입장을 위해 로그인해주세요</p>
            </div>
            
            <div class="space-y-4">
                <button id="googleLoginBtn" type="button" class="w-full py-3 bg-white border border-gray-300 text-gray-700 rounded-xl font-bold hover:bg-gray-50 transition-colors shadow-sm flex items-center justify-center gap-2">
                    <img src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg" class="w-5 h-5">
                    구글 계정으로 로그인
                </button>
                
                <div class="relative flex py-2 items-center">
                    <div class="flex-grow border-t border-gray-200"></div>
                    <span class="flex-shrink-0 mx-4 text-gray-400 text-xs">또는 이메일로 로그인</span>
                    <div class="flex-grow border-t border-gray-200"></div>
                </div>

                <form id="userLoginForm" class="space-y-4">
                    <div>
                        <input type="email" id="userEmail" class="w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:outline-none" placeholder="이메일" required>
                    </div>
                    <div>
                        <input type="password" id="userPw" class="w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:outline-none" placeholder="비밀번호" required>
                    </div>
                    <button type="submit" class="w-full py-3 bg-indigo-600 text-white rounded-xl font-bold hover:bg-indigo-700 transition-colors shadow-lg shadow-indigo-200">
                        이메일 로그인
                    </button>
                </form>
            </div>
            <button onclick="window.closeLoginModal()" class="w-full mt-3 py-2 text-gray-400 hover:text-gray-600 text-sm font-medium">닫기</button>
        </div>
    </div>`;

    document.body.insertAdjacentHTML('beforeend', modalHTML);

    // Bind events shortly after injection
    setTimeout(bindLoginEvents, 50);
}

function bindLoginEvents() {
    // Email Login
    const loginForm = document.getElementById('userLoginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const email = document.getElementById('userEmail').value;
            const pw = document.getElementById('userPw').value;
            const btn = loginForm.querySelector('button[type="submit"]');

            try {
                const originalText = btn.innerHTML;
                btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> 로그인 중...';
                btn.disabled = true;

                await signInWithEmailAndPassword(auth, email, pw);
                window.closeLoginModal();
                btn.innerHTML = originalText;
                btn.disabled = false;
            } catch (error) {
                console.error("Email Login Error:", error);
                alert("로그인 실패: 이메일 또는 비밀번호를 확인해주세요.");
                btn.disabled = false;
                btn.innerHTML = '이메일 로그인';
            }
        });
    }

    // Google Login
    const googleBtn = document.getElementById('googleLoginBtn');
    if (googleBtn) {
        googleBtn.addEventListener('click', async () => {
            try {
                const provider = new GoogleAuthProvider();
                await signInWithPopup(auth, provider);
                window.closeLoginModal();
            } catch (error) {
                console.error("Google Login Error:", error);
                alert("구글 로그인 실패: " + error.message);
            }
        });
    }
}

// ==========================================
// 2. Global Window Helpers
// ==========================================

window.openLoginModal = () => {
    const modal = document.getElementById(LOGIN_MODAL_ID);
    if (!modal) {
        injectLoginModal(); // Just in case
        setTimeout(() => document.getElementById(LOGIN_MODAL_ID)?.classList.remove('hidden'), 50);
    } else {
        modal.classList.remove('hidden');
    }
};

window.closeLoginModal = () => {
    const modal = document.getElementById(LOGIN_MODAL_ID);
    if (modal) modal.classList.add('hidden');
};

window.userLogout = async () => {
    if (confirm("로그아웃 하시겠습니까?")) {
        try {
            await signOut(auth);
            window.location.reload();
        } catch (error) {
            console.error("Logout Error:", error);
            alert("로그아웃 중 오류가 발생했습니다.");
        }
    }
};

// ==========================================
// 3. Auth State & Initialization
// ==========================================

/**
 * Initializes the application: setup Auth listener, inject modals, handle auto-login params.
 * @param {Object} options Configuration options
 * @param {Function} options.onLogin Callback when user logs in
 * @param {Function} options.onLogout Callback when user logs out
 * @param {boolean} options.requireAuth Whether to redirect if not logged in
 */
export function initApp(options = {}) {
    const { onLogin, onLogout, requireAuth = false, redirectUrl = 'index.html' } = options;

    // 1. Inject UI Components
    injectLoginModal();

    // 2. Monitor Auth State
    onAuthStateChanged(auth, (user) => {
        if (user) {
            // User is signed in
            console.log("User logged in:", user.email);
            if (onLogin) onLogin(user);
        } else {
            // User is signed out
            console.log("User logged out");
            if (requireAuth) {
                alert("로그인이 필요한 페이지입니다.");
                window.location.href = redirectUrl;
            }
            if (onLogout) onLogout();
        }
    });

    // 3. Check for Auto-Login URL Param (?apply=true)
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('apply') === 'true') {
        setTimeout(() => window.openLoginModal(), 500);
    }
}
