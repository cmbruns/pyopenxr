import xr
from xr.ext import KhrOpenGLEnable

assert KhrOpenGLEnable.NAME == xr.KHR_OPENGL_ENABLE_EXTENSION_NAME
assert KhrOpenGLEnable.NAME == "XR_KHR_opengl_enable"

instance = xr.create_instance(xr.InstanceCreateInfo(
    enabled_extension_names=[KhrOpenGLEnable.NAME],
))
system_id = xr.get_system(instance)
graphics_requirements = KhrOpenGLEnable.get_opengl_graphics_requirements(instance, system_id)

assert isinstance(graphics_requirements, xr.GraphicsRequirementsOpenGLKHR)
