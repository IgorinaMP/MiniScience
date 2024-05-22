import gmsh
import sys

gmsh.initialize()

gmsh.model.add("ex1")

lc = 1e-2
gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(0, 0, 1, lc, 2)
gmsh.model.geo.addPoint(0, 1, 0, lc, 3)
gmsh.model.geo.addPoint(1, 0, 0, lc, 4)
gmsh.model.geo.addPoint(0, 1, 1, lc, 5)
gmsh.model.geo.addPoint(1, 1, 0, lc, 6)
gmsh.model.geo.addPoint(1, 0, 1, lc, 7)
gmsh.model.geo.addPoint(1, 1, 1, lc, 8)

gmsh.model.geo.addLine(1, 2, 1)
gmsh.model.geo.addLine(1, 3, 2)
gmsh.model.geo.addLine(1, 4, 3)
gmsh.model.geo.addLine(2, 5, 4)
gmsh.model.geo.addLine(2, 7, 5)
gmsh.model.geo.addLine(3, 5, 6)
gmsh.model.geo.addLine(3, 6, 7)
gmsh.model.geo.addLine(4, 6, 8)
gmsh.model.geo.addLine(4, 7, 9)
gmsh.model.geo.addLine(8, 5, 10)
gmsh.model.geo.addLine(8, 6, 11)
gmsh.model.geo.addLine(8, 7, 12)

gmsh.model.geo.addCurveLoop([5, -12, 10, -4], 1)
gmsh.model.geo.addPlaneSurface([1], 1)

gmsh.model.geo.addCurveLoop([8, -11, 12, -9], 2)
gmsh.model.geo.addPlaneSurface([2], 2)

gmsh.model.geo.addCurveLoop([11, -7, 6, -10], 3)
gmsh.model.geo.addPlaneSurface([3], 3)

gmsh.model.geo.addCurveLoop([1, 4, -6, -2], 4)
gmsh.model.geo.addPlaneSurface([4], 4)

gmsh.model.geo.addCurveLoop([3, 9, -5, -1], 5)
gmsh.model.geo.addPlaneSurface([5], 5)

gmsh.model.geo.addCurveLoop([-8, -3, 2, 7], 6)
gmsh.model.geo.addPlaneSurface([6], 6)

l = gmsh.model.geo.addSurfaceLoop([i + 1 for i in range(6)])
gmsh.model.geo.addVolume([l])

gmsh.model.geo.synchronize()

gmsh.model.mesh.generate(3)


gmsh.write("ex1.msh")
gmsh.write("ex1.geo_unrolled")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()


gmsh.finalize()
