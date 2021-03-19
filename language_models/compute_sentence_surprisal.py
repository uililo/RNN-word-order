import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}


matplotlib.rc('font', **font)

sent_m_s = []
sent_s_s = []
avg_m_s = []
avg_s_s = []

def tokens_to_sentences(input_df, remove_unk=False):
    df = input_df.copy()
    sent_count = 0
    for i in df.index:
        df.loc[i, 'sentence_num'] = sent_count
        if df.loc[i, 'word'] == '<eos>':
            sent_count += 1
    df_sent = df.groupby(['sentence_num'], as_index=False)[['word','surprisal']].agg(lambda x: list(x))
    df_sent.sentence_num = df_sent.index.values
    df_sent['avg_surprisal'] = df_sent.apply(lambda row: np.mean(row.surprisal[1:-1]), axis=1)
    df_sent['sentence_surprisal'] = df_sent.apply(lambda row: sum(row.surprisal), axis=1)

    if remove_unk:
        for i, row in df_sent.iterrows():
            if '<unk>' in row.word:
                df_sent = df_sent.drop([i])
    # print(np.mean(df_sent.avg_surprisal.values))
    return df_sent

for s_type in ['all_short','long_IO','long_DO','all_long']:
    dfa = pd.read_table('language_models/dative/%s_DO.out'%s_type, header=None, names=['word','surprisal'])
    dfa_sent = tokens_to_sentences(dfa,True)
    dfb = pd.read_table('language_models/dative/%s_PO.out'%s_type, header=None, names=['word','surprisal'])
    dfb_sent = tokens_to_sentences(dfb,True)
    print(s_type)
    # print('sentence level')
    diff = dfa_sent.sentence_surprisal.values - dfb_sent.sentence_surprisal.values
    m = np.mean(diff)
    s = np.std(diff)
    sent_m_s.append(m)
    sent_s_s.append(s/np.sqrt(len(dfa_sent)))
    # print('mean %s, std %s' % (m,s))
    diff = dfa_sent.avg_surprisal.values - dfb_sent.avg_surprisal.values
    m = np.mean(diff)
    s = np.std(diff)
    avg_m_s.append(m)
    avg_s_s.append(s/np.sqrt(len(dfa_sent)))
    print('average:')
    print(np.mean(dfa_sent.avg_surprisal.values), np.mean(dfb_sent.avg_surprisal.values), )
    print('mean %s, std %s' % (m, s))

matplotlib.rc('font', **font)
plt.figure()
fig, ax = plt.subplots()
sent_type = ['all short','long IO','long DO','all long']
x_pos = np.arange(len(sent_type))
ax.bar(x_pos, avg_m_s, yerr=avg_s_s, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('preference for PO')
ax.set_ylim([0,2])
ax.set_xticks(x_pos)
ax.set_xticklabels(sent_type)
ax.set_title('')
ax.yaxis.grid(True)
plt.show()