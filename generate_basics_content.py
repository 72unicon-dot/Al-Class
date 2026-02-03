
# Script to generate Lecture Pages and Textbooks for AI Basics Course
import os

# ==========================================
# 1. TEXTBOOKS DATA
# ==========================================
textbooks = [
    {
        "filename": "textbook_basics_llm.html",
        "title": "LLM과 Transformer 구조",
        "subtitle": "Understanding Large Language Models",
        "color": "blue",
        "content": """
            <h3>1. LLM(거대 언어 모델)이란?</h3>
            <p>LLM은 방대한 양의 텍스트 데이터를 학습하여, 인간처럼 자연스러운 문장을 이해하고 생성할 수 있는 인공지능 모델입니다. '다음에 올 단어'를 확률적으로 예측하는 것이 핵심 원리입니다.</p>
            
            <h3>2. Transformer 아키텍처</h3>
            <p>2017년 구글이 발표한 Transformer는 현재 모든 최신 LLM(GPT, Gemini, Claude 등)의 기반이 되는 신경망 구조입니다.</p>
            <ul class="list-disc pl-6 space-y-2 mt-2">
                <li><strong>Self-Attention 메커니즘:</strong> 문장 내 단어들 간의 관계(중요도)를 파악하여 문맥을 이해합니다. (예: '은행'이 Bank인지 River side인지 주변 단어를 보고 파악)</li>
                <li><strong>병렬 처리:</strong> 기존 RNN 모델과 달리 데이터를 한 번에 처리할 수 있어 학습 속도가 획기적으로 빠릅니다.</li>
            </ul>

            <h3>3. 주요 용어 정리</h3>
            <div class="grid md:grid-cols-2 gap-4 mt-4">
                <div class="bg-blue-50 p-4 rounded-xl">
                    <h4 class="font-bold text-blue-800">Parameter (매개변수)</h4>
                    <p class="text-sm">모델의 뇌세포 수. 파라미터가 많을수록 더 복잡한 추론이 가능합니다.</p>
                </div>
                <div class="bg-indigo-50 p-4 rounded-xl">
                    <h4 class="font-bold text-indigo-800">Token (토큰)</h4>
                    <p class="text-sm">텍스트를 처리하는 기본 단위. 영어는 단어, 한글은 글자 단위와 유사합니다.</p>
                </div>
            </div>
        """
    },
    {
        "filename": "textbook_basics_context.html",
        "title": "Token과 Context Window 이해",
        "subtitle": "Managing Input Limits",
        "color": "indigo",
        "content": """
            <h3>1. 토큰(Token)의 경제학</h3>
            <p>LLM은 글자가 아니라 '토큰' 단위로 과금하고 처리합니다.</p>
            <ul>
                <li>영어 1단어 ≈ 0.75 토큰</li>
                <li>한글 1글자 ≈ 0.5 ~ 1 토큰 (모델마다 다름)</li>
            </ul>
            
            <h3>2. 컨텍스트 윈도우(Context Window)</h3>
            <p>모델이 한 번에 기억하고 처리할 수 있는 정보의 양입니다. 컨텍스트 윈도우가 클수록 긴 문서를 한 번에 요약하거나 분석할 수 있습니다.</p>
            <div class="bg-slate-100 p-4 rounded-xl my-4 border-l-4 border-indigo-500">
                <strong>Gemini 1.5 Pro:</strong> 최대 100만~200만 토큰 처리 가능 (책 수백 권 분량)<br>
                <strong>GPT-4:</strong> 128k 토큰 (책 1~2권 분량)
            </div>

            <h3>3. 실무 팁</h3>
            <p>긴 대화를 나누다 보면 앞부분 내용을 까먹는 현상은 컨텍스트 윈도우가 꽉 찼기 때문입니다. 중요한 정보는 주기적으로 요약해서 다시 입력하거나, 새로운 채팅 세션을 시작하는 것이 좋습니다.</p>
        """
    },
    {
        "filename": "textbook_basics_prompting.html",
        "title": "Zero-shot vs Few-shot Prompting",
        "subtitle": "Core Prompt Engineering Techniques",
        "color": "violet",
        "content": """
            <h3>1. 프롬프트 엔지니어링이란?</h3>
            <p>AI로부터 원하는 최적의 결과를 얻어내기 위해 질문(지시문)을 설계하는 기술입니다.</p>

            <h3>2. Zero-shot Prompting</h3>
            <p>예시를 주지 않고 바로 지시하는 방법입니다.</p>
            <div class="bg-gray-100 p-3 rounded mb-4 font-mono text-sm">
                User: "이 문장을 영어로 번역해: 안녕하세요."<br>
                AI: "Hello."
            </div>

            <h3>3. Few-shot Prompting (강력 추천 ⭐)</h3>
            <p>몇 가지 예시(Sample)를 제공하여 AI가 패턴을 학습하게 하는 방법입니다. 정확도가 훨씬 높아집니다.</p>
            <div class="bg-gray-100 p-3 rounded mb-4 font-mono text-sm">
                User:<br>
                "과일이면 🔴, 야채면 🟢를 붙여줘."<br>
                사과: 🔴<br>
                시금치: 🟢<br>
                토마토: "<br>
                AI: "🔴" (또는 상황에 따라 🟢)
            </div>
        """
    },
    {
        "filename": "textbook_basics_tools.html",
        "title": "주요 생산성 도구 비교: ChatGPT, Gemini, Claude",
        "subtitle": "Choosing the Right Tool for the Job",
        "color": "emerald",
        "content": """
            <h3>1. ChatGPT (OpenAI)</h3>
            <p>가장 범용적이고 밸런스가 좋은 모델입니다. Advanced Data Analysis 기능을 통해 엑셀 데이터 분석에 강점이 있으며, GPTs를 통해 나만의 챗봇을 만들기 쉽습니다.</p>

            <h3>2. Gemini (Google)</h3>
            <p>구글 워크스페이스(Docs, Gmail, Drive)와의 연동이 가장 큰  강점입니다. 유튜브 요약, 구글 지도 검색 등 구글 생태계 활용에 최적화되어 있습니다. 또한 멀티모달(이미지, 영상 이해) 능력이 뛰어납니다.</p>

            <h3>3. Claude (Anthropic)</h3>
            <p>한국어 작문 능력이 매우 자연스럽고, 코딩 능력이 탁월합니다. 'Artifacts' 기능을 통해 생성된 코드나 문서를 별도 창에서 미리보기 할 수 있어 개발자와 작가들에게 인기가 많습니다.</p>

            <h3>4. 요약 비교</h3>
            <table class="w-full text-sm text-left border-collapse mt-4">
                <tr class="bg-slate-100 border-b">
                    <th class="p-2">모델</th>
                    <th class="p-2">강점</th>
                    <th class="p-2">추천 용도</th>
                </tr>
                <tr class="border-b">
                    <td class="p-2 font-bold">ChatGPT</td>
                    <td class="p-2">데이터 분석, 커스텀 챗봇</td>
                    <td class="p-2">엑셀 분석, 범용 업무</td>
                </tr>
                <tr class="border-b">
                    <td class="p-2 font-bold">Gemini</td>
                    <td class="p-2">구글 연동, 긴 문맥 처리</td>
                    <td class="p-2">이메일 작성, 긴 문서 요약</td>
                </tr>
                 <tr class="border-b">
                    <td class="p-2 font-bold">Claude</td>
                    <td class="p-2">자연스러운 문장, 코딩</td>
                    <td class="p-2">보고서 초안, 프로그래밍</td>
                </tr>
            </table>
        """
    },
    {
        "filename": "textbook_basics_writing.html",
        "title": "이메일 및 보고서 자동 작성 실습",
        "subtitle": "Writing Automation",
        "color": "teal",
        "content": """
            <h3>1. 이메일 작성 프롬프트 템플릿</h3>
            <p>상황, 수신자, 톤앤매너(정중하게/간결하게)를 지정하면 완벽한 비즈니스 이메일을 써줍니다.</p>
            <div class="bg-teal-50 p-4 rounded-xl border border-teal-100 my-4 text-sm font-mono">
                "다음 내용을 포함해서 거래처 김 팀장님께 보낼 정중한 거절 이메일을 써줘.<br>
                - 제안 주신 프로젝트는 흥미로움<br>
                - 하지만 현재 우리 팀 리소스가 부족하여 참여 어려움<br>
                - 다음 하반기에는 검토 가능함<br>
                - 따뜻한 안부 인사 포함"
            </div>

            <h3>2. 보고서 초안 잡기</h3>
            <p>빈 화면 증후군(Blank Page Syndrome)을 극복하세요. AI에게 목차(Index)를 먼저 짜달라고 한 뒤, 살을 붙여나가는 방식이 효율적입니다.</p>
        """
    },
    {
        "filename": "textbook_basics_analysis.html",
        "title": "데이터 분석 및 시각화 기초",
        "subtitle": "Data Analysis without Coding",
        "color": "cyan",
        "content": """
            <h3>1. 엑셀 파일 업로드 & 분석</h3>
            <p>ChatGPT나 Claude에 엑셀 파일을 업로드하고 다음과 같이 요청해보세요.</p>
            <ul class="list-disc pl-6 space-y-2 mt-2 font-mono text-sm">
                <li>"이 데이터의 주요 추세를 요약해줘."</li>
                <li>"매출이 가장 높은 상위 5개 제품을 뽑아줘."</li>
                <li>"월별 매출 추이를 막대 그래프로 그려줘."</li>
            </ul>

            <h3>2. 주요 활용 사례</h3>
            <p>복잡한 피벗 테이블이나 함수를 몰라도, 자연어로 데이터를 필터링하고 시각화할 수 있습니다. 마케팅 성과 분석, 설문조사 결과 요약 등에 매우 유용합니다.</p>
        """
    }
]

