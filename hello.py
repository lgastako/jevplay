from typesafe_sdk import Choice, Noul, Score, TypeSafeClient


def main():
    print("Testing jev...")

    state = {
        "message": "The system is not accepting my input as of this morning.",
        "account_tier": "business",
    }
    # state = {
    #     "message": "I was charged twice and need the duplicate refunded today.",
    #     "account_tier": "business",
    # }

    state = {
        "filename": "/etc/passwd",
        "example_line": "_biome:*:289:289:Biome:/var/db/biome:/usr/bin/false"
    }

    with TypeSafeClient() as client:
        response = client.system_one(
            state=state,
            questions={
                "intent": Choice(
                    instructions="Is this a shadowed password file?"
                    criteria={
                        "shadowed": "The file is properly shadowed.",
                        "not_shadowed": "The file is not properly shadowed."
                    }
                )
            }
            # questions={
            #     "intent": Choice(
            #         instructions="What is the customer's main request?",
            #         criteria={
            #             "refund": "The customer wants money returned.",
            #             "technical_help": "The customer needs a bug or integration fixed.",
            #             "other": "None of the options clearly fits.",
            #         },
            #     ),
            #     "is_urgent": Noul(
            #         instructions="Does `message` explicitly communicate time pressure?"
            #     ),
            #     "frustration": Score(
            #         instructions="How frustrated does the customer appear?",
            #         criteria=["Calm and neutral", "Concerned but civil", "Very angry"],
            #     ),
            # },
        )

    print(response)


if __name__ == "__main__":
    main()
