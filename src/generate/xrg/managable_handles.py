from xml.etree import ElementTree


def main():
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

    print(f"{len(handles)} handles found")
    print(f"\n{create_count} create commands found")
    print(f"\n{destroy_count} destroy commands found")
    assert destroy_count == len(handles)

    # TODO: report on multiple create commands
    for handle in handles:
        name = handle
        d = handles[handle]
        assert "destroy" in d
        if "create" not in d:
            pass
            # print(f"Skipping presumably async creation for {name}")
        else:
            creates = d["create"]
            if len(creates) > 1:
                # Choose one create function to use the constructor as a convenience for
                # print(f"Multiple creation functions for {name}:")
                # 1) filter by minimum parameters count
                min_param_count = None
                creates_by_count = {}
                for c in creates:
                    params = c.findall("param")
                    if len(params) not in creates_by_count:
                        creates_by_count[len(params)] = []
                    creates_by_count[len(params)].append(c)
                    if min_param_count is None or min_param_count > len(params):
                        min_param_count = len(params)
                if len(creates_by_count[min_param_count]) > 1:
                    print(f"Multiple creation functions for {name}:")
                    for c in creates_by_count[min_param_count]:
                        params = c.findall("param")
                        ps = ", ".join(f"{p.find('name').text}: {p.find('type').text}" for p in params)
                        print(f"  {c.find('proto').find('name').text}({ps})")


if __name__ == "__main__":
    main()
