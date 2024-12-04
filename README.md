# Minimal reproducible example for `DataFrame.apply` type hints vs. returning `set` from the applied function

This is a minimal reproducible example for [this StackOverflow
question](https://stackoverflow.com/q/79250681/1826241).

Instructions:

0. Install [uv](https://docs.astral.sh/uv/) (for dependency management) and clone the
   repo.
1. Run `uv run python reprex.py` to see the code works fine at runtime:
   ```
   0       {a, d}
   1    {e, a, b}
   2    {c, f, a}
   dtype: object
   ```
2. Run `uv run pyright reprex.py` to see that type checking generates errors, claiming
   that the function applied by `DataFrame.apply` cannot return `set`:
   ```
   /Users/david/repos/eva/pandas-apply-set/reprex.py
     /Users/david/repos/eva/pandas-apply-set/reprex.py:10:7 - error: No overloads for "apply" match the provided arguments (reportCallIssue)
     /Users/david/repos/eva/pandas-apply-set/reprex.py:10:16 - error: Argument of type "(row: Unknown) -> set[Unknown]" cannot be assigned to parameter "f" of type "(...) -> Series[Any]" in function "apply"
       Type "(row: Unknown) -> set[Unknown]" is not assignable to type "(...) -> Series[Any]"
         Function return type "set[Unknown]" is incompatible with type "Series[Any]"
           "set[Unknown]" is not assignable to "Series[Any]" (reportArgumentType)
   2 errors, 0 warnings, 0 informations
   ```
