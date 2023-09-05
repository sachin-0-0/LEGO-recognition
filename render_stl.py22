import bpy
import math
import random
import os

# List of the normalized colors you provided
colors = [
    (1, 1, 1),
    (0, 0, 0),
    (0.7686, 0, 0),
    (0, 0.2, 0.698),
    (1, 0.8039, 0),
    (0, 0.5216, 0.1686),
    (0.3333, 0.2, 0.1059),
    (0.3333, 0.349, 0.3333),
    (0.6471, 0.6471, 0.6431),
    (0.8235, 0.7451, 0.5882),
    (0, 0.4, 0.2),
    (1, 0.4824, 0),
    (0.4706, 0.5647, 0.5098),
    (1, 0.6078, 0.8039),
    (0.6392, 0.2863, 0.6392),
    (0.6275, 1, 0),
    (0, 0.0627, 0.6902),
    (0, 0.502, 0.502),
    (0.4549, 0.5255, 0.6157),
    (0.5451, 0, 0)
]

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

def add_lego_material(obj):
    material = bpy.data.materials.new(name="LEGO_Material")
    material.specular_intensity = 0.5  # Increase specular reflection
    material.roughness = 0.5  # Decrease roughness for shiny look
    obj.data.materials.append(material)
    return material

def clear_lights():
    """Delete all light sources in the current scene."""
    bpy.ops.object.select_all(action='DESELECT')  # Deselect all objects
    bpy.ops.object.select_by_type(type='LIGHT')  # Select all light sources
    bpy.ops.object.delete()  # Delete selected light sources
    

for stl_part_number in range(3020, 3021):
    clear_mesh_objects()

    imported_object = load_stl(stl_part_number)
    if not imported_object:
        continue
    material = add_lego_material(imported_object)
    imported_object.location = (0, 0, 0)
    imported_object.scale = (1, 1, 1)


    bpy.context.scene.world.node_tree.nodes['Background'].inputs[0].default_value = (.6, .6, .6, 1)
    camera = bpy.data.objects['Camera']
    camera.data.clip_start = 0.1
    camera.data.clip_end = 1000
    track_to = camera.constraints.new(type='TRACK_TO')
    track_to.target = imported_object
    track_to.track_axis = 'TRACK_NEGATIVE_Z'
    track_to.up_axis = 'UP_Y'

    clear_lights()

    light_data = bpy.data.lights.new(name="Camera_Light", type='POINT')
    light_data.energy = .01
    light_object = bpy.data.objects.new("Camera_Light", object_data=light_data)
    bpy.context.collection.objects.link(light_object)
    camera.data.lens = 50

    for i in range(250):
        color = random.choice(colors)
        material.diffuse_color = (*color, 1)
        
        azimuth = math.radians(random.uniform(0, 360))
        elevation = math.radians(random.uniform(0, 360))
        radius = 200
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
