<!-- IBAMA logo -->
[ibama_logo]: http://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Logo_IBAMA.svg/150px-Logo_IBAMA.svg.png

![][ibama_logo]  
[Brazilian Institute of Environment and Renewable Natural Resources](http://www.ibama.gov.br)

# Auxiliary Window Plugin QGIS

Plugin for open synchronized window with selected layers.

## Author
Luiz Motta

## Changelog
- 2015-07-23
 Add message box in auxiliary window
- 2015-07-06 
 Update clearBridge, check if self.bridge already initialized
 Update onAddSelectedLayersQgis, added clearBridge, ltg.addLayer has postponed trigger for adding layers. This caused changes in the extent of the windows.
- 2015-07-05 
 Add an entry in Plugins menu (ticket #13057 closed)
- 2015-06-27
 Initial plugin

