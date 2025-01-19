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

<b>What is a data model?</b>
* Conceptual, with different definitions depending on context
* Represents the logical meaning behind a set of data
* How the data and its components relate
* Helps users collaborate and understand the data in a common way
* For example, in a list of species of animals, we can include the number of legs, and if the
animal is venomous. This provides for the collaboration between users/programs as we have defined a set of
attributes for communicating about the animal
* There are always tradeoffs when defining a model, including complexity, amount of space required, etc.


<b>What is a model in dbt?</b>
* Represents something more specific than a basic data model -- it represents the various transformations
performed on the raw source datasets
* Typically written in SQL, newer versions can use Python for models/transformations
* Each model, or transformation, is usually a `SELECT` query, transforming the source dataset as required
* Each model represented by a text file with a .sql extension. dbt will automatically use these files when tasked with
various operations, such as `dbt run`


<b>Workflow to create simple dbt model</b>
1. Create directory in models directory (e.g., "order")
2. Create a .sql file in that directory (e.g., "customer_orders.sql")
3. Run `dbt run` to materialize the model


<b>Reading from Parquet</b>
* Parquet is a columnar, binary file format used by many tools to efficiently store data
* It is becoming widespread for the purposes of sharing and distributing datasets
* Columnar is in contrast to row-based, like typical relational database formats
* Some common tools that use it for efficient data storage:
  * Apache Spark
  * Apache Arrow
  * DuckDB
    * DuckDB can read Parquet files directly from read_parquet:
    * `SELECT * FROM`
      `read_parquet('filename.parquet')`


<b>Updating dbt models</b>
* Update just like any other code, work is iterative
* Fixing bugs with queries / models
* Migrating to different sources / destinations


<b>Workflow to update model</b>
1. Check out from source control
`git clone dbt_project`
2. Find the model you want to update
3. Update query contents
4. Regenerate with `dbt run`, or run `dbt run -f` (force full refresh)
5. Check changes back to source control


<b>YAML files</b>
* Some updates may require changes to YAML / .yml files
* Typically, the changes would be in `dbt_project.yml` or `model_properties.yml`
* These files contain configuration for full project -- project name / version, directory locations,
model materialization settings (global). There is one `dbt_project.yml` file per project
* `model_properties.yml` contains settings that reference models -- description, documentation details,
much more. The name can actually be anything with `.yml` in models/ subdirectory.
* Project-level files:
  * `profiles.yml`
  * `dbt_project.yml`
* Model-only files:
  * `test_model.sql`
  * `model_properties.yml`
  * `models/test_model.yml`

<b>Hierarchical models</b>
* Represents dependencies between models
* Also known as a directed acyclic graph (DAG), or lineage graph, which is a common concept in data engineering
workflows/tools like Spark and Airflow
* dbt DAG allows models to be built / updated according to dependencies
* Without a lineage graph, tables are built in alphabetical order


<b>Defining hierarchies in dbt</b>
* Built using the Jinja template language in the model file(s)
* Most often using the `ref` function
* Replace table name with `{{ ref('model_name') }}` in SQL:
  * `SELECT
  first_name, last_name
  FROM taxi_rides_raw`
  * becomes:
  * `SELECT
  first_name, last_name
  FROM {{ ref('taxi_rides_raw') }}`
* Re-materialize table with `dbt run`
* `ref` templates are substituted with actual table names
* Simply put the desired content in between the braces, and when dbt is run, it will replace the contents of the
  braces with the correct result.
* dbt has many Jinja functions available for use. `{{ ... }}` represents a template substitution.
    * `ref`, `config`, `docs` are just some of the available Jinja functions


<b>Common model issues</b>
* Common issues:
  * Syntax erros in SQL
  * Logic errors in SQL
  * Invalid references (typo in table name, etc.)
* Query errors:
  * Syntax / misspelling, incorrect ordering
  * Wrong SQL type, etc.
  * Not grouping by all non-aggregated columns, incorrect CTEs
* Invalid references:
  * Table / view named differently than expected
  * Referencing objects that have not yet been created


<b>Troubleshooting methods</b>
* `dbt run` -> view output
* View the logs in `logs/dbt.log` or `run_results.json` can show errors found during the run
* View the generated SQL queries or run manually to verify it's working as expected
* Verify that fixes worked and didn't cause some other issue

