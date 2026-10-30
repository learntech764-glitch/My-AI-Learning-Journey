from pydantic import BaseModel,Field,field_validator,model_validator,computed_field,ConfigDict
from typing import Optional,Literal #(limited choices)

class Category(BaseModel):#Pydantic model for category field
    name : Literal['starter','main_course','dessert','beverage'] #exact fileds to be in category

class Model(BaseModel): # BaseModel is used for checking incoming data is valid or not

        model_config =ConfigDict( 
            extra='forbid', # Extra fields
            frozen = True,  # Frozen Model cannot change the value of fields after object creation
            strict = True,  # Strict pydantic strict type checking for fields
            validate_assignment = True, # validate assignment of fields after object creation
                                 ) # extra='forbid' - to restrict extra fields in incoming data     
            
        # Field       : value Type
        id           : int
        name         : str = Field(...,min_length=3,max_length=50,description="Item name",alias="item_name") # making field required #alias - to use different name for field in incoming data
        price        : float = Field(...,gt=0,description="Item price") # making field required
        category     : Category 
        is_available : bool = Field(default=True) # making field required
        description  : Optional[str] = None # making field optional


        #Field Validator - when u one to work on one field
        #name = "Paneer TIKKA" - > title - > "Paneer Tikka"Field
        @field_validator('name')
        @classmethod
        def title_name(cls,value):#cls - Class,value - "Paneer TIKKA"
              return value.title() #returning title case of name field
        #Model Validator - multiple fields
        @model_validator(mode='after') #before - before validation, after - after validation
        def check_available(self):
            if self.is_available and self.price > 100:
                raise ValueError("Price is too high for available item")
            return self
        #Computed Field
        @computed_field
        @property
        def price_with_tax(self) -> float:
            return self.price * 1.18 # 18% tax



item = Model(id=1,item_name="Paneer TIKKA"
        ,price=1.1,category=Category(name='main_course')
        ,is_available=True,  description="A strong coffee" \
                " made by forcing steam" \
                " through ground coffee beans.") 
print(item)
print(type(item))

## in and out seralization
#1. model_dump() - > convert object to dictionary and this will only work inside python
print('Dictionary representation of object')
print(item.model_dump()) # convert object to dictionary

#2. model_dump_json() - > convert object to json string and this will work when we need to send to website or internet
print('JSON representation of object')
print(item.model_dump_json()) # convert object to json string







""" item = Model(id=1,name="Paneer TIKKA"
        ,price=1.1,category=Category(name='main_course')
        ,is_available=True,  description="A strong coffee" \
                " made by forcing steam" \
                " through ground coffee beans.",spicy=True) """  # Extra field scenario


""" item = Model(id=1,name="Espresso"
        ,price=2.5,category=Category(name='Sweet')
        ,is_available=True,  description="A strong coffee" \
                " made by forcing steam" \
                " through ground coffee beans.") """
# Pass scenario

""" item = Model(id=1,name="Espresso"
        ,price=2.5,category="Beverage"
        ,is_available=True) """
 # Pass scenario 

""" item = Model(id=1,name="Espresso"
        ,price=2.5,category="Beverage"
        ,is_available=True,
        description="A strong coffee" \
        " made by forcing steam" \
        " through ground coffee beans.")
 """  # Pass scenario 

""" item = Model(id=1,name="Espresso"
        ,price="two point five",category="Beverage"
        ,is_available=True,
        description="A strong coffee" \
        " made by forcing steam" \
        " through ground coffee beans.")
 """  # Failed scenario for incorrect value type in price field

""" item = Model(id=1
        ,price=2.5,category="Beverage"
        ,is_available=True,
        description="A strong coffee" \
        " made by forcing steam" \
        " through ground coffee beans.")
   """ # Failed scenario for missing required field name
