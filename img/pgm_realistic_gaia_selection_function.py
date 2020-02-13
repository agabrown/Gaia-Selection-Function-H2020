"""
Realistic Gaia selection function as probabilistic graphical model.

Anthony Brown Feb 2020
"""

from matplotlib import rc
rc("font", family="serif", size=12)
rc("text", usetex=False)

import daft

pgm = daft.PGM([10,10], origin=[0, 0], node_unit=1.5, grid_unit=2.5)

pgm.add_node(daft.Node("Gsource", "$G_\mathrm{source}$", 3, 9))
pgm.add_node(daft.Node("scanlaw", "Actual\nscan law", 2, 9, fixed=True, aspect=1))
pgm.add_node(daft.Node("events", "S/C+Payload\noutages", 1, 9, fixed=True, aspect=1))
pgm.add_node(daft.Node("Gvpu", "$G_\mathrm{VPU}$", 3, 8))
pgm.add_node(daft.Node("fovhist", "FoV\nhistory", 1.5, 8, aspect=1.5))
pgm.add_node(daft.Node("detection", "detection", 3, 7, aspect=2.25))
pgm.add_node(daft.Node("confirmation", "confirmation", 3, 6, aspect=2.25))
pgm.add_node(daft.Node("Gvpulim", "$G_\mathrm{VPU,lim}$", 1, 7, fixed=True, aspect=1, offset=(0,6)))

pgm.add_edge("Gsource", "Gvpu")
pgm.add_edge("Gvpu", "detection")
pgm.add_edge("Gvpulim", "detection")
pgm.add_edge("fovhist", "detection")
pgm.add_edge("events", "fovhist")
pgm.add_edge("scanlaw", "fovhist")
pgm.add_edge("detection", "confirmation")

pgm.render()
pgm.figure.savefig("pgm_realistic_gsf.pdf")
pgm.figure.savefig("pgm_realistic_gsf.png", dpi=150)
