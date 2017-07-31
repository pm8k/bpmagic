# bpmagic

bpmagic is a library to save and load boilerplate code. With a few simple commands, you can save and load bits of frequently used code to speed up programming in iPython and Jupyter.

## Install
bpmagic is up on pip, so you can simply call:
`pip install bpmagic`

## Loading bpmagic
To load the bpmagic namespaces, you can use the load_ext magic function:
`%load_ext bpmagic`
To prevent typing this everytime, you can add this to your ipython profile startup (mine is in `/.ipython/profile_default/startup/`) and place the above command into a `*.ipy` file (you can name it whatever you want, I used `bpmagic.ipy`)



## Save

Using the `%%isave` magic function, you can write and save a chunk of code into a new bpmagic namespace. For example:

```
	%%isave data
	import pandas as pd
	import numpy as np
	import scipy as sp
``` 

This will save your current cell of code into the namespace `data`. If the namespace is already defined, you can overwrite using the -o flag:

```
	%%isave plot -o
	import matplotlib.pyplot as plt
	import seaborn as sns
	%matplotlib inline
``` 

## Load

Using the `%iload` function, you can load up 1 or more profiles at once. For example:

`%iload data plot`

This will load the boiler plate code for `data` and `plot` and replace the cell that contained `%iload` with:

```
	# data
	import pandas as pd
	import numpy as np
	import scipy as sp

	# plot
	import matplotlib.pyplot as plt
	import seaborn as sns
	%matplotlib inline

``` 

## Delete
If you pass a profile name after `%idelete`, you will remove that profile name. Example:
`%idelete data`

## Rename
Passing in the old name followed by the new profile name will change the name of a profile:
`%irename plot plotting`


## List
To get a list of current profiles, simply call `%ilist` in ipython, and it will return a list of all of your current profiles.