# Installable package

Prebuilt pure-Python wheel:

`cosmic_synaptic_memory-0.1.0-py3-none-any.whl`

SHA-256:

`8e114527c4a84bbe2179ec68c257ead341329689ed7d3e36db08e419057223b4`

Install without building from source:

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install dist/cosmic_synaptic_memory-0.1.0-py3-none-any.whl
cosmic-memory --help
```

The base wheel has no runtime dependencies beyond Python >= 3.10. Optional API/Azure/BLE integrations still require their documented extras/dependencies.

This wheel was smoke-tested by installing it into a fresh isolated virtual environment, writing a durable memory, and recalling that memory through the installed CLI.