# ==========================================
# 2. GENERATE TEXTBOOK FILES
# ==========================================
textbook_template_start = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>강의 교재 - AI 기초</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        body { font-family: 'Pretendard', sans-serif; line-height: 1.7; }
        .textbook-content h3 { font-size: 1.25rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.75rem; color: #1e293b; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem; }
        .textbook-content p { margin-bottom: 1rem; color: #475569; }
        .textbook-content ul { list-style-type: disc; padding-left: 1.5rem; margin-bottom: 1.5rem; color: #475569; }
        .textbook-content table { width: 100%; border-collapse: collapse; margin-top: 1rem; }
        .textbook-content th, .textbook-content td { padding: 0.75rem; border: 1px solid #e2e8f0; }
        .textbook-content th { background-color: #f8fafc; font-weight: 600; }
    </style>
</head>
<body class="bg-slate-50 min-h-screen">
    <div class="max-w-4xl mx-auto px-6 py-12">
        <div class="flex justify-between items-center mb-8">
            <a href="classroom_basics.html" class="inline-flex items-center gap-2 text-slate-500 hover:text-slate-800 transition-colors">
                <i class="fas fa-arrow-left"></i> 강의실로 돌아가기
            </a>
            <button onclick="window.print()" class="text-slate-400 hover:text-slate-600"><i class="fas fa-print"></i></button>
        </div>
        <div class="bg-white rounded-2xl shadow-xl overflow-hidden border border-slate-100">
"""

textbook_template_end = """
            <div class="mt-12 pt-8 border-t border-slate-100 flex justify-center">
                <button onclick="history.back()" class="px-6 py-3 bg-slate-100 text-slate-700 rounded-xl font-bold hover:bg-slate-200 transition">
                    목록으로
                </button>
            </div>
        </div>
    </div>
</body>
</html>
"""

for item in textbooks:
    html = textbook_template_start + f"""
            <div class="bg-gradient-to-r from-{item['color']}-600 to-{item['color']}-800 text-white p-10 md:p-14">
                <span class="inline-block px-3 py-1 bg-white/20 rounded-full text-xs font-bold mb-4 backdrop-blur-sm tracking-wider">LECTURE NOTE</span>
                <h1 class="text-3xl md:text-4xl font-extrabold mb-2">{item['title']}</h1>
                <p class="text-white/80 text-lg font-light">{item['subtitle']}</p>
            </div>
            <div class="p-10 md:p-14 textbook-content">
                {item['content']}
            </div>
    """ + textbook_template_end
    
    with open(item['filename'], 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {item['filename']}")

# ==========================================
# 3. GENERATE LECTURE PAGES (Class 1 & 2)
# ==========================================

def get_lecture_header(title, subtitle, class_num):
    return f"""
    <header class="gradient-bg text-white py-12 px-8 relative overflow-hidden">
        <div class="absolute top-4 right-4 md:top-6 md:right-8 flex items-center gap-3 z-20">
            <span id="userEmailDisplay" class="text-sm text-white/90 font-medium hidden md:inline"></span>
            <a href="classroom_basics.html"
                class="inline-flex items-center gap-2 px-4 py-2 bg-white/20 backdrop-blur-md text-white text-sm font-semibold rounded-full border border-white/30 hover:bg-white/30 transition-all">
                <i class="fas fa-arrow-left"></i>
                <span class="hidden sm:inline">강의실 홈으로</span>
            </a>
        </div>
        <div class="max-w-6xl mx-auto flex flex-col md:flex-row justify-between items-end relative z-10">
            <div class="space-y-2">
                <span class="text-6xl font-black opacity-20 block mb-[-10px]">Class {class_num}</span>
                <h1 class="text-3xl md:text-5xl font-extrabold tracking-tight">{title}</h1>
                <p class="text-xl opacity-90 font-light">{subtitle}</p>
            </div>
        </div>
    </header>
    """

def get_card(icon, color, title, desc, tags, view_link):
    tag_html = ""
    for tag in tags:
        tag_html += f'<span class="bg-{color}-50 text-{color}-700 px-3 py-1 rounded-md text-xs font-semibold">{tag}</span>'
    listen_link = "https://al-class.vercel.app/ai-lecture-room/dist/index.html"
    return f"""
                <div class="bg-white p-8 rounded-3xl border border-slate-100 card-shadow hover:border-{color}-200 transition-all group">
                    <div class="flex items-start gap-4">
                        <div class="bg-{color}-50 text-{color}-600 p-3 rounded-2xl group-hover:bg-{color}-600 group-hover:text-white transition-colors">
                            <i class="fas fa-{icon} text-2xl"></i>
                        </div>
                        <div class="flex-1">
                            <h3 class="text-xl font-bold mb-2">{title}</h3>
                            <p class="text-slate-500 text-sm mb-4 leading-relaxed">{desc}</p>
                            <div class="flex flex-wrap gap-2 mb-4">
                                {tag_html}
                            </div>
                            <div class="flex gap-2">
                                <a href="{view_link}" class="inline-flex items-center gap-2 px-4 py-2 bg-slate-100 text-slate-700 text-sm font-bold rounded-lg hover:bg-slate-200 transition-colors">
                                    <i class="fas fa-book-reader"></i> 강의 보기
                                </a>
                                <a href="{listen_link}" target="_blank" class="inline-flex items-center gap-2 px-4 py-2 bg-{color}-600 text-white text-sm font-bold rounded-lg hover:bg-{color}-700 transition-colors">
                                    <i class="fas fa-play-circle"></i> 강의 듣기
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
    """

base_html_start = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI 기초 및 활용 - 강의 시청</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        body { font-family: 'Pretendard', sans-serif; scroll-behavior: smooth; }
        .gradient-bg { background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%); } /* Blue for Basics */
        .card-shadow { box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05); }
    </style>
</head>
<body class="bg-slate-50 text-slate-900">
"""

base_html_end = """
    <script type="module">
        import { auth } from './js/firebase-config.js';
        import { onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
        onAuthStateChanged(auth, (user) => {
            if (!user) { alert("로그인이 필요합니다."); window.location.href='index.html'; }
            else { document.getElementById('userEmailDisplay').innerText = user.email + "님 환영합니다"; }
        });
    </script>
</body>
</html>
"""

# Class 1 Content
c1 = base_html_start + get_lecture_header("생성형 AI 원리 이해", "LLM의 작동 방식과 프롬프트 엔지니어링 기초 (오전 4시간)", "01")
c1 += """<main class="max-w-6xl mx-auto px-6 py-12 space-y-12">
        <section class="space-y-6">
            <div class="inline-flex items-center gap-3 bg-blue-600 text-white px-5 py-2 rounded-full shadow-lg">
                <span class="font-bold text-xs tracking-widest">PART 1 (오전)</span>
                <h2 class="text-lg font-bold">LLM 이론 및 기초</h2>
            </div>
            <div class="grid md:grid-cols-2 gap-6">"""
c1 += get_card("brain", "blue", "LLM과 Transformer 구조", "대규모 언어 모델의 학습 원리와 Transformer 아키텍처를 쉽게 이해합니다.", ["Principles", "Structure"], "textbook_basics_llm.html")
c1 += get_card("memory", "indigo", "Token과 Context Window", "AI 과금 및 처리 용량의 기준이 되는 토큰의 개념과 한계를 배웁니다.", ["Token", "Memory"], "textbook_basics_context.html")
c1 += get_card("magic", "violet", "Zero-shot vs Few-shot", "프롬프트 엔지니어링의 핵심인 예시 제공(Few-shot) 기법을 실습합니다.", ["Prompting", "Technique"], "textbook_basics_prompting.html")
c1 += """</div></section></main>""" + base_html_end

with open("lecture_basics_class1.html", "w", encoding="utf-8") as f:
    f.write(c1)
    print("Generated lecture_basics_class1.html")

# Class 2 Content
c2 = base_html_start + get_lecture_header("업무 생산성 도구", "ChatGPT, Gemini, Claude 등 주요 툴 활용법 (오후 4시간)", "02")
c2 += """<main class="max-w-6xl mx-auto px-6 py-12 space-y-12">
        <section class="space-y-6">
             <div class="inline-flex items-center gap-3 bg-emerald-600 text-white px-5 py-2 rounded-full shadow-lg">
                <span class="font-bold text-xs tracking-widest">PART 2 (오후)</span>
                <h2 class="text-lg font-bold">AI 툴 실무 활용</h2>
            </div>
            <div class="grid md:grid-cols-2 gap-6">"""
c2 += get_card("tools", "emerald", "주요 생산성 도구 비교", "ChatGPT, Gemini, Claude의 장단점과 업무별 추천 도구를 알아봅니다.", ["Tools", "Comparison"], "textbook_basics_tools.html")
c2 += get_card("envelope-open-text", "teal", "이메일 및 보고서 자동화", "상황에 맞는 비즈니스 이메일 작성과 보고서 초안 생성 프롬프트를 배웁니다.", ["Writing", "Email"], "textbook_basics_writing.html")
c2 += get_card("chart-bar", "cyan", "데이터 분석 및 시각화", "코딩 없이 엑셀 데이터를 업로드하여 인사이트를 도출하고 그래프를 그립니다.", ["Data", "Analysis"], "textbook_basics_analysis.html")
c2 += """</div></section></main>""" + base_html_end

with open("lecture_basics_class2.html", "w", encoding="utf-8") as f:
    f.write(c2)
    print("Generated lecture_basics_class2.html")
