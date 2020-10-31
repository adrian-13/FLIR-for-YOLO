# FLIR for YOLO
Transfer FLIR thermal dataset annotations to YOLO annotations format. 

## About
This script extract informations about annotations from FLIR thermal_annotations.json file and transfer it to text file. Each text file consists of annotations about one image.  
The format is:  

[**c**,  **bx**, **by**, **bw**, **bh**]

**c** -  class  
**bx** - box center coordinate x / image width  
**by** - box center coordinate y / image height  
**bw** - box width / image width  
**bh** - box height / image height  

  ### **Example:**
  3 0.41875 0.490234375 0.20625 0.23828125
  
  3 - class  
  0.41875 - box center coordinate x / image width  
  0.490234375 - box center coordinate y / image height  
  0.20625 - box width / image width  
  0.23828125 - box height / image height  
  
## How to use:  
Type: `python annotations_convertor.py -src "source folder" -dst "destinaion folder"`  
Example: `python annotations_convertor.py src "/content/thermal_annotations.json" -dst "/content/Thermal_dataset/"`

* Conversion takes approx one minute.
