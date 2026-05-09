import llvm

if __name__ == "__main__":
    with llvm.create_context() as ctx:
        with ctx.create_module("example_module") as mod:
            types = ctx.types
            func_type = types.function(types.i32, [types.i32, types.i32])
            add_func = mod.add_function("add", func_type)
            entry = add_func.append_basic_block("entry")
            with entry.create_builder() as builder:
                a, b = add_func.params
                a.name = "a"
                b.name = "b"
                result = builder.add(a, b, "sum")
                builder.ret(result)

            print(mod.to_string())
