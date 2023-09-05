import bpy
import math
import random
import os

def clear_mesh_objects():
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

def load_stl(stl_part_number):
    stl_path = f"/home/sachin/Desktop/filtered-parts/{stl_part_number}.stl"
    if not os.path.exists(stl_path):  # Check if the STL file exists
        return None
    bpy.ops.import_mesh.stl(filepath=stl_path)
    return bpy.context.active_object

for stl_part_number in range(1, 11):  # Adjust this range based on how many STL files you have
    clear_mesh_objects()

    imported_object = load_stl(stl_part_number)
    if not imported_object:  # If the STL file did not exist, it will return None, so skip this iteration
        continue
    
    imported_object.location = (0, 0, 0)
    imported_object.scale = (1, 1, 1)

    object_color = (0.5, 0.5, 0)
    material = bpy.data.materials.new(name="Custom_Material")
    material.diffuse_color = (*object_color, 1)
    imported_object.data.materials.append(material)

    bpy.context.scene.world.node_tree.nodes['Background'].inputs[0].default_value = (1, 1, 1, 1)
    camera = bpy.data.objects['Camera']
    camera.data.clip_start = 0.1
    camera.data.clip_end = 10000
    track_to = camera.constraints.new(type='TRACK_TO')
    track_to.target = imported_object
    track_to.track_axis = 'TRACK_NEGATIVE_Z'
    track_to.up_axis = 'UP_Y'

    light_data = bpy.data.lights.new(name="Camera_Light", type='POINT')
    light_data.energy = 5000
    light_object = bpy.data.objects.new("Camera_Light", object_data=light_data)
    bpy.context.collection.objects.link(light_object)
    camera.data.lens = 50

    for i in range(250):
        azimuth = math.radians(random.uniform(0, 360))
        elevation = math.radians(random.uniform(0, 360))
        radius = 100
        x = radius * math.cos(elevation) * math.sin(azimuth)
        y = radius * math.cos(elevation) * math.cos(azimuth)
        z = radius * math.sin(elevation)
        camera.location = (x, y, z)
        camera.rotation_euler = (0, 0, 0)  
        light_object.location = (x, y, z)
        output_path = f"/home/sachin/Desktop/images/{stl_part_number}/{stl_part_number}_{i}.png"
        bpy.context.scene.render.filepath = output_path
        bpy.ops.render.render(write_still=True)

bpy.ops.wm.quit_blender()
