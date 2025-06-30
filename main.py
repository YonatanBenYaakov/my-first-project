def file_to_dict(file_path):
    dic = {}
    with open(file_path) as f:  #פותח את הקובץ טקסט
        for line in f:         
            words_lst = line.split()  # מחלק את השורה על פי רווחים והופך אותה לליסט
            for word in words_lst: # עובר על כל מי בליסט
                if word in dic:
                    dic[word] += 1  # אם המילה במילון תוסיף אחד לערך שלה כלומר כמות הפעמים שמילה מופיעה
                else:
                    dic[word] = 1 # מיקום במילון של המילה שמופיעה פעם אחת
    return dic

def sort_dict(dic, n):
    sorted_dict = dict(sorted(dic.items(), key=lambda word: word[1], reverse=True)[:n])
    return sorted_dict

file_path = input("enter file name ") #מקבל path ומספר
number = int(input("enter amount of words")) # מקבל מספר מילים
word_counts = file_to_dict(file_path)

sorted_counts = sort_dict(word_counts,number)

print(sorted_counts)