import csv

DATA_PATH = './data/source.csv'

def check_name(name):
    with open(DATA_PATH, mode='r') as file:
        list = [row for row in csv.reader(file)][0]
        if set([name]) <= set(list):
            print(f'{name}は追加済みです')
        else:
            print(f'存在しません。{name}を追加します')
            with open(DATA_PATH, mode='w') as file_w:
                list.append(name)
                writer = csv.writer(file_w)
                writer.writerow(list)

def main():
    charactor_name = input("好きなキャラクター名を入力してください（'fin'で終了）：")
    if charactor_name != "fin":
        check_name(charactor_name)
        return True
    else:
        print("終了します")
        return False

if __name__ == "__main__":
    flg = True
    while flg:
        flg = main()
    

