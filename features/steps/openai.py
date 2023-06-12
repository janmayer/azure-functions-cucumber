from behave import given


@given("the AI description generator is functional")
def mock_openai(context):
    context.openai.post(
        "mappings",
        json={
            "request": {
                "url": "/v1/completions",
                "method": "POST",
                "headers": {
                    "Authorization": {"equalTo": "Bearer my_openai_api_key"},
                },
            },
            "response": {
                "status": 200,
                "headers": {"Content-Type": "application/json"},
                "jsonBody": {
                    "id": "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
                    "object": "text_completion",
                    "created": 1589478378,
                    "model": "VAR_model_id",
                    "choices": [
                        {
                            "text": "Tolle Karre.",
                            "index": 0,
                            "logprobs": None,
                            "finish_reason": "length",
                        }
                    ],
                    "usage": {
                        "prompt_tokens": 5,
                        "completion_tokens": 7,
                        "total_tokens": 12,
                    },
                },
            },
        },
    ).raise_for_status()
