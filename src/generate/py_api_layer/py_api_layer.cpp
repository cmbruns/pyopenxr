#include "loader_interfaces.h"
#include <string>
#include <map>
// #pragma warning(disable : 26812)

#ifdef _WIN32
#  define MODULE_API __declspec(dllexport)
#else
#  define MODULE_API
#endif

extern "C" {

// storage for pure python api layers
static std::map<std::string, PFN_xrNegotiateLoaderApiLayerInterface> s_LayerTable;

// xrNegotiateLoaderApiLayerInterface is the function the loader looks for in the DLL
MODULE_API XrResult xrNegotiateLoaderApiLayerInterface(
	const XrNegotiateLoaderInfo* loaderInfo,
	const char* cLayerName,
	XrNegotiateApiLayerRequest* apiLayerRequest)
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

MODULE_API void insertXrApiLayer(const char* pName, int nameLength, PFN_xrNegotiateLoaderApiLayerInterface negotiateFunction)
{
	std::string layerName(pName, nameLength);
	s_LayerTable[layerName] = negotiateFunction;
}

}  // extern "C"
