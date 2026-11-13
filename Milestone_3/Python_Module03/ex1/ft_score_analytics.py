#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        return
    else:
        scores = []
        i = 1
        while i < len(sys.argv):
            try:
                num = int(sys.argv[i])
                scores.append(num)

            except ValueError:
                print(f"Invalid parameter: '{sys.argv[i]}'")
            i += 1
    if not scores:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {scores}")
        add = sum(scores)
        s_max = max(scores)
        s_min = min(scores)
        print(f"Total players: {len(scores)}")
        print(f"Total score: {add}")
        print(f"Average score: {round(add / len(scores), 1)}")
        print(f"High score: {s_max}")
        print(f"Low score: {s_min}")
        print(f"Score range: {s_max - s_min}")


if __name__ == "__main__":
    main()
