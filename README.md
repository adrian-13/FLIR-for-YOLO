# FLIR for YOLO
Transfer FLIR thermal dataset annotations to YOLO annotations format. 

## About
This script extract informations about annotations from FLIR thermal_annotations.json file and transfer it to text file. Each text file consists of annotations about one image.  
The format is:  

[**c  bx  by  bw  bh**]

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
1. Change source_path (line 22) - folder with thermal_annotations.json file 
2. Change number_of_images (line 23) - 8862 (number of dataset image labels)
3. Change destination path (line 24) - folder where annotations will be created
4. Type: `python annotations_convertor.py` 

* Conversion takes approx one minute.
