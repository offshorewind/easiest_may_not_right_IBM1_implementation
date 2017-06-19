trg = ''
begin = 0
begin_2 = 0

with open('4.readable.txt', encoding='utf-8') as fin:
    for line in fin:
        if line.startswith('==') and begin == 0:
            begin = 1
            trg = ''

        elif line.startswith('(src)') and begin == 1:
            begin_2 = 1

        elif line.startswith('==') and begin == 1 and begin_2 == 1 and trg != '':
            begin = 1
            begin_2 = 0
            print(trg)
            trg=''

        elif line.startswith('==') and begin == 1 and begin_2 == 1 and trg == '':
            begin = 1
            begin_2 = 0
            trg=''

        elif line.startswith('(trg)') and begin_2 == 1:
            digi = line.find('> ')
            sv = (line[digi + 2:].rstrip())
            trg = trg + sv







#if line.startswith('(src)') and previous_line == 'none':
#    digi = line.find('> ')
#    en = (line[digi + 2:].rstrip())