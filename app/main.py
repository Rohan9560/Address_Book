from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import engine, SessionLocal, Base
from helper import calculate_distance


# Import the Address model from database.py
from database import Address

# Create FastAPI app
app = FastAPI()

# Pydantic model for request body validation
class AddressRequest(BaseModel):
    name: str
    street: str
    city: str
    state: str
    zip: int
    latitude: float
    longitude: float

# Pydantic model for request body validation
class GetDistance(BaseModel):
    latitude: float
    longitude: float
    distance: float

# Route to create a new address
@app.post("/addresses/")
def create_address(address: AddressRequest):
    db = SessionLocal()
    if not (-90 <= address.latitude <= 90) or not (-180 <= address.longitude <= 180):
        raise HTTPException(status_code=400, detail="Invalid coordinates")
    try:
        # Create a new address object
        db_address = Address(name=address.name, street=address.street, city=address.city, state=address.state,
                             zip=address.zip, latitude=address.latitude, longitude=address.longitude)
        # Add to the database
        db.add(db_address)
        db.commit()
        db.refresh(db_address)
        return {"message": "Address created successfully", "address_id": db_address.id}
    finally:
        db.close()

# Route to retrieve addresses within a given distance from a specified location
@app.get("/addresses/within_distance")
def get_addresses_within_distance(latitude: float, longitude: float, distance: float):
    db = SessionLocal()
    if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
        raise HTTPException(status_code=400, detail="Invalid coordinates")
    try:
        addresses = db.query(Address).all()
        filtered_addresses = []
        for addr in addresses:
            addr_distance = calculate_distance(latitude, longitude, addr.latitude, addr.longitude)
            if addr_distance <= distance:
                filtered_addresses.append({
                    "id": addr.id,
                    "name": addr.name,
                    "street": addr.street,
                    "city": addr.city,
                    "state": addr.state,
                    "zip": addr.zip,
                    "latitude": addr.latitude,
                    "longitude": addr.longitude,
                    "distance": addr_distance  # Include the distance in the response
                })
        return filtered_addresses
    finally:
        db.close()

# Route to fetch all addresses
@app.get("/addresses/all")
def get_all_addresses():
    db = SessionLocal()
    try:
        addresses = db.query(Address).all()
        return addresses
    finally:
        db.close()

# Route to delete addresses
@app.delete("/addresses/{address_id}")
def delete_address(address_id: int):
    db = SessionLocal()
    address = db.query(Address).filter(Address.id == address_id).first()
    if address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    db.delete(address)
    db.commit()
    return {"message": "Address deleted successfully"}

@app.put("/addresses/{address_id}")
def update_address(address_id: int, address: AddressRequest):
    db = SessionLocal()
    db_address = db.query(Address).filter(Address.id == address_id).first()
    if db_address:
        db_address.name = address.name
        db_address.street = address.street
        db_address.city = address.city
        db_address.state = address.state
        db_address.zip = address.zip
        db_address.latitude = address.latitude
        db_address.longitude = address.longitude
        db.commit()
        return {"message": "Address updated successfully"}
    raise HTTPException(status_code=404, detail="Address not found")

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)