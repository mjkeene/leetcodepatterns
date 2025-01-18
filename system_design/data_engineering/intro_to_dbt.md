<h2>Intro to DBT</h2>

https://campus.datacamp.com/courses/introduction-to-dbt

<h3>1. Welcome to DBT</h3>

<b>What is dbt?</b>
* "data build tool"
* Primarily handles the T in ELT (sometimes ETL)
* Allows easy switching between data warehouses
* Ideal for teams with different needs
* Provides source / code control

<b>What does dbt do?</b>
* Primarily defines data models and transformations using SQL
* Newer versions can use Python
* Translates between SQL dialects
* Can define relationships between data models
* Runs the data transformation process(es) as requested
* Can test for data quality requirements

<b>What does dbt look like?</b>
* Command line tool `dbt`
* Also called `dbt-core`, open source
* Adapters provide connections to different warehouses
  * dbt-snowflake
  * dbt-bigquery
  * dbt-sqlserver
* dbt Cloud

<b>dbt subcommands</b>
* `dbt <subcommand> -h` : help for subcommand
* `dbt init` : creates new dbt projects
* `dbt run` : runs the data generation / transformations
* `dbt test` : used to test data quality
* `dbt debug` : can check connections to data warehouses
* many others

<b>dbt project structure</b>
* A dbt project encompasses components for working with data in dbt
  * Project configuration
  * Data sources and destinations
  * SQL queries
  * Templates
  * Documentation
  * Implemented as a folder structure, can easily be copied, modified, or placed in source control as needed

<b>Project Profiles</b>
* A profile represents a given deployment scenario
  * Development
  * Staging / Test
  * Production
* A dbt project can have multiple profiles
* Defined in the `properties.yml` file

<b>Workflow for dbt</b>
1. Create project (`dbt init`)
2. Define configuration (`profiles.yml`)
3. Create / use models / templates
4. Instantiate models (`dbt run`)
5. Verify / Test / Troubleshoot
6. Repeat as needed

`dbt run`
* Run whenever the model changes, or when data process needs to be materialized
* Output provides many details on the success or failure of various steps

`dbt init`
* Creates new dbt project
* Asks for project name, and database / data warehouse type
* New projects has a directory with 6 folders:
  * analyses
  * macros
  * models
  * seeds
  * snapshots
  * tests

<b>Table vs. View</b>
* Table
  * Object within database / data warehouse
  * Takes up space within db / dw
  * Content only updated when changed
* View
  * Queryable like a table, but holds no info
  * Usually defined as a select query against another table or tables
  * Content generated with each query
* dbt can create tables or views


<h3>2. dbt models</h3>

<b>What is a dbt model?</b>
* 





