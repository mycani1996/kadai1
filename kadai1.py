import csv

path = './data/charactor_list.csv'
csv_header = ['No','Name']

def check_char(char_in):
    with open(path, mode='r') as char_file:
        char_list = [row for row in csv.reader(char_file)][0]
        # print(char_list)
        if set([char_in]) <= set(char_list):
            print('"',char_in,'"は追加済みです')
        else:
            print('存在しません。"',char_in,'"を追加します')
            with open(path, mode='w') as char_file_w:
                char_list.append(char_in)
                writer = csv.writer(char_file_w)
                writer.writerow(char_list)
                # print(char_list)
char_name = input("好きなキャラクター名を入力してください（'fin'で終了）：")
while char_name != "fin":
    check_char(char_name)
    char_name = input("好きなキャラクター名を入力してください（'fin'で終了）：")
print("終了します")
