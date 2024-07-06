from agent_actions import AgentAction, AgentActionMessageLog, AgentFinish, AgentStep

class AgentEnvironment:
    def __init__(self):
        self.steps = []

    def execute_action(self, action: AgentAction) -> AgentStep:
        # Simulate executing the action and getting an observation
        observation = f"Executed {action.tool} with input {action.tool_input}"
        step = AgentStep(action=action, observation=observation)
        self.steps.append(step)
        return step

    def finish(self, return_values: dict) -> AgentFinish:
        log = "Final result obtained"
        finish = AgentFinish(log=log, return_values=return_values)
        return finish

# Initialize the environment
env = AgentEnvironment()
