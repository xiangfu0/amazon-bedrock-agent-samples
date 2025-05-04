from InlineAgent.tools import MCPStdio
from InlineAgent.action_group import ActionGroup
from InlineAgent.agent import InlineAgent

from config import pinot_mcp_params, perplexity_server_params


async def main():

    pinot_mcp_client = await MCPStdio.create(server_params=pinot_mcp_params)
    perplexity_mcp_client = await MCPStdio.create(server_params=perplexity_server_params)

    try:
        pinot_mcp_group = ActionGroup(
            name="PinotMCPGroup",
            mcp_clients=[pinot_mcp_client, perplexity_mcp_client],
        )
        
        print("Trying to invoke pinot agent") 

        await InlineAgent(
            foundation_model="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
            instruction="""You are a friendly assistant that is responsible for resolving user queries.
            
            You have access to list pinot table information and query pinot table and code interpreter. 
            
            """,
            agent_name="pinot_agent",
            action_groups=[
                pinot_mcp_group,
            ],
        ).invoke(
            input_text="Try to explore information about pinot table and query pinot table. Be pricise and create a bar graph."
        )
    finally:
        # LIFO
        await perplexity_mcp_client.cleanup()
        await pinot_mcp_client.cleanup()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
