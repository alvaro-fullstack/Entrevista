import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'ultron_hack', 'src'))

from ultron.app import run_problem_1, run_problem_2, run_problem_3

if __name__ == "__main__":
    run_problem_1()
    run_problem_2()
    run_problem_3()
