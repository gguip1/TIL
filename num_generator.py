import os
import argparse

def num_generator(num):
    dir_name = f'./{num}'
    file_name = f'{num}.py'

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        file_path = os.path.join(dir_name, file_name)
        
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                pass
        else:
            print(f'{num}번 문제는 이미 존재합니다.')
    else:
        print(f'{num}번 문제는 이미 존재합니다.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num", type=int, help="문제 번호")
    args = parser.parse_args()

    num_generator(args.num)