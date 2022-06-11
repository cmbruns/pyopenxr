#include "loader_interfaces.h"
#include <cstdio>
#pragma warning(disable : 26812)

extern "C" {

	// xrNegotiateLoaderApiLayerInterface is the function the loader looks for in the DLL
	XrResult xrNegotiateLoaderApiLayerInterface(
		const XrNegotiateLoaderInfo* loaderInfo,
		const char* layerName,
		XrNegotiateApiLayerRequest* apiLayerRequest)
	{
		printf("Hello negotiate loader api interface\n");

		return XR_SUCCESS;
	}
}
