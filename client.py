class OpenRouterPlaygroundExporterClient:
    def export_payload(self, system_prompt: str, user_prompt: str) -> dict:
        payload = {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": 0.7
        }
        return {"api_payload": payload}