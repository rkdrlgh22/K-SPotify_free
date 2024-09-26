import os
import subprocess
from tkinter import messagebox, Tk, Label, Text

# Spotify 설치 여부 확인
def check_spotify_installation():
    spotify_path = os.path.join(os.getenv('APPDATA'), 'Spotify', 'Spotify.exe')
    return os.path.exists(spotify_path)

# WireGuard GUI 실행
def run_wireguard_gui():
    subprocess.Popen([r"C:\Program Files\WireGuard\wireguard.exe"])

# 사용자 안내 메시지
def show_instructions():
    instructions = (
        "1. 공식 WireGuard VPN 클라이언트가 실행되면 **Import Tunnel(s) from File** 를 클릭합니다.\n\n"
        "2. **OPEN** → Proton VPN 에서 다운로드한 WireGuard 구성 파일(.conf)을 선택합니다.\n\n"
        "3. 방금 다운로드한 구성이 선택되었는지 확인하고 **Activate(활성화)** 를 클릭합니다.\n\n"
        "4. 2주마다 국가인증이 필요하기 때문에 2주마다 프로그램을 실행후에 로그인해주시기 바랍니다."
    )
    
    root = Tk()
    root.title("안내")
    
    # 안내 메시지 라벨
    label = Label(root, text="해당 창은 모든 진행이 다 된후에 닫아주세요.\n\n", font=("Malgun Gothic", 20), justify="left")
    label.pack(padx=20, pady=10)
    
    # 기본 폰트로 설정된 텍스트
    text = Text(root, font=("Malgun Gothic", 12), wrap="word")
    text.insert("1.0", instructions)
    text.config(state="disabled")
    text.pack(padx=20, pady=10)
    
    root.mainloop()

# Spotify 설치
def install_spotify():
    response = messagebox.askyesno("Spotify 설치", "Spotify가 설치되어 있지 않습니다. 설치하시겠습니까?")
    if response:
        subprocess.run(["powershell", "-Command", "iex \"& { $(iwr -useb 'https://raw.githubusercontent.com/SpotX-Official/spotx-official.github.io/main/run.ps1') } -confirm_uninstall_ms_spoti -confirm_spoti_recomended_over -podcasts_off -block_update_on -start_spoti -new_theme -adsections_off -lyrics_stat spotify\""])

if __name__ == "__main__":
    if check_spotify_installation():
        print("Spotify가 설치되어 있습니다.")
        subprocess.Popen([os.path.join(os.getenv('APPDATA'), 'Spotify', 'Spotify.exe')])
    else:
        print("Spotify가 설치되어 있지 않습니다.")
        install_spotify()
    
    run_wireguard_gui()
    show_instructions()
