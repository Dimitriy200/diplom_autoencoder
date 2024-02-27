import pandas as pd
import os

from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


class PrepData():

    defaultPipline = None


    '''
    B inpFilesList и outFilesList указывать полный путь
    '''
    def __init__(self, defaultPipline):
        self.defaultPipline = PrepData.createDefaultPipline()
    
    
    def createDefaultPipline(self):
        simple_inputer = KNNImputer(n_neighbors = 2)
        std_scaler = StandardScaler()
        pipe_num = Pipeline([('imputer', simple_inputer),('scaler', std_scaler)])

        return pipe_num
    
    def processing_data(self,
                        inpFilesList = [], 
                        outFilesList = [], 
                        pipline = 
                        defaultPipline):
        
