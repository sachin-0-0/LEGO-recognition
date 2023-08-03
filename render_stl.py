import bpy
import math
import random

# Clear existing mesh objects in the scene
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

stl_part_number = 8
# Import the STL file
stl_path = f"/Users/sachinchaubal/Desktop/filtered-parts/{stl_part_number}.stl" # change this to your file path
bpy.ops.import_mesh.stl(filepath=stl_path)

# Assume the imported object is now the active object
imported_object = bpy.context.active_object

# Define RGB color (values between 0 and 1)
object_color = (0.5, 0.5, 0) # This will be grey; change to your desired color

# Set the object's material to the specified color
material = bpy.data.materials.new(name="Custom_Material")
material.diffuse_color = (*object_color, 1)
imported_object.data.materials.append(material)

# Set render engine, resolution, and other settings
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080

# Set the world's background color to white
bpy.context.scene.world.node_tree.nodes['Background'].inputs[0].default_value = (1, 1, 1, 1)

# Select the camera object
camera = bpy.data.objects['Camera']

# Adjust the camera's clipping distances
camera.data.clip_start = 0.1
camera.data.clip_end = 10000

# Create and configure a Track To constraint
track_to = camera.constraints.new(type='TRACK_TO')
track_to.target = imported_object
track_to.track_axis = 'TRACK_NEGATIVE_Z'
track_to.up_axis = 'UP_Y'

# Create a point light and parent it to the camera
light_data = bpy.data.lights.new(name="Camera_Light", type='POINT')
light_data.energy = 1000 # Adjust energy as needed
light_object = bpy.data.objects.new("Camera_Light", object_data=light_data)
bpy.context.collection.objects.link(light_object)
light_object.parent = camera

# Loop to render images
for i in range(10):
    # Generate random angles for azimuth and elevation
    azimuth = math.radians(random.uniform(0, 360))
    elevation = math.radians(random.uniform(0, 360)) # adjust as needed
    radius = 100 # Distance from object

    # Convert spherical to Cartesian coordinates
    x = radius * math.cos(elevation) * math.sin(azimuth)
    y = radius * math.cos(elevation) * math.cos(azimuth)
    z = radius * math.sin(elevation)

    camera.location = (x, y, z)

    # Set the camera's focal length (in millimeters)
    camera.data.lens = 50 # you can change this value

    # Set the render path
    render_path = f"/Users/sachinchaubal/Desktop/images/{stl_part_number}/{stl_part_number}_{i}.png" # change this to where you want to save the render
    bpy.context.scene.render.filepath = render_path

    # Render the image
    bpy.ops.render.render(write_still=True)
