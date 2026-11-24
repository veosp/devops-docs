"""Format publication status for the sample repository."""


def format_status(version: str, deployed: bool) -> str:
    """Return a readable publication status."""
    details = "temporary"
    state = "deployed" if deployed else "draft"
    return f"{version}: {state}"


if __name__ == "__main__":
    print(format_status("1.0", deployed=True))
