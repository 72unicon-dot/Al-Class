import { db, storage } from './firebase-config.js';
import { collection, query, where, getDocs } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

async function loadClassResources() {
    // 1. Get Context from Page
    // Expecting meta tags or body attributes: <meta name="course-id" content="basics">, <meta name="class-id" content="01">
    const courseId = document.querySelector('meta[name="course-id"]')?.content;
    const classId = document.querySelector('meta[name="class-id"]')?.content;

    if (!courseId || !classId) {
        console.warn("Course/Class context missing");
        return;
    }

    console.log(`Loading resources for ${courseId} - Class ${classId}`);

    try {
        // 2. Query Firestore
        const q = query(
            collection(db, "resources"),
            where("course", "==", courseId),
            where("classNum", "==", classId)
        );

        const querySnapshot = await getDocs(q);

        // 3. Map to Buttons
        querySnapshot.forEach((doc) => {
            const data = doc.data();
            // Find button with matching data-title
            // Titles might have minor spacing diffs, so simple trim/match
            const btn = document.querySelector(`button[data-title="${data.title}"]`);

            if (btn) {
                console.log(`Resource found for: ${data.title}`);
                // Enable Button
                btn.onclick = () => window.open(data.url, '_blank');
                btn.classList.remove('bg-slate-200', 'text-slate-700', 'hover:bg-slate-300'); // Remove disabled style

                // Add Active Style (e.g., specific color based on course? or generic active color)
                // Let's use a generic 'brand' color or keep it simple
                btn.classList.add('bg-rose-500', 'text-white', 'hover:bg-rose-600', 'cursor-pointer');
                btn.innerHTML = '<i class="fas fa-file-download"></i> PDF 다운로드';
                btn.title = data.filename;
            }
        });

    } catch (error) {
        console.error("Error loading resources:", error);
    }
}

// Initial Load
document.addEventListener('DOMContentLoaded', loadClassResources);
