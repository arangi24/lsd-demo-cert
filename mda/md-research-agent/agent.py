from managed_deepagents import define_deep_agent


agent = define_deep_agent(
    name="md-research-agent",
    model="openai:gpt-5.6-terra",
    tools=[{"type": "web_search"}],
)
