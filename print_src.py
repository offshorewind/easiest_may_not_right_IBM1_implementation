

with open('4.readable.txt', encoding='utf-8') as fin:
    for line in fin:
        if line.startswith('=='):
            begin = '=='
            srt = ''
        elif line.startswith('(src)') and begin == '==':
            digi = line.find('> ')
            en = (line[digi + 2:].rstrip())
            if srt == '':
                srt = srt + en
            else:
                srt = srt + ' '+ en
        elif line.startswith('(trg)') and srt != '' and begin == '==':
            print(srt)
            begin = '='


#if line.startswith('(src)') and previous_line == 'none':
#    digi = line.find('> ')
#    en = (line[digi + 2:].rstrip())