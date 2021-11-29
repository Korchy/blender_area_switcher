# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_area_switcher

from . import area_switcher_ops
from . import area_switcher_ui
from . import area_switcher_preferences
from . import area_switcher_keymap
from .addon import Addon


bl_info = {
    'name': 'AreaSwitcher',
    'category': 'All',
    'author': 'Nikita Akimov',
    'version': (1, 2, 1),
    'blender': (2, 83, 0),
    'location': 'Areas header menu',
    'wiki_url': 'https://b3d.interplanety.org/en/blender-add-on-area-switcher/',
    'tracker_url': 'https://b3d.interplanety.org/en/blender-add-on-area-switcher/',
    'description': 'Button for quickly switching between area types'
}


def register():
    if not Addon.dev_mode():
        area_switcher_ops.register()
        area_switcher_preferences.register()
        area_switcher_ui.register()     # after preferences
        area_switcher_keymap.register()
    else:
        print('It seems you are trying to use the dev version of the ' + bl_info['name'] + ' add-on. It may work not properly. Please download and use the release version!')


def unregister():
    if not Addon.dev_mode():
        area_switcher_keymap.unregister()
        area_switcher_ui.unregister()
        area_switcher_preferences.unregister()
        area_switcher_ops.unregister()


if __name__ == '__main__':
    register()
