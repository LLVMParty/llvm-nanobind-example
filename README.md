# llvm-nanobind-example

Super basic [llvm-nanobind](https://github.com/LLVMParty/llvm-nanobind) example project.

## Building

Allow CMake to find your LLVM installation:

```bash
export LLVM_ROOT=$(brew --prefix llvm)
```

Set up the environment:

```bash
uv sync
```

Run the example

```bash
uv run example.py
```
