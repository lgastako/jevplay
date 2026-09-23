import sys
import laya
from laya import Router

QUESTIONS = {
    "happiness": {
        "type": "choice",
        "instructions": "How satisfied is the user?",
        "criteria": {
            "very": "Very happy.",
            "somewhat": "Somewhat happy.",
            "not_very": "Not very happy.",
            "not": "Not at all happy."
        }
    }
}

def main():
    if len(sys.argv) != 2:
        print("Need either 'loop' or an observation as a single arg.")
        sys.exit(-1)

    _, o = sys.argv
    router = Router(preload=True)

    if o == "loop":
        print("Loop mode.")
        loop(router)
    else:
        print("One-shot mode.")
        once(router, o)


def loop(router):
    while True:
        print("Enter observation >> ", end="")
        o = input()
        once(router, o)


def once(router, o):
    state = {
        "user_input": o
    }
    res = router.predict(state, QUESTIONS)

    # Example response:
    {'model': 'laya-rl-agent', 'answers': {'happiness': {'type': 'choice', 'choice': 'not', 'probabilities': {'very': 0.2869, 'somewhat': 0.1618, 'not_very': 0.1927, 'not': 0.3586}, 'confidence': 0.0348, 'action': {'act_probability': 1.0}}}, 'usage': {'input_tokens': 54, 'output_tokens': 0}, 'routing': {'model': 'english', 'repo': 'convaiinnovations/laya', 'reason': 'English Latin text', 'detection': {'script': 'latin', 'script_profile': {'latin': 1.0}, 'language': None, 'is_english': True, 'language_undecided': True, 'diacritic_rate': 0.0, 'non_latin_fraction': 0.0}, 'workflow': None}}
    print(res)



if __name__ == "__main__":
    main()
