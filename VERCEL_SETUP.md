# 🚀 Vercel 환경 변수 설정 가이드

AI Class 앱의 AI 강의 조수 기능을 활성화하려면 Vercel에 환경 변수를 설정해야 합니다.

---

## 📋 설정 단계

### 1. Vercel 대시보드 접속

브라우저에서 다음 URL로 이동:
```
https://vercel.com/dashboard
```

### 2. 프로젝트 선택

- 프로젝트 목록에서 **`al-class`** 프로젝트 클릭

### 3. Settings 메뉴 이동

- 상단 탭에서 **Settings** 클릭

### 4. Environment Variables 설정

1. 왼쪽 사이드바에서 **Environment Variables** 클릭
2. **Add New** 버튼 클릭
3. 다음 정보 입력:

| 필드 | 값 |
|------|-----|
| **Name** | `VITE_GEMINI_API_KEY` |
| **Value** | `AIzaSyCzo3F_zbuOJRlyHFPvD4mKXB0lM0PblwU` |
| **Environment** | ✅ Production<br>✅ Preview<br>✅ Development |

4. **Save** 버튼 클릭

### 5. 재배포

환경 변수를 추가한 후 프로젝트를 재배포해야 합니다:

1. 상단 탭에서 **Deployments** 클릭
2. 최신 배포 항목의 **⋯** (점 3개) 메뉴 클릭
3. **Redeploy** 선택
4. **Redeploy** 버튼 클릭하여 확인

---

## ✅ 확인 방법

재배포가 완료되면 (약 1-2분 소요):

1. https://al-class.vercel.app/ 접속
2. **강의실 입장하기** 클릭
3. 우측 하단의 **AI 강의 조수** 아이콘 클릭
4. 메시지 입력 후 AI 응답 확인

---

## 🔧 문제 해결

### AI가 응답하지 않는 경우

1. 브라우저 개발자 도구 열기 (F12)
2. **Console** 탭에서 에러 확인
3. 에러 메시지에 "API key" 관련 내용이 있다면:
   - Vercel 환경 변수가 올바르게 설정되었는지 확인
   - 재배포가 완료되었는지 확인

### 환경 변수가 적용되지 않는 경우

- 환경 변수 추가 후 **반드시 재배포** 필요
- 기존 배포는 새 환경 변수를 인식하지 못함

### 구글 로그인 실패 (auth/unauthorized-domain)

이 에러는 Vercel 배포 주소가 Firebase 인증 도메인 목록 보완되지 않아서 발생합니다.

1. [Firebase Console](https://console.firebase.google.com/) 접속
2. **Authentication** > **Settings** 탭 > **Authorized domains** (승인된 도메인) 메뉴 이동
3. **도메인 추가** 버튼 클릭
4. 현재 배포된 주소(예: `al-class.vercel.app`) 입력 및 추가


### "The requested action is invalid" 에러

이 에러는 구글 클라우드 콘솔의 **API 키 제한** 설정 때문에 발생합니다. API 키가 특정 도메인(예: localhost)에서만 작동하도록 잠겨있기 때문입니다.

1. [Google Cloud Console > 사용자 인증 정보](https://console.cloud.google.com/apis/credentials) 접속
2. 프로젝트 선택 (`lms01-bc677`)
3. **API 키** 목록에서 사용 중인 키 클릭 (편집 아이콘)
4. **애플리케이션 제한사항** 항목 확인:
   - "없음"으로 되어 있다면 이 문제는 아님
   - **"웹사이트 제한"**이 걸려 있다면, 다음 항목을 목록에 **모두** 추가해야 합니다:
     - `http://localhost:3000/*` (로컬 테스트용)
     - `https://lms01-bc677.firebaseapp.com/*` (필수: 인증 핸들러용)
     - `https://al-class.vercel.app/*` (배포된 앱용)
5. **저장** 클릭 후 5분 정도 대기 (적용 시간 소요)

---

**참고**: 이 가이드는 보안상 민감한 정보를 포함하고 있으므로 외부에 공유하지 마세요.
