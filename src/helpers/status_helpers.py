# Path: helpers/status_helpers.py

STATUS_COLORS: dict[bool, str] = {
    True: "lightgreen",
    False: "lightyellow",
}


def status_color(completed: bool) -> str:
    return STATUS_COLORS.get(completed, "lightgrey")
