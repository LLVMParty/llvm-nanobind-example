import llvm

if __name__ == "__main__":
    with llvm.create_context() as ctx:
        with ctx.create_module("example_module") as mod:
            func_type = ctx.function_type(
                ctx.int32_type(), [ctx.int32_type(), ctx.int32_type()]
            )
            add_func = mod.add_function("add", func_type)
            entry = add_func.append_basic_block("entry", ctx)
            with ctx.create_builder() as builder:
                builder.position_at_end(entry)
                a, b = add_func.params
                a.name = "a"
                b.name = "b"
                result = builder.add(a, b, "sum")
                builder.ret(result)

            print(mod.to_string())
