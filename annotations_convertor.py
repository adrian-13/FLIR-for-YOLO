import json

def convertor(source_path, number_of_images, destination_path):
  with open(source_path) as json_file:
    data = json.load(json_file)
    
    counter = 0
    for p in data['annotations']:
      for p in data['annotations']:
        if (p['image_id'] == counter):
          print(p['category_id'], end=" ", file=open(destination_path +'/FLIR_0{:04d}.txt'.format(counter + 1), 'a'))
          print((p['segmentation'][0][0] + p['segmentation'][0][4])/ 2 / 640, end=" ", file=open(destination_path + '/FLIR_0{:04d}.txt'.format(counter + 1), 'a'))
          print((p['segmentation'][0][1] + p['segmentation'][0][3]) / 2 / 512, end=" ", file=open(destination_path + '/FLIR_0{:04d}.txt'.format(counter + 1), 'a'))
          print(p['bbox'][2] / 640, end=" ", file=open(destination_path + '/FLIR_0{:04d}.txt'.format(counter + 1), 'a'))
          print(p['bbox'][3] / 512, file=open(destination_path + '/FLIR_0{:04d}.txt'.format(counter + 1), 'a'))
      counter += 1
      if (counter >= number_of_images):
        print("Convertion succesfully!" )
        break
