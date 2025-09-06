from xml.etree import ElementTree


def parse_manageable_handles_xml():
    # Open official OpenXR registry xml file
    with open("headers/xr.xml", "rb") as stream:
        xr_registry = ElementTree.parse(stream).getroot()

    # Find handle types
    handles = {}
    for types in xr_registry.findall("types"):
        for type in types.findall("type"):
            try:
                if type.attrib["category"] == "handle":
                    name = type.find("name").text
                    handles[name] = {}
                    parent = None
                    try:
                        parent = type.attrib["parent"]
                    except KeyError:
                        pass
                    handles[name]["parent"] = parent
            except KeyError as e:
                pass

    # Find create and destroy commands
    destroy_count = 0
    create_count = 0
    for commands in xr_registry.findall("commands"):
        for command in commands.findall("command"):
            proto = command.find("proto")
            if proto is None:
                continue
            name = proto.find("name").text
            params = []
            for param in command.findall("param"):
                params.append(param)
            if "Destroy" in name:
                assert len(params) == 1
                type_name = params[-1].find("type").text
                assert type_name in handles
                assert "destroy" not in handles[type_name]
                handles[type_name]["destroy"] = command
                destroy_count += 1
            if "Create" in name:
                assert len(params) > 0
                # Is there a handle return parameter?
                handle_param_count = 0
                for param in params:
                    type_name = param.find("type").text
                    if type_name not in handles:
                        continue
                    param_name = param.find("name").text
                    full_text = "".join(param.itertext())
                    is_pointer = "*" in full_text
                    is_const = "const" in full_text.split(param_name)[0]
                    if is_pointer and not is_const:
                        handle_param_count += 1
                        handle_type_name = type_name
                assert handle_param_count < 2
                if handle_param_count == 1:
                    create_count += 1
                    h = handles[handle_type_name]
                    if "create" not in h:
                        h["create"] = []
                    h["create"].append(command)
    assert destroy_count == len(handles)

    # TODO: report on multiple create commands
    best_create_count = 0
    for handle in handles:
        d = handles[handle]
        assert "destroy" in d
        if "create" not in d:
            pass
            # print(f"Skipping presumably async creation for {name}")
        else:
            creates = d["create"]
            if len(creates) > 0:
                # Choose one create function to use the constructor as a convenience for
                # Use the first defined create function, except for XrInstance
                # So use the rule "first defined create function with 3 arguments"
                # filter by minimum parameters count
                min_param_count = None
                best_create = None
                creates_by_count = {}
                for c in creates:
                    params = c.findall("param")
                    if len(params) not in creates_by_count:
                        creates_by_count[len(params)] = []
                    creates_by_count[len(params)].append(c)
                    if min_param_count is None or min_param_count > len(params):
                        min_param_count = len(params)
                        best_create = c
                assert best_create is not None
                d["best_create"] = best_create
                best_create_count += 1
    manageable_handles = {}
    for h in handles:
        d = handles[h]
        if "destroy" not in d:
            continue
        if "best_create" not in d:
            continue
        manageable_handles[h] = {
            "create": d["best_create"],
            "destroy": d["destroy"],
        }
    return manageable_handles


if __name__ == "__main__":
    manageable_handles = parse_manageable_handles_xml()
    print(f"{len(manageable_handles)} manageable handles found")
