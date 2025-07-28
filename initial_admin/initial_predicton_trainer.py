import pickle
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from crud import ModelCrud


class InitialPredictionTrainer:
    
    
    def __init__(self, segment, game):
        self.segment = segment
        self.game = game
        self.features=None
        self.target=None
        self.pipeline=None
        self.model_type="prediction" 
        self.model_bytes=None
    
    def extract_features(self, clean_data):
        self.features = clean_data[['total_rounds', 'kd']]
        self.target = clean_data['rating']

    def initpipeline(self):
        self.pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('regressor', SGDRegressor(max_iter=1000, tol=1e-3, random_state=42))
        ])
        
    def train_model(self):
        self.pipeline.fit(self.features, self.target)
    
    def byte_model(self):
        self.model_bytes = pickle.dumps(self.pipeline)

    
    def save_model(self):
        MC=ModelCrud(self.segment, self.game)
        MC.create_mlmodel(
            model_type=self.model_type,
            model_bytes=self.model_bytes
        )

