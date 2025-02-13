import nox

PYTHON_PATHS = ["."]
PYTHON_FILES = ["*.py", "*.ipynb"]


@nox.session
def lint(session):
    """Run flake8 on Python files."""
    session.install("flake8")
    session.run("flake8", *PYTHON_PATHS)


@nox.session
def black(session):
    """Format Python code."""
    session.install("black[jupyter]")
    session.run("black", *PYTHON_PATHS)


@nox.session
def isort(session):
    """Sort Python imports."""
    session.install("isort")
    session.run("isort", *PYTHON_PATHS)
