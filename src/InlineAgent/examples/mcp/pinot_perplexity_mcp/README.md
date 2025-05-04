# Pinot MCP Agent

> [!IMPORTANT]
> Never expose AWS keys publicly, use least privilege IAM roles, and rotate credentials every 90 days. Utilize AWS Secrets Manager, implement MFA, avoid hard-coding credentials, and continuously monitor access.

<p align="center">
  <a href="https://hub.docker.com/r/mcp/perplexity-ask"><img src="https://img.shields.io/badge/Docker-perplexity_ask-blue" /></a>
  <a href="https://github.com/jsonallen/perplexity-mcp"><img src="https://img.shields.io/badge/Github-perplexity_mcp-blue" /></a>
</p>

1. Follow setup instructions [here](../../../README.md#getting-started)
2. Create .env file with [.env.example](./.env.example)
3. Setup `pinot-mcp-server` MCP server

```python
git clone https://github.com/startreedata/mcp-pinot.git
cd mcp-pinot
docker build -t mcp-pinot-server .
```

4. Run example `python main.py`

## Output

```
Connected to server with tools:['read-query', 'list-tables', 'table-details', 'segment-list', 'index-column-details', 'segment-metadata-details', 'tableconfig-schema-details']
Perplexity MCP Server running on stdio with Ask, Research, and Reason tools

Connected to server with tools:['perplexity_ask', 'perplexity_research', 'perplexity_reason']
Trying to invoke pinot agent
SessionId: 247f11ba-20e4-489c-bafb-1b0e7d8560e5
2025-05-04 11:57:36,898 - botocore.credentials - INFO - Found credentials in shared credentials file: ~/.aws/credentials
Input Tokens: 1424 Output Tokens: 83
Thought: Let me explore the Pinot tables first and then create a meaningful visualization based on the data.
First, I'll list all available tables.
Tool use: list-tables with these inputs:
Tool output: ['poly_market_extract']
Input Tokens: 2114 Output Tokens: 126
Thought: I notice there are several interesting tables. Let's explore the 'poly_market_extract' table as it might contain some meaningful market data. I'll check its schema first.
Tool use: tableconfig-schema-details with these inputs: tableName[poly_market_extract] (string)
Tool output: {'tableName': 'poly_market_extract',  ... }
Input Tokens: 5100 Output Tokens: 183
Thought: Let's analyze some interesting metrics from this table. I'll create a query to get the average maker and taker base fees for different market conditions.
Tool use: read-query with these inputs: query[SELECT
  active,
  COUNT(*) as market_count,
  AVG(maker_base_fee) as avg_maker_fee,
  AVG(taker_base_fee) as avg_taker_fee
FROM poly_market_extract
GROUP BY active
ORDER BY market_count DESC] (string)
Tool output: [{'active': 'true', 'market_count': 15388, 'avg_maker_fee': 0.0, 'avg_taker_fee': 0.2079542500649857}, {'active': 'false', 'market_count': 608, 'avg_maker_fee': 0.0, 'avg_taker_fee': 0.0}]
Input Tokens: 5385 Output Tokens: 191
Based on the analysis of the poly_market_extract table:

1. Active Markets (true):
   - Count: 15,388 markets
   - Average Maker Fee: 0%
   - Average Taker Fee: 20.8%

2. Inactive Markets (false):
   - Count: 608 markets
   - Average Maker Fee: 0%
   - Average Taker Fee: 0%

This shows that active markets have a significant taker fee while maintaining zero maker fees, likely to incentivize market making and liquidity provision.

Here's a simple bar graph representation:

Active Markets:    |█████████████████████████| 15,388
Inactive Markets: |█| 608

Note: The length of bars represents the relative number of markets in each category.
Agent made a total of 4 LLM calls, using 14606 tokens (in: 14023, out: 583), and took 24.4 total seconds
```