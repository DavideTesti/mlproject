from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.utils import save_object

def main():
    # Data ingestion
    ingestion = DataIngestion()
    train_data, test_data = ingestion.initiate_data_ingestion()

    # Data transformation
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    # Model training
    model_trainer = ModelTrainer()
    model = model_trainer.initiate_model_trainer(train_arr, test_arr)

    # Save the model and preprocessor
    save_object('artifacts/model.pkl', model)

if __name__ == "__main__":
    main()

