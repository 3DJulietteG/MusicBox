import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMpx

nodeName ="CompileBBNode_MusicBox"
nodeID = OpenMaya.MTypeId(0x100fff)

class CompileBBNode_MusicBox(OpenMayaMpx.MPxNode):
   
    inBBMin = OpenMaya.MObject()
    inBBMax = OpenMaya.MObject()
    RestPose = OpenMaya.MObject()
    Keys = OpenMaya.MObject()
    inLocatorsA = OpenMaya.MObject()
    inLocatorsB = OpenMaya.MObject()
    outTranslateA = OpenMaya.MObject()
    outTranslateB = OpenMaya.MObject()

    
    def __init__(self):
        OpenMayaMpx.MPxNode.__init__(self)
    
    def compute(self,plug,dataBlock):

        if plug==CompileBBNode_MusicBox.outTranslateA or plug==CompileBBNode_MusicBox.outTranslateB:

            BBMinVal = dataBlock.inputValue(CompileBBNode_MusicBox.inBBMin).asFloat3()
            BBMaxVal = dataBlock.inputValue(CompileBBNode_MusicBox.inBBMax).asFloat3()
            LocRestVal = dataBlock.inputValue(CompileBBNode_MusicBox.RestPose).asFloat3()
            
            KeysArrayHandle = dataBlock.inputArrayValue(CompileBBNode_MusicBox.Keys)
            LocAPossible=[]
            LocBPossible=[]
            
            for i in range(KeysArrayHandle.elementCount()):
                KeysArrayHandle.jumpToArrayElement(i)
                KeyHandle = KeysArrayHandle.inputValue()

                LocAVal = KeyHandle.child(CompileBBNode_MusicBox.inLocatorsA).asFloat3()
                LocBVal = KeyHandle.child(CompileBBNode_MusicBox.inLocatorsB).asFloat3()

                if BBMinVal[0]<=LocAVal[0]<=BBMaxVal[0]:
                    if BBMinVal[1]<=LocAVal[1]<=BBMaxVal[1]:
                        if BBMinVal[2]<=LocAVal[2]<=BBMaxVal[2]:
                            LocAPossible.append(LocAVal)

                if BBMinVal[0]<=LocBVal[0]<=BBMaxVal[0]:
                    if BBMinVal[1]<=LocBVal[1]<=BBMaxVal[1]:
                        if BBMinVal[2]<=LocBVal[2]<=BBMaxVal[2]:
                            LocBPossible.append(LocBVal)

            if len(LocAPossible)==0:
                LocAOut=LocRestVal         
            else:     
                maxA=LocAPossible[0]           
                for each in LocAPossible:
                    if each[1]>maxA[1]:
                        maxA=each
                    if each[1]==maxA[1]:
                        if each[2]>maxA[2]:
                            maxA=each
                LocAOut=maxA   

            if len(LocBPossible)==0:
                LocBOut=LocRestVal  
            else:
                maxB=LocBPossible[0]         
                for each in LocBPossible:  
                    if each[1]>maxB[1]:   
                        maxB=each
                    if each[1]==maxB[1]:   
                        if each[2]>maxB[2]:   
                            maxB=each          
                LocBOut=maxB

            dataHTranslateA = dataBlock.outputValue(CompileBBNode_MusicBox.outTranslateA)
            dataHTranslateA.set3Float(LocAOut[0],LocAOut[1],LocAOut[2])

            dataHTranslateB = dataBlock.outputValue(CompileBBNode_MusicBox.outTranslateB)
            dataHTranslateB.set3Float(LocBOut[0],LocBOut[1],LocBOut[2])
        
            dataBlock.setClean(plug)
            
        else:
            return OpenMaya.kUnknownParameter
        
    
def nodeCreator():
    return OpenMayaMpx.asMPxPtr(CompileBBNode_MusicBox())

