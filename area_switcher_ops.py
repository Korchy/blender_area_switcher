# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_area_switcher

from bpy.types import Operator
from bpy.utils import register_class, unregister_class


class AREA_SWITCHER_OT_main(Operator):
    bl_idname = 'area_switcher.switch_area'
    bl_label = 'Switch Area'
    bl_description = 'Switch area type to next'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # get an area type to switch to (from add-on properties)
        current_area_state_var_name = next((e for e in context.preferences.addons[__package__].preferences.items if e[0] == context.area.ui_type), None)[5]
        if current_area_state_var_name:
            current_area_state_var = getattr(context.preferences.addons[__package__].preferences, current_area_state_var_name)
            if current_area_state_var != 'NONE':
                context.area.ui_type = current_area_state_var
        return {'FINISHED'}


def register():
    register_class(AREA_SWITCHER_OT_main)


def unregister():
    unregister_class(AREA_SWITCHER_OT_main)
