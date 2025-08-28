from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import re

Base = declarative_base()

class Route(Base):
    __tablename__ = 'routes'
    
    id = Column(Integer, primary_key=True)
    start = Column(String(50), nullable=False)
    destination = Column(String(50), nullable=False)
    sacco = Column(String(50), nullable=False)
    
    # One-to-many relationship with Fare
    fares = relationship("Fare", back_populates="route", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Route(id={self.id}, start='{self.start}', destination='{self.destination}', sacco='{self.sacco}')>"
    
    @classmethod
    def create(cls, session, start, destination, sacco):
        """Create a new route"""
        # Validate input
        if not (1 <= len(start) <= 50):
            raise ValueError("Start location must be between 1-50 characters")
        if not (1 <= len(destination) <= 50):
            raise ValueError("Destination must be between 1-50 characters")
        if not (1 <= len(sacco) <= 50):
            raise ValueError("Sacco must be between 1-50 characters")
        
        # Create and save route
        route = cls(start=start, destination=destination, sacco=sacco)
        session.add(route)
        session.commit()
        return route
    
    @classmethod
    def delete(cls, session, route_id):
        """Delete a route by ID"""
        route = session.query(cls).filter_by(id=route_id).first()
        if not route:
            raise ValueError(f"Route with ID {route_id} not found")
        
        session.delete(route)
        session.commit()
        return True
    
    @classmethod
    def get_all(cls, session):
        """Get all routes"""
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, session, route_id):
        """Find route by ID"""
        route = session.query(cls).filter_by(id=route_id).first()
        if not route:
            raise ValueError(f"Route with ID {route_id} not found")
        return route

class Fare(Base):
    __tablename__ = 'fares'
    
    id = Column(Integer, primary_key=True)
    stage = Column(String(25), nullable=False)
    price = Column(Integer, nullable=False)
    route_id = Column(Integer, ForeignKey('routes.id'), nullable=False)
    
    # Many-to-one relationship with Route
    route = relationship("Route", back_populates="fares")
    
    def __repr__(self):
        return f"<Fare(id={self.id}, stage='{self.stage}', price={self.price}, route_id={self.route_id})>"
    
    @classmethod
    def create(cls, session, stage, price, route_id):
        """Create a new fare"""
        # Validate input
        if not (1 <= len(stage) <= 25):
            raise ValueError("Stage must be between 1-25 characters")
        if price < 0:
            raise ValueError("Price must be a non-negative integer")
        
        # Check if route exists
        route = session.query(Route).filter_by(id=route_id).first()
        if not route:
            raise ValueError(f"Route with ID {route_id} not found")
        
        # Create and save fare
        fare = cls(stage=stage, price=price, route_id=route_id)
        session.add(fare)
        session.commit()
        return fare
    
    @classmethod
    def delete(cls, session, fare_id):
        """Delete a fare by ID"""
        fare = session.query(cls).filter_by(id=fare_id).first()
        if not fare:
            raise ValueError(f"Fare with ID {fare_id} not found")
        
        session.delete(fare)
        session.commit()
        return True
    
    @classmethod
    def get_all(cls, session):
        """Get all fares"""
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, session, fare_id):
        """Find fare by ID"""
        fare = session.query(cls).filter_by(id=fare_id).first()
        if not fare:
            raise ValueError(f"Fare with ID {fare_id} not found")
        return fare
    
    @classmethod
    def search_by_stage(cls, session, stage_pattern):
        """Search fares by stage name pattern"""
        return session.query(cls).filter(cls.stage.ilike(f"%{stage_pattern}%")).all()
