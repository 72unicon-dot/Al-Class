# AI 실무 마스터 클래스 - 8일차 커리큘럼 가이드

## 📚 앱 소개

### AI 실무 마스터 클래스란?

**AI 실무 마스터 클래스**는 8일 만에 AI 도구 활용부터 실제 웹 애플리케이션 배포까지 완성하는 집중 교육 과정입니다.

#### 🎯 핵심 목표
- **10대 AI 도구 마스터**: Gemini, Claude, NotebookLM, Canva, Runway 등 실무 필수 도구
- **바이브 코딩 체득**: AI와 대화하며 코드를 작성하는 새로운 개발 패러다임
- **실전 앱 배포**: 나만의 웹 애플리케이션을 전 세계에 공개

#### 💡 3대 강점

**1. 데이터 기반 의사결정 역량 강화**
- 복잡한 데이터를 AI로 분석하여 경영진 보고서 자동 생성
- 수작업 몇 시간 → AI로 몇 분 만에 완료

**2. 올인원 멀티모달 마스터**
- 텍스트(보고서) + 이미지(마케팅) + 영상(홍보)을 하나의 파이프라인으로 연결
- 1인 기업가 수준의 실무 역량 확보

**3. 성과 중심 프로젝트 설계**
- KPI(핵심성과지표) 기반 학습 결과물 평가
- 현업에 바로 제출 가능한 'AI 기반 비즈니스 기획안' 완성

---

## 📅 8일차: 종합 프로젝트 & 배포

### 🎯 학습 목표
8일간 배운 모든 AI 도구와 개발 기술을 종합하여 **나만의 웹 애플리케이션을 완성하고 전 세계에 배포**합니다.

---

### 📖 Part 1: 이론 - 배포 및 유지보수

#### 1️⃣ Git/GitHub 버전 관리 기초 (45분)

**학습 목표**
- Git의 기본 개념과 버전 관리의 필요성 이해
- GitHub를 활용한 코드 저장 및 협업 방법 습득
- 기본 Git 명령어 3가지 마스터

**핵심 개념**
- **Git**: 코드 변경 이력을 관리하는 '개발자의 타임머신'
- **GitHub**: 코드를 클라우드에 저장하고 협업하는 플랫폼
- **Repository(저장소)**: 프로젝트 파일들이 저장되는 공간
- **Commit**: 변경사항을 저장하는 단위 (스냅샷)

**필수 명령어 3가지**
```bash
git add .              # 변경된 파일을 봉투에 담기 (Staging)
git commit -m "메시지"  # 봉투를 밀봉하고 도장 찍기 (Save)
git push               # 우체통(GitHub)에 넣어서 보내기 (Upload)
```

**실습 예제**
```bash
# 1. 프로젝트 폴더에서 Git 초기화
git init

# 2. 모든 파일 추가
git add .

# 3. 첫 번째 커밋
git commit -m "Initial commit: 프로젝트 시작"

# 4. GitHub 저장소 연결
git remote add origin https://github.com/username/my-project.git

# 5. 코드 업로드
git push -u origin main
```

**GitHub 활용 팁**
- **포트폴리오**: GitHub 프로필을 예쁘게 꾸며서 자신을 어필
  - README.md 작성: 프로젝트 소개, 기술 스택, 스크린샷
  - GitHub Stats 카드 추가
- **오픈소스 기여**: 다른 사람의 코드를 보고 배우며 수정 제안(PR)
- **.gitignore**: 민감한 정보(API 키, 비밀번호) 제외하기

**주의사항**
⚠️ API 키, 비밀번호 등 민감한 정보는 절대 GitHub에 올리지 말 것!  
⚠️ `.env` 파일은 `.gitignore`에 추가하여 제외

---

#### 2️⃣ 클라우드 배포 플랫폼 이해 (40분)

**학습 목표**
- 클라우드 배포의 개념과 장점 이해
- 주요 배포 플랫폼 비교 및 선택 기준 파악
- Vercel을 활용한 자동 배포 프로세스 이해

**배포란?**
내가 만든 웹사이트 파일들을 24시간 켜져 있는 컴퓨터(서버)에 올려서, 누구나 주소(URL)만 치면 들어올 수 있게 하는 작업

