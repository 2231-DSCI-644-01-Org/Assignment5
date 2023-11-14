# Assignment #2

Welcome to Assignment #2 In this assignment, you will dive deep into the world of data acquisition, data modeling, and database management. This assignment is designed to take you through the process of building a complete data collection pipeline. So, let's get started!

## Task 1: Scraper Module 🌐

**Objective:** Create a scraper to fetch data from GitHub repositories.

1. Use the boilerplate code provided in `github_scraper/scraper.py` as a starting point.
2. Implement a GitHub scraper to retrieve repository details, issues, and comments.
3. Ensure error handling for network issues or GitHub rate limits.
4. The scraper must work with changes in params , handle cursor-based pagination, and fetch all the data and return it in a dictionary.


## Task 2: Database Configuration and Modeling 📊

**Objective:** Configure the database, define models, and use Alembic for schema management.

1. Use the boilerplate code in `database/config/config.py` to handle database configuration.
2. Based on the data you are fetching, design a database schema. Remember to consider the relationships between repositories, issues, and comments.
1. Implement Alembic for database schema management.Be sure to import the `Base` class from `database/models/base.py` in your migration scripts.
1. Create a migration to generate the initial database schema.
1. Run migrations to set up the database for your project.

## Task 3: Parser Module 🧙‍♂️

**Objective:** Create parsers to process the data acquired from the scraper.

1. Use the boilerplate code in `parser/parser.py` as a foundation.
2. Implement parsers for repositories, issues, and comments, inheriting from the `Parser` class.
3. Handle pagination using GraphQL cursors to fetch additional data. Parser must make use of cursors github provides to fetch all the data.
1. Prepare the parsed data for insertion into the database.

## Task 5: Database Handler 🏦

**Objective:** Create a database handler to interact with the database.

1. Implement database interaction functions in `database/handler.py`.
2. Include functions for inserting, updating, and querying data.
3. Utilize bulk insert methods for optimized data insertion.
4. Validate data before inserting it into the database.


## Task 4: Controller Module 🎮

**Objective:** Build a controller to orchestrate the data pipeline.

1. Create a `Controller` class in `controller/main.py`.
2. Integrate the scraper, parser, and database handler into the controller.
3. Fetch data, parse it, and pass it to the database handler. 
1. Controller is for orchestrating the data pipeline. It should not contain any business logic.
1. Handle exceptions and ensure a smooth data flow.


## Task 6: CLI Module 🚀

**Objective:** Build a command-line interface for your data pipeline.

1. Create a CLI handler in `cli_handler.py`.
2. Implement a CLI command that accepts a list of repository names or a file with a list of repositories as input.
3. Use the controller to fetch data for the specified repositories.
4. Provide options for users to specify the data they want to retrieve.

## Task 7: Testing 🧪

**Objective:** Write unit tests for your code.

1. Write unit tests for the scraper, parser, database handler, and controller.
1. Mock the graphQL API calls and database interactions.
1. Ensure that the tests cover all the code paths and handle exceptions.
1. Use the `pytest` framework to run the tests.

## Task 8: Dockerize 🐳

**Objective:** Dockerize your application.

1. Create a `Dockerfile` to build your application.
1. Use `docker-compose` to run your application.
1. Ensure that the application runs without any issues in the container.
1. Use the `docker-compose.yml` file provided in the boilerplate code as a reference.
