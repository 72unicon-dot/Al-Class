# 🚀 안티그래비티(Antigravity) 구축 가이드

AI 실무 마스터 클래스 콘텐츠를 안티그래비티에서 앱으로 만드는 방법입니다.

---

## 📊 1단계: CMS 컬렉션 설정

안티그래비티의 **Data > Collections** 메뉴에서 아래 컬렉션을 생성합니다.

### Collection 1: `Tools` (10대 AI 도구)

| 필드명 | 타입 | 설명 |
|--------|------|------|
| `tool_name` | Text | 도구 이름 (예: Perplexity) |
| `icon_class` | Text | FontAwesome 클래스 (예: fa-search) |
| `description` | Text | 도구 설명 |
| `category` | Text | 카테고리 (리서치, 생성AI, 콘텐츠, 개발, 자동화) |
| `border_color` | Color | 카드 테두리 색상 (예: #3b82f6) |
| `detail_link` | Link | 공식 홈페이지 URL |

**입력 데이터:**
```
Perplexity, fa-search, 출처가 명확한 실시간 AI 리서치, 리서치, #3b82f6, https://perplexity.ai
ChatGPT, fa-brain, 대화형 AI 어시스턴트의 표준, 생성AI, #10b981, https://chat.openai.com
Claude, fa-comments, 장문 분석 및 코딩에 최적화, 생성AI, #f97316, https://claude.ai
NotebookLM, fa-book-open, 문서 기반 AI 연구 어시스턴트, 리서치, #ef4444, https://notebooklm.google.com
Gamma, fa-presentation, AI 기반 프레젠테이션 자동 생성, 콘텐츠, #8b5cf6, https://gamma.app
Midjourney, fa-palette, 고품질 AI 이미지 생성, 콘텐츠, #ec4899, https://midjourney.com
Runway, fa-video, AI 영상 생성 및 편집, 콘텐츠, #06b6d4, https://runway.com
ElevenLabs, fa-microphone, 초현실적 AI 음성 합성, 콘텐츠, #f59e0b, https://elevenlabs.io
Cursor, fa-code, AI 페어 프로그래밍 IDE, 개발, #64748b, https://cursor.sh
Make / Zapier, fa-plug, 노코드 자동화 워크플로우, 자동화, #6366f1, https://make.com
```

---

### Collection 2: `Curriculum` (커리큘럼 타임라인)

| 필드명 | 타입 | 설명 |
|--------|------|------|
| `order` | Number | 정렬 순서 (1, 2, 3...) |
| `time_slot` | Text | 시간대 (예: 09:00 - 10:00) |
| `module_title` | Text | 모듈명 (예: M1. AI 리서치 혁신) |
| `sub_tools` | Text | 사용 도구 (예: Perplexity, NotebookLM) |
| `description` | Text | 상세 내용 |
| `duration` | Text | 소요 시간 |
| `is_break` | Boolean | 휴식 시간 여부 |

---

## 🎨 2단계: 페이지 레이아웃 구성

### Hero Section (상단 배너)

1. **Section** 컴포넌트 추가
2. 배경 설정:
   - Type: `Linear Gradient`
   - Colors: `#667eea` → `#764ba2`
   - Direction: 135deg
3. 내부에 **Container** 추가 (중앙 정렬)
4. 요소 배치:
   - Badge: "2026년 최신 커리큘럼" (배경 투명도 20%)
   - Heading H1: "AI 실무 마스터 클래스"
   - Paragraph: 부제목 텍스트
   - Flex Container: 태그들 (8시간, 실습 중심, 수료증)

---

### Tools Grid (10대 도구)

1. **Section** 컴포넌트 추가 (배경: 흰색)
2. **Repeat Container** 추가
   - Data Source: `Tools` 컬렉션 연결
   - Layout: Grid (5열)
   - Gap: 24px
3. 내부 카드 디자인:
   ```
   ┌─────────────────────┐
   │  [아이콘 영역]      │  ← Icon 요소, 배경색 바인딩
   │                     │
   │  도구명             │  ← Text, tool_name 바인딩
   │  설명               │  ← Text, description 바인딩
   └─────────────────────┘
   ```
4. 카드 스타일:
   - Border: 2px solid → `border_color` 필드 바인딩
   - Border Radius: 16px
   - Shadow: 0 10px 30px rgba(0,0,0,0.1)
   - Hover Effect: Transform translateY(-8px)

---

### Curriculum Timeline (커리큘럼)

1. **Section** 컴포넌트 추가 (배경: #f3f4f6)
2. **Container** (max-width: 900px, 중앙 정렬)
3. 타임라인 구조:
   ```
   ┌──────────────────────────────────────────┐
   │  [M1]  │  시간     모듈명                │
   │   ●────│         설명                    │
   │   │    │         [태그] [태그]           │
   │   │    └─────────────────────────────────┤
   │   │                                      │
   │  [M2]  │  ...                            │
   ```
4. **Repeat Container** 추가
   - Data Source: `Curriculum` 컬렉션 연결
   - Sort: `order` 필드 오름차순
5. 조건부 스타일:
   - `is_break = true` → 회색 스타일 적용

---

### Practice Prompts (실습 프롬프트)

1. **Section** 컴포넌트 추가
2. **Grid Layout** (3열)
3. 각 카드:
   - 배경: 그라디언트 (도구별 색상)
   - 아이콘 + 도구명
   - 프롬프트 텍스트 (배경 반투명 박스)

> 💡 **정적 콘텐츠이므로** CMS 연결 없이 직접 입력해도 됩니다.

---

## 🔧 3단계: HTML 직접 삽입 방법

HTML 코드를 그대로 사용하고 싶다면:

### Head 섹션에 추가할 내용
**Settings > Custom Code > Head** 에 입력:

```html
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap" rel="stylesheet">
```

### HTML 컴포넌트 사용
1. **HTML/Script** 컴포넌트를 캔버스에 배치
2. `ai_course_content.html` 파일에서 `<body>` 태그 내부 내용만 복사
3. 컴포넌트에 붙여넣기

---

## 📱 4단계: 반응형 설정

| 화면 크기 | Tools Grid | Timeline | Prompts |
|-----------|------------|----------|---------|
| Desktop (>1024px) | 5열 | 좌우 배치 | 3열 |
| Tablet (768-1024px) | 3열 | 좌우 배치 | 2열 |
| Mobile (<768px) | 1열 | 상하 배치 | 1열 |

---

## ✅ 체크리스트

- [ ] Tools 컬렉션 생성 및 데이터 입력
- [ ] Curriculum 컬렉션 생성 및 데이터 입력
- [ ] Hero Section 디자인
- [ ] Tools Grid Repeat Container 구성
- [ ] Timeline Repeat Container 구성
- [ ] Practice Prompts 섹션 구성
- [ ] 반응형 설정 적용
- [ ] 미리보기 테스트
- [ ] 퍼블리시

---

## 💡 프로 팁

1. **컬러 일관성**: 도구별 `border_color`를 태그 배경색에도 동일하게 사용
2. **애니메이션**: 카드 hover 시 `transition: all 0.3s ease` 적용
3. **타이포그래피**: Noto Sans KR 폰트로 통일
4. **스페이싱**: 섹션 간 padding 80px 유지

---

*이 가이드는 `ai_course_content.html` 파일과 함께 제공됩니다.*