**로컬 vs 배포 환경**
```
로컬 환경 (Local)          배포 환경 (Production)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
localhost:3000      →      my-app.vercel.app
내 컴퓨터에서만 접속       전 세계 누구나 접속
개발 & 테스트 용도         실제 서비스 운영
```

**플랫폼 비교**

| 플랫폼 | 특징 | 장점 | 단점 | 추천도 |
|--------|------|------|------|--------|
| **Vercel** ⭐ | GitHub 연동 자동 배포, Next.js 개발사 | 개인 프로젝트 평생 무료, 속도 매우 빠름 (CDN), 설정 간단 | 서버리스 함수 제한 | 🔥 강력 추천 |
| **Netlify** | 정적 사이트 배포 강자 | 드래그 앤 드롭 배포, 무료 플랜 넉넉, Form 처리 기능 | 빌드 시간 제한 | ✅ 추천 |
| **GitHub Pages** | GitHub 무료 호스팅 | 완전 무료, GitHub 통합 | 정적 사이트만 가능, 서버 기능 없음 | ✅ 정적 사이트용 |
| **AWS** | 세계 1위 클라우드 | 무한한 확장성, 모든 기능 제공 | 설정 매우 복잡, 초보자 비추천, 잘못 쓰면 요금 폭탄 | ⚠️ 비추천 |

**Vercel 배포 프로세스**
```
1. GitHub에 코드 푸시
   ↓
2. Vercel이 자동으로 감지
   ↓
3. 빌드 & 배포 자동 실행
   ↓
4. 고유 URL 생성 (예: my-app.vercel.app)
   ↓
5. HTTPS 자동 적용 ✅
```

**배포 시 체크리스트**
- ✅ 환경 변수(.env) 설정 완료
- ✅ 빌드 명령어 확인 (npm run build)
- ✅ 출력 디렉토리 확인 (dist, build, out 등)
- ✅ Node.js 버전 명시

---

#### 3️⃣ 도메인 연결 및 HTTPS (35분)

**학습 목표**
- 도메인의 개념과 필요성 이해
- HTTPS 보안 프로토콜의 중요성 파악
- 커스텀 도메인 연결 방법 습득

**도메인(Domain)이란?**
```
복잡한 IP 주소              사람이 기억하기 쉬운 주소
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
192.168.0.1:3000      →      my-awesome-app.com
```

**도메인 구조**
```
https://www.example.com/blog/post
  ↑      ↑    ↑       ↑    ↑
프로토콜  서브  도메인  TLD  경로
         도메인  이름

- 프로토콜: https (보안) / http (비보안)
- 서브도메인: www, blog, api 등
- 도메인 이름: example (원하는 이름)
- TLD (최상위 도메인): .com, .net, .kr 등
```

**도메인 구입처**
- 🇰🇷 **가비아** (gabia.com): 한국 최대, 한글 지원 우수
- 🌍 **GoDaddy** (godaddy.com): 글로벌 1위, 영문 도메인 저렴
- 🌍 **Namecheap** (namecheap.com): 가성비 좋음, 무료 WHOIS 보호
- 🌍 **Google Domains** (domains.google): 심플한 UI, Google 통합

**도메인 가격 (연간)**
- `.com`: 약 15,000원 ~ 20,000원
- `.net`: 약 18,000원 ~ 25,000원
- `.co.kr`: 약 20,000원 ~ 30,000원
- `.io`: 약 50,000원 ~ 70,000원 (개발자들이 선호)

**HTTPS 보안 접속**

| HTTP (❌ 비추천) | HTTPS (✅ 추천) |
|-----------------|----------------|
| 데이터가 암호화되지 않고 전송 | SSL 인증서로 암호화 |
| 해커가 중간에서 가로챌 수 있음 | 제3자가 데이터를 볼 수 없음 |
| 브라우저 주소창에 "주의 요함" 표시 | 자물쇠 아이콘 표시 🔒 |
| 로그인, 결제 시 매우 위험 | Vercel 배포 시 **무료로 자동 적용** |
| SEO 순위 하락 | Google 검색 순위 우대 |

