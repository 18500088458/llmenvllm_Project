import os
import unittest
from unittest.mock import Mock, patch

from demoLlmClient import LLMClient


class LLMClientTest(unittest.TestCase):
    def test_chat_posts_json_body_matching_siliconflow_example(self):
        response = Mock()
        response.json.return_value = {"choices": [{"message": {"content": "ok"}}]}

        with patch("demoLlmClient.requests.post", return_value=response) as post:
            client = LLMClient(api_key="test-key")
            result = client.chat(
                model="Pro/zai-org/GLM-4.7",
                messages=[
                    {"role": "system", "content": "你是一个有用的助手x"},
                    {"role": "user", "content": "你好，请介绍一下你自己"},
                ],
            )

        self.assertEqual({"choices": [{"message": {"content": "ok"}}]}, result)
        post.assert_called_once()
        args, kwargs = post.call_args
        self.assertEqual(("https://api.siliconflow.cn/v1/chat/completions",), args)
        self.assertEqual(
            {
                "Authorization": "Bearer test-key",
                "Content-Type": "application/json",
            },
            kwargs["headers"],
        )
        self.assertEqual(
            {
                "model": "Pro/zai-org/GLM-4.7",
                "messages": [
                    {"role": "system", "content": "你是一个有用的助手x"},
                    {"role": "user", "content": "你好，请介绍一下你自己"},
                ],
            },
            kwargs["json"],
        )
        self.assertNotIn("data", kwargs)
        self.assertEqual(10, kwargs["timeout"])

    def test_client_can_read_api_key_from_environment(self):
        response = Mock()
        response.json.return_value = {"ok": True}

        with patch.dict(os.environ, {"SILICONFLOW_API_KEY": "env-key"}):
            with patch("demoLlmClient.requests.post", return_value=response) as post:
                LLMClient().chat("Pro/zai-org/GLM-4.7", [])

        self.assertEqual(
            "Bearer env-key",
            post.call_args.kwargs["headers"]["Authorization"],
        )


if __name__ == "__main__":
    unittest.main()
