from pathlib import Path
from typing import Annotated

import typer
from typesafe_sdk import Noul, TypeSafeClient

DEFAULT_CUT_OFF = 0.75


def main(
    q: Annotated[str, typer.Argument(help="Semantic query to match lines against")],
    paths: Annotated[list[Path], typer.Argument(help="One or more files to search")],
    cut_off: Annotated[
        float,
        typer.Option("-c", "--cut-off", help="Minimum match score for a line to be printed"),
    ] = DEFAULT_CUT_OFF,
    show_noul: Annotated[
        bool,
        typer.Option("-s", "--show-noul", help="Prefix each matching line with its match score"),
    ] = False,
    all_results: Annotated[
        bool,
        typer.Option(
            "-a",
            "--all-results",
            help="Print every line with its score and [Y]/[N] match marker (implies --show-noul)",
        ),
    ] = False,
):
    with TypeSafeClient() as client:
        for path in paths:
            grep(client, path, cut_off, q, show_noul=show_noul, all_results=all_results)


def grep(client, path, cut_off, q, show_noul=False, all_results=False):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            n, matched = check_line(client, q, line, cut_off=cut_off)
            if all_results:
                marker = typer.style("Y", fg="green") if matched else typer.style("N", fg="red")
                typer.echo(f"{n:.4f} [{marker}]: {line}", nl=False)
            elif matched:
                if show_noul:
                    print(f"{n:.4f}: ", end="")
                print(line, end="")


def check_line(client, q, line, cut_off=DEFAULT_CUT_OFF):
    res = client.system_one(
        state={
            "context": "semantic-grep",
            "semantic_pattern": q,
            "current_line": line
        },
        questions={
            "semgrep": Noul(
                instructions="Does the 'current_line' match the semantic description from 'semantic_pattern'?"
            )
        })

    n = res.answers["semgrep"].noul
    return n, n >= cut_off


if __name__ == "__main__":
    typer.run(main)
