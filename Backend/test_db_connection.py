#!/usr/bin/env python3
"""
Test database connection to Render
"""

import os
import sys
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Load environment variables
load_dotenv()

def test_connection():
    database_url = os.getenv('SQLALCHEMY_DATABASE_URL')
    
    if not database_url:
        print("❌ Error: SQLALCHEMY_DATABASE_URL not found in .env file")
        return False
    
    print(f"Testing connection to: {database_url.split('@')[1] if '@' in database_url else 'database'}")
    
    try:
        engine = create_engine(database_url)
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version()"))
            version = result.fetchone()[0]
            print(f"✅ Connected successfully!")
            print(f"PostgreSQL version: {version[:50]}...")
            return True
            
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing Render Database Connection...")
    print("=" * 50)
    success = test_connection()
    
    if success:
        print("\n🎉 Database connection successful!")
        print("You can now deploy to Render.")
    else:
        print("\n💡 Next steps:")
        print("1. Verify your Render PostgreSQL database is running")
        print("2. Check the External Database URL is correct in .env")
        print("3. Ensure database allows external connections")
