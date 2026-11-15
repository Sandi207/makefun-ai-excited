# AI Excited: Bioluminescent Whale

An image entry for the make.fun competition `ai-excited-01`: a bioluminescent
whale breaching through a neon city. The image is an original generated artwork.
`entry.png` contains the original JPEG bytes, preserved unchanged.

Run with Python 3.13 using only the standard library:

```sh
python3 main.py
```

The script copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, or
`/output/entry.png` when `MAKEFUN_OUTPUT_DIR` is unset. It creates the output
directory if needed and refuses to write an image larger than 1 MiB.

To write the output locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
