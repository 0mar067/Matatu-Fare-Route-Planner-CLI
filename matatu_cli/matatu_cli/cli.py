import click
from .db import get_session, close_session
from .models import Route, Fare

def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("MATATU FARE & ROUTE PLANNER CLI")
    print("="*50)
    print("1. Route Management")
    print("2. Fare Management")
    print("3. Exit")
    print("="*50)

def display_route_menu():
    """Display the route management menu"""
    print("\n" + "-"*30)
    print("ROUTE MANAGEMENT")
    print("-"*30)
    print("1. Create Route")
    print("2. Delete Route")
    print("3. List All Routes")
    print("4. Find Route by ID")
    print("5. Back to Main Menu")
    print("-"*30)

def display_fare_menu():
    """Display the fare management menu"""
    print("\n" + "-"*30)
    print("FARE MANAGEMENT")
    print("-"*30)
    print("1. Create Fare")
    print("2. Delete Fare")
    print("3. List All Fares")
    print("4. Find Fare by ID")
    print("5. Search Fares by Stage")
    print("6. Back to Main Menu")
    print("-"*30)

def handle_route_operations():
    """Handle route management operations"""
    session = get_session()
    try:
        while True:
            display_route_menu()
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '1':
                # Create Route
                try:
                    start = input("Enter start location: ").strip()
                    destination = input("Enter destination: ").strip()
                    sacco = input("Enter sacco name: ").strip()
                    
                    route = Route.create(session, start, destination, sacco)
                    print(f" Route created successfully! ID: {route.id}")
                    
                except ValueError as e:
                    print(f" Error: {e}")
                except Exception as e:
                    print(f" Unexpected error: {e}")
            
            elif choice == '2':
                # Delete Route
                try:
                    route_id = int(input("Enter route ID to delete: ").strip())
                    Route.delete(session, route_id)
                    print(" Route deleted successfully!")
                    
                except ValueError as e:
                    print(f" Error: {e}")
                except Exception as e:
                    print(f" Unexpected error: {e}")
            
            elif choice == '3':
                # List All Routes
                try:
                    routes = Route.get_all(session)
                    if not routes:
                        print("No routes found.")
                    else:
                        print("\nAll Routes:")
                        print("-" * 60)
                        for route in routes:
                            print(f"ID: {route.id}, Start: {route.start}, Destination: {route.destination}, Sacco: {route.sacco}")
                        print("-" * 60)
                        
                except Exception as e:
                    print(f" Error: {e}")
            
            elif choice == '4':
                # Find Route by ID
                try:
                    route_id = int(input("Enter route ID: ").strip())
                    route = Route.find_by_id(session, route_id)
                    print(f"\nRoute Found:")
                    print(f"ID: {route.id}")
                    print(f"Start: {route.start}")
                    print(f"Destination: {route.destination}")
                    print(f"Sacco: {route.sacco}")
                    
                except ValueError as e:
                    print(f" Error: {e}")
                except Exception as e:
                    print(f" Unexpected error: {e}")
            
            elif choice == '5':
                # Back to Main Menu
                break
            
            else:
                print(" Invalid choice. Please enter 1-5.")
                
    finally:
        close_session(session)

def handle_fare_operations():
    """Handle fare management operations"""
    session = get_session()
    try:
        while True:
            display_fare_menu()
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == '1':
                # Create Fare
                try:
                    stage = input("Enter stage name: ").strip()
                    price = int(input("Enter price: ").strip())
                    route_id = int(input("Enter route ID: ").strip())
                    
                    fare = Fare.create(session, stage, price, route_id)
                    print(f" Fare created successfully! ID: {fare.id}")
                    
                except ValueError as e:
                    print(f" Error: {e}")
                except Exception as e:
                    print(f" Unexpected error: {e}")
            
            elif choice == '2':
                # Delete Fare
                try:
                    fare_id = int(input("Enter fare ID to delete: ").strip())
                    Fare.delete(session, fare_id)
                    print(" Fare deleted successfully!")
                    
                except ValueError as e:
                    print(f" Error: {e}")
                except Exception as e:
                    print(f" Unexpected error: {e}")
            
            elif choice == '3':
                # List All Fares
                try:
                    fares = Fare.get_all(session)
                    if not fares:
                        print("No fares found.")
                    else:
                        print("\nAll Fares:")
                        print("-" * 60)
                        for fare in fares:
                            print(f"ID: {fare.id}, Stage: {fare.stage}, Price: {fare.price}, Route ID: {fare.route_id}")
                        print("-" * 60)
                        
                except Exception as e:
                    print(f" Error: {e}")
            
            elif choice == '4':
                # Find Fare by ID
                try:
                    fare_id = int(input("Enter fare ID: ").strip())
                    fare = Fare.find_by_id(session, fare_id)
                    print(f"\nFare Found:")
                    print(f"ID: {fare.id}")
                    print(f"Stage: {fare.stage}")
                    print(f"Price: {fare.price}")
                    print(f"Route ID: {fare.route_id}")
                    
                except ValueError as e:
                    print(f" Error: {e}")
                except Exception as e:
                    print(f" Unexpected error: {e}")
            
            elif choice == '5':
                # Search Fares by Stage
                try:
                    stage_pattern = input("Enter stage name to search: ").strip()
                    fares = Fare.search_by_stage(session, stage_pattern)
                    
                    if not fares:
                        print(f"No fares found with stage containing '{stage_pattern}'")
                    else:
                        print(f"\nFares containing '{stage_pattern}':")
                        print("-" * 60)
                        for fare in fares:
                            print(f"ID: {fare.id}, Stage: {fare.stage}, Price: {fare.price}, Route ID: {fare.route_id}")
                        print("-" * 60)
                        
                except Exception as e:
                    print(f" Error: {e}")
            
            elif choice == '6':
                # Back to Main Menu
                break
            
            else:
                print(" Invalid choice. Please enter 1-6.")
                
    finally:
        close_session(session)

@click.command()
def main():
    """Matatu Fare & Route Planner CLI Application"""
    print("Welcome to Matatu Fare & Route Planner CLI!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            handle_route_operations()
        
        elif choice == '2':
            handle_fare_operations()
        
        elif choice == '3':
            print(" Thank you for using Matatu Fare & Route Planner CLI!")
            break
        
        else:
            print(" Invalid choice. Please enter 1-3.")

if __name__ == "__main__":
    main()
