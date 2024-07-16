# Technical_assessment
This repository contains the jupyter notebook that was used to create ETL pipeline.
Make sure to change your folder location and database connection credentials before running.
This pipeline follows the following process:
- The data is stored in a raw folder that mimics a sftp source.
- Using the file’s naming convention, our extraction processes sorts the file creation timestamp and picks up only the latest one.
- This ensures that each time the pipeline is executed, only the latest file is processed and thus prevents re-processing. If the same pipeline is run multiple times, our ETL processes ensures no duplication occur 
  in the data warehouse.
- The data is subjected to data quality checks such as stripping whitespaces, ensuring same data formats throughout the column etc.
- This file is then ingested to a fact table in the database with partitioning over year and month of the dataset. If multiple files for the same month are received, the pipeline overwrites the old dataset with the 
  new one.
- This is followed by the creation/update on the dimension tables. Our ETL ensures that the dimension tables are de-duped and consistent thus creating golden records.
- Next, the data marts are created, keeping in view the business KPIs presented.

