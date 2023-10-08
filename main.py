from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
import autogen
import openai

openai.api_key = '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'
webhook_url = 'https://falling-fire-5834.tines.com/webhook/838cf4b997f58f02354604972dae8875/b3884ec74bf13e2933695619cc44034a'

# Load LLM inference endpoints from an env variable or a file
# See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
# and OAI_CONFIG_LIST_sample.json
#config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
config_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": {
            "gpt-3.5-turbo"
        }
    }
)
#assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
#user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})
#user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")
# This initiates an automated chat between the two agents to solve the task

#response = openai.Image.create(
#  prompt="a white siamese cat",
#  n=1,
#  size="1024x1024"
#)
#image_url = response['data'][0]['url']
#print(image_url)

#create an AssistantAgent named "assistant"
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={
       "seed": 42,  # seed for caching and reproducibility
        "config_list": config_list,  # a list of OpenAI API configurations
        "temperature": 0,  # temperature for sampling
    },   #configuration for autogen's enhanced inference API which is compatible with OpenAI API
)
# create a UserProxyAgent instance named "user_proxy"
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    max_consecutive_auto_reply=10,
    human_input_mode="NEVER",
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False,  # set to True or image name like "python:3" to use docker
    },
)
# the assistant receives a message from the user_proxy, which contains the task description
user_proxy.initiate_chat(
    assistant,
    message="""What date is today? Compare the year-to-date gain for Microsoft and Okta""",
)