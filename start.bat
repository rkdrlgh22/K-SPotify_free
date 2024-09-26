@echo off
chcp 65001 >nul

REM Step 1: installation_cache.txt 파일 확인
if exist installation_cache.txt (
    REM Step 2: installation_cache.txt 파일에 필요한 내용이 있는지 확인
    findstr /c:"selenium installation complete." installation_cache.txt >nul && ^
    findstr /c:"requests installation complete." installation_cache.txt >nul && ^
    findstr /c:"tk installation complete." installation_cache.txt >nul && ^
    findstr /c:"webdriver_manager installation complete." installation_cache.txt >nul && ^
    (findstr /c:"WireGuard installation complete." installation_cache.txt >nul || findstr /c:"WireGuard was already installed." installation_cache.txt >nul)
    if errorlevel 1 (
        REM 필요한 내용이 없으면 first_install.bat 실행
        call first_install.bat
    )
) else (
    REM installation_cache.txt 파일이 없으면 first_install.bat 실행
    call first_install.bat
)

:ask_spotify_account
REM Step 3: 스포티파이 계정 여부 확인
set /p spotify_account="스포티파이 계정이 있습니까? (y/n): "

if /i "%spotify_account%"=="n" (
    REM 스포티파이 계정이 없으면 made_account.py 실행
    python made_account.py
) else if /i "%spotify_account%"=="y" (
    REM 스포티파이 계정이 있으면 아무것도 하지 않음
) else (
    echo 다시 타이핑해주세요.
    goto ask_spotify_account
)

REM Step 4: 마지막으로 check_install.py 실행
python check_install.py
