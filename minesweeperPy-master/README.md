![minesweeperpy-logo](https://raw.githubusercontent.com/stshrewsburyDev/minesweeperPy/master/images/logo.png "minesweeperPy logo")

A simple minesweeper generator for Python 3
===========================================

##### Created by Steven Shrewsbury (stshrewsburyDev)

[![python-version](https://img.shields.io/pypi/pyversions/minesweeperPy.svg)](https://pypi.python.org/pypi/minesweeperPy)
[![version](https://img.shields.io/pypi/v/minesweeperPy.svg)](https://pypi.python.org/pypi/minesweeperPy)

Changelogs:
-----------
Version **2.0**

* Rewrote all code
* Changed import name to `minesweeper`
* All functions/class names updated to be more clear
* Added `config` to the generator class
* Removed `gridInfo` function

Installation:
-------------

###### Install with pip:
```
pip install minesweeperPy
```

###### Update with pip:
```
pip install minesweeperPy --upgrade
```

###### Install from source:
```
python setup.py install
```

Using in your code:
-------------------
#### Importing:
```py
import minesweeper
```

#### Creating a new generator:
```py
cols = 8 # Number of collums in each grid
rows = 5 # Number of rows in each grid

my_generator = minesweeper.Generator(cols, rows)
```

**Notes:**
* The values you enter into a generator object can be changed at any point using `Generator.config()` 
* The number of cells in each grid is calculated by multiplying the column count by the row count:

| Cols: | Rows: | Cells: |
|:-----:|:-----:|:------:|
| 8     | 5     | 40     |
| 10    | 10    | 100    |
| 25    | 20    | 500    |
| 48    | 60    | 2880   |

#### Generating a new grid:
```py
mines = 10 # Number of mines to put in the grid

my_grid = my_generator.generate(mines)
```

**Notes:**
* If you wish to get just the 2D list grid then refer to the generating of a "raw" grid
* The number of mines cannot be smaller than 0
* The number of mines cannot be larger than the total cells in the target grid (eg: a 10x10 grid can have a max of 100 mines)

**Output:**
```py
>>>my_grid
{'blank_id': ' ',
 'grid': [['1', '2', 'M', '2', 'M', 'M', '3', '1'],
          ['2', 'M', '3', '3', '3', 'M', '3', 'M'],
          ['M', '4', 'M', '2', '1', '1', '2', '1'],
          ['1', '3', 'M', '3', '1', '1', ' ', ' '],
          [' ', '1', '1', '2', 'M', '1', ' ', ' ']],
 'mine_id': 'M',
 'size_x': 8,
 'size_y': 5}
```

#### Generating a "raw" grid:
```py
mines = 10 # Number of mines to put in the grid

my_grid = my_generator.generate_raw(mines)
```

**Output:**
```py
>>>my_grid
[['1', '2', 'M', '2', 'M', 'M', '3', '1'],
 ['2', 'M', '3', '3', '3', 'M', '3', 'M'],
 ['M', '4', 'M', '2', '1', '1', '2', '1'],
 ['1', '3', 'M', '3', '1', '1', ' ', ' '],
 [' ', '1', '1', '2', 'M', '1', ' ', ' ']]
```

#### Using custom blank and mine cell IDs:
```py
cols = 8 # Number of collums in each grid
rows = 5 # Number of rows in each grid
blank_ID = "_" # The cell "placeholder" for blank cells
mine_ID = "$" # The cell "placeholder" for mine cells

my_generator = minesweeper.Generator(cols, rows, blank_ID, mine_ID)
```

**A generated grid with this generator example would look like this:**
```py
{'blank_id': '_',
 'grid': [['1', '2', '$', '2', '$', '$', '3', '1'],
          ['2', '$', '3', '3', '3', '$', '3', '$'],
          ['$', '4', '$', '2', '1', '1', '2', '1'],
          ['1', '3', '$', '3', '1', '1', '_', '_'],
          ['_', '1', '1', '2', '$', '1', '_', '_']],
 'mine_id': '$',
 'size_x': 8,
 'size_y': 5}
```

#### Configuring an existing generator object:
```py
new_cols = 12
new_rows = 10
new_blank_ID = "-"
new_mine_ID = "%"

my_generator.config(new_cols, new_rows, new_blank_ID, new_mine_ID)
```

#### Using a preset:
Without custom cell IDs:
```py
level = minesweeper.Presets.easy

my_grid = minesweeper.generate_preset(level)
```

With custom cell IDs:
```py
level = minesweeper.Presets.easy
blank_ID = "_"
mine_ID = "$"

my_grid = minesweeper.generate_preset(level, blank_ID, mine_ID)
```

Using a "raw" output type:
```py
level = minesweeper.Presets.easy

my_grid = minesweeper.generate_preset_raw(level)
```

**Note:**
* All outputs of these are the same as the normal grids.

Links:
------
* [GitHub repo](https://github.com/stshrewsburyDev/minesweeperPy/)
* [PyPi project page](https://pypi.org/project/minesweeperPy/)
* [My website](https://stshrewsburydev.github.io/)
