# llvm-nanobind-example

Super basic [llvm-nanobind](https://github.com/LLVMParty/llvm-nanobind) example project.

## Building

Set the CMake prefix path to point to your LLVM installation:

```bash
export CMAKE_PREFIX_PATH=$(brew --prefix llvm)
```

Set up the environment:

```bash
uv sync
```

Run the example

```bash
uv run example.py
```
