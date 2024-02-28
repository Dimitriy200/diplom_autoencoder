import pandas as pd
import os

from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


class PrepData():

    def __init__(self):
        self.__defaultPipline = PrepData.createDefaultPipline()

  
    def createDefaultPipline(self):
        simple_inputer = KNNImputer(n_neighbors = 2)
        std_scaler = StandardScaler()
        pipe_num = Pipeline([('imputer', simple_inputer),('scaler', std_scaler)])

        return pipe_num


    @property
    def defaultPipline(self):
        return self.__defaultPipline


    # B inpFilesList и outFilesList указывать полный путь
    def processing_data(self,
                        inpFilesList: list, 
                        outFilesList: list, 
                        pipline: Pipeline = defaultPipline):
        
        status = {  "Access"    :   "Access", 
                    "Warning"   :   "Warning",
                    "Error"     :   "Error"      }


        for url in range(len(inpFilesList)):
            dataFrame = pd.read_csv(url)
            newDataFrame = pipline.fit_transform(dataFrame)
            newDataFrame = pd.DataFrame(newDataFrame, columns=pipline['scaler'].get_feature_names_out(dataFrame.columns))
            newDataFrame.to_csv(outFilesList[url])
        
        return status["Access"]

    
