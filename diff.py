#!/usr/bin/env python3

import pytz
import pandas
import datetime
df1 = pandas.read_csv('data-2021-02-28.csv', parse_dates=['VACCINATION_DATE'])
df2 = pandas.read_csv('data-2021-03-04.csv', parse_dates=['VACCINATION_DATE'])

# limit to dates prior to December 11, 2020

df1 = df1[df1['VACCINATION_DATE'] < datetime.datetime(2020, 12, 11, tzinfo=pytz.UTC)]
df2 = df2[df2['VACCINATION_DATE'] < datetime.datetime(2020, 12, 11, tzinfo=pytz.UTC)]

# just include the daily counts
df1 = df1[['VACCINATION_DATE']] #, 'DailyFirstDose', 'DailySecondDose']]
df2 = df2[['VACCINATION_DATE']] #, 'DailyFirstDose', 'DailySecondDose']]

merged = df1.merge(df2, indicator=True, how='outer')
merged = merged.sort_values('VACCINATION_DATE')

for i, row in merged.iterrows():
    if row['_merge'] == 'right_only':
        print('new row', row['VACCINATION_DATE'])
    elif row['_merge'] == 'left_only':
        print('deleted row', row['VACCINATION_DATE'])



