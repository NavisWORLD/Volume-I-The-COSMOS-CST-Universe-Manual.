from cosmic_memory import RecursiveMemory
from cosmic_memory.adapters import ModelMemoryAdapter

def your_model(prompt: str) -> str:
    # Replace with any local or hosted model call.
    return 'MODEL SAW:\n' + prompt[:400]

memory=RecursiveMemory('adapter.db',namespace='demo-agent')
agent=ModelMemoryAdapter(memory,your_model)
print(agent('Remember that my launch codename is Aurora.'))
print(agent('What is my launch codename?'))
memory.close()