**Vercel에서 커스텀 도메인 연결하기**
```
1. 도메인 구입 (가비아, GoDaddy 등)
   ↓
2. Vercel 프로젝트 설정 → Domains
   ↓
3. 도메인 입력 (예: myapp.com)
   ↓
4. DNS 설정 (A 레코드 또는 CNAME)
   - 가비아 DNS 관리 페이지에서 설정
   - Vercel이 제공하는 IP 주소 입력
   ↓
5. 자동으로 HTTPS 인증서 발급 (Let's Encrypt)
   ↓
6. 완료! https://myapp.com 접속 가능 ✅
```

**DNS 설정 예시**
```
타입    호스트    값
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
A       @         76.76.21.21 (Vercel IP)
CNAME   www       cname.vercel-dns.com
```

---

#### 4️⃣ 앱 유지보수 전략 (40분)

**학습 목표**
- 배포 후 모니터링의 중요성 이해
- 사용자 피드백 수집 및 대응 방법 습득
- 지속적인 업데이트 및 개선 전략 수립

**배포 후 체크리스트**
- ✅ **반응형 테스트**: 모바일에서 화면이 깨지지 않는가?
  - Chrome DevTools → Toggle Device Toolbar (Ctrl+Shift+M)
  - iPhone, iPad, Galaxy 등 다양한 기기에서 테스트
- ✅ **성능 최적화**: 이미지가 너무 늦게 뜨지 않는가?
  - 이미지 압축 (TinyPNG, ImageOptim)
  - Lazy Loading 적용
  - CDN 활용 (Vercel 자동 제공)
- ✅ **기능 테스트**: 회원가입/로그인이 정상 작동하는가?
  - 실제 사용자 시나리오대로 테스트
  - Edge Case (예외 상황) 확인
- ✅ **에러 확인**: 콘솔(Console)에 빨간 에러 메시지가 없는가?
  - F12 → Console 탭 확인
  - 404 에러, CORS 에러 등 해결

**성능 모니터링 도구**
- **Google Analytics**: 방문자 수, 페이지뷰, 체류 시간
- **Vercel Analytics**: 실시간 성능 지표, Core Web Vitals
- **Sentry**: 에러 추적 및 알림
- **Hotjar**: 사용자 행동 분석 (히트맵, 녹화)

**사용자 피드백 수집 채널**
- 📧 **이메일 문의**: support@myapp.com
- 💬 **디스코드 채널**: 실시간 커뮤니티 소통
- 💛 **카카오톡 채널**: 한국 사용자 친화적
- 📊 **Google 설문**: 정량적 피드백 수집
- 💡 **Typeform**: 인터랙티브한 설문 제작

> 💡 **개발자가 못 보는 버그를 사용자는 1초 만에 찾아냅니다. 소통 창구를 만드세요!**

**지속적인 업데이트 전략**
```
주간 사이클
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
월요일: 사용자 피드백 수집 및 분석
화요일: 우선순위 설정 (긴급/중요도)
수요일: 버그 수정 및 기능 개발
목요일: 테스트 및 QA
금요일: 배포 (GitHub → Vercel 자동)
```

**버전 관리 전략**
```
v1.0.0 → v1.0.1 → v1.1.0 → v2.0.0
  ↑        ↑        ↑        ↑
초기     버그     새 기능   대규모
출시     수정     추가      변경

- Major (v2.0.0): 호환성 깨지는 큰 변경
- Minor (v1.1.0): 새 기능 추가
- Patch (v1.0.1): 버그 수정
```



---

### 🛠️ Part 2: 실습 - 파이널 프로젝트

#### 실습 1: 개인 프로젝트 완성 (120분)

**목표**: 그동안 배운 모든 내용을 종합하여 나만의 웹 애플리케이션을 완성하고 다듬기

**프로젝트 유형 예시**
1. **AI 챗봇 서비스**
   - Gemini API 연동
   - 대화 히스토리 저장 (Firebase)
   - 반응형 채팅 UI

2. **업무 자동화 대시보드**
   - Make.com 워크플로우 통합
   - 실시간 데이터 시각화
   - 알림 기능

