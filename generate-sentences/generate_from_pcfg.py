import random
import numpy as np
from collections import defaultdict, Counter

def read_terminals(fname):
    return open(fname).read().split()


def general_mod():
    mods = []

    if control_post_position:
        post = 'pp'
    else:
        post = 'ni'

    for loc in ['table', 'apartment', 'hallway', 'house', 'garden']:
        for v in ['lived', 'stood', 'was', 'stayed', 'sat']:
            mods.append('%s %s %s' % (loc, post, v))

    for media in ['newspaper', 'television', 'twitter', 'magazine']:
        for v in ['seen', 'found', 'read', 'reported']:
            mods.append('%s %s %s' % (media, post, v))

    return mods

def io_specific_mod():
    mods = []

    if control_post_position:
        post = 'pp'
    else:
        post = 'wo'

    for activity in ['birdwatching', 'singing', 'painting', 'knitting']:
        for v in ['enjoyed', 'studied', 'hated', 'loved']:
            mods.append('%s %s %s' % (activity, post, v))

    for prop in ['dog', 'house', 'cat', 'plane', 'bike']:
        for v in ['had', 'owned']:
            mods.append('%s %s %s' % (prop, post, v))

    return mods

def do_specific_mod():
    mods = []

    if control_post_position:
        post = 'pp'
    else:
        post = ''

    for content in ['religion', 'politics', 'science', 'linguistics', 'engineering']:
        for v in ['about', 'focused', ]:
            mods.append('%s %s %s' % (content, post, v))

    if control_post_position:
        post = 'pp'
    else:
        post = 'de'

    for content in ['water', 'information', 'record', 'word']:
        for v in ['contained', 'filled', 'populated', 'held']:
            mods.append('%s %s %s' % (content, post, v))

    return mods


def sample_long_io_extra():
    s = random.choice(subj_iobj)
    io = random.choice(subj_iobj)
    while io == s:
        io = random.choice(subj_iobj)
    v = random.choice(verb)
    do = random.choice(dobj)
    io_mod_v = random.choice(verb)
    while io_mod_v == v:
        io_mod_v = random.choice(verb)
    io_mod_do = random.choice(dobj)
    while io_mod_do == do:
        io_mod_do = random.choice(dobj)
    sentence = '%s wa %s %s %s %s ni %s wo %s . <eos>\n' % (s, io_mod_do, 'wo', io_mod_v, io, do, v)
    return sentence

def sample_all_long():
    s = random.choice(subj_iobj)
    io = random.choice(subj_iobj)
    while io == s:
        io = random.choice(subj_iobj)
    v = random.choice(verb)
    do = random.choice(dobj)
    io_mod = random.choice(io_mods)
    do_mod = random.choice(do_mods)
    while io_mod == do_mod:
        do_mod = random.choice(do_mods)
    sentence = '%s wa %s %s ni %s %s wo %s . <eos>\n' % (s, io_mod, io, do_mod, do, v)
    return sentence

subj_iobj = read_terminals('generate-sentences/terminal/subj_iobj.txt')
dobj = read_terminals('generate-sentences/terminal/dobj.txt')
verb = read_terminals('generate-sentences/terminal/verb.txt')

control_post_position = False
io_mods = general_mod() + io_specific_mod()
do_mods = general_mod() + do_specific_mod()

random.seed(7)

all_short = open('generate-sentences/generated_set2/all_short.txt', 'w')
sentences = []
for s in subj_iobj:
    for io in subj_iobj:
        if s != io:
            for v in verb:
                for do in dobj:
                    sentences.append('%s wa %s ni %s wo %s . <eos>\n' % (s, io, do, v))

random.shuffle(sentences)
for sent in sentences:
    all_short.write(sent)
all_short.close()

long_do = open('generate-sentences/generated_set2/long_do.txt','w')
sentences = []
for i, s in enumerate(subj_iobj):
    print(i)
    for io in subj_iobj:
        if s != io:
            for v in verb:
                for do in dobj:
                    for mod in do_mods:
                        sentences.append('%s wa %s %s wo %s ni %s . <eos>\n' % (s, mod, do, io, v))
random.shuffle(sentences)
for sent in sentences:
    long_do.write(sent)
long_do.close()

# long_io = open('long_io.txt','w')
long_io = open('generate-sentences/generated_set2/long_io.txt','w')
sentences = []
for i, s in enumerate(subj_iobj):
    for io in subj_iobj:
        if s != io:
            for v in verb:
                for do in dobj:
                    for mod in io_mods:
                        sentences.append('%s wa %s %s ni %s wo %s . <eos>\n' % (s, mod, io, do, v))
random.shuffle(sentences)
for sent in sentences:
    long_io.write(sent)
long_io.close()

long_io_extra = open('generate-sentences/generated_set2/long_io_extra.txt','w')
sentences = []
for i in range(1000000):
    sentence = sample_long_io_extra()
    # while sentence in sentences:
    #     sentence = sample_long_io_extra()
    sentences.append(sentence)
    if i % 10000 == 0:
        print(i)
    long_io_extra.write(sentence)
long_io_extra.close()

all_long = open('generate-sentences/generated_set2/all_long.txt', 'w')
sentences = []
for i in range(1000000):
    sentence = sample_all_long()
    # while sentence in sentences:
    #     sentence = sample_all_long()
    sentences.append(sentence)
    if i % 10000 == 0:
        print(i)
    all_long.write(sentence)
all_long.close()