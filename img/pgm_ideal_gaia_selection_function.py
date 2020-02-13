"""
Idealized Gaia selection function as probabilistic graphical model.

Anthony Brown Feb 2020
"""

from matplotlib import rc
rc("font", family="serif", size=12)
rc("text", usetex=False)

import daft

pgm = daft.PGM([5,5], origin=[0, 0], node_unit=1.5, grid_unit=2.5)

pgm.add_node(daft.Node("Gsource", "$G_\mathrm{source}$", 3, 4.5))
pgm.add_node(daft.Node("afxpobs", "AF/XP", 3, 3.5, aspect=1.5))
pgm.add_node(daft.Node("afxprvsobs", "AF/XP/RVS", 3, 2.0, aspect=1.75))
pgm.add_node(daft.Node("GRVSsource", "$G_\mathrm{RVS,source}$", 1, 2.0, aspect=1.75))
pgm.add_node(daft.Node("scanlaw", "Commanded\nscan law", 1, 4.5, fixed=True, aspect=1))
pgm.add_node(daft.Node("Glim", "$G_\mathrm{lim}$", 1, 3.5, fixed=True, aspect=1, offset=(0,6)))
pgm.add_node(daft.Node("GRVSlim", "$G_\mathrm{RVS,lim}$", 1, 1.0, fixed=True, aspect=1, offset=(0,-24)))

pgm.add_edge("Gsource", "afxpobs")
pgm.add_edge("afxpobs", "afxprvsobs")
pgm.add_edge("GRVSsource", "afxprvsobs")
pgm.add_edge("scanlaw", "afxpobs")
pgm.add_edge("Glim", "afxpobs")
pgm.add_edge("GRVSlim", "afxprvsobs")

pgm.add_plate([2.3, 3, 2, 1], label="Astrometry/\nphotometry sample", position="bottom right", shift=0, fontsize=8)
pgm.add_plate([2.3, 1.5, 2, 1], label="RVS sample", position="bottom right", shift=0, fontsize=8)

pgm.render()
pgm.figure.savefig("pgm_ideal_gsf.pdf")
pgm.figure.savefig("pgm_ideal_gsf.png", dpi=150)
