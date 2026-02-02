# 🔒 보안 가이드

이 문서는 AI Class 애플리케이션의 보안 설정 및 관리 방법을 안내합니다.

---

## 📋 목차

1. [환경 변수 설정](#환경-변수-설정)
2. [Firebase Security Rules](#firebase-security-rules)
3. [Vercel 배포 설정](#vercel-배포-설정)
4. [API 키 관리](#api-키-관리)

---

## 환경 변수 설정

### 로컬 개발 환경

AI 강의실 앱(`ai-lecture-room`)에서 사용하는 환경 변수:

```bash
# ai-lecture-room/.env.local
VITE_GEMINI_API_KEY=your_actual_api_key_here
```

> [!IMPORTANT]
> `.env.local` 파일은 절대 Git에 커밋하지 마세요. `.gitignore`에 `*.local` 패턴이 포함되어 있는지 확인하세요.

### Vercel 배포 환경

1. Vercel 대시보드 접속: https://vercel.com/dashboard
2. 프로젝트 선택: `al-class`
3. **Settings** → **Environment Variables** 메뉴로 이동
4. 다음 환경 변수 추가:

| Name | Value | Environment |
|------|-------|-------------|
| `VITE_GEMINI_API_KEY` | `your_actual_api_key` | Production, Preview, Development |

5. **Save** 클릭
6. 프로젝트 재배포

---

## Firebase Security Rules

### Firestore Rules

Firebase Console (https://console.firebase.google.com/project/lms01-bc677/firestore/rules)에서 다음 규칙을 설정하세요:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    
    // 공지사항: 모두 읽기 가능, 관리자만 쓰기
    match /notices/{noticeId} {
      allow read: if true;
      allow create, update, delete: if request.auth != null && 
                                      request.auth.token.admin == true;
    }
    
    // 사용자 데이터: 본인만 접근 가능
    match /users/{userId} {
      allow read, write: if request.auth != null && 
                           request.auth.uid == userId;
    }
    
    // 리소스: 모두 읽기 가능, 관리자만 쓰기
    match /resources/{resourceId} {
      allow read: if true;
      allow write: if request.auth != null && 
                     request.auth.token.admin == true;
    }
    
    // 기본: 인증된 사용자만 읽기 가능
    match /{document=**} {
      allow read: if request.auth != null;
      allow write: if false;
    }
  }
}
```

### Storage Rules

Firebase Console (https://console.firebase.google.com/project/lms01-bc677/storage/rules)에서 다음 규칙을 설정하세요:

```javascript
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    
    // 강의 자료: 모두 읽기 가능, 관리자만 업로드
    match /resources/{allPaths=**} {
      allow read: if true;
      allow write: if request.auth != null && 
                     request.auth.token.admin == true;
    }
    
    // 과정 소개 PDF
    match /courseIntro.pdf {
      allow read: if true;
      allow write: if request.auth != null && 
                     request.auth.token.admin == true;
    }
    
    // 기본: 인증된 사용자만 읽기
    match /{allPaths=**} {
      allow read: if request.auth != null;
      allow write: if false;
    }
  }
}
```

### 관리자 권한 설정

Firebase Admin SDK를 사용하여 관리자 Custom Claims 설정:

```javascript
// Node.js 환경에서 실행
const admin = require('firebase-admin');
admin.initializeApp();

// 관리자 권한 부여
admin.auth().setCustomUserClaims('USER_UID', { admin: true })
  .then(() => {
    console.log('관리자 권한이 설정되었습니다.');
  });
```

---

## Vercel 배포 설정

### 자동 배포

- `main` 브랜치에 push하면 자동으로 프로덕션 배포
- 다른 브랜치에 push하면 프리뷰 배포 생성

### 수동 재배포

1. Vercel 대시보드에서 프로젝트 선택
2. **Deployments** 탭
3. 최신 배포의 **⋯** 메뉴 → **Redeploy**

---

## API 키 관리

### Firebase API 키 제한

Firebase Console (https://console.cloud.google.com/apis/credentials?project=lms01-bc677)에서:

1. **API 키** 섹션에서 Firebase API 키 선택
2. **애플리케이션 제한사항** 설정:
   - **HTTP 리퍼러(웹사이트)** 선택
   - 허용할 도메인 추가:
     ```
     https://al-class.vercel.app/*
     https://*.vercel.app/*
     http://localhost:*
     ```

### Gemini API 키 사용량 모니터링

Google AI Studio (https://aistudio.google.com/)에서:

1. **API Keys** 메뉴
2. 사용량 및 할당량 확인
3. 필요시 사용량 제한 설정

---

## 보안 체크리스트

배포 전 확인사항:

- [ ] `.env.local` 파일이 `.gitignore`에 포함되어 있음
- [ ] Vercel 환경 변수가 설정되어 있음
- [ ] Firebase Firestore Rules가 적용되어 있음
- [ ] Firebase Storage Rules가 적용되어 있음
- [ ] Firebase API 키에 HTTP Referrer 제한이 설정되어 있음
- [ ] 관리자 계정에 Custom Claims가 설정되어 있음
- [ ] API 사용량 모니터링이 활성화되어 있음

---

## 문제 해결

### AI 강의 조수가 작동하지 않는 경우

1. 브라우저 콘솔에서 에러 확인
2. Vercel 환경 변수 `VITE_GEMINI_API_KEY` 확인
3. Gemini API 키가 유효한지 확인
4. API 사용량 한도 초과 여부 확인

### Firebase 권한 오류

1. Firebase Console에서 Security Rules 확인
2. 사용자 인증 상태 확인
3. 관리자 Custom Claims 설정 확인

---

**마지막 업데이트**: 2026-02-02
