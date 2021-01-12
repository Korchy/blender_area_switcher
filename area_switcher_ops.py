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
        switch_to = context.preferences.addons[__package__].preferences.switch_to(ui_type=context.area.ui_type)
        # switch to new area type
        if switch_to != 'NONE':
            try:
                context.area.ui_type = switch_to
            except Exception as exception:
                print('Undefined area type. You may need to install external add-ons.')
        return {'FINISHED'}


def register():
    register_class(AREA_SWITCHER_OT_main)


def unregister():
    unregister_class(AREA_SWITCHER_OT_main)
