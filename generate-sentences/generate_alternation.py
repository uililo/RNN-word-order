def permute_all_short(fin, fout, order=['subj', 'dobj', 'iobj', 'verb']):
    lines = open(fin).readlines()
    fo = open(fout, 'w')
    for line in lines:
        words = line.split()
        subj = words[0:2]
        iobj = words[2:4]
        dobj = words[4:6]
        verb = words[6:7]
        pos2words = {'subj': subj, 'dobj': dobj, 'iobj': iobj, 'verb':verb}
        new_line = []
        for pos in order:
            new_line.extend(pos2words[pos])
        new_line = ' '.join(new_line) + ' . <eos>\n'
        fo.write(new_line)
    fo.close()

def permute_long_io(fin, fout, order=['subj', 'dobj', 'io_mod', 'iobj', 'verb']):
    lines = open(fin).readlines()
    fo = open(fout, 'w')
    for line in lines:
        words = line.split()
        subj = words[0:2]
        iobj = words[5:7]
        io_mod = words[2:5]
        dobj = words[7:9]
        verb = words[9:10]
        pos2words = {'subj': subj, 'dobj': dobj, 'iobj': iobj, 'io_mod':io_mod, 'verb':verb}
        new_line = []
        for pos in order:
            new_line.extend(pos2words[pos])
        new_line = ' '.join(new_line) + ' . <eos>\n'
        fo.write(new_line)
    fo.close()


def permute_long_do(fin, fout, order=['subj', 'iobj', 'do_mod', 'dobj', 'verb']):
    lines = open(fin).readlines()
    fo = open(fout, 'w')
    for line in lines:
        words = line.split()
        subj = words[0:2]
        dobj = words[5:7]
        do_mod = words[2:5]
        iobj = words[7:9]
        verb = words[9:10]
        pos2words = {'subj': subj, 'dobj': dobj, 'iobj': iobj, 'do_mod':do_mod, 'verb':verb}
        new_line = []
        for pos in order:
            new_line.extend(pos2words[pos])
        new_line = ' '.join(new_line) + ' . <eos>\n'
        fo.write(new_line)
    fo.close()

permute_all_short('generate-sentences/generated_set2/to_evaluate/all_short_SIDV.txt','generate-sentences/generated_set2/to_evaluate/all_short_SDIV.txt' )
permute_all_short('generate-sentences/generated_set2/to_evaluate/all_short_SIDV.txt','generate-sentences/generated_set2/to_evaluate/all_short_ISDV.txt', ['iobj', 'subj', 'dobj', 'verb'] )
permute_all_short('generate-sentences/generated_set2/to_evaluate/all_short_SIDV.txt','generate-sentences/generated_set2/to_evaluate/all_short_DSIV.txt', ['dobj','subj', 'iobj', 'verb'] )

permute_all_short('generate-sentences/generated_set2/to_evaluate/all_long_SIDV.txt','generate-sentences/generated_set2/to_evaluate/all_long_SDIV.txt' )
permute_all_short('generate-sentences/generated_set2/to_evaluate/all_long_SIDV.txt','generate-sentences/generated_set2/to_evaluate/all_long_ISDV.txt', ['iobj', 'subj', 'dobj', 'verb'] )
permute_all_short('generate-sentences/generated_set2/to_evaluate/all_long_SIDV.txt','generate-sentences/generated_set2/to_evaluate/all_long_DSIV.txt', ['dobj','subj', 'iobj', 'verb'] )

permute_long_io('generate-sentences/generated_set2/to_evaluate/long_io_SIDV.txt', 'generate-sentences/generated_set2/to_evaluate/long_io_SDIV.txt')
permute_long_io('generate-sentences/generated_set2/to_evaluate/long_io_SIDV.txt', 'generate-sentences/generated_set2/to_evaluate/long_io_ISDV.txt', ['io_mod', 'iobj', 'subj', 'dobj', 'verb'])
permute_long_io('generate-sentences/generated_set2/to_evaluate/long_io_SIDV.txt', 'generate-sentences/generated_set2/to_evaluate/long_io_DSIV.txt', [  'dobj', 'subj', 'io_mod', 'iobj', 'verb'])

permute_long_io('generate-sentences/generated_set2/to_evaluate/long_io_extra_SIDV.txt', 'generate-sentences/generated_set2/to_evaluate/long_io_extra_SDIV.txt')
permute_long_io('generate-sentences/generated_set2/to_evaluate/long_io_extra_SIDV.txt', 'generate-sentences/generated_set2/to_evaluate/long_io_extra_ISDV.txt', ['io_mod', 'iobj', 'subj', 'dobj', 'verb'])
permute_long_io('generate-sentences/generated_set2/to_evaluate/long_io_extra_SIDV.txt', 'generate-sentences/generated_set2/to_evaluate/long_io_extra_DSIV.txt', [  'dobj', 'subj', 'io_mod', 'iobj', 'verb'])

permute_long_do('generate-sentences/generated_set2/to_evaluate/long_do_SDIV.txt', 'generate-sentences/generated_set2/to_evaluate/long_do_SIDV.txt')
permute_long_do('generate-sentences/generated_set2/to_evaluate/long_do_SDIV.txt', 'generate-sentences/generated_set2/to_evaluate/long_do_ISDV.txt', ['iobj', 'subj', 'do_mod', 'dobj', 'verb'])
permute_long_do('generate-sentences/generated_set2/to_evaluate/long_do_SDIV.txt', 'generate-sentences/generated_set2/to_evaluate/long_do_DSIV.txt', [ 'do_mod', 'dobj','subj','iobj',  'verb'])