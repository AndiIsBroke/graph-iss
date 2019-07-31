#function to edit and set regitration map parameters 

def SetRegParameters(parametersMap):
    parametersMap["FixedImagePyramid"]= ["FixedRecursiveImagePyramid"]
    parametersMap["ImageSampler"]=["Random"]
    parametersMap["MaximumNumberOfIterations"]= ['1000']
    parametersMap["Metric"]= ["AdvancedNormalizedCorrelation"] 
    parametersMap["MovingImagePyramid"]= ["MovingRecursiveImagePyramid"]
    parametersMap["NumberOfResolutions"]=['3'] 
    parametersMap["NumberOfSpatialSamples"]=['2048'] 
    parametersMap["NewSamplesEveryIteration"]=["true"] 
    parametersMap["LinearInterpolationOrder"]=['1'] 
    parametersMap["FinalBSplineInterpolationOrder"]=['1'] 
    parametersMap["NumberOfHistogramBins"]=['64'] 
    parametersMap["Optimizer"]= ["AdaptiveStochasticGradientDescent"]
    parametersMap["ResampleInterpolator"]=["FinalBSplineInterpolator"]
    parametersMap["ResultImageFormat"]=["tif"]
    parametersMap["Interpolator"]=["BSplineInterpolator"]
    parametersMap["Registration"]=["MultiResolutionRegistration"]
    parametersMap["Resampler"]=["DefaultResampler"]
    parametersMap["HowToCombineTransforms "]=["Compose"]
    parametersMap["WriteResultImage"]= ["false"]
    parametersMap["FixedInternalImagePixelType"]=["long"]
    parametersMap["MovingInternalImagePixelType"]= ["long"]
    parametersMap["FixedImageDimension"]=['3']
    parametersMap["MovingImageDimension"]=['3']
    parametersMap["UseDirectionCosines"]=["true"]
    parametersMap["AutomaticScalesEstimation"]=["true"]
    parametersMap["AutomaticParameterEstimation"]=["true"]
    parametersMap["AutomaticTransformInitialization"]=["true"]
    parametersMap["AutomaticTransformInitializationMethod"]=["GeometricalCenter"]
    parametersMap["HowToCombineTransforms"]=["Compose"]
    parametersMap["ErodeMask"]=["false"]
    parametersMap["ResultImagePixelType"]=["long"]

    return parametersMap
