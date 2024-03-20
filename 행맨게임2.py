import random

# A가 영어 단어를 1개 생각한다.
f = open("voca.txt","r",encoding='UTF-8')
raw_data = f.read()
f.close()
print(raw_data.split("\n")[-1])
data_list = raw_data.split("\n")
data_list = data_list[:-1]
while True:
    r_index = random.randrange(0,len(data_list))
    word = data_list[r_index].replace(u"\xa0", u" ").split(" ")[1]
    if len(word) <= 6 :break
word = word.upper()

# 단어의 글자 수만큼 밑줄을 긋는다.
word_show = "_"*len(word)
print(word_show)
try_num = 0
ok_list = []
no_list = []
while True:
    # B가 다넝에 포함될 것 같은 알파벳을 하나씩 말한다.
    ans = input().upper()
    print(ans)
    # 알파벳이 단어에 포함되면 밑줄에 알파벳을 채워 놓고
    # 포함되지 않은다면 사람을 1획 씩 그린다.
    result = word.find(ans)
    print(result)
    if result == -1 : #없음
        print("오답")
        try_num == +1
        no_list.append(ans)
    else:
        print("정답")
        ok_list.append(ans)
        for i in range(len(word)):
            if word[i] == ans:
                word_show = word_show[:i] + ans + word_show[i+1:]
        print(word_show)
    if try_num == 7 : break
    if word_show.find("_") == -1: break
print(word)