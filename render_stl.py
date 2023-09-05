import bpy

# Clear existing mesh objects in the scene
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Import the STL file
stl_path = "/path/to/your/file.stl" # change this to your file path
bpy.ops.import_mesh.stl(filepath=stl_path)

# Optionally, you can set up the camera, lighting, etc. here

# Set render engine, resolution, and other settings
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080

# Render the image
render_path = "/path/to/save/render.png" # change this to where you want to save the render
bpy.context.scene.render.filepath = render_path
bpy.ops.render.render(write_still=True)
