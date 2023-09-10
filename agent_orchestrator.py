from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI

def init_agent_orchestrator(tools):
    llm = ChatOpenAI(temperature=0, model="gpt-4")
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    return agent