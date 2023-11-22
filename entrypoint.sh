#!/bin/bash

# Run Alembic migrations
alembic upgrade head

# Run data migration script
python data_migration.py

# Run the main application
python app.py
