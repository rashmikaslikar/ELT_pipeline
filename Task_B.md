### Task B - Backend

At a high level, we're going to:
- Extract and Load data from source (HTTP API) to destination (Postgres)
- Transform data for downstream applications.
- Write an endpoint to access the data from a frontend application.
  
This process is more commonly known as ELT, but there are variants such as ETL and reverse ETL, etc. They are all essentially the same underlying workflows but have slight differences in the order of data flow and where data is processed and stored.

#### Overview of solution  

![image info](images/task_b_pipeline.png)  

