import pytest
from src.bugbounty_ia.agents.base_agent import BaseAgent
from src.bugbounty_ia.agents.scanning_agent import ScanningAgent

def test_base_agent_init():
    class TestAgent(BaseAgent):
        def execute(self, target):
            pass
            
    agent = TestAgent("Test")
    assert agent.name == "Test"
    assert len(agent.results) == 0

def test_scanning_agent_init():
    agent = ScanningAgent()
    assert agent.name == "ScanningAgent"