3. **포트폴리오 웹사이트**
   - 프로젝트 갤러리
   - 이력서 다운로드
   - 연락처 폼

4. **AI 이미지 생성기**
   - Nano Banana API 연동
   - 프롬프트 템플릿 제공
   - 생성 이미지 갤러리

**완성 체크리스트**

**1. 기능 완성도 (40점)**
- [ ] 핵심 기능 3가지 이상 구현
- [ ] AI 도구 최소 1개 이상 활용
- [ ] 에러 처리 (try-catch, 사용자 피드백)
- [ ] 로딩 상태 표시 (스피너, 프로그레스 바)

**2. UI/UX 디자인 (30점)**
- [ ] 반응형 디자인 (모바일, 태블릿, 데스크톱)
- [ ] 일관된 색상 팔레트 및 타이포그래피
- [ ] 직관적인 네비게이션
- [ ] 접근성 고려 (alt 텍스트, 키보드 네비게이션)

**3. 코드 품질 (20점)**
- [ ] 의미 있는 변수명 및 함수명
- [ ] 주석 작성 (복잡한 로직 설명)
- [ ] 코드 재사용성 (함수 분리)
- [ ] 파일 구조 정리 (HTML, CSS, JS 분리)

**4. 창의성 및 실용성 (10점)**
- [ ] 독창적인 아이디어
- [ ] 실제 문제 해결
- [ ] 사용자 가치 제공

**코드 리팩토링 팁**
```javascript
// ❌ 나쁜 예: 반복되는 코드
document.getElementById('btn1').addEventListener('click', () => {
    fetch('/api/data1').then(res => res.json()).then(data => console.log(data));
});
document.getElementById('btn2').addEventListener('click', () => {
    fetch('/api/data2').then(res => res.json()).then(data => console.log(data));
});

// ✅ 좋은 예: 함수로 분리
async function fetchData(endpoint) {
    try {
        const response = await fetch(endpoint);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('데이터 로드 실패:', error);
        alert('데이터를 불러올 수 없습니다.');
    }
}

document.getElementById('btn1').addEventListener('click', () => fetchData('/api/data1'));
document.getElementById('btn2').addEventListener('click', () => fetchData('/api/data2'));
```

**최종 점검 항목**
```bash
# 1. 콘솔 에러 확인
F12 → Console 탭 → 빨간 에러 없는지 확인

# 2. 반응형 테스트
F12 → Toggle Device Toolbar (Ctrl+Shift+M)
→ iPhone, iPad, Desktop 모두 확인

# 3. 성능 테스트
F12 → Lighthouse 탭 → Generate Report
→ Performance 80점 이상 목표

# 4. 크로스 브라우저 테스트
Chrome, Firefox, Safari, Edge에서 모두 테스트
```

---

#### 실습 2: Vercel로 배포하기 (60분)

**목표**: 완성된 프로젝트를 Vercel을 통해 전 세계 누구나 접속 가능한 URL로 배포

**사전 준비**
- ✅ GitHub 계정 생성 (github.com)
- ✅ Vercel 계정 생성 (vercel.com)
- ✅ Git 설치 (git-scm.com)

**Step 1: GitHub에 코드 업로드 (15분)**

```bash
# 1. 프로젝트 폴더로 이동
cd my-project

# 2. Git 초기화
git init

# 3. .gitignore 파일 생성 (중요!)
# 다음 내용을 .gitignore 파일에 추가:
node_modules/
.env
.DS_Store
*.log

# 4. 모든 파일 추가
git add .

# 5. 첫 번째 커밋
git commit -m "Initial commit: 프로젝트 배포 준비"

# 6. GitHub에서 새 저장소 생성
# https://github.com/new 에서 저장소 생성

# 7. 원격 저장소 연결
git remote add origin https://github.com/username/my-project.git

# 8. 코드 푸시
git push -u origin main
```

**Step 2: Vercel 배포 설정 (20분)**

