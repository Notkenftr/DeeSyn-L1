import time
import yaml
from rich.console import Console
from colorama import Fore
import os

console = Console()

def setting():
    with open('config.yml', 'r') as f:
        config = yaml.safe_load(f)
    console.print("Main", style="rgb(216,240,250)")
    console.print("[1] Import token", style="rgb(216,240,250)")
    console.print("[2] Import Gemini Api", style="rgb(216,240,250)")
    console.print("[3] Run Bot", style="rgb(216,240,250)")

    user_chose = int(input("Nhập lựa chọn của bạn, 1/2/3: "))
    if user_chose not in [1, 2, 3]:
        print(Fore.RED + "Vui lòng chọn lại, lựa chọn của bạn không hợp lệ..." + Fore.RESET)
        time.sleep(2)
        os.system('cls')
        setting()
    if user_chose == 1:
        token = str(input("Nhập token của bạn: "))
        config['Bot-token'] = token
        print("Đã import thành công token...")
        with open('config.yml', 'w') as f:
            yaml.safe_dump(config, f, sort_keys=False)
        time.sleep(2)
        os.system('cls')
        setting()
    if user_chose == 2:
        api = str(input("Nhập api của bạn: "))
        config['Gemini-api'] = api
        print("Đã import thành công api...")
        with open('config.yml', 'w') as f:
            yaml.safe_dump(config, f, sort_keys=False)
        time.sleep(2)
        os.system('cls')
        setting()
    if user_chose == 3:
        print("Bot đang khởi động vui lòng chờ...")
        time.sleep(2)
        os.system('python3 Core/DeepMyst.py')
