# Contributing

PRs and issues are welcome. Suggest a paper, fix a broken link, add your lab to the map, or flip a `code = "soon"` to a real link once the code is out.

## Scope

- **In:** humanoid robots, real or simulated robot models (G1, T1, E1, OP3, NAO, …), playing **table tennis, tennis, badminton, soccer or basketball**, or practicing one of the sport's skills: striking, kicking, dribbling, shooting, goalkeeping, rallying.
- **Only official sources:** the original paper, and the authors' own project page and repo. Research-group demos that don't have a paper yet count too, if the authors announced them themselves.
- **Out:** third-party reimplementations and "inspired by" projects; company promo demos with no paper or code; non-humanoid robots (arms, quadrupeds); physics-based character animation; generic locomotion or manipulation papers where the sport is only one example task; benchmarks, competitions and surveys.

## How the list is built

The paper tables and the map in `README.md` are generated. Don't edit anything between `<!-- gen:… -->` and `<!-- /gen -->` by hand. Instead:

1. Add the paper to [`data/papers.toml`](data/papers.toml):

   ```toml
   [[paper]]
   date = "2025.08"                 # YYYY.MM of the first public version (usually arXiv v1)
   title = "HITTER: A HumanoId Table TEnnis Robot via Hierarchical Planning and Learning"
   sport = "table-tennis"           # table-tennis | tennis | badminton | soccer | basketball, or a list
   venue = "ICRA 2026"              # conference or journal once accepted, otherwise "arXiv"
   robot = "Unitree G1"
   real = true                      # real-robot experiments?
   paper = "https://arxiv.org/abs/2508.21043"
   project = "https://humanoid-table-tennis.github.io/"   # optional
   code = "https://github.com/..."  # optional; "soon" for placeholder repos
   lab = "berkeley-sastry"          # the LAST author's group, an id from data/labs.toml
   ```

   For a demo without a paper, set `status = "announced"`, point `paper` at the authors' announcement (post, video or project page), and leave out `venue`.

2. If the group is new, add it to [`data/labs.toml`](data/labs.toml). Each paper has exactly one group: the last author's, with the last author as `pi`. If the institution is new too, add it as well: each institution is one map marker, placed at its campus coordinates. Leave out `lab` only for anonymous or individual work.

3. Regenerate the README and commit both files:

   ```sh
   uv run scripts/build.py      # or: python3.11+ scripts/build.py
   ```

CI runs `scripts/build.py --check` and fails if the README is out of date or the data is inconsistent (unknown lab ids, bad dates, and so on).
