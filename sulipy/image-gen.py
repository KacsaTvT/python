import os
import openai
openai.api_key = os.getenv("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")
openai.Image.create(
  prompt="A cute baby sea otter",
  n=2,
  size="1024x1024"
)
