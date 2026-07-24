import re

# Matches lines like "UPF\tUser Plane Function" or "MB-UPF\tMulticast/Broadcast
# User Plane Function" -- the standard glossary/abbreviations format used in
# 3GPP spec documents (and similar telecom docs). One mtch per line.
_GLOSSARY_PATTERN = re.compile(
    r'^([A-Z][A-Z0-9\-/ ]{0,12})\t([A-Z][\w\s\-/(),.]{2,100})$'
)


def extract_glossary_entries(text):
    """
    Scan raw document text line-by-line for "ABBR<TAB>Full Name" style
    glossary entries and return a deduplicated list of (abbr, full_name)
    tuples.
    """
    seen = set()
    entries = []

    for line in text.splitlines():
        match = _GLOSSARY_PATTERN.match(line.strip())

        if not match:
            continue

        abbr = match.group(1).strip()
        full_name = match.group(2).strip()

        key = (abbr, full_name)

        if key in seen:
            continue

        seen.add(key)
        entries.append((abbr, full_name))

    return entries


def glossary_entries_to_chunks(entries):
    """
    Convert (abbr, full_name) tuples into short, natural-language chunks
    that embed well against questions like "What is AMF?".
    """
    return [
        f"{abbr} stands for {full_name}."
        for abbr, full_name in entries
    ]
