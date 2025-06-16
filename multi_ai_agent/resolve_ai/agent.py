from google.adk.agents import LoopAgent,SequentialAgent
from .subagents.planner_agent.agent import agent_planning
from .subagents.enrichment_agent.agent import EnrichmentAgent
from.subagents.evaluator_agent.agent import EvaluatorAgent
from .subagents.final_agent.agent import FinalAgent

execution_loop = LoopAgent(
    name='ExecutionLoop',
    max_iterations=2,
    sub_agents=[EnrichmentAgent,EvaluatorAgent],
    description="Iteratively executes and enriches the planned tasks using external tools. It uses enrichment_agent to fetch data and evaluator_agent to decide whether the goal has been met or if further refinement is needed."


)

root_agent=SequentialAgent(
    name="ResolveAI",
    sub_agents=[agent_planning,execution_loop,FinalAgent],
    description="Drives the full workflow—planning the user’s goal and coordinating agents to execute, enrich, and refine results until the goal is achieved",
    
)
