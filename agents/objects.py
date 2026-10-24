from pydantic import BaseModel,Field

class Answer(BaseModel):
    answer:str=Field(description="answer needed for the user's query")
    conversation:bool=Field(description="This is an indicator to know if the conversation shud continue or not"\
        "if the agentt has made decision about tthe refund this shud be false"\
            "but if it still needs togather information for refund it should be true",default=True)

class PurchaseItem(BaseModel):
    name:str=Field(description="name of the item purchased")

