import os


dict_file = {}
with open('Quest 3/1.txt') as txt1:
    count_txt1 = len(txt1.readlines())
    file_path1 = os.path.join(os.getcwd(), '1.txt')
    file_name1 = os.path.basename(file_path1)
    dict_file[file_name1] = count_txt1

    

with open('Quest 3/2.txt') as txt2:
    count_txt2 = len(txt2.readlines())
    file_path2 = os.path.join(os.getcwd(), '2.txt')
    file_name2 = os.path.basename(file_path2)
    dict_file[file_name2] = count_txt2
 

with open('Quest 3/3.txt') as txt3:
    count_txt3 = len(txt3.readlines())
    file_path3 = os.path.join(os.getcwd(), '3.txt')
    file_name3 = os.path.basename(file_path3)
    dict_file[file_name3] = count_txt3

    
sort_dict_file = sorted(dict_file.items(), key=lambda item: item[1])
print(sort_dict_file)
with open('Quest 3/1-3.txt', 'a') as txt13:
    for txt in sort_dict_file:
        txt13.write(txt[0] + '\n')
        txt13.write(str(txt[1]) + '\n')

        if txt[0] == '1.txt':
            with open('Quest 3/1.txt') as txt1:
                tx1 = txt1.read()
                txt13.write(tx1 + '\n')
                
        elif txt[0] == '2.txt':
            with open('Quest 3/2.txt') as txt2:
                tx2 = txt2.read()
                txt13.write(tx2 + '\n')
        else:
            with open('Quest 3/3.txt') as txt3:
                tx3 = txt3.read()
                txt13.write(tx3 + '\n')




    
