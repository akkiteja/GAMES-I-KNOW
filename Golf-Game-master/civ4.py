def areaExp(self, pCity):
    	
	### Set up counters (could do with a dictionary, but this way is simpler)
	iForest = 0
	iJungle = 0
	iHill = 0
	iCoast = 0
			
	iPlotX = pCity.getX()
	iPlotY = pCity.getY()	
		for iXLoop in range(iPlotX - 2, iPlotX + 3):
		for iYLoop in range(iPlotY - 2, iPlotY + 3):
			### Checks for tiles not in city radius
			if ((iXLoop != 2) and (iYLoop != 2)) or \
			   ((iXLoop != -2) and (iYLoop != 2)) or \
			   ((iXLoop != 2) and (iYLoop != -2)) or \
			   ((iXLoop != -2) and (iYLoop != -2)):
			
				lPlot = CyMap().plot(iXLoop, iYLoop)
			
				if lPlot.getTerrainType() == gc.getInfoTypeForString("TERRAIN_HILL"):
					iHill += 1
				if lPlot.getTerrainType() == gc.getInfoTypeForString("TERRAIN_COAST"):
					iCoast += 1
				if lPlot.getFeatureType() == gc.getInfoTypeForString("FEATURE_FOREST"):
					iForest += 1
				if lPlot.getFeatureType() == gc.getInfoTypeForString("FEATURE_JUNGLE"):
					iJungle += 1