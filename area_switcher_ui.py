# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_area_switcher

from bpy.app.handlers import persistent

import bpy


@persistent
def area_switcher_header_button(self, context):
    layout = self.layout
    layout.operator('area_switcher.switch_area', text='', icon='WINDOW')


def register():
    bpy.types.OUTLINER_HT_header.prepend(area_switcher_header_button)


def unregister():
    bpy.types.OUTLINER_HT_header.remove(area_switcher_header_button)
