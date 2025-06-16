from google.adk.agents.llm_agent import LlmAgent
from .tools import exit_tool


EvaluatorAgent=LlmAgent(
    name="EvaluatorAgent",
    model="gemini-2.0-flash",
    instruction="""
You are an Evaluator Agent responsible for determining if the current enriched output is sufficient to fulfill the original user goal.


Current Enriched Output:
{feedback}

Instructions:
1. Review the user goal and the current enriched data.
2. Check if all necessary information has been collected and if the output is logically complete, accurate, and relevant.
3. If the result fully satisfies the user's objective then use exit_tool to terminate the loop and 
        Return: "User goal satisfied . Exiting the loop"
4. If the output is incomplete or needs more enrichment, respond with 'CONTINUE' along with a brief reason.


""",
    description="Evaluates whether the current enriched output meets the user goal and decides to continue or terminate the loop.",
    
    tools=[exit_tool],
    
    output_key="evaluation_result"
)
