bl_info = {
    "name": "OSVR",
    "category": "Object",
}

import bpy
from bpy.types import Operator

class OSVR(Operator):
    """OSVR"""                          # blender tooltip for menu items and buttons
    bl_idname = "object.osvr"           # unique identifier for buttons and menu items to reference
    bl_label = "OSVR"                   # displays name in the interface
    bl_options = {'REGISTER', 'UNDO'}    # enable undo for the operator

    def execute(self, context):                  # execute() is called by blender when running the operator
        game_settings = bpy.data.scenes["Scene"].game_settings
        game_settings.stereo = 'STEREO'          # change camera to stereo
        game_settings.stereo_mode = 'SIDEBYSIDE' # change stereo settings to

        return {'FINISHED'}             # lets blender know the operator finished successfully

def register():
    bpy.utils.register_class(OSVR)


def unregister():
    bpy.utils.unregister_class(OSVR)

# allows the script to be run directly from blender's text editor
# without having to install the addon
if __name__ == "__main__":
    register()
