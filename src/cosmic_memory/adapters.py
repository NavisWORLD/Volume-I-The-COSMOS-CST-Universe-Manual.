from __future__ import annotations
from typing import Callable, Any
from .memory import RecursiveMemory

class ModelMemoryAdapter:
    """Tiny adapter that can wrap any callable model(prompt)->text."""
    def __init__(self, memory: RecursiveMemory, model: Callable[[str], str], *, recall_limit: int = 5):
        self.memory = memory; self.model = model; self.recall_limit = recall_limit

    def __call__(self, prompt: str) -> str:
        ctx = self.memory.context_for(prompt, limit=self.recall_limit)
        augmented = prompt if not ctx else (
            "[PERSISTENT MEMORY — relevant prior records; do not invent beyond them]\n" + ctx +
            "\n\n[CURRENT REQUEST]\n" + prompt
        )
        answer = self.model(augmented)
        self.memory.remember("User: " + prompt, metadata={"role": "user"})
        self.memory.remember("Assistant: " + answer, metadata={"role": "assistant"})
        return answer

class ChatMessagesAdapter:
    """Build a message list for chat-style model SDKs without depending on a vendor."""
    def __init__(self, memory: RecursiveMemory, *, recall_limit: int = 5):
        self.memory = memory; self.recall_limit = recall_limit

    def inject(self, messages: list[dict[str, Any]]) -> list[dict[str, Any]]:
        last = next((m.get("content", "") for m in reversed(messages) if m.get("role") == "user"), "")
        ctx = self.memory.context_for(str(last), limit=self.recall_limit)
        if not ctx: return list(messages)
        system = {"role": "system", "content": "Relevant persistent memory:\n" + ctx}
        return [system, *messages]
