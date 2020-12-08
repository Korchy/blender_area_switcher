# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_area_switcher

import bpy
from bpy.types import AddonPreferences
from bpy.props import BoolProperty, EnumProperty
from bpy.utils import register_class, unregister_class
from .area_switcher_ui import AREA_SWITCHER_ui


class AREA_SWITCHER_preferences(AddonPreferences):

    bl_idname = __package__

    # [(id, name, description, icon, id_num, variable name, area header name), ...]
    items = [
        ('NONE', 'None', 'None', '', 0, '', ''),
        ('VIEW_3D', '3D Viewport', '3D Viewport', 'VIEW3D', 1, 'view_3d', 'VIEW3D_HT_tool_header'),
        ('VIEW', 'Image Editor', 'Image Editor', 'IMAGE', 2, 'image_editor', 'IMAGE_HT_header'),
        ('UV', 'UV Editor', 'UV Editor', 'UV', 3, 'uv_editor', 'IMAGE_HT_header'),
        ('ShaderNodeTree', 'Shader Editor', 'Shader Editor', 'SHADING_RENDERED', 4, 'shader_editor', 'NODE_HT_header'),
        ('CompositorNodeTree', 'Compositor', 'Compositor', 'NODE_COMPOSITING', 5, 'compositor', 'NODE_HT_header'),
        ('TextureNodeTree', 'Texture Node Editor', 'Texture Node Editor', 'NODE_TEXTURE', 6, 'texture_node_editor', 'NODE_HT_header'),
        ('SEQUENCE_EDITOR', 'Video Squiencer', 'Video Sequencer', 'SEQUENCE', 7, 'sequence_editor', 'SEQUENCER_HT_header'),
        ('CLIP_EDITOR', 'Movie Clip Editor', 'Movie Clip Editor', 'TRACKER', 8, 'clip_editor', 'CLIP_HT_header'),
        ('DOPESHEET', 'Dope Sheet', 'Dope Sheet', 'ACTION', 9, 'doppesheet', 'DOPESHEET_HT_header'),
        ('TIMELINE', 'TimeLine', 'TimeLine', 'TIME', 10, 'timeline', 'DOPESHEET_HT_header'),
        ('FCURVES', 'Graph Editor', 'Graph Editor', 'GRAPH', 11, 'fcurves', 'GRAPH_HT_header'),
        ('DRIVERS', 'Drivers', 'Drivers', 'DRIVER', 12, 'drivers', 'GRAPH_HT_header'),
        ('NLA_EDITOR', 'Nonlinear Animation', 'Nonlinear Animation', 'NLA', 13, 'nla_editor', 'NLA_HT_header'),
        ('TEXT_EDITOR', 'Text Editor', 'Text Editor', 'TEXT', 14, 'text_editor', 'TEXT_HT_header'),
        ('CONSOLE', 'Python Console', 'Python Console', 'CONSOLE', 15, 'console', 'CONSOLE_HT_header'),
        ('INFO', 'Info', 'Info', 'INFO', 16, 'info', 'INFO_HT_header'),
        ('OUTLINER', 'Outliner', 'Outliner', 'OUTLINER', 17, 'outliner', 'OUTLINER_HT_header'),
        ('PROPERTIES', 'Properties', 'Properties', 'PROPERTIES', 18, 'properties', 'PROPERTIES_HT_header'),
        ('FILE_BROWSER', 'File Browser', 'File Browser', 'FILEBROWSER', 19, 'file_browser', 'FILEBROWSER_HT_header'),
        ('PREFERENCES', 'Preferences', 'Preferences', 'PREFERENCES', 20, 'preferences', 'USERPREF_HT_header')
    ] if bpy.app.version < (2, 91, 0) else [
        ('NONE', 'None', 'None', '', 0, '', ''),
        ('VIEW_3D', '3D Viewport', '3D Viewport', 'VIEW3D', 1, 'view_3d', 'VIEW3D_HT_tool_header'),
        ('IMAGE_EDITOR', 'Image Editor', 'Image Editor', 'IMAGE', 2, 'image_editor', 'IMAGE_HT_header'),
        ('UV', 'UV Editor', 'UV Editor', 'UV', 3, 'uv_editor', 'IMAGE_HT_header'),
        ('ShaderNodeTree', 'Shader Editor', 'Shader Editor', 'SHADING_RENDERED', 4, 'shader_editor', 'NODE_HT_header'),
        ('CompositorNodeTree', 'Compositor', 'Compositor', 'NODE_COMPOSITING', 5, 'compositor', 'NODE_HT_header'),
        ('TextureNodeTree', 'Texture Node Editor', 'Texture Node Editor', 'NODE_TEXTURE', 6, 'texture_node_editor', 'NODE_HT_header'),
        ('SEQUENCE_EDITOR', 'Video Squiencer', 'Video Sequencer', 'SEQUENCE', 7, 'sequence_editor', 'SEQUENCER_HT_header'),
        ('CLIP_EDITOR', 'Movie Clip Editor', 'Movie Clip Editor', 'TRACKER', 8, 'clip_editor', 'CLIP_HT_header'),
        ('DOPESHEET', 'Dope Sheet', 'Dope Sheet', 'ACTION', 9, 'doppesheet', 'DOPESHEET_HT_header'),
        ('TIMELINE', 'TimeLine', 'TimeLine', 'TIME', 10, 'timeline', 'DOPESHEET_HT_header'),
        ('FCURVES', 'Graph Editor', 'Graph Editor', 'GRAPH', 11, 'fcurves', 'GRAPH_HT_header'),
        ('DRIVERS', 'Drivers', 'Drivers', 'DRIVER', 12, 'drivers', 'GRAPH_HT_header'),
        ('NLA_EDITOR', 'Nonlinear Animation', 'Nonlinear Animation', 'NLA', 13, 'nla_editor', 'NLA_HT_header'),
        ('TEXT_EDITOR', 'Text Editor', 'Text Editor', 'TEXT', 14, 'text_editor', 'TEXT_HT_header'),
        ('CONSOLE', 'Python Console', 'Python Console', 'CONSOLE', 15, 'console', 'CONSOLE_HT_header'),
        ('INFO', 'Info', 'Info', 'INFO', 16, 'info', 'INFO_HT_header'),
        ('OUTLINER', 'Outliner', 'Outliner', 'OUTLINER', 17, 'outliner', 'OUTLINER_HT_header'),
        ('PROPERTIES', 'Properties', 'Properties', 'PROPERTIES', 18, 'properties', 'PROPERTIES_HT_header'),
        ('FILE_BROWSER', 'File Browser', 'File Browser', 'FILEBROWSER', 19, 'file_browser', 'FILEBROWSER_HT_header'),
        ('PREFERENCES', 'Preferences', 'Preferences', 'PREFERENCES', 20, 'preferences', 'USERPREF_HT_header')
    ]

    view_3d: EnumProperty(
        name='View 3D',
        items=[elem[:5] for elem in items],
        default='ShaderNodeTree',
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )
    image_editor: EnumProperty(
        name='Image Editor',
        items=[elem[:5] for elem in items],
        default='UV',
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )
    uv_editor: EnumProperty(
        name='UV Editor',
        items=[elem[:5] for elem in items],
        default=('VIEW' if bpy.app.version < (2, 91, 0) else 'IMAGE_EDITOR'),
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )
    shader_editor: EnumProperty(
        name='Shader Editor',
        items=[elem[:5] for elem in items],
        default='VIEW_3D',
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )
    compositor: EnumProperty(
        name='Compositor',
        items=[elem[:5] for elem in items],
        default='NONE',
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )
    texture_node_editor: EnumProperty(
        name='Texture Node Editor',
        items=[elem[:5] for elem in items],
        default='NONE',
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )
    sequence_editor: EnumProperty(
        name='Video Squiencer',
        items=[elem[:5] for elem in items],
        default='NONE',
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )
    clip_editor: EnumProperty(
        name='Movie Clip Editor',
        items=[elem[:5] for elem in items],
        default='NONE',
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )
    doppesheet: EnumProperty(
        name='Dope Sheet',
        items=[elem[:5] for elem in items],
        default='NONE',
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )
    timeline: EnumProperty(
        name='TimeLine',
        items=[elem[:5] for elem in items],
        default='NONE',
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )
    fcurves: EnumProperty(
        name='Graph Editor',
        items=[elem[:5] for elem in items],
        default='NLA_EDITOR',
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )
    drivers: EnumProperty(
        name='Drivers',
        items=[elem[:5] for elem in items],
        default='NONE',
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )
    nla_editor: EnumProperty(
        name='Nonlinear Animation',
        items=[elem[:5] for elem in items],
        default='FCURVES',
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )
    text_editor: EnumProperty(
        name='Text Editor',
        items=[elem[:5] for elem in items],
        default='NONE',
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )
    console: EnumProperty(
        name='Python Console',
        items=[elem[:5] for elem in items],
        default='INFO',
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )
    info: EnumProperty(
        name='Info',
        items=[elem[:5] for elem in items],
        default='CONSOLE',
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )
    outliner: EnumProperty(
        name='Outliner',
        items=[elem[:5] for elem in items],
        default='PROPERTIES',
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )
    properties: EnumProperty(
        name='Properties',
        items=[elem[:5] for elem in items],
        default='OUTLINER',
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )
    file_browser: EnumProperty(
        name='File Browser',
        items=[elem[:5] for elem in items],
        default='NONE',
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )
    preferences: EnumProperty(
        name='Preferences',
        items=[elem[:5] for elem in items],
        default='NONE',
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )

    dynamic_icons: BoolProperty(
        name='Dynamic Icons',
        default=True,
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )

    def switch_to(self, ui_type):
        # return property which defines switching target
        switch_to_var = 'NONE'
        switch_to_info = next((area_type for area_type in self.items if area_type[0] == ui_type), None)
        if switch_to_info:
            switch_to_var_name = switch_to_info[5]
            switch_to_var = getattr(self, switch_to_var_name)
        return switch_to_var

    def switch_to_icon(self, ui_type):
        # return dest icon for switched area type
        icon = 'NONE'
        switch_to_var = self.switch_to(ui_type=ui_type)
        if switch_to_var != 'NONE':
            icon_info = next((area_type for area_type in self.items if area_type[0] == switch_to_var), None)
            if icon_info:
                icon = icon_info[3]
        return icon

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
        layout.prop(self, property='dynamic_icons')


def register():
    register_class(AREA_SWITCHER_preferences)


def unregister():
    unregister_class(AREA_SWITCHER_preferences)
