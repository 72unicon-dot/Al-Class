import os

# Course Data
courses = [
    {
        "filename": "intro_ethics.html",
        "title": "AI소개 및 윤리",
        "tag": "초급 과정",
        "color": "blue",
        "icon": "fa-shield-alt",
        "duration": "1일 (4시간)",
        "price": "₩100,000",
        "desc": "AI 기본 개념, 사회적 영향, 데이터 개인정보 및 저작권 기초",
        "detail": "AI의 기본 개념을 이해하고, 급변하는 사회적 영향과 윤리적 이슈를 파악합니다. 데이터 저작권과 보안의 기초를 다집니다."
    },
    {
        "filename": "intro_basics.html",
        "title": "AI 기초 입문",
        "tag": "초급 과정",
        "color": "blue",
        "icon": "fa-seedling",
        "duration": "1일 (8시간)",
        "price": "₩200,000",
        "desc": "ChatGPT/Gemini 기본 사용법, 프롬프트 기초, 업무 자동화 첫걸음",
        "detail": "생성형 AI의 기초 사용법부터 실무 적용을 위한 프롬프트 엔지니어링 입문까지, AI와 친해지는 첫걸음입니다."
    },
    {
        "filename": "intro_business.html",
        "title": "AI 비즈니스 활용",
        "tag": "초급 과정",
        "color": "blue",
        "icon": "fa-briefcase",
        "duration": "2일 (16시간)",
        "price": "₩400,000",
        "desc": "직무별 활용 케이스, 생성형 AI 기반 문서 및 제안서 작성 실습",
        "detail": "실제 비즈니스 현장에서 쓰이는 직무별 AI 활용 사례를 학습하고, 보고서 및 제안서를 자동 생성하는 실습을 진행합니다."
    },
    {
        "filename": "expert_advanced.html",
        "title": "AI 전문가 심화",
        "tag": "상급 과정",
        "color": "orange",
        "icon": "fa-crown",
        "duration": "10일 (80시간)",
        "price": "₩1,500,000",
        "desc": "Fine-tuning 및 RAG 시스템 구축, AI 에이전트 개발, 기업 도입 전략",
        "detail": "독자적인 AI 모델 튜닝과 검색 증강 생성(RAG) 시스템을 구축하고, 자율 AI 에이전트를 개발하는 고급 기술을 마스터합니다."
    },
    {
        "filename": "special_marketing.html",
        "title": "AI 마케팅 전문가",
        "tag": "특화 과정",
        "color": "pink",
        "icon": "fa-bullhorn",
        "duration": "5일 (40시간)",
        "price": "₩600,000",
        "desc": "AI 콘텐츠 생성, 고객 데이터 타겟팅, 캠페인 자동화 시스템",
        "detail": "카피라이팅부터 이미지, 영상 생성까지 마케팅 콘텐츠를 AI로 자동화하고, 데이터 기반 타겟팅 전략을 수립합니다."
    },
    {
        "filename": "special_manufacturing.html",
        "title": "AI 제조 전문가",
        "tag": "특화 과정",
        "color": "gray",
        "icon": "fa-industry",
        "duration": "5일 (40시간)",
        "price": "₩700,000",
        "desc": "제조 공정 이상 감지, 공정 최적화 및 스마트 팩토리 AI 사례",
        "detail": "스마트 팩토리 데이터를 분석하여 공정 이상을 사전에 감지하고, 생산 효율성을 극대화하는 AI 솔루션을 학습합니다."
    },
    {
        "filename": "special_data.html",
        "title": "AI 데이터 분석가",
        "tag": "특화 과정",
        "color": "cyan",
        "icon": "fa-chart-bar",
        "duration": "5일 (40시간)",
        "price": "₩900,000",
        "desc": "Python & Pandas 기초, AI 예측 모델링, 비즈니스 시각화",
        "detail": "코딩 없이도 가능한 데이터 분석부터 Python을 활용한 고급 분석까지, 데이터에서 인사이트를 도출하고 시각화합니다."
    },
    {
        "filename": "special_video.html",
        "title": "AI 영상 크리에이터",
        "tag": "특화 과정",
        "color": "red",
        "icon": "fa-video",
        "duration": "5일 (40시간)",
        "price": "₩700,000",
        "desc": "영상 편집/자막 자동화, AI 보이스오버, 숏폼 대량 생산",
        "detail": "촬영 없이 AI로 고퀄리티 영상을 제작하고, 숏폼 콘텐츠를 대량 생산하여 채널을 빠르게 성장시키는 비법을 배웁니다."
    },
    {
        "filename": "management_leadership.html",
        "title": "AI시대의 리더십",
        "tag": "관리 과정",
        "color": "yellow",
        "icon": "fa-user-tie",
        "duration": "1일 (8시간)",
        "price": "₩300,000",
        "desc": "성공적인 AI 도입을 위한 경영진의 의사결정과 조직 혁신 전략",
        "detail": "AI 트랜스포메이션 시대, 리더가 알아야 할 핵심 기술 트렌드와 조직 관리, 윤리적 의사결정 전략을 수립합니다."
    },
    {
        "filename": "strategy_consultant.html",
        "title": "AI 비즈니스 컨설턴트",
        "tag": "전략 과정",
        "color": "emerald",
        "icon": "fa-chess",
        "duration": "20일 (160시간)",
        "price": "₩2,400,000",
        "desc": "AI 도입 ROI 분석, 프로세스 재설계(Re-design), 로드맵 수립",
        "detail": "기업의 AI 도입 타당성을 분석하고, 비즈니스 프로세스를 재설계하여 실질적인 ROI를 창출하는 전문 컨설턴트로 성장합니다."
    },
    {
        "filename": "master_app_creator.html",
        "title": "비즈니스 앱 크리에이터",
        "tag": "마스터 과정",
        "color": "indigo",
        "icon": "fa-robot",
        "duration": "60일 (480시간)",
        "price": "₩7,200,000",
        "desc": "LangChain & Vector DB, 멀티채널 챗봇, 엔터프라이즈급 앱 배포",
        "detail": "현업 수준의 복잡한 AI 애플리케이션을 직접 설계 및 개발하고, 실제 서비스로 배포하여 운영하는 최상위 과정입니다."
    }
]

# Read template
with open('master_index.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Generate files
for course in courses:
    content = template
    
    # Simple Replacements
    content = content.replace("AI 실무 마스터 클래스", course['title'])
    content = content.replace("중급 과정", course['tag'])
    content = content.replace("8일 완성 과정", f"{course['duration']} 완성")
    content = content.replace("업무 혁신을 이끄는 <b>10대 AI 도구</b>와 <b>바이브 코딩</b>을 8일 동안 마스터하세요", 
                            f"{course['desc']}<br><span class='text-base font-normal mt-2 block'>{course['detail']}</span>")
    
    # Helper for Color Replacement (Purple is default in template)
    # We need to replace specific color classes if they exist in the Hero/Tags
    # This is a bit tricky with simple replace, but we'll try to target the Hero tags
    
    target_color = course['color']
    if target_color != "purple":
        # Replace Hero Badge Color
        content = content.replace("bg-purple-600/80", f"bg-{target_color}-600/80")
        
        # Replace Hero icon (Rocket is default)
        content = content.replace("fa-rocket mr-2", f"{course['icon']} mr-2")
        
        # NOTE: Not replacing all purple instances as they might be part of the design system (gradients etc).
        # Just updating the main identity elements.
    
    # Write file
    with open(course['filename'], 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {course['filename']}")

print("\nAll 11 course pages created successfully!")
