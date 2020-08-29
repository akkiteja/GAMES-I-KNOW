import minesweeper
from pprint import pprint

gen = minesweeper.Generator(5, 7)

print("%s - %s\nCreated by: %s" % (minesweeper.__title__, minesweeper.__version__, minesweeper.__author__))
print("-" * 50)
print("Using Generator.generate():")
pprint(gen.generate(14))
print("-" * 50)
print("Using Generator.generate_raw():")
pprint(gen.generate_raw(14))
print("-" * 50)
print("With custom mine/blank IDs:")
gen.config(blank_id="-", mine_id="F")
pprint(gen.generate(14))
print("-" * 50)
print("Using a preset:")
pprint(minesweeper.preset(minesweeper.Presets.easy))
print("-" * 50)
print("Using a raw preset:")
pprint(minesweeper.preset_raw(minesweeper.Presets.easy))
