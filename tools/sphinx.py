import subprocess
import logging


def main():
    cmd = [
        ["sphinx-apidoc", "-f", "-o", "docs/api", "src/"],
        ["sphinx-build", "-M", "html", "docs/", "public/"],
        ["touch", "public/.nojekyll"]
    ]

    for c in cmd:
        try:
            ret = subprocess.run(c)
            logging.info(ret.stdout)
        except subprocess.TimeoutExpired as e:
            logging.error(ret.stderr)
            logging.error(f'timeout = {e.timeout}')
        except subprocess.CalledProcessError as e:
            logging.error(ret.stderr)
            logging.error(f'returncode = {e.returncode}')
            logging.error(f'output = {e.output}')
