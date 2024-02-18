text_list = []

file_names = ('1.txt', '2.txt', '3.txt')
for file_name in file_names:
    with open (file_name, encoding= 'utf-8') as text_files:
        text_files_list = text_files.readlines()
        txt_all_list = [len(text_files_list), file_name, text_files_list]
        text_list.append(txt_all_list)
text_list.sort()

sorted_text = (f'{text_list[0][1]}\n{text_list[0][0]}\n{text_list[0][2]}'
            f'\n\n{text_list[1][1]}\n{text_list[1][0]}\n{text_list[1][2]}'
            f'\n\n{text_list[2][1]}\n{text_list[2][0]}\n{text_list[2][2]}')

with open ('sorted_text.txt', 'w', encoding= 'utf-8') as new_file:
    new_file.write(sorted_text)