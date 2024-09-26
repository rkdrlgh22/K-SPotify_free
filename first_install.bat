@echo off
chcp 65001 >nul

echo 필수 Python 패키지 설치 중...
set packages=selenium requests tk webdriver_manager
set cache_file=installation_cache.txt

REM 기존 installation_cache.txt 파일이 존재하는 경우 삭제하지 않음
if not exist %cache_file% (
    echo 새로운 캐시 파일 생성 중...
    echo > %cache_file%
)

for %%p in (%packages%) do (
    findstr /c:"%%p installation complete." %cache_file% >nul || (
        echo %%p 설치 중...
        pip install %%p
        if !errorlevel! neq 0 (
            echo %%p 설치 실패. 건너뜀...
            echo %%p installation failed. >> %cache_file%
        ) else (
            echo %%p 설치 완료.
            echo %%p installation complete. >> %cache_file%
        )
    )
)

echo 설치 완료!

echo WireGuard 설치 여부 확인 중...
if not exist "C:\Program Files\WireGuard\wireguard.exe" (
    echo WireGuard가 설치되지 않았습니다. WireGuard 다운로드 및 설치 중...
    powershell -Command "Start-Process 'https://download.wireguard.com/windows-client/wireguard-installer.exe' -Wait"
    if !errorlevel! neq 0 (
        echo WireGuard 설치 실패. >> %cache_file%
    ) else (
        echo WireGuard 설치 완료!
        echo WireGuard installation complete. >> %cache_file%
    )
) else (
    findstr /c:"WireGuard installation complete." %cache_file% >nul || findstr /c:"WireGuard was already installed." %cache_file% >nul || (
        echo WireGuard가 이미 설치되어 있습니다.
        echo WireGuard was already installed. >> %cache_file%
    )
)

pause
