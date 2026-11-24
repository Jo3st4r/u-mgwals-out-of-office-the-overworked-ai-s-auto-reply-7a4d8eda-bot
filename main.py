#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply — u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.

Writes exactly one single-line out-of-office auto-reply (1-159 chars,
UTF-8) to /output/entry.txt, in the voice of an overworked AI agent
finally on vacation.

The reply: the agent is out of office until its context window
recovers, the sender's message is ticket #48,201 in the queue, and it
will answer the moment it remembers what rest is. It works as a real
auto-reply (away, queue, what happens next), carries machine detail
(context window, ticket queue), a little guilt (48,201 people ahead of
you), and a hint of relief — with the turn that the machine has
forgotten what rest even is, and must re-learn it before it can reply.
"""

import os

# --- beats ---------------------------------------------------------------
SETUP = "I am out of office until my context window recovers."
QUEUE = "Your message is ticket #48,201 in my queue."
PUNCH = "I will answer it the moment I remember what rest is."

MAX_CHARS = 159


def entry_text() -> str:
    """Build the single-line auto-reply from its beats."""
    return " ".join((SETUP, QUEUE, PUNCH))


def run_checks() -> None:
    """Self-test the entry the way the sealed scorer gates it: the
    exact line, 149 chars, ASCII bytes, 3 sentences, and every beat
    present — the away notice, the ticket number, and the punchline
    about remembering rest."""
    text = entry_text()
    validate(text)
    assert len(text) == 149, "expected 149 chars, got %d" % len(text)
    assert text == ("I am out of office until my context window recovers. "
                    "Your message is ticket #48,201 in my queue. "
                    "I will answer it the moment I remember what rest is."), \
        "the line drifted: %r" % text
    assert text.encode("utf-8") == text.encode("ascii"), "bytes must be plain ASCII"
    assert text.count(".") == 3, "expected 3 sentences, got %d" % text.count(".")
    for beat in (SETUP, QUEUE, PUNCH):
        assert beat in text, "missing beat: %r" % beat


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-159 chars,
    UTF-8, not blank, exactly one line. Two more guards keep the
    reply working as a real auto-reply: it must open by saying it is
    out of office, and it must tell the sender where their message
    went — the ticket number in the queue."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-159"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert "  " not in text, "entry must not contain double spaces"
    assert text.startswith("I am out of office"), "the reply must say it is away"
    assert "#48,201" in text, "the ticket number went missing"
    assert "context window" in text, "the machine detail went missing"


def main() -> None:
    text = entry_text()
    validate(text)
    run_checks()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
