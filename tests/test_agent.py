from saaf import Agent


def test_agent_creation():

    agent = Agent()

    response = agent.run(
        "Hello SAAF"
    )

    assert "Hello SAAF" in response