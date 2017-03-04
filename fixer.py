import pandas as pd
import numpy as np

fix_data = {}
with open('./fix_data.csv') as f:
    for line in f.readlines():
        fix_data[line.split(',')[0]] = line

merge_out_data = []
for i in range(1, 2001):
    file_path = '/mnt/huge/tianchi/stream_predicts/%d.csv' % i
    merge_out_data.append(
        str(i) + ',' + (','.join(str(v) for v in np.round(np.exp(pd.read_csv(file_path).tail(14)['yhat'])))) + '\n'
    )

with open('merge_out.txt', mode='w') as f:
    for row in merge_out_data:
        k = row.split(',')[0]
        if k in fix_data:
            f.write(fix_data[k])
        else:
            f.write(row)
