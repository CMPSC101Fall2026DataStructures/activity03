# Tutorial 4: The Guild Roster

In this tutorial, you'll help organize an adventurer's guild by writing
your own sets, list comprehensions, and dictionary comprehensions --
compact tools for building and filtering collections of data.

## Setup Instructions

1. Navigate to this directory:
   ```bash
   cd tutorials/tutorial_04_sets_and_comprehensions
   ```

2. Initialize the UV project (if not already done):
   ```bash
   uv init
   ```

3. Run the program:
   ```bash
   uv run roster.py
   ```

This tutorial only uses Python's standard library, so `python3 roster.py`
works too if you'd rather not use UV.

## What You'll Learn

- How to build a `set` from a list to remove duplicates
- How to combine sets with the intersection (`&`) and difference (`-`)
  operators
- How to write a list comprehension to transform every item in a list
- How to write a list comprehension with an `if` filter to keep only
  matching items
- How to write a dictionary comprehension to build a new dictionary
  from a list or another dictionary

## Tasks

There are **5 TODOs** in `roster.py`. Each one is marked with a `TODO`
comment and a `Hint` right above it:

1. `unique_attendees()` - build a `set` from a list of names
2. `guild_overlap()` - use `&` to find members in both guilds
3. `guild_a_exclusive()` - use `-` to find members in only one guild
4. `double_damage()` - write a list comprehension that transforms values
5. `name_lengths()` - write a dictionary comprehension that maps names
   to their lengths

Two functions, `strong_fighters()` and `rank_by_level()`, are already
complete -- read them for extra examples of a list comprehension with
a filter and a dictionary comprehension with a condition.

Run `uv run roster.py` and check your output against the `# Expected:`
comment next to each result.

## Expected Output

When all TODOs are complete, every printed result should match its
`# Expected:` comment in `roster.py`.

## Tips

- A set never keeps duplicate values -- `set(["a", "a", "b"])` becomes
  `{"a", "b"}`.
- Sets are unordered, so the order of items in a printed set may not
  match the order in the `# Expected:` comment -- that's OK as long as
  the same items are present.
- The general list comprehension pattern is:
  `[expression for item in iterable]`, or with a filter:
  `[expression for item in iterable if condition]`.
- The general dictionary comprehension pattern is:
  `{key_expr: value_expr for item in iterable}`.
