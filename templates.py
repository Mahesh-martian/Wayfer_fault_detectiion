import os
from pathlib import Path

list_of_files = ['flask_monitoringdashboard.db',
                 'main.py',
                 'manifest.yml',
                 'predictFromModel.py',
                 'prediction_Validation_Insertion.py',
                 'Procfile.pr',
                 'requirements.txt',
                 'runtime.txt',
                 'schema_prediction.json',
                 'schema_training.json',
                 'test.py',
                 'trainingModel.py',
                 'training_Validation_Insertion.py',
                 'application_logging/logger.py',
                 'best_model_finder/tuner.py',
                 'DataTransformation_Prediction/'
                 'DataTransformation_Prediction/DataTransformationPrediction.py',
                 'DataTransform_Training/DataTransformation.py',
                 'DataTypeValidation_Insertion_Prediction/DataTypeValidationPrediction.py',
                 'DataTypeValidation_Insertion_Training/DataTypeValidation.py',
                 'data_ingestion/__init__.py'
                 'data_ingestion/data_loader.py',
                 'data_ingestion/data_loader_prediction.py',
                 'data_preprocessing/clustering.py',
                 'data_preprocessing/preprocessing.py',
                 'file_operations/__init__.py',
                 'file_operations/file_methods.py',
                 'models/',
                 'PredictionArchivedBadData/__init__.py',
                 'Prediction_Batch_files/__init__.py',
                 'Prediction_Database/__init__.py',
                 'Prediction_FileFromDB/__init__.py',
                 'Prediction_Logs/__init__.py'
                 'Prediction_Logs/columnValidationLog.txt',
                 'Prediction_Logs/DataBaseConnectionLog.txt',
                 'Prediction_Logs/dataTransformLog.txt',
                 'Prediction_Logs/DbInsertLog.txt',
                 'Prediction_Logs/DbTableCreateLog.txt',
                 'Prediction_Logs/ExportToCsv.txt',
                 'Prediction_Logs/GeneralLog.txt',
                 'Prediction_Logs/missingValuesInColumn.txt',
                 'Prediction_Logs/nameValidationLog.txt',
                 'Prediction_Logs/Prediction_Log.txt',
                 'Prediction_Output_File/__init__.py',
                 'Prediction_Raw_Data_Validation/predictionDataValidation.py',
                 'preprocessing_data/',
                 'templates/index.html',
                 'TrainingArchiveBadData/',
                 'Training_Batch_Files/',
                 'Training_Database/',
                 'Training_FileFromDB/',
                 'Training_Logs/columnValidationLog.txt',
                 'Training_Logs/DataBaseConnectionLog.txt',
                 'Training_Logs/dataTransformLog.txt',
                 'Training_Logs/DbInsertLog.txt',
                 'Training_Logs/DbTableCreateLog.txt',
                 'Training_Logs/ExportToCsv.txt',
                 'Training_Logs/GeneralLog.txt',
                 'Training_Logs/missingValuesInColumn.txt',
                 'Training_Logs/ModelTrainingLog.txt',
                 'Training_Logs/nameValidationLog.txt',
                 'Training_Logs/Training_Main_Log.txt',
                 'Training_Logs/valuesfromSchemaValidationLog.txt',
                 'Training_Raw_data_validation/rawValidation.py',
                 'Training_Raw_files_validated/']

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    emp_folder= ''

    """ how exist_ok works:if "directory" already exists,
    os.makedirs() will not raise an error, and it will do nothing.
    If "my_directory" doesn't exist, it will create the directory.
    """
    print(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if '.' not in filename:
        emp_folder = filename
        os.makedirs(filename, exist_ok=True)
        print(emp_folder)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):

        if emp_folder != str(filepath):
            with open(filepath, "w") as f:
                pass
    else:
        print("file already exists")

