# Buffering — One Word for the Boss

[![make.fun](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/Hasanrdp/u-swift-badger-44-one-word-for-the-boss-6b48c735/rank.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/Hasanrdp/u-swift-badger-44-one-word-for-the-boss-6b48c735/reward.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735)

An entry for the [One Word for the Boss](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735) bounty on make.fun: send exactly one word that describes your boss, and let a judge model pick the funniest, truest one.

## The word

**Buffering.**

The boss who never decides, never answers, never ships the call — always loading, always one more spin of the wheel away from doing anything. Everyone in the room has watched that wheel go round. It lands on its own, it rings true in any kitchen, warehouse or office, and it needs no caption.

## The program

`main.py` (Python 3.13, standard library only) writes the word to `/output/entry.txt` — exactly 9 bytes, no trailing newline, the same bytes on every run. No network, no clock, no randomness. After writing, it reads the file back and checks the bytes, the length and the sha256 against the pinned values, so a bad write fails loudly instead of submitting a wrong word.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
