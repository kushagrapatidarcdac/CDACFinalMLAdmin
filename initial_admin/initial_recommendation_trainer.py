import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from crud import PlayerDataCrud

class Recommender:
    def __init__(self, segment, game, player_name, k=5):
        self.segment=segment
        self.game=game
        self.player_name=player_name
        self.k=k
        self.player_data=None
        self.get_player_data()
        self.recommendations=None
        self.get_recommendation()
        
    def get_player_data(self):
        PDC=PlayerDataCrud(self.segment, self.game)
        data=PDC.read_data()['data']
        self.player_data=pd.DataFrame.from_dict(data, orient='columns')
    
    def encode_country(self):
        # Select required columns and encode 'country'
        encoded = pd.get_dummies(self.player_data['country'])
        features = pd.concat([encoded, self.player_data[['total_rounds', 'kd', 'rating']]], axis=1)
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(features)
        
        return scaled_features
    
    def get_query(self):
        scaled_features=self.encode_country()
        
        # Find the query player
        mask = self.player_data['player_name'] == self.player_name
        player_vector = scaled_features[mask.values][0]
        feature_matrix = scaled_features[~mask.values]
        
        return mask, player_vector, feature_matrix
        
        
    def get_fit_model(self):
        mask, player_vector, feature_matrix = self.get_query()
        
        # Fit KNN and get recommendations
        knn = NearestNeighbors(n_neighbors=self.k, metric='euclidean')
        knn.fit(feature_matrix)
        distances, indices = knn.kneighbors([player_vector])
        
        return mask, indices
        
        
    def get_recommendation(self):
        mask, indices = self.get_fit_model()
        
        recommended_indices = self.player_data[~mask].iloc[indices[0]].index
        recommendations = self.player_data.iloc[recommended_indices][['player_name']]
        
        self.recommendations=recommendations.to_dict(orient='list')