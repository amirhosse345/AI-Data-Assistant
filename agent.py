import json
from dotenv import load_dotenv
from openai import OpenAI

from tools import (
    calculate_total_sales,
    get_best_selling_product,
    get_sales_by_category
)

load_dotenv()
client = OpenAI()

tools = {
    "calculate_total_sales": calculate_total_sales,
    "get_best_selling_product": get_best_selling_product,
    "get_sales_by_category": get_sales_by_category
}

tool_descriptions = [
    {
        "type": "function",
        "name": "get_sales_by_category",
        "description": "Calculate total sales for a specific category.",
        "parameters": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "description": "The product category to calculate sales for."
                }
            },
            "required": ["category"],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "calculate_total_sales",
        "description": "Calculate total sales for all products.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False
        }
    },
    {
    "type": "function",
    "name": "get_best_selling_product",
    "description": "Find the product with the highest sales.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": [],
        "additionalProperties": False
    }
    },
]


question = input("Ask something: ")

response = client.responses.create(
    model="gpt-5-mini",
    input=question,
    tools=tool_descriptions
)

for item in response.output:
    if item.type == "function_call":
        print(item.name)

        arguments = json.loads(item.arguments)

        tool_function = tools.get(item.name)
        result = tool_function(**arguments)

        print("Tool:", item.name, "| Result:", result)

        final_response = client.responses.create(
            previous_response_id=response.id,
            input=[
                {
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": str(result)
                }
            ]
        )

        print(final_response.output_text)