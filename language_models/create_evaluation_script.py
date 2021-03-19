import sys
import glob

folder = sys.argv[1]
fout = open(sys.argv[2],'w')
model = sys.argv[3]
data = sys.argv[4]

for fname in glob.glob('%s/*.txt'%folder):
    out_fname = fname[:-3] + 'out'
    fout.write('python evaluate_target_word_test.py --checkpoint %s --surprisalmode True --data %s --prefixfile %s --outf %s\n' % (model, data, fname, out_fname))
print('chmod +x %s' % sys.argv[2])
fout.close()
