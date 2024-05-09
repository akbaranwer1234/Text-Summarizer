import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    
    def validate_all_files_exist(self)-> bool:
        try:
            validation_status = None

            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))
            
            with open(self.config.STATUS_FILE, 'a') as f:

                for file in all_files:
                    # print(file)
                    
                    if file not in self.config.ALL_REQUIRED_FILES:
                        validation_status = False
                    else:
                        validation_status = True
                    f.write(f"File {file}: Validation status: {validation_status}\n")
                
                f.write(f"*****************************************************\n")

            return validation_status
        
        except Exception as e:
            raise e