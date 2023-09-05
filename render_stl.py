import bpy
import math

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

# Set render engine, resolution, and other settings
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080

# Select the camera object
camera = bpy.data.objects['Camera']

# Create and configure a Track To constraint
track_to = camera.constraints.new(type='TRACK_TO')
track_to.target = imported_object
track_to.track_axis = 'TRACK_NEGATIVE_Z'
track_to.up_axis = 'UP_Y'

# Loop to render 2 images
for i in range(2):
    # Move the camera around the object (you can customize these values)
    angle = math.radians(i * 180)
    radius = 10 # Distance from object
    camera.location = (radius * math.sin(angle), radius * math.cos(angle), 10)

    # Set the camera's focal length (in millimeters)
    camera.data.lens = 50 # you can change this value

    # Set the render path
    render_path = f"/Users/sachinchaubal/Desktop/images/{stl_part_number}/{stl_part_number}_{i}.png" # change this to where you want to save the render
    bpy.context.scene.render.filepath = render_path

    # Render the image
    bpy.ops.render.render(write_still=True)
