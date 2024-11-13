# SalesLT_Azure_ETL_Project
## Project Purpose

This project establishes an automated data pipeline on Azure to process and analyze data from an on-premises SQL data source. Data is stored in Azure Data Lake, transformed, and then loaded into Azure SQL Server. The data is visualized in Tableau to support business and investment decision-making.

The pipeline provides insights such as:

- Sales performance
- Sales trend analysis
- Revenue distribution across customer segments
![image (2)](https://github.com/user-attachments/assets/c4fcc171-c6d6-4603-a8d3-0d26cdc49dcb)
---

## Architecture

The system comprises the following core components:

1. **Data Source (On-Premise SQL Server)**: The initial source of raw data stored in an on-premises SQL Server.
2. **Azure Data Lake Storage Gen 2**:
    - **Raw Layer**: Stores raw, unprocessed data as-is from the source.
    - **Ingested Layer**: Contains data that has undergone basic validation and ingestion checks.
    - **Presentation Layer**: Holds cleansed and processed data, ready for analysis or loading into Azure SQL Server.
3. **Azure SQL Server**: Acts as the final storage point, making data readily accessible for Tableau visualization.
4. **Tableau**: Used for data visualization, creating reports and dashboards for end-users.
5. **Azure Data Factory**:
    - **Orchestration**: Manages and orchestrates ETL tasks, including copying data from on-premises SQL to Azure Data Lake and performing transformations.
    - **Data Ingestion**: Copies data from on-premises SQL Server to Azure Data Lake on a scheduled basis.
6. **Azure Databricks**: Processes and transforms data, performing complex transformations and calculations before loading into the Presentation Layer.
![Biểu đồ không có tiêu đề drawio (3)](https://github.com/user-attachments/assets/c45b97c5-93d5-493c-8ef5-b783f997e65d)

---

## Technology Stack

- **Azure Data Factory (ADF)**: Manages data orchestration and scheduling. ADF is responsible for connecting to the on-premises SQL Server, copying data to Azure, and triggering Databricks for transformations.
- **Azure Data Lake Storage Gen 2**: A scalable storage solution for managing raw, ingested, and presentation layers of data, providing a foundation for structured data processing.
- **Azure Databricks**: Handles data transformations and calculations within the data pipeline, ensuring data is properly formatted and structured in the Presentation Layer.
- **Azure SQL Server**: Serves as the final data warehouse, enabling efficient data retrieval for business intelligence and visualization.
- **Tableau**: Connects to Azure SQL Server to provide data visualization, creating reports and dashboards that deliver insights to end-users.

---

## Lessons Learned

1. **Azure Data Factory**:
    - Data Factory is powerful for orchestration and integration but should be optimized to reduce costs by limiting the number of activities, as each is billed based on runtime.
    - Fine-tune **Data Integration Units (DIUs)** to control costs, especially for small datasets where lower DIUs can still achieve good performance.
2. **Azure Databricks**:
    - Organize data processing into logical steps within Databricks, making transformations easier to manage.
    - Utilize Databricks for complex transformations to minimize the load on SQL Server.
3. **Tableau**:
    - Preparing and structuring data in the Presentation Layer significantly reduces query times and optimizes performance when visualizing data in Tableau.

---

## Description

1. **Copy Data from On-Premises SQL Server to Azure Data Lake**: Use Azure Data Factory to create a pipeline that copies data from the on-premises SQL Server to the Raw Layer in Azure Data Lake.
2. **Transform Data with Azure Databricks**: Set up notebooks in Azure Databricks to clean and transform data from the Ingested Layer and load it into the Presentation Layer.
3. **Load Data into Azure SQL Server**: Use Azure Data Factory to load transformed data from the Presentation Layer into Azure SQL Server.
4. **Visualize in Tableau**: Connect Tableau to Azure SQL Server to create interactive dashboards, charts, and data analysis reports.
---
- Data Source: https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms
