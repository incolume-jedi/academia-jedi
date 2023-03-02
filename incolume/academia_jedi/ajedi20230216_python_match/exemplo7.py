"""Soft Keywords."""
import re


def check(support_ticket: str):

    match = re.match(r"Support case no\.: (\d+) is (opened|closed)\.", support_ticket)
    match = match.groups() if match else None
    match match:
        case case, "closed":
            print(f"Case {case} is done.")
        case case, "opened":
            print(f"Case {case} is still in progress.")
        case _:
            print("Case has unknown status")


def run():
    support_tickets = (
        "Support case no.: 152 is closed.",
        "Support case no.: 153 is opened.",
        "Support case no.: 151 is closed.",
    )
    for ticket in support_tickets:
        check(ticket)


if __name__ == "__main__":  # pragma: no cover
    run()
