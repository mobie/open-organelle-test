import mobie


def create_hela_project():
    root = './data'
    address = 'https://janelia-cosem.s3.amazonaws.com/jrc_hela-2/jrc_hela-2.n5'

    # add the raw data
    clims = [2849, 6012]  # determined qualitatively
    raw_view = mobie.metadata.get_default_view("image", "fibsem-uint16", contrastLimits=clims)
    mobie.add_open_organelle_data(address, root, internal_path="em/fibsem-uint16", view=raw_view)

    # add "endo_pred"
    mobie.add_open_organelle_data(address, root, internal_path="labels/endo_pred")


if __name__ == '__main__':
    create_hela_project()
