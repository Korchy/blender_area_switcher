# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_area_switcher

import bpy


class AREA_SWITCHER_KeyMap:

    _keymaps = []

    @classmethod
    def register(cls, context):
        # add keys
        if context.window_manager.keyconfigs.addon:
            keymap = context.window_manager.keyconfigs.addon.keymaps.new(name='Window', space_type='EMPTY')
            # add keys
            keymap_item = keymap.keymap_items.new('area_switcher.switch_area', 'D', 'PRESS', ctrl=True, shift=True)
            cls._keymaps.append((keymap, keymap_item))

    @classmethod
    def unregister(cls):
        # clear keys
        for keymap, keymap_item in cls._keymaps:
            keymap.keymap_items.remove(keymap_item)
        cls._keymaps.clear()


def register():
    AREA_SWITCHER_KeyMap.register(context=bpy.context)


def unregister():
    AREA_SWITCHER_KeyMap.unregister()
