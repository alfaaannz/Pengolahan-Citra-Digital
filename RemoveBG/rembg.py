from rembg import remove 
from PIL import Image 

input_path = "kucing.jpg"

output_path = "hasil.png" 

input = Image.open(input_path)  
output = remove(input) 

output.save(output_path)