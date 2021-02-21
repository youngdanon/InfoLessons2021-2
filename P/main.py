f = open('./db2', 'r', encoding='utf-8')
file_lst = []
ip_dict = {}
line_count = 0
hints = []
for line in f:
    tab_count = 0
    buf_lst = line.split('\t')
    if len(buf_lst) < 4:
        hints.append(buf_lst)
    else:
        line_count += 1
        buffer = ""
        for i in range(len(buf_lst[2])):
            if not buf_lst[2][i] in ['-', '(', ')']:
                buffer += buf_lst[2][i]
        buffer = tuple(buffer.split())
        buf_lst[2] = buffer
        file_lst.append(buf_lst)

        if buffer[0] in ['+7', '8']:
            print('RUSSIAN NUMBER DETECTED: ', line)

        if buf_lst[1] in ip_dict:
            ip_buff_lst = ip_dict[buf_lst[1]]
            ip_buff_lst.append(line_count)
            ip_dict.update({buf_lst[1]: ip_buff_lst})
        else:
            ip_dict.update({buf_lst[1]: [line_count]})

print("\n\n\n+++++++++++ REPEATED IPS +++++++++++")
for key in ip_dict:
    if len(ip_dict[key]) > 1:
        for line_num in ip_dict[key]:
            print(file_lst[line_num - 1])
        print('======================================')

print("HINTS : ", hints)
