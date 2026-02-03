
# Refactored generator for Ethics Course (Class 1 / Class 2 Structure)

def get_header(title, subtitle, class_num="01"):
    return f"""
    <header class="gradient-bg text-white py-12 px-8 relative overflow-hidden">
        <div class="absolute top-4 right-4 md:top-6 md:right-8 flex items-center gap-3 z-20">
            <span id="userEmailDisplay" class="text-sm text-white/90 font-medium hidden md:inline"></span>
            <a href="classroom_ethics.html"
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

# Updated get_card to accept specific links
def get_card(icon, color, title, desc, tags, view_link, pdf_url=""):
    tag_html = ""
    for tag in tags:
        tag_html += f'<span class="bg-{color}-50 text-{color}-700 px-3 py-1 rounded-md text-xs font-semibold">{tag}</span>'
    
    listen_link = "https://al-class.vercel.app/ai-lecture-room/dist/index.html"
    
    # PDF Button Logic
    if pdf_url:
        pdf_btn = f"""
        <button onclick="window.open('{pdf_url}', '_blank')" class="inline-flex items-center gap-2 px-4 py-2 bg-{color}-600 text-white text-sm font-bold rounded-lg hover:bg-{color}-700 transition-colors cursor-pointer">
            <i class="fas fa-file-download"></i> PDF
        </button>
        """
    else:
        pdf_btn = f"""
        <button data-title="{title}" onclick="alert('등록된 자료가 없습니다.')" class="inline-flex items-center gap-2 px-4 py-2 bg-slate-200 text-slate-700 text-sm font-bold rounded-lg hover:bg-slate-300 transition-colors">
            <i class="fas fa-file-download"></i> PDF
        </button>
        """

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
                                {pdf_btn}
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
    <title>AI소개 및 윤리 - 강의 시청</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <meta name="course-id" content="ethics">
    <meta name="class-id" content="{class_num}">
    <style>
        body { font-family: 'Pretendard', sans-serif; scroll-behavior: smooth; }
        .gradient-bg { background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); }
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
    <script type="module" src="./js/resource-loader.js"></script>
</body>
</html>
"""

# ==========================================
# Generate Class 1
# ==========================================
class1_content = base_html_start + get_header("AI 윤리와 규제 트렌드", "국내외 규제 현황과 리스크 분석", "01") + """
    <main class="max-w-6xl mx-auto px-6 py-12 space-y-12">
        <section class="space-y-6">
            <div class="inline-flex items-center gap-3 bg-indigo-600 text-white px-5 py-2 rounded-full shadow-lg">
                <span class="font-bold text-xs tracking-widest">PART 1</span>
                <h2 class="text-lg font-bold">규제와 법적 이슈</h2>
            </div>
            <div class="grid md:grid-cols-2 gap-6">
"""
# Link the specific PDF here
target_pdf = "https://firebasestorage.googleapis.com/v0/b/lms01-bc677.firebasestorage.app/o/resources%2F1770156348748_cleaned_AI_Copyright_The_Dojo_Of_Wisdom.pdf?alt=media&token=078a3e99-cd83-48bd-b6b3-fd0ce532e1a9"
class1_content += get_card("balance-scale", "indigo", "생성형 AI와 저작권 분쟁", "AI 학습 데이터 및 산출물의 저작권 인정 여부에 대한 최근 판례와 이슈를 분석합니다.", ["Copyright", "Legal Case"], "textbook_ethics_copyright.html", target_pdf)
class1_content += get_card("globe", "blue", "글로벌 AI 규제: EU AI Act", "세계 최초의 포괄적 AI 규제법인 EU AI Act의 등급별 규제와 기업 영향을 알아봅니다.", ["EU AI Act", "Risk-based"], "textbook_ethics_eu_act.html")
class1_content += get_card("user-secret", "red", "개인정보보호와 AI", "데이터 학습 및 활용 과정에서 발생할 수 있는 개인정보 침해 이슈와 비식별화 기술을 다룹니다.", ["Privacy", "GDPR"], "textbook_ethics_privacy.html")
class1_content += get_card("building", "slate", "기업 데이터 유출 사고 사례", "삼성전자 등 주요 기업의 생성형 AI 도입 초기 데이터 유출 사고와 시사점을 분석합니다.", ["Security", "Data Leak"], "textbook_ethics_leak.html")
class1_content += """
            </div>
        </section>
    </main>
""" + base_html_end

