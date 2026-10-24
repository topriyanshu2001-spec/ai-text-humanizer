# Saathi — Bazaario support chat

Saathi is the support bot on a marketplace storefront: rule-based intent
matching, quick-reply buttons, order and payment cards, and a handoff to a
human specialist once it has failed twice. The name sits in the register
Indian marketplaces use for their assistants — short, spoken, vernacular
(*saathi*, companion) — rather than a generic "Support Assistant" label.
Rename it in one place, the `BOT` constant.

No build step, no dependencies. One HTML file, vanilla JS. Fonts come from
Google Fonts; everything else is inline.

## Files

| File | What it is |
| --- | --- |
| `index.html` | The source page. Authored for the Artifact runtime, which supplies the document skeleton. |
| `saathi-support-chat.html` | The shareable build: one self-contained file. Generated — don't hand-edit it. |
| `wrap.py` | Builds the shareable file from `index.html`: `python3 wrap.py`. |

Edit `index.html`, then re-run the wrapper.

## Sharing it

The build is one file with everything inside it — markup, styles, script, and
the three typefaces as base64. It makes no network calls at all, so it renders
identically on a machine that has never opened it before, connected or not.

**As a file.** Send it over WhatsApp, Slack or email as a document, or carry it
on a USB stick. The recipient saves it and double-clicks; it opens in whatever
browser they have. WhatsApp won't preview an HTML attachment — it downloads,
which is exactly what you want when the target is a laptop.

**As a link.** Put the file on any static host (GitHub Pages, a Netlify drop,
S3) and share the URL. Links travel better than attachments in chat, since
phones open them without a download step.

`python3 wrap.py --no-fonts` builds a 40 KB version that pulls the typefaces
from Google Fonts instead — smaller, but it needs a connection to look right.

## The scenario it was built around

Rahul orders earbuds. The ₹1,799 leaves his bank account, no confirmation
arrives, and he opens the chat:

> My money has been deducted, but I have not received my order confirmation.

The bot answers with the line that case warrants, then two buttons —
**Check Order** and **Payment Help** — so he picks instead of typing another
paragraph. Check Order renders the order with its status timeline stalled at
*Payment confirmation*. Payment Help shows the UPI reference, explains the
24-hour bank window and the automatic 3–5 day reversal, and opens a trace
reference against the amount.

Every substantive answer ends with **That solved it** / **Still stuck**.

## Escalation

Two unproductive attempts is the ceiling. A fallback (nothing matched) and a
*Still stuck* each count as one; at two the bot stops guessing and offers a
specialist. The header also carries a person icon that jumps straight there,
because a customer who wants a human should never have to earn one.

The handoff raises a ticket, shows a queue position, and the specialist
arrives already holding the transcript — the amount, the bank reference and
the order ID — so nothing has to be repeated.

Not everyone wants to keep typing, though. The care number sits in the panel
footer at all times, appears with a copy button whenever the bot gives up or
the chat closes, and comes back directly if someone just asks for it
("customer care number", "helpline", "toll free"). `CARE` holds the number,
hours and address. The one in the demo is a placeholder that dials nothing —
swap it before this goes anywhere real.

Copying uses the clipboard API, which embedded browser views often refuse. On
a refusal it selects the number and says to press Ctrl/⌘C rather than silently
doing nothing.

## Adding an intent

`INTENTS` is an ordered list of `{id, keys}`, where `keys` are
`[substring, weight]` pairs matched against space-padded, punctuation-stripped
text. Scores sum; anything below 2 falls through to the fallback, and ties go
to whichever intent sits earlier in the list.

```js
{id:'warranty', keys:[['warranty',3],['guarantee',2],['service centre',3]]}
```

Then add a matching entry to `FLOWS`, returning the lines to say and the chips
to offer:

```js
warranty: () => ({
  lines:[`Z40 earbuds carry a one-year warranty from Acoustic Labs.`],
  chips:[chip('Find a service centre','address'), ...RESOLVE]
})
```

Hinglish phrasings (`paisa kat gaya`, `kab aayega`, `kahan hai`) are matched
alongside the English ones, since that is how these messages actually arrive.

## Wiring it to a real backend

Three seams, in the order you would replace them:

1. `ORDER` / `PAST_ORDER` — swap the literals for your orders API response.
2. `detect()` — keep it as the cheap first pass, or forward the text to an
   NLU service and keep these rules as the offline fallback.
3. `handoff()` — replace the simulated ticket and specialist with your live
   chat provider's session handoff, passing the transcript along.

The payment copy encodes real policy (source-account refunds, the 3–5 day
window, no cancellation fee before packing). Check it against yours before
shipping anything customer-facing.
