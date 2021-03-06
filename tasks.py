from invoke import Context, task


@task
def run(c, backend="tui"):
    # type: (Context, str) -> None
    c.run(f"python py_calc_rpn/entrypoint/{backend}/main.py", pty=True)


@task(aliases=["fmt"])
def format(c, all_files=False):
    # type: (Context, bool) -> None
    precommit_options = []

    if all_files:
        precommit_options.append("--all-files")

    hooks = [
        "end-of-file-fixer",
        "trailing-whitespace",
        "pyupgrade",
        "add-trailing-comma",
        "yesqa",
        "isort",
        "black",
    ]
    for hook in hooks:
        cmd = " ".join(["pre-commit", "run", *precommit_options, hook])
        c.run(cmd, pty=True)


@task
def lint(c, all_files=False):
    # type: (Context, bool) -> None
    precommit_options = []

    if all_files:
        precommit_options.append("--all-files")

    hooks = [
        "check-added-large-files",
        "check-json",
        "check-merge-conflict",
        "check-toml",
        "check-yaml",
        "debug-statements",
        "detect-private-key",
        "name-tests-test",
        "flake8",
        "mypy",
        "vulture",
        "bandit",
    ]
    for hook in hooks:
        cmd = " ".join(["pre-commit", "run", *precommit_options, hook])
        c.run(cmd, pty=True)


@task
def check(c, all_files=False):
    # type: (Context, bool) -> None
    precommit_options = []

    if all_files:
        precommit_options.append("--all-files")

    cmd = " ".join(["pre-commit", "run", *precommit_options])
    c.run(cmd, pty=True)


@task
def tests(c, quiet=False):
    # type: (Context, bool) -> None
    pytest_options: list[str] = []

    if quiet:
        pytest_options.append("-q")

    cmd = " ".join(
        [
            "coverage",
            "run",
            "-m",
            "pytest",
            *pytest_options,
        ],
    )
    c.run(cmd, pty=True)


@task
def coverage(c):
    # type: (Context) -> None
    c.run("coverage report", pty=True)
