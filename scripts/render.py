"""Portable Blender render entrypoint for the supplied portrait scene."""
import bpy
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
scene = bpy.context.scene
scene.render.resolution_x = 1080
scene.render.resolution_y = 1920
scene.render.resolution_percentage = 100
scene.render.fps = 24
scene.frame_start = 1
scene.frame_end = 576
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = str(root / 'output' / 'frame_')
(root / 'output').mkdir(exist_ok=True)

if '--preview' in sys.argv:
    scene.render.resolution_percentage = 25
    scene.cycles.samples = 8
    scene.frame_set(576)
    scene.render.filepath = str(root / 'output' / 'preview.png')
    bpy.ops.render.render(write_still=True)
else:
    scene.cycles.samples = 48
    bpy.ops.render.render(animation=True)
