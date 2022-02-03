# -*- coding: utf-8 -*-
"""
ZoomLevel

 A QGIS plugin to display the zoom level of the map in the status bar.
                              -------------------
        begin                : 2020-01-23
        copyright            : (C) 2020 by Keith Jenkins
        email                : kgjenkins@gmail.com
 /***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from math import log2

class ZoomLevel:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

        # Display zoom level whenever the map scale changes
        self.iface.mapCanvas().scaleChanged.connect(self.displayZoomLevel)


    def initGui(self):
        """This plugin makes no menu or toolbar changes."""
        pass


    def unload(self):
        """This plugin makes no menu or toolbar changes."""
        pass


    def displayZoomLevel(self):
        """Display the current zoom level in the status bar"""

        scale = self.iface.mapCanvas().scale()
        # scale denominator at zoom level 0 of GoogleCRS84Quad
        s0 = 559082264.0287178
        scale = self.iface.mapCanvas().scale()
        # Convert the scale to the equivalent zoom level
        # (This is accurate enough for at least 2 decimal places)
        zoom = log2(s0 / scale) / log2(2) - 1
        self.iface.mainWindow().statusBar().showMessage('Zoom Level {:.2f}'.format(zoom))
