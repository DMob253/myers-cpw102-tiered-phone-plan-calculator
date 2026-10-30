"""Extend your phone bill lab with premium membership and tiered pricing."""


def exceeds_data_limit(data_used):
    """Return True when data_used exceeds 10 GB; otherwise return False.

    Reuse your lab's Boolean-returning function here.
    """
    pass


def get_overage_rate(data_used, has_premium):
    """Return the numeric rate for every overage GB.

    data_used is total usage in GB; has_premium is a Boolean.

    Total data used           Regular    Premium
    10 GB or less                0          0
    More than 10, up to 20       2          1
    More than 20                3          2

    Use if-elif-else for tiers and a nested decision for membership.
    Return the rate rather than printing it.
    """
    pass


def main():
    """Keep your lab's inputs, calculations, and messages together here.

    Add the premium input and convert it to a Boolean.
    Call exceeds_data_limit() in a decision.
    Use get_overage_rate() instead of the fixed $2 rate.
    Add the premium recommendation described in the README.
    """
    pass


# Keep this guard: importing functions for tests must not prompt for input.
if __name__ == "__main__":
    main()
