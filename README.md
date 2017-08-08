# code_jam

## Design Notes
* `main.py`, `config.py`, and `base_problem.py` are copied in each `./problems/year/round` folder, as they might change from round to round. This also makes it more straightforward to submit the full problem code, without needing to consider folder structure.
* `.in` and `.out` files are also saved in a flat file structure for ease of upload.

## Instructions
To solve new code jam problems:

* Create folder under `problems` named `y{year}/r{round name}`, e.g. `problems/y2017/r1A`
* Copy in `base_problem.py`, `config.py`, and `main.py` from prior round.
* Save `.in` files to this folder, e.g. `A-large.in`, `A-small.in`.
* Also create a `A-sample.in` file based on the problem sample input for initial testing.
* Set round folder as Sources Root.
* Run this round's `main.py` (set as execution script).
* Create classes for each problem in the round, e.g.:
  * `a.py`

        from base_problem import BaseProblem

        class Problem(BaseProblem):
            '''
            Problem description
            '''

            def some_problem_method(self):
                pass

