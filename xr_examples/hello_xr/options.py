import xr


class Options(object):
    def __init__(self):
        self.graphics_plugin = "OpenGL"
        self.form_factor = "Hmd"
        self.view_configuration = "Stereo"
        self.environment_blend_mode = "Opaque"
        self.app_space = "Local"
        self.parsed = {
            "form_factor": xr.FormFactor.HEAD_MOUNTED_DISPLAY,
            "view_config_type": xr.ViewConfigurationType.PRIMARY_STEREO,
            "environment_blend_mode": xr.EnvironmentBlendMode.OPAQUE,
        }

    @property
    def background_clear_color(self) -> tuple:
        slate_grey = (0.184313729, 0.309803933, 0.309803933, 1.0)
        if self.parsed["environment_blend_mode"] == xr.EnvironmentBlendMode.OPAQUE:
            return slate_grey  # SlateGrey
        elif self.parsed["environment_blend_mode"] == xr.EnvironmentBlendMode.ADDITIVE:
            return 0, 0, 0, 1  # Black
        elif self.parsed["environment_blend_mode"] == xr.EnvironmentBlendMode.ALPHA_BLEND:
            return 0, 0, 0, 0  # TransparentBlack
        else:
            return slate_grey

    @staticmethod
    def get_xr_environment_blend_mode(environment_blend_mode_string: str) -> xr.EnvironmentBlendMode:
        return {
            "Opaque": xr.EnvironmentBlendMode.OPAQUE,
            "Additive": xr.EnvironmentBlendMode.ADDITIVE,
            "AlphaBlend": xr.EnvironmentBlendMode.ALPHA_BLEND,
        }[environment_blend_mode_string]

    @staticmethod
    def get_xr_environment_blend_mode_string(environment_blend_mode: xr.EnvironmentBlendMode) -> str:
        return {
            xr.EnvironmentBlendMode.OPAQUE: "Opaque",
            xr.EnvironmentBlendMode.ADDITIVE: "Additive",
            xr.EnvironmentBlendMode.ALPHA_BLEND: "AlphaBlend",
        }[environment_blend_mode]

    @staticmethod
    def get_xr_form_factor(form_factor_string: str) -> xr.FormFactor:
        if form_factor_string == "Hmd":
            return xr.FormFactor.HEAD_MOUNTED_DISPLAY
        elif form_factor_string == "Handheld":
            return xr.FormFactor.HANDHELD_DISPLAY
        raise ValueError(f"Unknown form factor '{form_factor_string}'")

    @staticmethod
    def get_xr_view_configuration_type(view_configuration_string: str) -> xr.ViewConfigurationType:
        if view_configuration_string == "Mono":
            return xr.ViewConfigurationType.PRIMARY_MONO
        elif view_configuration_string == "Stereo":
            return xr.ViewConfigurationType.PRIMARY_STEREO
        raise ValueError(f"Unknown view configuration '{view_configuration_string}'")

    def parse_strings(self):
        self.parsed["form_factor"] = self.get_xr_form_factor(self.form_factor)
        self.parsed["view_config_type"] = self.get_xr_view_configuration_type(self.view_configuration)
        self.parsed["environment_blend_mode"] = self.get_xr_environment_blend_mode(self.environment_blend_mode)

    def set_environment_blend_mode(self, environment_blend_mode: xr.EnvironmentBlendMode) -> None:
        self.environment_blend_mode = self.get_xr_environment_blend_mode_string(environment_blend_mode)
        self.parsed["environment_blend_mode"] = environment_blend_mode
