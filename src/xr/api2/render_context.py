import enum
import inspect

import numpy
from OpenGL import GL
from OpenGL.GL.shaders import compileShader, compileProgram

import xr


class ColorSpace(enum.Enum):
    LINEAR = 1,
    SRGB = 2,


class RenderContext(object):
    """
    Contains enough information for renderers to display,
    including projection matrix and view matrix.
    """
    def __init__(
            self,
            color_space=ColorSpace.LINEAR,
            projection_matrix=xr.Matrix4x4f.create_scale(1),
            view_matrix=xr.Matrix4x4f.create_scale(1),
    ):
        self.projection_matrix = projection_matrix
        self.view_matrix = view_matrix
        self.color_space = color_space

    @staticmethod
    def from_view(
            view: xr.View,
            near_z=0.05,
            color_space: ColorSpace = ColorSpace.LINEAR
    ):
        # TODO: cache projection matrix for performance
        projection_matrix = xr.Matrix4x4f.create_projection_fov(
            graphics_api=xr.GraphicsAPI.OPENGL,
            fov=view.fov,
            near_z=near_z,
            far_z=-1,  # tip: use negative far_z for infinity projection...
        ).as_numpy()
        to_view = xr.Matrix4x4f.create_translation_rotation_scale(
            translation=view.pose.position,
            rotation=view.pose.orientation,
            scale=(1, 1, 1),
        )
        view_matrix = xr.Matrix4x4f.invert_rigid_body(to_view).as_numpy()
        return RenderContext(color_space=color_space, projection_matrix=projection_matrix, view_matrix=view_matrix)


class ColorCubeRenderer(object):
    """
    Colorful cube with default edge length 1 meter.
    """
    def __init__(self, model_matrix=xr.Matrix4x4f.create_scale(1)):
        self.vao = None
        self.shader = None
        self._model_matrix = numpy.array(model_matrix, dtype=numpy.float32).flatten()
        self.do_show = True

    def __enter__(self):
        self.init_gl()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.destroy_gl()

    @property
    def model_matrix(self):
        return self._model_matrix

    @model_matrix.setter
    def model_matrix(self, value):
        m = numpy.array(value, dtype=numpy.float32).flatten()
        assert len(m) == 16
        self._model_matrix = m

    def init_gl(self):
        if self.vao is not None:
            return
        vertex_shader = compileShader(
            inspect.cleandoc("""
            #version 430
            #line 55

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
            layout(location = 4) uniform mat4 View = mat4(1);
            const float s = 0.2;  // default cube scale 20 cm
            layout(location = 8) uniform mat4 Model = mat4(
                s, 0, 0, 0,
                0, s, 0, 0,
                0, 0, s, 0,
                0, s, 0, 1);  // raise cube to sit on floor

            const float r = 0.5;  // "radius" is 0.5, so cube edge length is 1.0
            const vec3 UNIT_CUBE[8] = vec3[8](
              vec3(-r, -r, -r), // 0: lower left rear
              vec3(+r, -r, -r), // 1: lower right rear
              vec3(-r, +r, -r), // 2: upper left rear
              vec3(+r, +r, -r), // 3: upper right rear
              vec3(-r, -r, +r), // 4: lower left front
              vec3(+r, -r, +r), // 5: lower right front
              vec3(-r, +r, +r), // 6: upper left front
              vec3(+r, +r, +r)  // 7: upper right front
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

              gl_Position = Projection * View * Model * vec4(UNIT_CUBE[vertexIndex], 1.0);
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
        self.shader = compileProgram(vertex_shader, fragment_shader)
        self.vao = GL.glGenVertexArrays(1)
        GL.glEnable(GL.GL_DEPTH_TEST)

    def paint_gl(self, render_context: RenderContext):
        if not self.do_show:
            return
        GL.glUseProgram(self.shader)
        GL.glUniformMatrix4fv(0, 1, False, render_context.projection_matrix)
        GL.glUniformMatrix4fv(4, 1, False, render_context.view_matrix)
        if self._model_matrix is not None:
            GL.glUniformMatrix4fv(8, 1, False, self._model_matrix)
        GL.glBindVertexArray(self.vao)
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, 36)

    def destroy_gl(self):
        if self.shader is not None:
            GL.glDeleteProgram(self.shader)
            self.shader = None
        if self.vao is not None:
            GL.glDeleteVertexArrays(1, (self.vao,))
            self.vao = None


__all__ = [
    "ColorCubeRenderer",
    "ColorSpace",
    "RenderContext",
]
