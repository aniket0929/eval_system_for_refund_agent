from agents.models import model
from agents.tools import get_user_purchase_history,calculate_right_refund,issue_refund_ticket,get_today_date
from dotenv import load_dotenv
from langchain.agents import create_agent
from agents.prompts import agent_system_prompt
from agents.objects import Answer
from langgraph.checkpoint.memory import InMemorySaver
from langchain.messages import HumanMessage
from uuid import uuid4

load_dotenv()


#create agent 
agent =create_agent(
    model=model,
    system_prompt=agent_system_prompt,
    tools=[get_user_purchase_history,calculate_right_refund,issue_refund_ticket,get_today_date],
    response_format=Answer,
    checkpointer=InMemorySaver()
)



def run_conversation():
    #for keepiing msgs seperate/ threads
    config={
        "configurable":{
            "thread_id":str(uuid4())
        }
    }

    text="I would like to request a refund"
    print(text)

    question=HumanMessage(content=text)

    conversation=True

    while conversation:

        #invoke the agent
        response = agent.invoke({"messages":question}, config=config)

        structured_response=response["structured_response"]

        print(structured_response.answer)

        conversation=structured_response.conversation

        if conversation:
         user_input = input("reply: \n")
         question = HumanMessage(content=user_input)
    
    print("the job is done!")



run_conversation()