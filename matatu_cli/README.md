# Matatu Fare & Route Planner CLI

A simple command-line interface application for managing matatu routes and fares using Python, SQLAlchemy, and Click.

## Features

- Manage matatu routes (create, delete, list, find by ID)
- Manage fare stages (create, delete, list, find by ID, search by stage)
- SQLAlchemy ORM with Alembic migrations
- Input validation with friendly error messages
- Simple and beginner-friendly code

## Installation

1. Clone or download this project
2. Navigate to the project directory
3. Install dependencies:

```bash
pipenv install
pipenv shell
```

4. Set up the database:

```bash
alembic upgrade head
```

5. Run the application:

```bash
python -m matatu_cli.cli
```

## Usage

The application provides an interactive menu with the following options:

### Route Management
- Create a new route
- Delete a route
- List all routes
- Find route by ID

### Fare Management
- Create a new fare stage
- Delete a fare stage
- List all fare stages
- Find fare by ID
- Search fares by stage name

### Exit
- Exit the application

## Database Schema

- **Route**: id, start, destination, sacco, fares (relationship)
- **Fare**: id, stage, price, route_id (foreign key)

## Dependencies

- click: For CLI interface
- sqlalchemy: For ORM and database operations
- alembic: For database migrations
