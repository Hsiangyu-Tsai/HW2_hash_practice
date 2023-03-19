file = open("hw2_data.txt", "r")  # 開啟檔案
hash_dict = {}
oneline_list = []
non_repeating_list = []
for oneline in file:
    oneline = oneline.strip()
    oneline_list.append(oneline)  # 把每一行的字串丟到oneline_list

arr_length = len(oneline_list)
for i in range(0, arr_length, 1):
    if oneline_list[i] in hash_dict:  # 如果在dict裡就讓dict value++
        hash_dict[oneline_list[i]] += 1
    else:
        hash_dict[oneline_list[i]] = 1  # 如果不在dict裡就把它加入dict 設value=1
        non_repeating_list.append(oneline_list[i])  # 順便把它加到不重複的list中 因為重複的詞經過條件判斷只會跑到這裡一次

count = 0  # 用來計算沒有重複詞的數量
for i in range(0, arr_length, 1):
    if hash_dict[oneline_list[i]] == 1:
        count += 1

print("總共有%d個不重複的英文字" % count)  # 第一個問題
for i in range(0, len(non_repeating_list), 1):
    print(non_repeating_list[i] + '出現次數:' + str(hash_dict[non_repeating_list[i]]))  # 第二個問題

file.close()  # 關閉檔案
