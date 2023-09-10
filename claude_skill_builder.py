import anthropic

def build_claude_skill(prompt_template, data_context):
    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        messages=[{"role": "user", "content": f"Build a data engineering skill: {prompt_template} with context: {data_context}"}]
    )
    return message.content