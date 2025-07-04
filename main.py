def file_to_dict(file_path):
    """
    פותח קובץ טקסט ומחזיר מילון שבו כל מילה ומספר ההופעות שלה.

    :param file_path: נתיב לקובץ הטקסט
    :return: מילון {מילה: מספר הופעות}
    """
     
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
    """
    מקבלת מספר ומילון מסדרת את המילון ונותן את המספר של המילים שחש העח הרבה.

    :param file_path: מילון,מספר
    :return: מילון מסודר {מילה: מספר הופעות}
    """
     
    sorted_dict = dict(sorted(dic.items(), key=lambda word: word[1], reverse=True)[:n]) # צריך לעשות ריוורס כדי שיהיה מהגדול לקטן
    return sorted_dict

file_path = input("enter file name ") #מקבל path ומספר
number = int(input("enter amount of words")) # מקבל מספר מילים
word_counts = file_to_dict(file_path)

sorted_counts = sort_dict(word_counts,number)

print(sorted_counts)