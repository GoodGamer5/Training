import bpy
from math import radians


MODEL_NAME = "TrainingModel"
COLLECTION_NAME = "TrainingModel"


def get_or_create_material(name, color, metallic=0.0, roughness=0.5):
    material = bpy.data.materials.get(name)
    if material is None:
        material = bpy.data.materials.new(name=name)

    material.use_nodes = True
    principled = material.node_tree.nodes.get("Principled BSDF")
    principled.inputs["Base Color"].default_value = color
    principled.inputs["Metallic"].default_value = metallic
    principled.inputs["Roughness"].default_value = roughness
    return material


def get_or_create_collection(name):
    collection = bpy.data.collections.get(name)
    if collection is None:
        collection = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(collection)
    return collection


def remove_existing_model():
    collection = bpy.data.collections.get(COLLECTION_NAME)
    if collection is None:
        return

    for obj in list(collection.objects):
        bpy.data.objects.remove(obj, do_unlink=True)

    bpy.data.collections.remove(collection)


def assign_material(obj, material):
    obj.data.materials.clear()
    obj.data.materials.append(material)


def move_to_collection(obj, collection):
    if collection not in obj.users_collection:
        collection.objects.link(obj)

    for current in list(obj.users_collection):
        if current != collection:
            current.objects.unlink(obj)


def create_cube(name, size, location, material, collection, rotation=(0.0, 0.0, 0.0)):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=location, rotation=rotation)
    obj = bpy.context.active_object
    obj.name = name
    obj.scale = size
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    assign_material(obj, material)
    move_to_collection(obj, collection)
    return obj


def build_model():
    remove_existing_model()
    collection = get_or_create_collection(COLLECTION_NAME)

    green = get_or_create_material("Training Green", (0.1, 0.55, 0.2, 1.0), roughness=0.45)
    black = get_or_create_material("Training Black", (0.04, 0.04, 0.04, 1.0), roughness=0.7)
    metal_black = get_or_create_material(
        "Training Metal Black",
        (0.08, 0.08, 0.08, 1.0),
        metallic=1.0,
        roughness=0.25,
    )

    parts = [
        create_cube("Body", (1.5, 0.9, 0.45), (0.0, 0.0, 0.45), green, collection),
        create_cube("Cabin", (0.7, 0.55, 0.35), (0.0, 0.0, 1.15), metal_black, collection),
        create_cube("FrontPlate", (1.65, 0.15, 0.35), (0.0, 0.75, 0.45), black, collection),
        create_cube("RearPlate", (1.45, 0.12, 0.28), (0.0, -0.7, 0.45), black, collection),
        create_cube("LeftPod", (0.22, 0.85, 0.22), (-1.4, 0.0, 0.35), metal_black, collection),
        create_cube("RightPod", (0.22, 0.85, 0.22), (1.4, 0.0, 0.35), metal_black, collection),
        create_cube(
            "TopAccent",
            (1.0, 0.25, 0.08),
            (0.0, 0.0, 1.55),
            black,
            collection,
            rotation=(0.0, radians(0), radians(18)),
        ),
    ]

    bpy.ops.object.select_all(action="DESELECT")
    for part in parts:
        part.select_set(True)

    bpy.context.view_layer.objects.active = parts[0]
    bpy.ops.object.join()

    model = bpy.context.active_object
    model.name = MODEL_NAME
    model.data.name = MODEL_NAME
    return model


build_model()
