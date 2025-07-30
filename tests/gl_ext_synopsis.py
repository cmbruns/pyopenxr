import xr
import xr.ext.KHR.opengl_enable as opengl_enable

assert opengl_enable.NAME == xr.KHR_OPENGL_ENABLE_EXTENSION_NAME
assert opengl_enable.NAME == "XR_KHR_opengl_enable"

instance = xr.create_instance(xr.InstanceCreateInfo(
    enabled_extension_names=[opengl_enable.NAME],
))
system_id = xr.get_system(instance)
graphics_requirements = opengl_enable.get_opengl_graphics_requirements(instance, system_id)

assert isinstance(graphics_requirements, xr.GraphicsRequirementsOpenGLKHR)
