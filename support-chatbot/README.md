# Bazaario support chat

A customer-support chat box for a marketplace storefront: rule-based intent
matching, quick-reply buttons, order and payment cards, and a handoff to a
human specialist once the bot has failed twice.

No build step, no dependencies. One HTML file, vanilla JS. Fonts come from
Google Fonts; everything else is inline.

## Files

| File | What it is |
| --- | --- |
| `index.html` | The page. Authored for the Artifact runtime, which supplies the document skeleton. |
| `wrap.py` | Adds that skeleton so the page opens from the filesystem: `python3 wrap.py` → `standalone.html`. |

`standalone.html` is generated, so edit `index.html` and re-run the wrapper.

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
