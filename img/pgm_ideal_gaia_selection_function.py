"""
Idealized Gaia selection function as probabilistic graphical model.

Anthony Brown Feb 2020
"""

from matplotlib import rc
rc("font", family="serif", size=12)
rc("text", usetex=True)

import daft

pgm = daft.PGM([5,5], origin=[0, 0], aspect=1.75, node_unit=1.5, grid_unit=2.5)

pgm.add_node(daft.Node("Gsource", "$G_\mathrm{source}$", 3, 4.5))
pgm.add_node(daft.Node("afxpobs", "AF/XP", 3, 3.5))
pgm.add_node(daft.Node("afxprvsobs", "AF/XP/RVS", 3, 2.5))
pgm.add_node(daft.Node("GRVSsource", "$G_\mathrm{RVS,source}$", 1, 2.5))
pgm.add_node(daft.Node("scanlaw", "Commanded scan law", 1, 4.5, fixed=True, aspect=1))
pgm.add_node(daft.Node("Glim", "$G_\mathrm{lim}$", 1, 3.5, fixed=True, aspect=1))
pgm.add_node(daft.Node("GRVSlim", "$G_\mathrm{RVS,lim}$", 1, 1.5, fixed=True, aspect=1, offset=(0,-24)))

pgm.add_edge("Gsource", "afxpobs")
pgm.add_edge("afxpobs", "afxprvsobs")
pgm.add_edge("GRVSsource", "afxprvsobs")
pgm.add_edge("scanlaw", "afxpobs")
pgm.add_edge("Glim", "afxpobs")
pgm.add_edge("GRVSlim", "afxprvsobs")

pgm.render()
pgm.figure.savefig("pgm_ideal_gsf.pdf")
pgm.figure.savefig("pgm_ideal_gsf.png", dpi=150)
