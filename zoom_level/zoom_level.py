# -*- coding: utf-8 -*-
"""
ZoomLevel

 A QGIS plugin to display the zoom level of the map in the status bar.
                              -------------------
        begin                : 2020-01-17
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
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        pass


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        pass


    def displayZoomLevel(self):
        """Display the current zoom level in the status bar"""

        scale = self.iface.mapCanvas().scale()
        zoom = 29.1402 - log2(scale)
        self.iface.mainWindow().statusBar().showMessage('Zoom Level {:.2f}'.format(zoom))
