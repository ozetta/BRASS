import asyncio
import fastapi_poe as fp
import json

class BRASS:
    def __init__(self, api_key, bot_name="ChatGPT"):
        self.api_key = api_key
        self.bot_name = "BRASS-" + bot_name

    async def get_full_response(self, messages):
        output = ""
        async for partial in fp.get_bot_response(messages=messages, bot_name=self.bot_name, api_key=self.api_key, temperature=0):
            # parse the text from JSON '{"text": "output"}'
            output += json.loads(partial.raw_response["text"])["text"]
        return output

    def query(self, *prompts):
        req = [fp.ProtocolMessage(role="user", content=p) for p in prompts]
        resp = asyncio.run(self.get_full_response(req))
        return resp

    def query_json(self, *prompts):
        try:
            output = self.query(*prompts)
            if "```json" in output:
                ps = output.index("```json")
                pe = len(output) - output[::-1].index("```")
                json_output = output[ps+7:pe-3]            
            elif "{" in output or "[" in output:
                if "{" in output:
                    cur = output.index("{")
                else:
                    cur = 2147483647
                if "[" in output:
                    sqr = output.index("[")
                else:
                    sqr = 2147483647
                if cur < sqr:
                    ps = output.index("{")
                    pe = len(output) - output[::-1].index("}")
                    json_output = output[ps:pe]
                else:
                    ps = output.index("[")
                    pe = len(output) - output[::-1].index("]")
                    json_output = output[ps:pe]
            else:
                json_output = "null"
            return json.loads(json_output)
        except Exception:
            return None