with open("lecture_ethics_class1.html", "w", encoding="utf-8") as f:
    f.write(class1_content)

# ==========================================
# Generate Class 2
# ==========================================
class2_content = base_html_start + get_header("실무 가이드라인 수립", "안전하고 윤리적인 AI 활용 가이드", "02") + """
    <main class="max-w-6xl mx-auto px-6 py-12 space-y-12">
        <section class="space-y-6">
            <div class="inline-flex items-center gap-3 bg-emerald-600 text-white px-5 py-2 rounded-full shadow-lg">
                <span class="font-bold text-xs tracking-widest">PART 1</span>
                <h2 class="text-lg font-bold">사내 보안 및 윤리 가이드</h2>
            </div>
            <div class="grid md:grid-cols-2 gap-6">
"""
class2_content += get_card("shield-alt", "emerald", "프롬프트 입력 보안 수칙", "기밀 정보, 개인정보 입력을 방지하기 위한 프롬프트 필터링 및 보안 가이드를 수립합니다.", ["Security", "Prompt"], "textbook_ethics_prompt.html")
class2_content += get_card("file-signature", "teal", "AI 산출물 책임과 권한", "AI가 작성한 코드나 문서의 오류에 대한 책임 소재와 검수 프로세스를 정립합니다.", ["Accountability", "Review"], "textbook_ethics_accountability.html")
class2_content += get_card("exclamation-triangle", "amber", "할루시네이션 대응 전략", "AI의 거짓 답변(환각)을 식별하고 크로스체크(Fact Check)하는 실무 프로세스를 배웁니다.", ["Hallucination", "Fact Check"], "textbook_ethics_hallucination.html")
class2_content += """
            </div>
        </section>
        
        <section class="space-y-6">
             <div class="inline-flex items-center gap-3 bg-purple-600 text-white px-5 py-2 rounded-full shadow-lg">
                <span class="font-bold text-xs tracking-widest">PART 2 실습</span>
                <h2 class="text-lg font-bold">윤리 헌장 만들기 프로젝트</h2>
            </div>
            <div class="grid md:grid-cols-1 gap-6">
                 <div class="bg-white p-8 rounded-3xl border border-slate-100 card-shadow hover:border-purple-200 transition-all group">
                    <div class="flex flex-col md:flex-row items-center gap-6">
                         <div class="w-20 h-20 bg-purple-50 text-purple-600 rounded-2xl flex items-center justify-center group-hover:bg-purple-600 group-hover:text-white transition-colors">
                            <i class="fas fa-scroll text-3xl"></i>
                        </div>
                        <div class="flex-1 text-center md:text-left">
                            <h3 class="text-xl font-bold mb-2">우리 회사 AI 윤리 강령 작성하기</h3>
                            <p class="text-slate-500 text-sm mb-4">제공된 템플릿을 활용하여 조직의 핵심 가치를 반영한 'AI 사용 윤리 헌장' 초안을 작성해보는 실습입니다.</p>
                             <button class="w-full md:w-auto px-8 py-3 bg-purple-600 text-white font-bold rounded-xl hover:bg-purple-700 transition-colors">
                                실습 시작하기 <i class="fas fa-arrow-right ml-2"></i>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>
""" + base_html_end

with open("lecture_ethics_class2.html", "w", encoding="utf-8") as f:
    f.write(class2_content)

print("Regenerated lecture_ethics_class1.html and lecture_ethics_class2.html with links")
