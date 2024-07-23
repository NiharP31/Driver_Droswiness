from imports import *
from data import *

all_dirs = drowsy_data_path + non_drowsy_data_path

# Load the data
data = []
for i in all_dirs:
    img = cv2.imread(i)
    img = cv2.resize(img, (224, 224))
    data.append(img)
# display a sample image    
plt.imshow(data[0])
plt.show()
# Convert the data to a tensor
data = np.array(data)
data = data / 255.0
data = torch.tensor(data, dtype=torch.float32)
data = data.permute(0, 3, 1, 2)



