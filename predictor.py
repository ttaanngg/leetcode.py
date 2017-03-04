from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import pandas as pd
import numpy as np
from fbprophet import Prophet

START_NUM = 1
NUM = 2000


def predict(shop_id):
    file_path = '/mnt/huge/dataset/shop_stream/%d.txt' % shop_id
    df = pd.read_csv(file_path, header=None)

    try:  # use logistic predict
        df['ds'] = df[0]
        y_max = np.max(df[1])
        df['y'] = np.log(df[1])
        df['cap'] = np.log(y_max)
        m = Prophet(growth='logistic')
        m.fit(df)
        future_df = m.make_future_dataframe(periods=14)
        future_df['cap'] = np.log(y_max * 1.5)
        forecast = m.predict(future_df)
        forecast['yhat'] = np.exp(forecast['yhat'])
    except:  # if failed use linear predict
        df['y'] = df[1]
        m = Prophet()
        m.fit(df)
        forecast = m.predict(m.make_future_dataframe(periods=14))
    forecast['yhat'] = np.round(forecast['yhat'])
    forecast.tail(14).to_csv('/mnt/huge/tianchi/stream_predicts/%d.csv' % shop_id, index=False)


with ProcessPoolExecutor(max_workers=24) as executor:
    for i in range(START_NUM, NUM + 1):
        executor.submit(predict, i)
        if i % 200 == 0:
            print("submitted %d%%" % (i / 2000 * 100))

with open('merge_out.txt', mode='w') as f:
    for i in range(1, NUM + 1):
        file_path = '/mnt/huge/tianchi/stream_predicts/%d.csv' % i
        f.write(str(i) + ',' + (','.join(str(int(v)) for v in pd.read_csv(file_path).tail(14)['yhat'])) + '\n')
