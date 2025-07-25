#!/usr/bin/env python3
"""
Database deployment script for Render
Run this script to set up the database on Render
"""

import os
import sys
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from alembic.config import Config
from alembic import command

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def deploy_database():
    """Deploy database to Render"""
    
    # Load environment variables
    load_dotenv()
    
    database_url = os.getenv('SQLALCHEMY_DATABASE_URL')
    
    if not database_url:
        print("Error: SQLALCHEMY_DATABASE_URL not found in environment variables")
        return False
    
    print(f"Connecting to database...")
    
    try:
        # Test database connection
        engine = create_engine(database_url)
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version()"))
            version = result.fetchone()[0]
            print(f"Connected successfully! PostgreSQL version: {version}")
        
        # Run Alembic migrations
        print("Running database migrations...")
        alembic_cfg = Config("alembic.ini")
        command.upgrade(alembic_cfg, "head")
        print("Migrations completed successfully!")
        
        return True
        
    except Exception as e:
        print(f"Error deploying database: {e}")
        return False

if __name__ == "__main__":
    success = deploy_database()
    if success:
        print("Database deployment completed successfully!")
    else:
        print("Database deployment failed!")
        sys.exit(1)