def nodeInitializer():

    #Create fonction for numeric attributes
    mFnAttr=OpenMaya.MFnNumericAttribute()
    mFnCoumpound=OpenMaya.MFnCompoundAttribute()
    
    #Create attributes

    #Collider
    CompileBBNode_MusicBox.inBBMin = mFnAttr.create("BoundingBoxMin", "BBMin", OpenMaya.MFnNumericData.k3Float, 0.0)
    mFnAttr.setReadable(True)
    mFnAttr.setWritable(True)
    mFnAttr.setStorable(True)
    
    CompileBBNode_MusicBox.inBBMax = mFnAttr.create("BoundingBoxMax", "BBMax", OpenMaya.MFnNumericData.k3Float, 0.0)
    mFnAttr.setReadable(True)
    mFnAttr.setWritable(True)
    mFnAttr.setStorable(True)  

    CompileBBNode_MusicBox.RestPose = mFnAttr.create("RestPosition", "RestLoc", OpenMaya.MFnNumericData.k3Float, 0.0)
    mFnAttr.setReadable(True)
    mFnAttr.setWritable(True)
    mFnAttr.setStorable(True)

    #Locators
    CompileBBNode_MusicBox.inLocatorsA = mFnAttr.create("PositionLocatorA", "LocA", OpenMaya.MFnNumericData.k3Float, 0.0)
    mFnAttr.setReadable(True)
    mFnAttr.setWritable(True)
    mFnAttr.setStorable(True)
    
    CompileBBNode_MusicBox.inLocatorsB = mFnAttr.create("PositionLocatorB", "LocB", OpenMaya.MFnNumericData.k3Float, 0.0)
    mFnAttr.setReadable(True)
    mFnAttr.setWritable(True)
    mFnAttr.setStorable(True) 

    CompileBBNode_MusicBox.Keys = mFnCoumpound.create("Keys", "k")
    mFnCoumpound.addChild(CompileBBNode_MusicBox.inLocatorsA)
    mFnCoumpound.addChild(CompileBBNode_MusicBox.inLocatorsB)
    mFnCoumpound.setArray(True)

    #Output
    CompileBBNode_MusicBox.outTranslateA = mFnAttr.create("outTranslateA", "outA", OpenMaya.MFnNumericData.k3Float,0.0)
    mFnAttr.setReadable(True)
    mFnAttr.setWritable(False)
    mFnAttr.setStorable(False)  

    CompileBBNode_MusicBox.outTranslateB = mFnAttr.create("outTranslateB", "outB", OpenMaya.MFnNumericData.k3Float,0.0)
    mFnAttr.setReadable(True)
    mFnAttr.setWritable(False)
    mFnAttr.setStorable(False)

    #Attach attributes
    CompileBBNode_MusicBox.addAttribute(CompileBBNode_MusicBox.inBBMin)
    CompileBBNode_MusicBox.addAttribute(CompileBBNode_MusicBox.inBBMax)
    CompileBBNode_MusicBox.addAttribute(CompileBBNode_MusicBox.RestPose)
    CompileBBNode_MusicBox.addAttribute(CompileBBNode_MusicBox.Keys)
    CompileBBNode_MusicBox.addAttribute(CompileBBNode_MusicBox.outTranslateA)
    CompileBBNode_MusicBox.addAttribute(CompileBBNode_MusicBox.outTranslateB)
    
    #Create relations (if there is a change to attribute A it will affect attribute B)
    CompileBBNode_MusicBox.attributeAffects(CompileBBNode_MusicBox.inBBMin, CompileBBNode_MusicBox.outTranslateA)
    CompileBBNode_MusicBox.attributeAffects(CompileBBNode_MusicBox.inBBMax, CompileBBNode_MusicBox.outTranslateA)
    CompileBBNode_MusicBox.attributeAffects(CompileBBNode_MusicBox.inBBMin, CompileBBNode_MusicBox.outTranslateB)
    CompileBBNode_MusicBox.attributeAffects(CompileBBNode_MusicBox.inBBMax, CompileBBNode_MusicBox.outTranslateB)
    CompileBBNode_MusicBox.attributeAffects(CompileBBNode_MusicBox.RestPose, CompileBBNode_MusicBox.outTranslateA)
    CompileBBNode_MusicBox.attributeAffects(CompileBBNode_MusicBox.RestPose, CompileBBNode_MusicBox.outTranslateB)
    CompileBBNode_MusicBox.attributeAffects(CompileBBNode_MusicBox.Keys, CompileBBNode_MusicBox.outTranslateA)
    CompileBBNode_MusicBox.attributeAffects(CompileBBNode_MusicBox.Keys, CompileBBNode_MusicBox.outTranslateB)
    CompileBBNode_MusicBox.attributeAffects(CompileBBNode_MusicBox.inLocatorsA, CompileBBNode_MusicBox.outTranslateA)
    CompileBBNode_MusicBox.attributeAffects(CompileBBNode_MusicBox.inLocatorsB, CompileBBNode_MusicBox.outTranslateB)

    

def initializePlugin(mobject):
    mplugin = OpenMayaMpx.MFnPlugin(mobject)
    try:
        mplugin.registerNode(nodeName, nodeID, nodeCreator, nodeInitializer)
    except:
        sys.stderr.write("Failed to register command: %s\n" % nodeName)
        
def uninitializePlugin(mobject):
    mplugin = OpenMayaMpx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode(nodeName, nodeID, nodeCreator, nodeInitializer)
    except:
        sys.stderr.write("Failed to register command: %s\n" % nodeName)
    


'''
import maya.cmds as cmds
cmds.loadPlugin('D:\Desktop\Projets\scripts\CustomNodes\Mwahaha.py')
cmds.createNode('CompileBBNode_MusicBox')

// Error: TypeError: file D:/Desktop/Projets/scripts/CustomNodes/Mwahaha.py line 35: in method 'MDataHandle_child', argument 2 of type 'MObject const &'
Additional information:
Wrong number or type of arguments for overloaded function 'MDataHandle_child'.
  Possible C/C++ prototypes are:
    MDataHandle::child(MPlug const &)
    MDataHandle::child(MObject const &) //
'''