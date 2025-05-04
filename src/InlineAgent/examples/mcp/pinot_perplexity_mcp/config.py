from dotenv import load_dotenv
import os

from mcp import StdioServerParameters

from InlineAgent import AgentAppConfig

config = AgentAppConfig()

pinot_mcp_params = StdioServerParameters(
    command="docker",
    args=[
        "run",
        "-i",
        "--rm",
        "-e",
        "PINOT_CONTROLLER_URL",
        "-e",
        "PINOT_BROKER_HOST",
        "-e",
        "PINOT_BROKER_PORT",
        "-e",
        "PINOT_BROKER_SCHEME",
        "-e",
        "PINOT_USERNAME",
        "-e",
        "PINOT_PASSWORD",
        "-e",
        "PINOT_TOKEN",
        "-e",
        "PINOT_USE_MSQE",
        "-e",
        "PINOT_DATABASE",
        "mcp-pinot-server:latest",
    ],
    env={
        "PINOT_CONTROLLER_URL": config.PINOT_CONTROLLER_URL,
        "PINOT_BROKER_HOST": config.PINOT_BROKER_HOST,
        "PINOT_BROKER_PORT": config.PINOT_BROKER_PORT,
        "PINOT_BROKER_SCHEME": config.PINOT_BROKER_SCHEME,
        "PINOT_USERNAME": config.PINOT_USERNAME,
        "PINOT_PASSWORD": config.PINOT_PASSWORD,
        "PINOT_TOKEN": config.PINOT_TOKEN,
        "PINOT_USE_MSQE": config.PINOT_USE_MSQE,
        "PINOT_DATABASE": config.PINOT_DATABASE,
        "AWS_ACCESS_KEY_ID": config.AWS_ACCESS_KEY_ID,
        "AWS_SECRET_ACCESS_KEY": config.AWS_SECRET_ACCESS_KEY,
        "AWS_REGION": config.AWS_REGION,
        "BEDROCK_LOG_GROUP_NAME": config.BEDROCK_LOG_GROUP_NAME,
    },
)
