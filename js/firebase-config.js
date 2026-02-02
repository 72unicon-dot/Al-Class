// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-analytics.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";
import { getStorage } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-storage.js";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyDkd--6Gr_RarAVY8ik-dwXs5jNdam9WwE",
    authDomain: "lms01-bc677.firebaseapp.com",
    projectId: "lms01-bc677",
    storageBucket: "lms01-bc677.firebasestorage.app",
    messagingSenderId: "111431869097",
    appId: "1:111431869097:web:e9cffc9aa3afa4bb5effb8",
    measurementId: "G-SEZ92EMG38"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth(app);
const db = getFirestore(app);
const storage = getStorage(app);

// Export services
export { app, auth, db, analytics, storage };
