import sys

import laya

# from laya import Router
from lclient import remote

DEFAULT_CUT_OFF = 0.75


def main():
    if len(sys.argv) < 3:
        print("Need a semantic query and one or more paths to target files")
        sys.exit(-1)

    _, q, *paths = sys.argv
    router = None

    for path in paths:
        grep(router, path, cut_off, q)


def grep(router, path, cut_off, q):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if check_line(router, q, line, cut_off=cut_off):
                print(line, end="")


def check_line(router, q, line, cut_off=CUT_OFF):
    # res = router.predict(
    res = remote(
        {
            "context": "semantic-grep",
            "semantic_pattern": q,
            "current_line": line
        },
        {
            "semgrep": {
                "type": "noul",
                "instructions": "Does the current_line match the semantic_pattern in a semantic grep sense?"
            }
        })
    return res["answers"]["semgrep"]["noul"] >= cut_off


if __name__ == "__main__":
    main()
