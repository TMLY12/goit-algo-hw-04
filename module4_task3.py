import sys
from pathlib import Path
from colorama import Fore, Style, init
def visualize_directory(path, indent=""):
    root = Path(path)
    if not root.exists():
        print(f"{Fore.RED}Пути нет!{Style.RESET_ALL}")
    for item in root.iterdir():
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}📂{item.name}{Style.RESET_ALL}")
            visualize_directory(item, indent + "  ")
        else:
            print(f"{indent}{Fore.GREEN}📜{item.name}{Style.RESET_ALL}")
if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_path = sys.argv[1]
        visualize_directory(user_path)
    else:
        print(f"{Fore.YELLOW}Укажите путь{Style.RESET_ALL}")