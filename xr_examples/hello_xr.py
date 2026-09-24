import xr.api_layer
from xr_examples.hello_xr.main import main


xr.api_layer.activate_core_validation_layer()
xr.api_layer.activate_best_practices_validation_layer()


if __name__ == "__main__":
    main()
