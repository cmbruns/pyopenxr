#include <string>
#include <map>
#include <iostream>

#include <openxr/openxr.h>
#include "loader_interfaces.h"

// #pragma warning(disable : 26812)

using namespace std;

#if defined(__GNUC__) && __GNUC__ >= 4
#define LAYER_EXPORT __attribute__((visibility("default")))
#elif defined(__SUNPRO_C) && (__SUNPRO_C >= 0x590)
#define LAYER_EXPORT __attribute__((visibility("default")))
#else
#define LAYER_EXPORT __declspec(dllexport)
#endif

extern "C" {

// storage for pure python api layers
static std::map<std::string, PFN_xrNegotiateLoaderApiLayerInterface> s_LayerTable;

// Function used to negotiate an interface betewen the loader and a layer.  Each library exposing one or
// more layers needs to expose at least this function.
LAYER_EXPORT XrResult xrNegotiateLoaderApiLayerInterface(
    const XrNegotiateLoaderInfo *loaderInfo,
    const char *cLayerName,
    XrNegotiateApiLayerRequest *apiLayerRequest)
{
	// Check whether the named api layer has been registered.
	std::string sLayerName(cLayerName);
	auto it = s_LayerTable.find(sLayerName);
	if (it == s_LayerTable.end())
		return XR_ERROR_INITIALIZATION_FAILED;

	PFN_xrNegotiateLoaderApiLayerInterface negotiateFunction = it->second;
	auto result = negotiateFunction(loaderInfo, cLayerName, apiLayerRequest);
	return result;
}

LAYER_EXPORT void insertXrApiLayer(const char* pName, int nameLength, PFN_xrNegotiateLoaderApiLayerInterface negotiateFunction)
{
	std::string layerName(pName, nameLength);
	s_LayerTable[layerName] = negotiateFunction;
}

}  // extern "C"
