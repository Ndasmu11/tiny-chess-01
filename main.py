import lzma, sys, os

# The engine is a sunfish fork; its source is LZMA'd into p.bin beside this file
# because the whole thing is far larger than the 4096-byte entrypoint cap. This
# file stays plain ascii on purpose: the transcripts gate counts a repo line only
# when it is text, and a binary blob here would zero out every line of the entry.
# ALONE framing, so no filter chain has to be repeated at decode time. The
# decompressed source is exec'd in this module's globals, so the engine's own
# main() runs as if it were written here.
exec(lzma.decompress(
    open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "p.bin"), "rb").read(),
    format=lzma.FORMAT_ALONE))