```
1. Vercel 로그인 (vercel.com)
   ↓
2. "New Project" 클릭
   ↓
3. "Import Git Repository" → GitHub 연동
   ↓
4. 배포할 저장소 선택
   ↓
5. 프로젝트 설정
   - Framework Preset: Vite / Next.js / Other
   - Build Command: npm run build (또는 비워두기)
   - Output Directory: dist / build / public
   ↓
6. 환경 변수 설정 (Environment Variables)
   - VITE_API_KEY: your-api-key
   - DATABASE_URL: your-database-url
   ↓
7. "Deploy" 클릭!
   ↓
8. 배포 완료 🎉
   - URL: https://my-project.vercel.app
```

**환경 변수 설정 예시**
```
Vercel Dashboard → Settings → Environment Variables

Name                    Value
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VITE_GEMINI_API_KEY     AIzaSyD...your-key
VITE_FIREBASE_API_KEY   AIzaSyC...your-key
DATABASE_URL            postgresql://...
```

**Step 3: 배포 확인 및 테스트 (15분)**

**배포 후 확인사항**
- ✅ **URL 접속**: https://my-project.vercel.app 정상 작동 확인
- ✅ **HTTPS 확인**: 주소창에 자물쇠 아이콘 🔒 표시
- ✅ **모바일 테스트**: 실제 스마트폰에서 접속 테스트
- ✅ **기능 테스트**: 모든 버튼, 링크, API 호출 정상 작동
- ✅ **콘솔 에러**: F12 → Console에 에러 없는지 확인

**배포 로그 확인**
```
Vercel Dashboard → Deployments → 최신 배포 클릭

빌드 로그 예시:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Building...
✓ Compiled successfully
✓ Optimizing images...
✓ Deploying to production...
✅ Deployment completed!

URL: https://my-project.vercel.app
```

**Step 4: 커스텀 도메인 연결 (선택, 10분)**

```
1. 도메인 구입 (가비아, GoDaddy 등)
   예: myapp.com (연간 약 15,000원)
   ↓
2. Vercel → Settings → Domains
   ↓
3. "Add Domain" → myapp.com 입력
   ↓
4. DNS 설정 안내 확인
   ↓
5. 가비아 DNS 관리 페이지에서 설정
   - A 레코드: @ → 76.76.21.21 (Vercel IP)
   - CNAME: www → cname.vercel-dns.com
   ↓
6. DNS 전파 대기 (최대 48시간, 보통 1시간 내)
   ↓
7. https://myapp.com 접속 가능! 🎉
```

**배포 트러블슈팅**

| 문제 | 원인 | 해결 방법 |
|------|------|----------|
| 404 Not Found | 빌드 경로 오류 | Output Directory 확인 (dist, build, public) |
| API 호출 실패 | 환경 변수 미설정 | Vercel 환경 변수에 API 키 추가 |
| 이미지 안 보임 | 절대 경로 사용 | 상대 경로로 변경 (./images/logo.png) |
| CORS 에러 | 백엔드 설정 문제 | 백엔드에서 CORS 허용 설정 |

---

#### 실습 3: 수료식 및 발표 (90분)

**목표**: 프로젝트 결과물을 동료들과 공유하고 피드백을 주고받으며 과정을 마무리

**발표 준비 (30분)**

**발표 자료 구성 (5분 발표)**

**1. 프로젝트 소개 (1분)**
```
안녕하세요, [이름]입니다.
오늘 소개할 프로젝트는 "[프로젝트명]"입니다.

[문제 정의]
현재 [타겟 사용자]는 [문제 상황]으로 어려움을 겪고 있습니다.

[솔루션]
이를 해결하기 위해 [핵심 기능]을 제공하는 웹 애플리케이션을 개발했습니다.
```

**2. 기술 스택 & AI 도구 (1분)**
```
사용한 AI 도구:
- Gemini: 챗봇 대화 생성
- Cursor: 코드 자동 완성
- Make.com: 이메일 자동화

개발 환경:
- Frontend: HTML, CSS, JavaScript
- Backend: Firebase (인증, 데이터베이스)
- Deployment: Vercel
```

**3. 핵심 기능 시연 (2분)**
```
[화면 공유 시작]

기능 1: [기능명]
→ [실제 시연]
→ "이 기능은 [AI 도구]를 활용하여 구현했습니다."

기능 2: [기능명]
→ [실제 시연]

기능 3: [기능명]
→ [실제 시연]
```

