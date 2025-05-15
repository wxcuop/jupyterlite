from invoke import task

@task
def build(c):
    """Build the project using python's build module"""
    c.run("python -m build")

@task
def install_dev(c):
    """Install testing dependencies"""
    c.run("pip install .[dev]")

@task
def test(c):
    """Run tests with pytest"""
    c.run("pytest")

@task(pre=[build, install_dev])
def build_and_test(c):
    """Build the project and then run tests"""
    c.run("pytest")