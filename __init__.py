# -*- coding: utf-8 -*-
"""
/***************************************************************************
Name                 : Auxiliary Window
Description          : Plugin for open synchronized window with selected layers
Date                 : June, 2015
copyright            : (C) 2015 by Luiz Motta
email                : motta.luiz@gmail.com

 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4.QtGui import ( QAction, QIcon )
from PyQt4.QtCore import pyqtSlot

from qgis.core import ( QgsProject )

import os

from auxiliarywindow import ContainerAuxiliaryWindow

def classFactory(iface):
  return AuxiliaryWindowPlugin( iface )

class AuxiliaryWindowPlugin:

  def __init__(self, iface):
    self.iface = iface
    self.plugin = ContainerAuxiliaryWindow( iface.mainWindow() )
    self.namePlugin = "&Auxiliary Window"

  def _connect(self, isConnect = True):
    signal_slot = (
      { 'signal': QgsProject.instance().readProject, 'slot': self.plugin.onReadProject },
      { 'signal': QgsProject.instance().writeProject, 'slot': self.plugin.onWriteProject }
    )
    if isConnect:
      for item in signal_slot:
        item['signal'].connect( item['slot'] )
    else:
      for item in signal_slot:
        item['signal'].disconnect( item['slot'] )

  def initGui(self):
    title = "Auxiliary window"
    icon = QIcon( os.path.join( os.path.dirname(__file__), 'auxiliarywindow.png' ) )
    self.action = QAction( icon, title, self.iface.mainWindow() )
    self.action.setObjectName( "AuxiliaryWindow" )
    self.action.setWhatsThis( title )
    self.action.setStatusTip( title )
    self.action.triggered.connect( self.run )
    self.iface.addToolBarIcon( self.action )
    self.iface.addPluginToMenu( self.namePlugin, self.action)
    self._connect()

  def unload(self):
    self.iface.removeToolBarIcon( self.action )
    self.iface.removePluginMenu( self.namePlugin, self.action)
    del self.action
    self._connect( False )
    self.plugin.close()
  
  @pyqtSlot()
  def run(self):
    self.plugin.run()
