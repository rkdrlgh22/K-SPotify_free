import subprocess
import time
import socket
from tkinter import messagebox, Tk, Label, Text

# WireGuard GUI 실행
def run_wireguard_gui():
    subprocess.Popen([r"C:\Program Files\WireGuard\wireguard.exe"])

# 사용자 안내 메시지
def show_instructions():
    GREEN = '\033[92m'
    RESET = '\033[0m'
    instructions = (
        f"1. 공식 WireGuard VPN 클라이언트가 실행되면 **Import Tunnel(s) from File** 를 클릭합니다.\n\n"
        f"2.  **OPEN** → Proton VPN 에서 다운로드한 WireGuard 구성 파일(.conf)을 선택합니다.\n\n"
        f"3. 방금 다운로드한 구성이 선택되었는지 확인하고  **Activate(활성화)**  를 클릭합니다."
    )
    
    root = Tk()
    root.title("안내")
    
    # 큰 폰트로 설정된 라벨
    label_large = Label(root, text="해당 창은 모든 진행이 다 된후에 닫아주세요.\n\n", font=("Malgun Gothic", 20), justify="left")
    label_large.pack(padx=20, pady=10)
    
    # 기본 폰트로 설정된 텍스트
    text = Text(root, font=("Arial", 12), wrap="word")
    text.insert("1.0", instructions)
    text.config(state="disabled")
    text.pack(padx=20, pady=10)
    
    root.mainloop()

# IP 주소 확인
def check_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Spotify 계정 생성 페이지 열기
def open_spotify_signup():
    subprocess.run(["start", "chrome", "https://www.spotify.com/signup/"], shell=True)

if __name__ == "__main__":
    initial_ip = check_ip()
    print(f"초기 IP 주소: {initial_ip}")
    
    run_wireguard_gui()
    show_instructions()
    input("VPN을 활성화한 후 Enter 키를 누르세요...")
    
    while True:
        new_ip = check_ip()
        if new_ip != initial_ip:
            print(f"새로운 IP 주소: {new_ip}")
            break
        print("IP 주소가 아직 변경되지 않았습니다. 5초 후에 다시 시도합니다...")
        time.sleep(5)
    
    open_spotify_signup()
