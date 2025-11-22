## structural — Clean, categorized examples for Python learners

Summary
---------
Small, focused Python scripts organized by topic. Each file illustrates one core concept so you can read, run, and modify code quickly.

Audience
--------
- Absolute beginners who want short, runnable examples.
- People who learn by reading small programs and experimenting.

Prerequisites
-------------
- Python 3.8 or newer (use `python3` on Linux/macOS).
- A terminal and a text editor or IDE.

Quick start
-----------
1. Open a terminal and change to this folder:

```bash
cd structural
```

2. Run a single example:

```bash
python3 01_basics_01_hello_world.py
```

Check the top of each file for a short comment describing what it shows. If a script requests input, follow the prompt.

Organized file index
-------------------
Basics
- `01_basics_01_hello_world.py` — prints a greeting; environment check.
- `01_basics_02_type_casting.py` — converting between str/int/float/bool.
- `01_basics_03_operators.py` — arithmetic and boolean operators.
- `01_basics_04_variable_scope.py` — local vs global scope.
- `01_basics_05_conditionals.py` — `if`, `elif`, `else` examples.

Data structures
- `02_data_structures_01_lists.py` — lists: create, index, slice, common ops.
- `02_data_structures_02_tuples.py` — tuples and immutability.
- `02_data_structures_03_sets.py` — sets and set operations.
- `02_data_structures_04_dictionaries.py` — dict basics and iteration.
- `02_data_structures_05_dict_of_dicts.py` — nested dictionaries.

Loops & control flow
- `03_loops_01_for_loops.py` — `for` loop patterns.
- `03_loops_02_while_loops.py` — `while` loop examples.
- `03_loops_03_break_continue.py` — `break` and `continue` usage.
- `03_loops_04_break_examples_from_range.py` — `range()` examples.

Functions
- `04_functions_01_functions_return.py` — define functions and return values.
- `04_functions_02_varargs.py` — `*args` for variable positional args.
- `04_functions_03_kwargs.py` — `**kwargs` for variable keyword args.

Strings & CLI
- `05_strings_01_string_escape.py` — escape sequences and raw strings.
- `05_strings_02_cli_email.py` — small CLI example (see file header).

Conventions
-----------
- Filenames: `NN_category_NN_name.py` to preserve learning order.
- Each example should include a 1–2 line header comment describing purpose and input.
- Keep files short and focused (ideally < 200 lines).

Run examples safely
-------------------
Run a single file:

```bash
python3 02_data_structures_01_lists.py
```

Run all non-interactive files (safe loop):

```bash
for f in *.py; do
  if grep -q "input(" "$f"; then
    echo "skipping interactive: $f"
    continue
  fi
  printf "\n--- %s ---\n" "$f"
  python3 "$f"
done
```

Note: review scripts before running the full loop — some may require input or print lots of output.

Learning path
-------------
1. Basics (01_basics_01 → 01_basics_05)
2. Data structures (02_data_structures_*)
3. Loops & control flow (03_loops_*)
4. Functions (04_functions_*) — refactor earlier examples into functions.

Next exercises
--------------
- Add CLI argument parsing with `argparse`.
- Refactor a script into reusable functions and add docstrings.
- Add basic tests using `unittest` or simple `assert` checks.

Contributing
------------
- Add examples using the established filename pattern.
- Include a concise header comment in any new file and add one-line description to this README.

License
-------
Educational examples — add a `LICENSE` file at the repo root if you want explicit licensing (MIT is a common choice).

Need help?
----------
If you'd like, I can:
- Add a one-line header comment to each script.
- Create a small test harness that runs only non-interactive scripts.
- Add example unit tests for a few functions.
