# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsRegressor

class Model:
  def __init__(self):
    processed_data = self.get_data()
    self.knn_model = self.knn(processed_data)

  def get_data(self):
    excel = pd.ExcelFile('app/data/HainanClean_New.xlsx')
    hainan = excel.parse("fulldf")
    hainan.columns = hainan.columns.str.replace('  ', '_')
    hainan.columns = hainan.columns.str.replace(' ', '_')
    hainan.columns = hainan.columns.str.replace('(', '')
    hainan.columns = hainan.columns.str.replace('（', '')
    hainan.columns = hainan.columns.str.replace(')', '')

    d = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6,
         'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
    hainan.Month = hainan.Month.map(d)
    hainan.BioCNG_Produced_Nm3 = hainan.BioCNG_Produced_m3.shift(-15)
    hainan.drop(hainan.tail(15).index,inplace=True)
    hainan = hainan[np.isfinite(hainan['Month'])]
    hainan['BioCNG_cumsum'] = hainan.BioCNG_Produced_m3.cumsum()
    hainan = hainan[np.isfinite(hainan['Lemon_waste_t'])]
    hainan = hainan[np.isfinite(hainan['Percolate_t'])]
    hainan = hainan.replace(' ',0)
    hainan = hainan.replace('',0)
    hainan = hainan.replace('  ',0)
    hainan = hainan.drop(['Year', 'Month', 'Day', 'Month_#', 'Day_#', 'Raw_Biogas_Produced_m3',
            'BioCNG_Sold_m3', 'Vehicle_use_m3', 'Liquid_Fertilizer_Produced_t', 'Solid_fertilizer_produced_t',
           'Wastewater_flow_to_WWTP_unit?', 'Solid_residues_kg','50%_NaOH/kg', 'FeCl2/kg', 'PAM/kg',
           'Defoamer/kg', 'Project_electricity_use/kWh',
           'Office_space_electricity_use/kWh', 'Water/m3', 'Diesel/L'], axis=1)
    sumcum = hainan['BioCNG_cumsum']
    hainan.drop(labels=['BioCNG_cumsum'], axis=1,inplace = True)
    hainan.insert(0, 'BioCNG_cumsum', sumcum)
    return hainan

  def knn(self, data):
    knn = KNeighborsRegressor(n_neighbors=4)
    min_max_scaler = preprocessing.MinMaxScaler()
    np_scaled = min_max_scaler.fit_transform(data[['BioCNG_cumsum', 'Pig_Manure_t',
           'Cassava_t', 'Fish_waste_water_t', 'Kitchen_food_waste_t',
           'Municipal_fecal_residue_t', 'Tea_waste_t', 'Chicken_litter_t',
           'Bagasse_feed_t', 'Alcohol_waste_t', 'Chinese_medicine_waste_t',
           'Energy_grass_t', 'Banana_fruit_shafts_t', 'Lemon_waste_t',
           'Percolate_t', 'Other_waste_t']])
    data_normalized = pd.DataFrame(np_scaled)

    Xnor_train = data_normalized.iloc[:, 1:16]
    ynor_train = data_normalized[0]

    knn.fit(Xnor_train, ynor_train)
    return knn

  def predict(self, model, x):
    return model.predict(x)
