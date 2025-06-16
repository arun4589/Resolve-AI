from google.adk.agents.llm_agent import LlmAgent




agent_planning=LlmAgent(
    name='PlanningAgent',
    model='gemini-2.0-flash',
    instruction="""
    
    Given a user goal, break it down into a clear, step-by-step plan that can be executed by downstream agents. Ensure the steps are logically ordered, interdependent, and specify what data needs to be fetched or processed at each stage to achieve the final objective.""",
    description="Generate a step by step plan to achieve the final goal",
    output_key="planning"
)