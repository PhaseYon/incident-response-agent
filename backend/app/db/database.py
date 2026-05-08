"""
In-memory database module.

Provides a simple in-memory store for incident reports during development.
Replace with a real database (PostgreSQL, SQLite, etc.) when moving to production.
"""

from typing import Any

# In-memory store: maps incident_id -> incident dict
incidents_store: dict[str, Any] = {}
