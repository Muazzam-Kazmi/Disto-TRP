import glob
import cv2
import os
from skimage import io
import pandas as pd
from sklearn.model_selection import train_test_split
Work_Dir = 'D:/PROJECT LAB/PAPERS/TRP-Channels/2. DATA/'
path = Work_Dir+'2. DISTOGRAM/trpchannels/'
lst_values, lst_final_values = [], []
lst_identifier = []
for file in glob.glob(path+"*.png"):
    images = cv2.imread(file , 0)
    lst_values.append(images)
    
    identifier = file.split('.png')[0].split("\\")[1]
    lst_identifier.append(identifier)
    
for item_values in lst_values:
    newimage = list(item_values.flatten())
    lst_final_values.append(newimage)     
df_trp_channels = pd.DataFrame(lst_final_values)
df_trp_channels['identifier'] = pd.DataFrame(lst_identifier)
df_trp_channels['class'] = 1

trp_test_class = df_trp_channels.pop('class')
trp_test_id = df_trp_channels.pop('identifier')

df_trp_channels.insert(0, 'class', trp_test_class)
df_trp_channels.insert(0, 'identifier', trp_test_id)

path = Work_Dir+'2. DISTOGRAM/non_trpchannels/'
lst_values, lst_final_values = [], []
lst_identifier = []
for file in glob.glob(path+"*.png"):
    images = cv2.imread(file , 0)
    lst_values.append(images)
    
    identifier = file.split('.png')[0].split("\\")[1]
    lst_identifier.append(identifier)
    
for item_values in lst_values:
    newimage = list(item_values.flatten())
    lst_final_values.append(newimage)     
df_non_trp_channels = pd.DataFrame(lst_final_values)
df_non_trp_channels['identifier'] = pd.DataFrame(lst_identifier)
df_non_trp_channels['class'] = 0

non_trp_test_class = df_non_trp_channels.pop('class')
non_trp_test_id = df_non_trp_channels.pop('identifier')

df_non_trp_channels.insert(0, 'class', non_trp_test_class)
df_non_trp_channels.insert(0, 'identifier', non_trp_test_id)

trp_trn, trp_tst = train_test_split(df_trp_channels, test_size=0.2, random_state=42, shuffle=True)
non_trp_trn, non_trp_tst = train_test_split(df_non_trp_channels, test_size=0.2, random_state=42, shuffle=True)

final_test_class1 = trp_tst.append(non_trp_tst)
final_train_class1 = trp_trn.append(non_trp_trn)

output_path = Work_Dir+'3.Feature sets/1.Alfafold_distogram/'

final_test_class1.to_csv(output_path+"alfafold_distogram_test_class1.csv", encoding='utf-8', sep=',', index=False, header=True )
final_train_class1.to_csv(output_path+"alfafold_distogram_train_class1.csv", encoding='utf-8', sep=',', index=False, header=True )


for x in df_trp_channels['identifier'].values.tolist():
    if x in df_non_trp_channels['identifier'].values.tolist():
        print(x)
    
# import os
# from skimage import io
# path = 'C:/Users/USER/Downloads/distogram/test/'
# WIDTH = 320
# HEIGHT = 320
# all_images = []
# for image_path in os.listdir(path):
#     print(image_path)
#     img = io.imread(image_path , 0)
#     print(img)
    
#     img = img.reshape([WIDTH, HEIGHT, 1])
#     all_images.append(img)
    
    
# x_train = np.array(all_images)
# import glob
# import cv2
# import os
# from skimage import io
# import pandas as pd
# path = 'C:/Users/USER/Downloads/distogram/test'

# images = [cv2.imread(file , 0) for file in glob.glob(path+"/*.png")]
# lst_append_images = []
# for image in images:
#     newimage = image.flatten()
#     lst_append_images.append(newimage.tolist())
# df = pd.DataFrame(lst_append_images)
    

    
    