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

    # [(id, name, description, icon, id_num, variable name, area header name, from addon), ...]
    items = [
        ('NONE', 'None', 'None', '', 0, '', '', False),
        ('VIEW_3D', '3D Viewport', '3D Viewport', 'VIEW3D', 1, 'view_3d', 'VIEW3D_HT_tool_header', False),
        ('VIEW', 'Image Editor', 'Image Editor', 'IMAGE', 2, 'image_editor', 'IMAGE_HT_header', False)
        if bpy.app.version < (2, 91, 0)
        else ('IMAGE_EDITOR', 'Image Editor', 'Image Editor', 'IMAGE', 2, 'image_editor', 'IMAGE_HT_header', False),
        ('UV', 'UV Editor', 'UV Editor', 'UV', 3, 'uv_editor', 'IMAGE_HT_header', False),
        ('CompositorNodeTree', 'Compositor', 'Compositor', 'NODE_COMPOSITING', 5, 'compositor', 'NODE_HT_header', False),
        ('TextureNodeTree', 'Texture Node Editor', 'Texture Node Editor', 'NODE_TEXTURE', 6, 'texture_node_editor', 'NODE_HT_header', False),
        ('GeometryNodeTree', 'Geometry Node Editor', 'Geometry Node Editor', 'NODETREE', 22, 'geometry_node_editor', 'NODE_HT_header', False),
        ('ShaderNodeTree', 'Shader Editor', 'Shader Editor', 'SHADING_RENDERED', 4, 'shader_editor', 'NODE_HT_header', False),
        ('SEQUENCE_EDITOR', 'Video Squiencer', 'Video Sequencer', 'SEQUENCE', 7, 'sequence_editor', 'SEQUENCER_HT_header', False),
        ('CLIP_EDITOR', 'Movie Clip Editor', 'Movie Clip Editor', 'TRACKER', 8, 'clip_editor', 'CLIP_HT_header', False),
        ('DOPESHEET', 'Dope Sheet', 'Dope Sheet', 'ACTION', 9, 'doppesheet', 'DOPESHEET_HT_header', False),
        ('TIMELINE', 'TimeLine', 'TimeLine', 'TIME', 10, 'timeline', 'DOPESHEET_HT_header', False),
        ('FCURVES', 'Graph Editor', 'Graph Editor', 'GRAPH', 11, 'fcurves', 'GRAPH_HT_header', False),
        ('DRIVERS', 'Drivers', 'Drivers', 'DRIVER', 12, 'drivers', 'GRAPH_HT_header', False),
        ('NLA_EDITOR', 'Nonlinear Animation', 'Nonlinear Animation', 'NLA', 13, 'nla_editor', 'NLA_HT_header', False),
        ('TEXT_EDITOR', 'Text Editor', 'Text Editor', 'TEXT', 14, 'text_editor', 'TEXT_HT_header', False),
        ('CONSOLE', 'Python Console', 'Python Console', 'CONSOLE', 15, 'console', 'CONSOLE_HT_header', False),
        ('INFO', 'Info', 'Info', 'INFO', 16, 'info', 'INFO_HT_header', False),
        ('OUTLINER', 'Outliner', 'Outliner', 'OUTLINER', 17, 'outliner', 'OUTLINER_HT_header', False),
        ('PROPERTIES', 'Properties', 'Properties', 'PROPERTIES', 18, 'properties', 'PROPERTIES_HT_header', False),
        ('FILE_BROWSER', 'File Browser', 'File Browser', 'FILEBROWSER', 19, 'file_browser', 'FILEBROWSER_HT_header', False)
        if bpy.app.version < (2, 92, 0)
        else ('FILES', 'File Browser', 'File Browser', 'FILEBROWSER', 19, 'file_browser', 'FILEBROWSER_HT_header', False),
        ('ASSETS', 'Asset Browser', 'Asset Browser', 'ASSET_MANAGER', 23, 'asset_browser', 'FILEBROWSER_HT_header', False),
        ('SPREADSHEET', 'Spreadsheet', 'Spreadsheet', 'SPREADSHEET', 24, 'spreadsheet', 'SPREADSHEET_HT_header', False),
        ('PREFERENCES', 'Preferences', 'Preferences', 'PREFERENCES', 20, 'preferences', 'USERPREF_HT_header', False),
        ('an_AnimationNodeTree', 'Animation Nodes', 'Animation Nodes', 'ONIONSKIN_ON', 21, 'animation_nodes', 'NODE_HT_header', True)
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
    animation_nodes: EnumProperty(
        name='Animation Nodes',
        items=[elem[:5] for elem in items],
        default='NONE',
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )
    geometry_node_editor: EnumProperty(
        name='Geometry Nodes',
        items=[elem[:5] for elem in items],
        default='NONE',
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )
    asset_browser: EnumProperty(
        name='Asset Browser',
        items=[elem[:5] for elem in items],
        default='NONE',
        update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )
    spreadsheet: EnumProperty(
        name='Spreadsheet',
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
        box.label(text='Switching From - To:')
        # base
        for item in (i for i in self.items if not i[7]):
            if hasattr(bpy.types, item[6]):
                box.prop(self, property=item[5])
        # from add-ons
        box.separator()
        box.label(text='May need external add-ons:')
        for item in (i for i in self.items if i[7]):
            if hasattr(bpy.types, item[6]):
                box.prop(self, property=item[5])
        # dynamic icons
        layout.prop(self, property='dynamic_icons')


def register():
    register_class(AREA_SWITCHER_preferences)


def unregister():
    unregister_class(AREA_SWITCHER_preferences)
