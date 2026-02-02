# Day02-08 강의 상세 페이지 헤더 업데이트 스크립트 (개선 버전)

$ErrorActionPreference = "Continue"

# 업데이트할 파일 목록 (샘플 - Day02, Day03, Day04)
$files = @(
    @{file="day02_llm_comparison.html"; day="02"; title="ChatGPT vs Gemini vs Claude"; subtitle="대표 LLM 비교 분석"},
    @{file="day02_role_cot.html"; day="02"; title="역할 부여 & 사고의 연쇄"; subtitle="프롬프트 엔지니어링 핵심 기법"},
    @{file="day03_canva_ai.html"; day="03"; title="Canva AI 기능 마스터"; subtitle="AI 디자인 도구 활용"},
    @{file="day03_design_principles.html"; day="03"; title="AI 디자인 원칙"; subtitle="효과적인 비주얼 제작"},
    @{file="day03_nano_banana.html"; day="03"; title="Nano Banana 플랫폼"; subtitle="AI 이미지 생성 도구"},
    @{file="day04_video_ai.html"; day="04"; title="AI 영상 생성 기술"; subtitle="Text-to-Video 혁신"},
    @{file="day04_runway_gen3.html"; day="04"; title="Runway Gen-3 핵심 기능"; subtitle="고급 영상 제어"},
    @{file="day04_audio_synthesis.html"; day="04"; title="AI 음성 합성 원리"; subtitle="TTS 모델의 작동 방식"}
)

$updatedCount = 0
$failedCount = 0

foreach ($item in $files) {
    $filePath = Join-Path (Get-Location) $item.file
    
    if (-not (Test-Path $filePath)) {
        Write-Host "파일 없음: $($item.file)" -ForegroundColor Yellow
        $failedCount++
        continue
    }
    
    Write-Host "`n처리 중: $($item.file)" -ForegroundColor Cyan
    
    try {
        # 파일 읽기
        $content = Get-Content $filePath -Raw -Encoding UTF8
        
        # 1. 헤더 클래스에 relative overflow-hidden 추가
        $content = $content -replace 'class="gradient-bg text-white py-12 px-8"', 'class="gradient-bg text-white py-12 px-8 relative overflow-hidden"'
        
        # 2. 기존 헤더 구조 찾기 및 교체
        $oldHeaderPattern = '(?s)<header class="gradient-bg[^"]*">.*?</header>'
        
        $newHeader = @"
    <header class="gradient-bg text-white py-12 px-8 relative overflow-hidden">
        <!-- 사용자 정보 및 버튼 영역 -->
        <div class="absolute top-4 right-4 md:top-6 md:right-8 flex items-center gap-3 z-20">
            <span id="userEmailDisplay" class="text-sm text-white/90 font-medium hidden md:inline"></span>
            <a href="day$($item.day)_lecture.html"
                class="inline-flex items-center gap-2 px-4 py-2 bg-white/20 backdrop-blur-md text-white text-sm font-semibold rounded-full border border-white/30 hover:bg-white/30 transition-all">
                <i class="fas fa-arrow-left"></i> <span class="hidden sm:inline">강의로 돌아가기</span>
            </a>
        </div>
        
        <div class="max-w-4xl mx-auto">
            <h1 class="text-3xl md:text-4xl font-bold mb-2">$($item.title)</h1>
            <p class="text-xl opacity-90">$($item.subtitle)</p>
        </div>
    </header>
"@
        
        $content = $content -replace $oldHeaderPattern, $newHeader
        
        # 3. JavaScript에 이메일 표시 로직 추가
        if ($content -match 'window\.location\.href = [''"]index\.html[''"];' -and $content -notmatch 'emailDisplay\.innerText') {
            $jsPattern = "(window\.location\.href = ['\`"]index\.html['\`"];)\s*}"
            $jsReplacement = @"
`$1
        } else {
            const emailDisplay = document.getElementById('userEmailDisplay');
            if (emailDisplay) emailDisplay.innerText = user.email + "님 환영합니다";
        }
"@
            $content = $content -replace $jsPattern, $jsReplacement
        }
        
        # 파일 저장
        [System.IO.File]::WriteAllText($filePath, $content, [System.Text.UTF8Encoding]::new($false))
        
        Write-Host "✓ 완료: $($item.file)" -ForegroundColor Green
        $updatedCount++
    }
    catch {
        Write-Host "✗ 오류: $($item.file) - $_" -ForegroundColor Red
        $failedCount++
    }
}

Write-Host "`n========================================" -ForegroundColor Yellow
Write-Host "업데이트 완료: $updatedCount 파일" -ForegroundColor Green
Write-Host "실패: $failedCount 파일" -ForegroundColor Red
Write-Host "========================================" -ForegroundColor Yellow
