import xgenm as xg
import xgenm.xgGlobal as xgg
import xgenm.XgExternalAPI as xge

xgmSubdPatchList = []
palettes = xg.palettes()
for palette in palettes:

    descriptions = xg.descriptions(palette)
    for description in descriptions:
        xgmSubdPatch =  cmds.listRelatives(description,ad=1,type='xgmSubdPatch')
        if xgmSubdPatch:
            xgmSubdPatchList.append(xgmSubdPatch[0])

for xgmSubdPatch in xgmSubdPatchList:
        GetxgmMakeGuide = cmds.listConnections(xgmSubdPatch,type='xgmMakeGuide')
        if GetxgmMakeGuide:
            for i in GetxgmMakeGuide:
                xgmSplineGuide =cmds.listConnections(i,type='xgmSplineGuide',sh=1)
                listConnect = cmds.listConnections(i+'.outputMesh', source=False, destination=True)
                if not listConnect:
                    cmds.connectAttr(i+'.outputMesh',list(set(xgmSplineGuide))[0]+'.inputMesh')
