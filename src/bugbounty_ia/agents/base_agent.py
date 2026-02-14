from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """Abstract base class for all agents."""

    @abstractmethod
    def act(self):
        """Perform an action.""" 
        pass

    @abstractmethod
    def learn(self):
        """Update the agent based on feedback.""" 
        pass

    @abstractmethod
    def reset(self):
        """Reset the agent to an initial state.""" 
        pass
