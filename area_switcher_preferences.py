# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_area_switcher

from bpy.types import AddonPreferences
from bpy.props import StringProperty, EnumProperty
from bpy.utils import register_class, unregister_class


class AREA_SWITCHER_preferences(AddonPreferences):

    bl_idname = __package__

    # [(id, name, description, icon, id_num, variable name), ...]
    items = [
        ('NONE', 'None', 'None', '', 0, ''),
        ('VIEW_3D', '3D Viewport', '3D Viewport', 'VIEW3D', 1, 'view_3d'),
        ('VIEW', 'Image Editor', 'Image Editor', 'IMAGE', 2, 'image_editor'),
        ('UV', 'UV Editor', 'UV Editor', 'UV', 3, 'uv_editor'),
        ('ShaderNodeTree', 'Shader Editor', 'Shader Editor', 'SHADING_RENDERED', 4, 'shader_editor'),
        ('CompositorNodeTree', 'Compositor', 'Compositor', 'NODE_COMPOSITING', 5, 'compositor'),
        ('TextureNodeTree', 'Texture Node Editor', 'Texture Node Editor', 'NODE_TEXTURE', 6, 'texture_node_editor'),
        ('SEQUENCE_EDITOR', 'Video Squiencer', 'Video Sequencer', 'SEQUENCE', 7, 'sequence_editor'),
        ('CLIP_EDITOR', 'Movie Clip Editor', 'Movie Clip Editor', 'TRACKER', 8, 'clip_editor'),
        ('DOPESHEET', 'Dope Sheet', 'Dope Sheet', 'ACTION', 9, 'doppesheet'),
        ('TIMELINE', 'TileLine', 'TimeLine', 'TIME', 10, 'timeline'),
        ('FCURVES', 'Graph Editor', 'Graph Editor', 'GRAPH', 11, 'fcurves'),
        ('DRIVERS', 'Drivers', 'Drivers', 'DRIVER', 12, 'drivers'),
        ('NLA_EDITOR', 'Nonlinear Animation', 'Nonlinear Animation', 'NLA', 13, 'nla_editor'),
        ('TEXT_EDITOR', 'Text Editor', 'Text Editor', 'TEXT', 14, 'text_editor'),
        ('CONSOLE', 'Python Console', 'Python Console', 'CONSOLE', 15, 'console'),
        ('INFO', 'Info', 'Info', 'INFO', 16, 'info'),
        ('OUTLINER', 'Outliner', 'Outliner', 'OUTLINER', 17, 'outliner'),
        ('PROPERTIES', 'Properties', 'Properties', 'PROPERTIES', 18, 'properties'),
        ('FILE_BROWSER', 'File Browser', 'File Browser', 'FILEBROWSER', 19, 'file_browser'),
        ('PREFERENCES', 'Preferences', 'Preferences', 'PREFERENCES', 20, 'preferences')
    ]

    view_3d: EnumProperty(
        name='View 3D',
        items=[elem[:5] for elem in items],
        default='ShaderNodeTree'
    )
    image_editor: EnumProperty(
        name='Image Editor',
        items=[elem[:5] for elem in items],
        default='UV'
    )
    uv_editor: EnumProperty(
        name='UV Editor',
        items=[elem[:5] for elem in items],
        default='VIEW'
    )
    shader_editor: EnumProperty(
        name='Shader Editor',
        items=[elem[:5] for elem in items],
        default='VIEW_3D'
    )
    compositor: EnumProperty(
        name='Compositor',
        items=[elem[:5] for elem in items],
        default='NONE'
    )
    texture_node_editor: EnumProperty(
        name='Texture Node Editor',
        items=[elem[:5] for elem in items],
        default='NONE'
    )
    sequence_editor: EnumProperty(
        name='Video Squiencer',
        items=[elem[:5] for elem in items],
        default='NONE'
    )
    clip_editor: EnumProperty(
        name='Movie Clip Editor',
        items=[elem[:5] for elem in items],
        default='NONE'
    )
    doppesheet: EnumProperty(
        name='Dope Sheet',
        items=[elem[:5] for elem in items],
        default='NONE'
    )
    timeline: EnumProperty(
        name='TileLine',
        items=[elem[:5] for elem in items],
        default='NONE'
    )
    fcurves: EnumProperty(
        name='Graph Editor',
        items=[elem[:5] for elem in items],
        default='NLA_EDITOR'
    )
    drivers: EnumProperty(
        name='Drivers',
        items=[elem[:5] for elem in items],
        default='NONE'
    )
    nla_editor: EnumProperty(
        name='Nonlinear Animation',
        items=[elem[:5] for elem in items],
        default='FCURVES'
    )
    text_editor: EnumProperty(
        name='Text Editor',
        items=[elem[:5] for elem in items],
        default='NONE'
    )
    console: EnumProperty(
        name='Python Console',
        items=[elem[:5] for elem in items],
        default='NONE'
    )
    info: EnumProperty(
        name='Info',
        items=[elem[:5] for elem in items],
        default='NONE'
    )
    outliner: EnumProperty(
        name='Outliner',
        items=[elem[:5] for elem in items],
        default='PROPERTIES'
    )
    properties: EnumProperty(
        name='Properties',
        items=[elem[:5] for elem in items],
        default='OUTLINER'
    )
    file_browser: EnumProperty(
        name='File Browser',
        items=[elem[:5] for elem in items],
        default='NONE'
    )
    preferences: EnumProperty(
        name='Preferences',
        items=[elem[:5] for elem in items],
        default='NONE'
    )

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        box.label(text='Switching From - To')
        box.prop(self, property='view_3d')
        box.prop(self, property='image_editor')
        box.prop(self, property='uv_editor')
        box.prop(self, property='shader_editor')
        box.prop(self, property='compositor')
        box.prop(self, property='texture_node_editor')
        box.prop(self, property='sequence_editor')
        box.prop(self, property='clip_editor')
        box.prop(self, property='doppesheet')
        box.prop(self, property='timeline')
        box.prop(self, property='fcurves')
        box.prop(self, property='drivers')
        box.prop(self, property='nla_editor')
        box.prop(self, property='text_editor')
        box.prop(self, property='console')
        box.prop(self, property='info')
        box.prop(self, property='outliner')
        box.prop(self, property='properties')
        box.prop(self, property='file_browser')
        box.prop(self, property='preferences')


def register():
    register_class(AREA_SWITCHER_preferences)


def unregister():
    unregister_class(AREA_SWITCHER_preferences)
