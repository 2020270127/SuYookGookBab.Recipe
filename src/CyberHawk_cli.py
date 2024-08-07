from extensions.util import *

if __name__ == "__main__":
    user_input = input("어떤 명령을 수행하시겠습니까? (ls, mkdir, rm, touch, cp, mv, filehash, virus_scan): ")

    try: #인자가 있는 함수
        function_name, *args = user_input.split() #공백 기준
    except ValueError: #인자가 없는 함수
        function_name = user_input
        args = [] 

    try:
        command = globals()[function_name]
        command(*args)
    except KeyError:
        print("잘못된 명령어입니다.")
