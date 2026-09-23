import sys

from typesafe_sdk import Choice, Noul, Score, TypeSafeClient


def noul_to_answer(n):
    if 0.0 == n:
        return "Nope"
    if 0.2 >= n:
        return "Probably not."
    if 1.0 == n:
        return "Yep"
    if 0.8 <= n:
        return "Probably."
    return "Hard to say.  Better check it yourself."


def main():
    print("Testing jev...")

    if len(sys.argv) != 3:
        print("Need two args: question and input.")
        sys.exit(-1)

    _, q, o = sys.argv

    print(f"question: {q}")
    print(f"observation: {o}")

    with TypeSafeClient() as client:
        response = client.system_one(
            state=o,
            questions={
                "shadowedness": Noul(instructions=q)
            }
        )

    n = response.answers["shadowedness"].noul
    print("Answer:", noul_to_answer(n), f"({n})")


if __name__ == "__main__":
    main()
