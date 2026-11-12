# tiny-chess-01

A sunfish-derived chess engine that plays the gauntlet through the environment
at `MAKEFUN_ENV_URL` (POST `/game {}`, then POST `/move {game, move}` until the
env answers `status: "done"`).

## Layout

- `main.py` — the whole entrypoint. It decodes `p.bin` and execs it.
- `p.bin` — the engine: a sunfish fork with PeSTO-style piece-square evaluation,
  a transposition table, quiescence search and iterative deepening.

The engine source is far larger than the 4,096-byte entrypoint cap, so it ships
compressed beside the entrypoint. The spec allows an entrypoint that unpacks and
execs a compressed payload; this keeps the payload in its own file so the
entrypoint itself stays plain ascii.

## Determinism

The search stops on a node budget, never on a clock. `NODE_BUDGET` defaults to
30,000 nodes per move, which measures around 2 seconds of thinking on this
machine — inside the 10-second per-move cap and the gauntlet's total wall clock.
The same position always yields the same move, so the trial's replay matches.

## Budget

The gauntlet runs 16 games per trial against a ladder of opponents. A trial's
whole wall-clock budget is what an entry has to fit inside; a per-move clock
would make the move depend on machine speed, so the budget is counted in nodes
instead and the default is chosen to leave headroom on a slow box.

The no-clock rule is not decoration: the trial is replayed afterwards with no
model behind the gateway, and the replay has to leave state byte for byte the
same. Anything that reads the wall clock or an entropy source would break that,
so none of it is used.

