from crud import PlayerDataCrud
import pandas as pd

class DataHandler:
    def __init__(self, segment, game):
        self.segment = segment
        self.game = game
        
    def get_filepath(self):
        # This function is used to get the file path based on segment and game
        return ('initial_admin\\datasets\cleaned\\'+self.segment+'\\'+self.game+'\\player_stats.csv','datasets\cleaned\\'+self.segment+'\\'+self.game+'\\player_stats.csv')

    def get_dataset(self, filepath):
        # This function is used to get the dataset from a file
        return pd.read_csv(filepath)

    def data_to_dict(self, data):
        # This function converts the DataFrame to a dictionary
        return data.to_dict(orient='list')

    def save_to_db(self, data_dict):
        # This function saves the cleaned data to the database
        PDC = PlayerDataCrud(self.segment, self.game)
        PDC.create_data(data_dict)

if __name__ == "__main__":
    print("Load Test OK")