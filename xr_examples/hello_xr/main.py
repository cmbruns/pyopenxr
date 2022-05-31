import argparse
import logging
import platform
import sys
import threading
import time

import xr
from xr_examples.hello_xr.program import OpenXRProgram
from xr_examples.hello_xr.graphics_plugins import OpenGLGraphicsPlugin
from xr_examples.hello_xr.platform_plugins import Win32PlatformPlugin

key_press_event = threading.Event()
logger = logging.getLogger("hello_xr.main")


def create_graphics_plugin(options):
    graphics_plugin_map = {
        "OpenGL": OpenGLGraphicsPlugin,
    }
    if options.graphics not in graphics_plugin_map:
        raise NotImplementedError
    return graphics_plugin_map[options.graphics]()


def create_platform_plugin(options):
    if platform.system() == "Windows":
        return Win32PlatformPlugin()
    raise NotImplementedError


def poll_keyboard():
    logger.info("Press any key to shutdown...")
    try:
        sys.stdin.read(1)
        key_press_event.set()
        logger.debug("A key was pressed")
    except:
        pass


def main():
    logging.basicConfig(
        format="%(asctime)s.%(msecs)03d %(module)s %(levelname)s: %(message)s",
        datefmt='%m/%d/%y %I:%M:%S',
        level=logging.INFO,
    )
    options = update_options_from_command_line()

    # Install keyboard handler to exit on keypress
    threading.Thread(target=poll_keyboard, daemon=True).start()

    request_restart = False
    while True:
        platform_plugin = create_platform_plugin(options)
        with (create_graphics_plugin(options) as graphics_plugin,
              OpenXRProgram(options, platform_plugin, graphics_plugin) as program,
              ):
            program.create_instance()
            program.initialize_system()
            program.initialize_session()  # TODO: keep translating
            program.create_swapchains()
            graphics_plugin.focus_window()
            while not key_press_event.is_set():
                exit_render_loop, request_restart = program.poll_events()
                if exit_render_loop:
                    break
                if program.session_running:
                    if program.session_state == xr.SessionState.FOCUSED:
                        program.poll_actions()
                    program.render_frame()
                else:
                    # Throttle loop since xrWaitFrame won't be called.
                    time.sleep(0.250)
            if key_press_event.is_set() or not request_restart:
                break


def update_options_from_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--graphics", "-g", required=True,
        choices=["D3D11", "D3D12", "OpenGLES", "OpenGL", "Vulkan2", "Vulkan"],
    )
    parser.add_argument(
        "--formfactor", "-ff", default="Hmd",
        choices=["Hmd", "Handheld"],
    )
    parser.add_argument(
        "--viewconfig", "-vc", default="Stereo",
        choices=["Mono", "Stereo"],
    )
    parser.add_argument(
        "--blendmode", "-bm", default="Opaque",
        choices=["Opaque", "Additive", "AlphaBlend"],
    )
    parser.add_argument(
        "--space", "-s", default="Local",
        choices=["View", "Local", "Stage"],
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
    )
    options = parser.parse_args()
    if options.verbose:
        logging.getLogger("hello_xr").setLevel(logging.DEBUG)
    return options


if __name__ == "__main__":
    main()
