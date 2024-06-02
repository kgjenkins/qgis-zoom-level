# -*- coding: utf-8 -*-
"""
ZoomLevel

 A QGIS plugin to display the zoom level of the map in the status bar.
                              -------------------
        begin                : 2020-01-23
        copyright            : (C) 2020-2024 by Keith Jenkins
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
from qgis.PyQt.QtWidgets import QLabel

class ZoomLevel:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

        # Add zoom widget to left side of status bar
        self.label = QLabel()
        iface.statusBarIface().addPermanentWidget(self.label)
        self.label.show()

        # Display zoom level whenever the map scale changes
        self.iface.mapCanvas().scaleChanged.connect(self.displayZoomLevel)

    def initGui(self):
        """This plugin makes no menu or toolbar changes."""
        pass


    def unload(self):
        """Remove widget"""
        self.iface.statusBarIface().removeWidget(self.label)


    def displayZoomLevel(self):
        """Display the current zoom level in the status bar"""

        # Zoom level 1 scale "1:591658688" is the scale that QGIS reports
        # after "zoom to native resolution (100%)" when viewing OpenStreetMap
        # zoom level 1 tiles in EPSG:3857
        #
        # Other code such as https://github.com/qgis/QGIS/blob/f9d3ca3afe6529e9a4b6cbb1b8a2008e7103039e/src/core/vectortile/qgsvectortileutils.h#L72
        # uses the value 559082264.0287178 but it is not clear where that number
        # comes from.
        #
        # Interestingly, but perhaps coincidentally, the ratio between the two numbers is very close to the
        # ratio of 90 to 85.06 -- 85.06 degrees is the north/south limit of the EPSG:3857 CRS
        # (and the 85.06 value can also be calculated as 85.05112878)

        z1scale = 591658688
        mapScale = self.iface.mapCanvas().scale()
        zoom = log2(z1scale / mapScale)
        msg = 'Zoom Level {:.2f}'.format(zoom)
        self.label.setText(msg)
