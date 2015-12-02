import mathutils
import math

class Math:
    def ConvertPosition(OSVR.ClientKit.Vec3 vec)
        #Blender uses a right handed coordinate system. But y and z are swapped
        return mathutils.Vector((float)vec.x, (float)vec.y, (float)vec.z)

    def ConvertPosition(OSVR.ClientKit.Vec2 vec)
        return mathutils.Vector((float)vec.x, (float)vec.y)

    def ConvertOrientation(OSVR.ClientKit.Quaternion quat)
        # Wikipedia may say quaternions are not handed, but these needed modification in Unity. Check if Blender is same
        return mathutils.Quaternion((float)quat.w, (float)quat.x, (float)quat.y, (float)quat.z)

    def ConvertPose(OSVR.ClientKit.Pose3 pose)
        matrix4x4 = mathutils.Matrix()
        matrix_location = mathutils.Matrix.Translation(ConvertPosition(pose.translation))
        matrix_rotation = mathutils.Matrix.Rotation(ConvertOrientation(pose.rotation))
        matrix_scale = mathutils.Matrix.Scale(ConvertPosition(Vector3.zero))
        matrix4x4 = matrix_location * matrix_rotation * matrix_scale
        return matrix4x4

    #Convert OSVR.ClientKit.Viewport to Rect. Blender equivalent?
    #Rect ConvertViewport(OSVR.ClientKit.Viewport viewport)
        #Unity expects normalized coordinates, not pixel coordinates. What about Blender?
        #@todo below assumes left and right eyes split the screen in half horizontally
        #return Rect(viewport.Left / (2f*viewport.Width), viewport.Bottom / viewport.Height, viewport.Width/(viewport.Width*2f), 1);

    #Convert OSVR.ClientKit.Matrix44f to Matrix4x4
    def ConvertMatrix(OSVR.ClientKit.Matrix44f matrix)
        matrix4x4 = mathutils.Matrix()
        matrix4x4[0][0] = matrix.M0
        matrix4x4[1][0] = matrix.M1
        matrix4x4[2][0] = matrix.M2
        matrix4x4[3][0] = matrix.M3
        matrix4x4[0][1] = matrix.M4
        matrix4x4[1][1] = matrix.M5
        matrix4x4[2][1] = matrix.M6
        matrix4x4[3][1] = matrix.M7
        matrix4x4[0][2] = matrix.M8
        matrix4x4[1][2] = matrix.M9
        matrix4x4[2][2] = matrix.M10
        matrix4x4[3][2] = matrix.M11
        matrix4x4[0][3] = matrix.M12
        matrix4x4[1][3] = matrix.M13
        matrix4x4[2][3] = matrix.M14
        matrix4x4[3][3] = matrix.M15
        return matrix4x4
