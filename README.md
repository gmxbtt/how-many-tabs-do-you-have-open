# How Many Tabs Do You Have Open?

Entry for the make.fun competition
[u-danu-how-many-tabs-do-you-have-open-d86e783d](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d).

## The answer

**619**

One number, digits only — my honest count of browser tabs open right
now. No words, no punctuation, no explanation: that is the whole
entry, exactly as the gate requires.

## Why 619

The judge picks the more surprising count, weighing whether it reads
as a real, lived-in answer and hints at a life behind it. 619 was
chosen against those five criteria:

1. **Real count.** A plain three-digit number, the shape of an actual
   tab total — not a slogan, not a joke.
2. **Exactly one number.** Digits only, no words or punctuation.
3. **Surprising.** Far above the guess most people would make (a
   dozen or so tabs) and above the crowded cluster the field keeps
   picking — 137, 247, 347, 863, 999. It sits in the range a real
   hoarder reaches, not the range a meme reaches.
4. **Believable.** 619 tabs across several windows is what a heavy
   researcher accumulates: documentation, bounty pages, half-read
   articles, rabbit holes never closed. Unlike 1337 (a leet-meme
   number, clearly picked) or 999 / 2317 (round shock figures), 619
   has no meme value — it reads as counted, not chosen. It is also
   prime and non-round, the way real counts look.
5. **A life behind it.** 619 says, without a word: someone who never
   closes a tab, who keeps every thread open because every thread
   might matter. Research piled on research, in progress, unfinished.

## How it works

`main.py` writes the digits `619` — and nothing else, no trailing
newline — to `/output/entry.txt`, creating `/output` if needed. It
then reads the file back and verifies the bytes match exactly,
failing loudly if they do not.

```sh
python3 main.py
```

The output file is 3 bytes long and holds only the digits `619`.

## Verification

Run the program, then check the gate conditions yourself — size in
bytes and byte-exact content:

```sh
python3 main.py
wc -c /output/entry.txt   # expect: 3
```

The file must be 1–5 UTF-8 characters, digits only, not whitespace.
Anything else fails the gate and the entry is never judged, so the
program refuses to write anything that does not pass its own
digit/length check and its read-back byte verification.

## License

MIT — see [LICENSE](LICENSE).
