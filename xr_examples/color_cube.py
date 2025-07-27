"""
pyopenxr example program color_cube.py
This example renders one big cube.
"""

import inspect
from OpenGL import GL
from OpenGL.GL.shaders import compileShader, compileProgram
import xr
from xr.utils import GraphicsAPI
from xr.utils.matrix4x4f import Matrix4x4f


# ContextObject is a high level pythonic class meant to keep simple cases simple.
with xr.utils.ContextObject(
    instance_create_info=xr.InstanceCreateInfo(
        enabled_extension_names=[
            # A graphics extension is mandatory (without a headless extension)
            xr.KHR_OPENGL_ENABLE_EXTENSION_NAME,
        ],
    ),
) as context:
    vertex_shader = compileShader(
        inspect.cleandoc("""
        #version 430
        
        // Adapted from @jherico's RiftDemo.py in pyovr
        
        /*  Draws a cube:
        
           2________ 3
           /|      /|
         6/_|____7/ |
          | |_____|_| 
          | /0    | /1
          |/______|/
          4       5          

         */

        layout(location = 0) uniform mat4 Projection = mat4(1);
        layout(location = 4) uniform mat4 ModelView = mat4(1);
        layout(location = 8) uniform float Size = 0.3;

        // Minimum Y value is zero, so cube sits on the floor in room scale
        const vec3 UNIT_CUBE[8] = vec3[8](
          vec3(-1.0, -0.0, -1.0), // 0: lower left rear
          vec3(+1.0, -0.0, -1.0), // 1: lower right rear
          vec3(-1.0, +2.0, -1.0), // 2: upper left rear
          vec3(+1.0, +2.0, -1.0), // 3: upper right rear
          vec3(-1.0, -0.0, +1.0), // 4: lower left front
          vec3(+1.0, -0.0, +1.0), // 5: lower right front
          vec3(-1.0, +2.0, +1.0), // 6: upper left front
          vec3(+1.0, +2.0, +1.0)  // 7: upper right front
        );

        const vec3 UNIT_CUBE_NORMALS[6] = vec3[6](
          vec3(0.0, 0.0, -1.0),
          vec3(0.0, 0.0, 1.0),
          vec3(1.0, 0.0, 0.0),
          vec3(-1.0, 0.0, 0.0),
          vec3(0.0, 1.0, 0.0),
          vec3(0.0, -1.0, 0.0)
        );

        const int CUBE_INDICES[36] = int[36](
          0, 1, 2, 2, 1, 3, // rear
          4, 6, 5, 6, 7, 5, // front
          0, 2, 4, 4, 2, 6, // left
          1, 3, 5, 5, 3, 7, // right
          2, 6, 3, 6, 3, 7, // top
          0, 1, 4, 4, 1, 5  // bottom
        );

        out vec3 _color;

        void main() {
          _color = vec3(1.0, 0.0, 0.0);
          int vertexIndex = CUBE_INDICES[gl_VertexID];
          int normalIndex = gl_VertexID / 6;

          _color = UNIT_CUBE_NORMALS[normalIndex];
          if (any(lessThan(_color, vec3(0.0)))) {
              _color = vec3(1.0) + _color;
          }

          gl_Position = Projection * ModelView * vec4(UNIT_CUBE[vertexIndex] * Size, 1.0);
        }
        """), GL.GL_VERTEX_SHADER)
    fragment_shader = compileShader(
        inspect.cleandoc("""
        #version 430
        
        in vec3 _color;
        out vec4 FragColor;

        void main() {
          FragColor = vec4(_color, 1.0);
        }
        """), GL.GL_FRAGMENT_SHADER)
    shader = compileProgram(vertex_shader, fragment_shader)
    vao = GL.glGenVertexArrays(1)
    GL.glBindVertexArray(vao)
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glClearColor(0.2, 0.2, 0.2, 1)
    GL.glClearDepth(1.0)
    for frame_index, frame_state in enumerate(context.frame_loop()):
        for view_index, view in enumerate(context.view_loop(frame_state)):
            if view_index == 1:
                # continue
                pass
            # print(view_index, view.pose.position)  # Are both eyes the same?
            projection = Matrix4x4f.create_projection_fov(
                graphics_api=GraphicsAPI.OPENGL,
                fov=view.fov,
                near_z=0.05,
                far_z=100.0,  # tip: use negative far_z for infinity projection...
            )
            to_view = Matrix4x4f.create_translation_rotation_scale(
                translation=view.pose.position,
                rotation=view.pose.orientation,
                scale=(1, 1, 1),
            )
            view = Matrix4x4f.invert_rigid_body(to_view)
            # print(projection, view)
            GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
            GL.glUseProgram(shader)
            GL.glUniformMatrix4fv(0, 1, False, projection.as_numpy().flatten("F"))
            GL.glUniformMatrix4fv(4, 1, False, view.as_numpy().flatten("F"))
            GL.glBindVertexArray(vao)
            GL.glDrawArrays(GL.GL_TRIANGLES, 0, 36)
        # if frame_index > 3: break
