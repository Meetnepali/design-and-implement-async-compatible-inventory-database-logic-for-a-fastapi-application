# Task Overview

You are working with a small business’s inventory management system built using FastAPI. The system needs to track products in the store database, supporting operations to add new products and retrieve the current inventory. The FastAPI routes for these operations are already written and thoroughly tested, but the actual PostgreSQL schema and the async database integration logic are missing. Your task is to design the inventory schema and write async-compatible database access logic so that the API endpoints are fully functional and ready for live usage.

# Project Structure & Guidance
- The FastAPI application, including all routes and Pydantic models, is already fully implemented. No changes to API code are needed.
- You will find the main data logic files in the `app/` directory:
  - `models.py` – for ORM table definitions
  - `schemas.py` – for API (de)serialization
  - `database.py` – for database connection and session management
  - `crud.py` – for implementing async-capable CRUD logic (to be written/completed by you)
- The `run.sh` script handles setup of all infrastructure, runs migrations, and loads sample data automatically.

# Database Access
- Host: `localhost`
- Port: `5432`
- Database: `inventory_db`
- Username: `inventory_user`
- Password: `inventory_pass`

You can connect using pgAdmin, DBeaver, psql, or similar tools. The schema and sample data are loaded as part of setup.

# Objectives
- Design a normalized PostgreSQL schema for the products inventory table, using logical data types and constraints.
- Implement SQLAlchemy async ORM models and async database logic (CRUD functions) using SQLAlchemy and asyncpg.
- Ensure all async DB operations are properly integrated and do not block the FastAPI event loop.
- The routes `/products` (GET) and `/products` (POST) must store and retrieve product records from the real database.

# How to Verify
- Start the application and use the `/products` POST endpoint to add a new product (all fields required).
- Use `/products` GET to verify that all products, including new entries, are returned with correct details (including auto-generated fields such as IDs and timestamps).
- Use a database client to verify that the product is properly persisted in PostgreSQL and constraints are respected.
- Attempt to add a product with a duplicate name to ensure that relevant unique constraints are enforced.