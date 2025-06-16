from typing import Dict,Any
from google.adk.tools import ToolContext


def exit_tool(tool_context:ToolContext)->Dict[str,Any]:
    """call this function only when user goal is met, signalling for the termination of loop
    args:
         tool_execution: context for tool execution

    returns:
         empty dictonary
         
    """
    tool_context.actions.escalate=True
    return {}