**4. 어려웠던 점 & 해결 방법 (1분)**
```
개발 중 가장 어려웠던 점:
[문제 상황 설명]

해결 방법:
1. [시도한 방법 1]
2. Cursor AI에게 질문: "[질문 내용]"
3. [최종 해결 방법]

배운 점:
[인사이트]
```

**5. 향후 계획 (30초)**
```
추가하고 싶은 기능:
- [기능 1]
- [기능 2]

실무 적용 계획:
[회사/팀에서 어떻게 활용할지]
```

**발표 슬라이드 템플릿**
```
슬라이드 1: 제목
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[프로젝트명]
[한 줄 소개]
발표자: [이름]

슬라이드 2: 문제 정의
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
😰 현재 상황
- [문제점 1]
- [문제점 2]

슬라이드 3: 솔루션
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 우리의 해결책
- [핵심 기능 1]
- [핵심 기능 2]
- [핵심 기능 3]

슬라이드 4: 기술 스택
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛠️ 사용한 도구
[AI 도구 로고들]
[개발 도구 로고들]

슬라이드 5: 데모 (스크린샷)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[실제 화면 캡처 3-4장]

슬라이드 6: 배운 점
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 Key Takeaways
- [인사이트 1]
- [인사이트 2]

슬라이드 7: 향후 계획
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 Next Steps
- [계획 1]
- [계획 2]

슬라이드 8: 감사 인사
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
감사합니다!
🔗 배포 URL: https://myproject.vercel.app
📧 연락처: email@example.com
```

**발표 팁**
- 🎤 **목소리**: 크고 명확하게, 적절한 속도로
- 👀 **시선**: 카메라 또는 청중을 바라보기
- ⏱️ **시간 관리**: 5분 엄수 (리허설 필수)
- 🖱️ **데모**: 미리 테스트, 백업 계획 준비
- 😊 **자신감**: 8일간 열심히 한 자신을 믿기!

**발표 및 피드백 (60분)**

**평가 기준 (동료 평가)**

| 항목 | 배점 | 평가 기준 |
|------|------|----------|
| **기능 완성도** | 30점 | 핵심 기능 구현, 에러 처리, 사용자 경험 |
| **UI/UX 디자인** | 20점 | 반응형, 일관성, 직관성 |
| **AI 도구 활용** | 20점 | 창의적 활용, 실용성 |
| **발표력** | 15점 | 명확한 전달, 시간 관리 |
| **창의성** | 15점 | 독창적 아이디어, 문제 해결 |

**피드백 양식**
```
프로젝트명: _______________________
발표자: _______________________

👍 잘한 점 (3가지):
1. 
2. 
3. 

💡 개선 제안 (2가지):
1. 
2. 

⭐ 종합 평가 (5점 만점): ___점

추가 코멘트:
```



---

## 🎓 학습 성과

8일차를 완료하면 다음을 할 수 있습니다:

✅ Git/GitHub로 코드 버전 관리  
✅ Vercel을 통한 원클릭 배포  
✅ 도메인 연결 및 HTTPS 보안 설정  
✅ 배포 후 모니터링 및 유지보수  
✅ **전 세계 누구나 접속 가능한 '나만의 AI 서비스' 런칭**

---

## 📊 전체 과정 요약

| 항목 | 내용 |
|------|------|
| **과정 기간** | 8일 |
| **AI 도구** | 10개 (Gemini, Claude, NotebookLM, Canva, Runway, ElevenLabs, Cursor, Make 등) |
| **실습 프로젝트** | 20+ 개 |
| **최종 결과물** | 1개의 배포된 웹 애플리케이션 |

---

## 🚀 다음 단계

1. **강의실 입장**: [classroom.html](classroom.html)에서 Day 8 강의 시작
2. **커리큘럼 확인**: [curriculum.html](curriculum.html)에서 전체 과정 복습
3. **실습 시작**: Day 8 실습 페이지에서 프로젝트 완성 및 배포

---

**© 2026 AI 실무 마스터 클래스. All rights reserved.**
