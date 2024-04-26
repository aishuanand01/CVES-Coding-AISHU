import numpy as np
from stl import mesh
import os

def stl_to_numpy(stl_file_path):
    if os.path.exists(stl_file_path):
        mesh_data = mesh.Mesh.from_file(stl_file_path)
        vertices = mesh_data.vectors.reshape((-1, 3))
        return vertices
    else:
        print(f"Error: File not found at path {stl_file_path}")
        return None

# Example usage
# Get the absolute path to the Downloads directory
downloads_dir = '/Users/aishwarya/Downloads'
stl_file_path = os.path.join(downloads_dir, '1_1.stl')

numpy_array = stl_to_numpy(stl_file_path)
if numpy_array is not None:
    np.save('vertices.npy', numpy_array)