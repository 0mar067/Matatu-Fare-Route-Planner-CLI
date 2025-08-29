#!/usr/bin/env python3
"""
Test script to verify the Matatu CLI application functionality
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

from matatu_cli.db import get_session, close_session
from matatu_cli.models import Route, Fare

def test_route_operations():
    """Test route operations"""
    session = get_session()
    try:
        print("Testing Route Operations...")
        
        # Test creating a route
        route = Route.create(session, "Kikuyu", "Nairobi", "KBS")
        print(f" Route created: ID={route.id}")
        
        # Test getting all routes
        routes = Route.get_all(session)
        print(f" Found {len(routes)} routes")
        
        # Test finding route by ID
        found_route = Route.find_by_id(session, route.id)
        print(f" Route found by ID: {found_route}")
        
        # Test creating a fare for the route
        fare = Fare.create(session, "Kikuyu Stage", 50, route.id)
        print(f" Fare created: ID={fare.id}")
        
        # Test getting all fares
        fares = Fare.get_all(session)
        print(f" Found {len(fares)} fares")
        
        # Test searching fares by stage
        search_fares = Fare.search_by_stage(session, "Kikuyu")
        print(f" Found {len(search_fares)} fares with 'Kikuyu' in stage name")
        
        # Test deleting fare
        Fare.delete(session, fare.id)
        print(" Fare deleted successfully")
        
        # Test deleting route
        Route.delete(session, route.id)
        print(" Route deleted successfully")
        
        print(" All tests passed!")
        
    except Exception as e:
        print(f" Test failed: {e}")
    finally:
        close_session(session)

if __name__ == "__main__":
    test_route_operations()
