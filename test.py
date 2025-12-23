# pip install pydantic email-validator
from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator,computed_field
from typing import List,Dict,Optional,Annotated

# We can apply Field function on integer or string field.

# combination of Annotated and Feild  is used to provide the metadata.

# field_validator is used for custom and complex data validation but it is only work on single field. It works on two mode : 
# mode="after" (default) : In this mode, value is received to field_validator after type coercion.
# mode="before"  : In this mode, value is received to field_validator before type coercion.


# model_validator is used for custom and complex data validation on multiple field.
# It works on two mode : 
# mode="after" (default) : In this mode, value is received to model_validator after type coercion.
# mode="before"  : In this mode, value is received to model_validator before type coercion.



# computed_field is used to make fields which depends on the other fields by doing calculation on some fields.


# nested model : 
# use models as a field


# Advantage of nested_model : 
# Better Organization of related data (eg: address,insurance)
# Reusability : Use vitals in multiple models (eg : Patient, MedicalRecord)
# Readability : Easier for developers and API consumers to understand
# Validation : Nested models are validated automatically-no extra work needed. 


class Address(BaseModel):
    city:str
    state:str
    pin:str



class Patient(BaseModel):
    name: Annotated[str,Field(max_length=20,title="name of the patient",description="name should be less than or equal to 20")]
    age:int = Field(gt=0,lt=120)
    email:EmailStr
    gender:Optional[str] = "Male"
    linkedin_url : AnyUrl
    weight:float = Field(gt=0) # in kgs
    height:float = Field(gt=0) # in mtr
    married:Annotated[Optional[bool],Field(default=False)]
    allergies : Optional[List[str]]=Field(default=None,max_length=5)
    contact_details : Dict[str,str] 

    address:Address # nested model


    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains = ["hdfc.com","icici.com"]
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a Valid domains')
        return value
    



    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @model_validator(mode="after")
    def validate_emergency_contact(self):
        if self.age>60 and 'emergency' not in self.contact_details : 
            raise ValueError("Patient older than 60 must have emergency contact no")
        else : 
            return self
        



    @computed_field
    @property
    def bmi(self)->float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    

address = {'city':"karnal","state":"haryana","pin":"132001"}
address1 = Address(**address)
# Here we need to unpack dictionaries because BaseModel accepts parameters in the form (city="karnal",state="haryana").


patient_info = {"name":"Ram","age":20,'email':"abc@hdfc.com","linkedin_url":"https://linkedin.com/Ram","weight":56.2,"height":1.52,"married":True,"allergies":["pollen","dust"],"contact_details":{"phone_no":'9087654321'},"address":address1}

def  insert_patient_data(patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.bmi)
    print(patient.address.city)

    print("inserted")

patient1 = Patient(**patient_info)

insert_patient_data(patient1)



# serialzation
# We can export this model 

temp = patient1.model_dump()
print(temp)
print(type(temp)) # dictionary

temp2 = patient1.model_dump_json()
print(temp2)
print(type(temp2)) # str

temp3 = patient1.model_dump(include=['name','age']) 
print(temp3)
temp4=  patient1.model_dump(exclude=['age'])
print(temp4)
temp5 = patient1.model_dump(exclude={'address':['state']})
print(temp5)
temp6 = patient1.model_dump(exclude_unset=True)
# It only export those which is defined in the "patient_info" and exclude the default values.
print(temp6)


