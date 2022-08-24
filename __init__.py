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
import bpy


bl_info = {
    'name': 'AreaSwitcher',
    'category': 'All',
    'author': 'Nikita Akimov',
    'version': (1, 3, 0),
    'blender': (2, 83, 0),
    'location': 'Areas header menu',
    'wiki_url': 'https://b3d.interplanety.org/en/blender-add-on-area-switcher/',
    'tracker_url': 'https://b3d.interplanety.org/en/blender-add-on-area-switcher/',
    'description': 'Button for quickly switching between area types'
}


def register():
    if not Addon.dev_mode():
        # To prevent conflicts with external add-ons (like LuxCore) the add-on must be registered last
        context = bpy.context
        if __name__ not in context.preferences.addons or \
                context.preferences.addons[-1].module == __name__:
            # if last or not registered yet - register
            area_switcher_ops.register()
            area_switcher_preferences.register()
            area_switcher_ui.register()     # after preferences
            area_switcher_keymap.register()
            area_switcher_preferences.AREA_SWITCHER_vars.registered = True
        else:
            # if not last in the bpy.context.preferences.addons list
            # remove from existed place
            addon_prefs_ptp = context.preferences.addons.get(__name__)
            addon_prefs_ptp_module = addon_prefs_ptp.module
            if addon_prefs_ptp:
                context.preferences.addons.remove(addon_prefs_ptp)
            # and add to the last place
            addon_prefs_new_ptp = context.preferences.addons.new()
            addon_prefs_new_ptp.module = addon_prefs_ptp_module
    else:
        print('It seems you are trying to use the dev version of the ' + bl_info['name'] + ' add-on. It may work not properly. Please download and use the release version!')


def unregister():
    if not Addon.dev_mode():
        if area_switcher_preferences.AREA_SWITCHER_vars.registered:
            area_switcher_keymap.unregister()
            area_switcher_ui.unregister()
            area_switcher_preferences.unregister()
            area_switcher_ops.unregister()
            area_switcher_preferences.AREA_SWITCHER_vars.registered = False


if __name__ == '__main__':
    register()
