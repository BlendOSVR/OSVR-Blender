bl_info = {
    "name": "OSVR",
    "category": "Object",
}

import bpy
import Math
from bpy.types import Operator
from ClientKit import ClientKit

class OSVR(Operator):
    """OSVR"""                          # blender tooltip for menu items and buttons
    bl_idname = "object.osvr"           # unique identifier for buttons and menu items to reference
    bl_label = "OSVR"                   # displays name in the interface
    bl_options = {'REGISTER', 'UNDO'}    # enable undo for the operator
    clientKit = None

    def execute(self, context):                  # execute() is called by blender when running the operator
        game_settings = bpy.data.scenes["Scene"].game_settings
        game_settings.stereo = 'STEREO'          # change camera to stereo
        game_settings.stereo_mode = 'SIDEBYSIDE' # change stereo settings to side by side views
        clientKit = ClientKit()

        return {'FINISHED'}             # lets blender know the operator finished successfully

def register():
    bpy.utils.register_class(OSVR)


def unregister():
    bpy.utils.unregister_class(OSVR)

# allows the script to be run directly from blender's text editor
# without having to install the addon
if __name__ == "__main__":
    register()

def updateButton():
    import bge

    controller = bge.logic.getCurrentController()       #gets Python Controller associated with this script
    obj = bpy.data.objects[controller.owner.name]
    bpy.context.scene.objects.active = obj
    obj.game.properties["button"].value = not obj.game.properties["button"].value

def updatePosition():
    import bge

    head = clientKit.instance.context.getInterface("/me/head")

    timestamp, pose = head.getPoseState()

    blendvec = Math.convertPosition(pose.translation)

    controller = bge.logic.getCurrentController()
    obj = bpy.data.objects[controller.owner.name]
    bpy.context.scene.objects.active = obj
    obj.location.x = blendvec.x
    obj.location.y = blendvec.y
    obj.location.z = blendvec.z
