from pydantic import BaseModel, Field

# este seria la parte de customers-------------------------------------------------------------------
class CustomerCreate(BaseModel):
   
    customer_id: int = Field(..., description="ID del cliente", example=1)
    name: str = Field(..., description="Nombre del cliente", example="John Doe")
    email: str = Field(..., description="Correo del cliente", example="johndoe@example.com")
    phone: str = Field(..., description="Teléfono del cliente", example="+1234567890")

class Customer(CustomerCreate):
    
    customer_id: int = Field(..., description="ID del cliente", example=1)
