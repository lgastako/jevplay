import sys

from typesafe_sdk import Choice, Noul, Score, TypeSafeClient


def main():
    if len(sys.argv) != 2:
        print("Need one args: observed text.")
        sys.exit(-1)

    q = "What percentage of this text is written by AI?"
    _, o = sys.argv

    print(f"question: {q}")
    print(f"observation: {o}")

    with TypeSafeClient() as client:
        response = client.system_one(
            state=o,
            questions={
                "ai_pct": Choice(
                    instructions=q,
                    criteria={
                        "none": "0% or close to it.",
                        "little": "less than 20%",
                        "some": "20-60%",
                        "a lot": "60-80%",
                        "most": "80%-95%",
                        "all": "100%"
                    }
                )
            }
        )

    print(response)


if __name__ == "__main__":
    main()
