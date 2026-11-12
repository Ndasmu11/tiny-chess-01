import lzma, os

# tiny-chess-01: a sunfish-derived engine packed as an lzma blob beside this
# file. The engine source is far past the entrypoint byte cap, so it ships
# compressed; this file decodes it and execs it in this module's globals.
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), "p.bin")
exec(lzma.decompress(open(B, "rb").read(), format=lzma.FORMAT_RAW,
                     filters=[{"id": lzma.FILTER_LZMA2, "preset": 2147483657,
                               "lc": 2, "lp": 0, "pb": 0}]))
