# 강의 상세 페이지 헤더 통일 스크립트
# Day02-08 페이지 (gradient-bg 이미 있는 페이지들)

$files = @(
    "day02_gems_ai.html",
    "day02_llm_comparison.html",
    "day02_prompt_principles.html",
    "day02_role_cot.html",
    "day03_canva_ai.html",
    "day03_design_principles.html",
    "day03_image_params.html",
    "day03_nano_banana.html",
    "day04_audio_synthesis.html",
    "day04_runway_gen3.html",
    "day04_video_ai.html",
    "day04_voice_cloning.html",
    "day05_automation_design.html",
    "day05_make_zapier.html",
    "day05_nocode_overview.html",
    "day05_trigger_action.html",
    "day06_coding_prompt.html",
    "day06_cursor_setup.html",
    "day06_pair_programming.html",
    "day06_vibe_coding.html",
    "day07_api_integration.html",
    "day07_database_connection.html",
    "day07_framework_overview.html",
    "day07_web_app_structure.html",
    "day08_cloud_deployment.html",
    "day08_domain_https.html",
    "day08_git_github.html",
    "day08_maintenance.html"
)

$basePath = "c:\Users\Win\Desktop\Antigravity 실습\AI Class"
$updatedCount = 0

foreach ($file in $files) {
    $filePath = Join-Path $basePath $file
    
    if (Test-Path $filePath) {
        Write-Host "Processing: $file" -ForegroundColor Cyan
        
        # 파일 읽기
        $content = Get-Content $filePath -Raw -Encoding UTF8
        
        # Day 번호 추출
        if ($file -match "day(\d+)_") {
            $dayNum = $matches[1]
            $lectureFile = "day${dayNum}_lecture.html"
        }
        
        # 1. 헤더 클래스 업데이트: relative overflow-hidden 추가
        $content = $content -replace '<header class="gradient-bg text-white py-12 px-8">', '<header class="gradient-bg text-white py-12 px-8 relative overflow-hidden">'
        
        # 2. 사용자 정보 영역이 없으면 추가
        if ($content -notmatch 'userEmailDisplay') {
            # 헤더 태그 다음에 사용자 정보 영역 삽입
            $userSection = @"
        <!-- 사용자 정보 및 버튼 영역 -->
        <div class="absolute top-4 right-4 md:top-6 md:right-8 flex items-center gap-3 z-20">
            <span id="userEmailDisplay" class="text-sm text-white/90 font-medium hidden md:inline"></span>
            <a href="$lectureFile"
                class="inline-flex items-center gap-2 px-4 py-2 bg-white/20 backdrop-blur-md text-white text-sm font-semibold rounded-full border border-white/30 hover:bg-white/30 transition-all">
                <i class="fas fa-arrow-left"></i> <span class="hidden sm:inline">강의로 돌아가기</span>
            </a>
        </div>
        
"@
            $content = $content -replace '(<header class="gradient-bg[^"]*">\s*)', "`$1$userSection"
        }
        
        # 3. JavaScript에 이메일 표시 로직 추가
        if ($content -match 'onAuthStateChanged\(auth, \(user\) => \{') {
            if ($content -notmatch 'emailDisplay\.innerText') {
                # window.location.href = 'index.html'; 다음에 else 블록 추가
                $content = $content -replace "(window\.location\.href = 'index\.html';)\s*\}", @"
`$1
        } else {
            const emailDisplay = document.getElementById('userEmailDisplay');
            if (emailDisplay) emailDisplay.innerText = user.email + "님 환영합니다";
        }
"@
            }
        }
        
        # 파일 저장
        $content | Out-File -FilePath $filePath -Encoding UTF8 -NoNewline
        
        Write-Host "✓ Updated: $file" -ForegroundColor Green
        $updatedCount++
    }
    else {
        Write-Host "✗ File not found: $file" -ForegroundColor Red
    }
}

Write-Host "`n========================================" -ForegroundColor Yellow
Write-Host "완료: $updatedCount / $($files.Count) 파일 업데이트" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Yellow
