from autogen_agentchat.agents import AssistantAgent
from config.settings import get_model_client
from agents.system_prompt import PROBLEM_SOLVER_SYSTEM_MESSAGE

model_client = get_model_client()

def get_problem_solver_agent():
    """
    Function to get the problem solver agent.
    This agent is responsible for solving DSA problems.
    It will work with the code executor agent to execute the code.
    """
    problem_solver_agent = AssistantAgent(
            name="DSA_Problem_Solver_Agent",
            description="An agent that solves DSA problems",
            model_client=model_client,
            system_message=PROBLEM_SOLVER_SYSTEM_MESSAGE
        )
    
    return problem_solver_agent