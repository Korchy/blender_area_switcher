# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_area_switcher

from bpy.app.handlers import persistent

import bpy


@persistent
def area_switcher_header_button(self, context):
    # draw function for area switch operator - add to area header
    if context.preferences.addons[__package__].preferences.switch_to(ui_type=context.area.ui_type) != 'NONE':   # additional check because some areas have the same header type
        layout = self.layout
        icon = 'WINDOW'
        if context.preferences.addons[__package__].preferences.dynamic_icons:
            icon = context.preferences.addons[__package__].preferences.switch_to_icon(ui_type=context.area.ui_type)
        layout.operator('area_switcher.switch_area', text='', icon=icon)


class AREA_SWITCHER_ui:

    @staticmethod
    def register(context):
        # register ui
        # bpy.types.OUTLINER_HT_header.prepend(area_switcher_header_button)
        for item in context.preferences.addons[__package__].preferences.items:
            if item[6] and hasattr(bpy.types, item[6]):
                window_haeder_cls = getattr(bpy.types, item[6])
                if not (hasattr(window_haeder_cls.draw, '_draw_funcs')
                        and area_switcher_header_button in window_haeder_cls.draw._draw_funcs):
                    current_area_state_var_name = item[5]
                    if current_area_state_var_name:
                        current_area_state_var = getattr(context.preferences.addons[__package__].preferences,
                                                         current_area_state_var_name)
                        if current_area_state_var != 'NONE':
                            window_haeder_cls.prepend(area_switcher_header_button)

    @staticmethod
    def unregister(context):
        # unregister ui
        # bpy.types.OUTLINER_HT_header.remove(area_switcher_header_button)
        for item in context.preferences.addons[__package__].preferences.items:
            if item[6] and hasattr(bpy.types, item[6]):
                window_haeder_cls = getattr(bpy.types, item[6])
                # if area_switcher_header_button in window_haeder_cls.draw._draw_funcs:
                window_haeder_cls.remove(area_switcher_header_button)

    @classmethod
    def update(cls, context):
        # update ui
        cls.unregister(context=context)
        cls.register(context=context)


def register():
    AREA_SWITCHER_ui.register(context=bpy.context)


def unregister():
    AREA_SWITCHER_ui.unregister(context=bpy.context)
