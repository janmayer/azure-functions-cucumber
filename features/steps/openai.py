from behave import given


@given("the AI description generator is functional")
def mock_openai(context):
    context.carservice.post(
        "mappings",
        json={
            "request": {
                "url": "/completions",
                "method": "POST",
                "headers": {
                    "Authorization": {"equalTo": "Bearer MY_OPENAI_API_KEY"},
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
                            "text": "This is indeed a test",
                            "index": 0,
                            "logprobs": null,
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
