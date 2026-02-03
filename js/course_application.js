import { db, auth } from './firebase-config.js';
import { collection, addDoc, serverTimestamp, query, where, getDocs } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";
import { onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

// ========================================================
// Course Application Logic
// ========================================================

/**
 * Initialize the course application functionality.
 * Should be imported and called at the bottom of course pages.
 * @param {string} courseId - Unique ID for the course (e.g., 'intro_ethics')
 * @param {string} courseName - Human readable name (e.g., 'AI 윤리 입문')
 */
export function initCourseApplication(courseId, courseName) {
    console.log(`Initializing application logic for: ${courseName} (${courseId})`);

    const applyBtn = document.getElementById('applyBtn');
    if (!applyBtn) return; // Only run if button exists (logged out state might hide it in original logic, but we need to control it)

    // Override the default onclick from HTML if possible, or assume listener takes precedence
    // We need to handle the state checking ourselves.

    // We expect the original page logic to handle Hide/Show of applyBtn based on Auth.
    // BUT, we want "Apply" to be visible even if logged in? Or if logged in, change to "Apply Now"?
    // The current template hides 'applyBtn' when logged in and shows 'enterBtn'.
    // We need to change this behavior: 
    // IF logged in AND NOT applied -> Show "Apply Now"
    // IF logged in AND applied -> Show "Enter Classroom"

    // Changing that requires changing the inline script in every HTML file, which is hard.
    // Strategy: We will inject a new "Real Apply Button" dynamically or hijack the existing one.

    // Let's attach the click handler to the document body to catch the button click if it exists
    // checking auth state inside.

    applyBtn.onclick = async (e) => {
        // Prevent default modal opening if we want to check logic first
        // But the inline onclick="window.openLoginModal()" might fire first or parallel.
        // We will modify the HTML to remove inline onclick using a python script later.
        // For now, let's assume we clean up the HTML.
        e.preventDefault();

        const user = auth.currentUser;
        if (!user) {
            // Not logged in -> Show Login Modal
            if (window.openLoginModal) window.openLoginModal();
            else alert("로그인이 필요합니다.");
            return;
        }

        // Logged in -> Confirm Application
        if (confirm(`${courseName} 과정을 신청하시겠습니까?`)) {
            await saveApplication(user, courseId, courseName);
        }
    };
}

// Function to save to Firestore
async function saveApplication(user, courseId, courseName) {
    try {
        // Check for duplicate application
        const q = query(collection(db, "applications"),
            where("userId", "==", user.uid),
            where("courseId", "==", courseId));
        const querySnapshot = await getDocs(q);

        if (!querySnapshot.empty) {
            alert("이미 신청한 과정입니다. 내 강의실로 이동합니다.");
            window.location.href = "dashboard.html";
            return;
        }

        // Save new application
        await addDoc(collection(db, "applications"), {
            userId: user.uid,
            userEmail: user.email,
            userName: user.displayName || user.email.split('@')[0],
            courseId: courseId,
            courseName: courseName,
            appliedAt: serverTimestamp(),
            status: 'pending' // pending -> approved
        });

        alert("수강 신청이 완료되었습니다! 강의실로 입장해주세요.");
        window.location.reload(); // Refresh to update UI state

    } catch (error) {
        console.error("Error saving application:", error);
        alert("수강 신청 중 오류가 발생했습니다: " + error.message);
    }
}

// Global helper to check application status and update UI
// This should be called by the page's auth state change
export async function checkApplicationStatus(user, courseId) {
    if (!user) return false;

    // Check if applied
    const q = query(collection(db, "applications"),
        where("userId", "==", user.uid),
        where("courseId", "==", courseId));
    const querySnapshot = await getDocs(q);

    return !querySnapshot.empty; // True if applied
}
