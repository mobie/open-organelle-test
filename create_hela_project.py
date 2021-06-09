from mobie.open_organelle import add_open_organelle_dataset


def create_hela_project():
    root = './data'
    address = 'https://janelia-cosem.s3.amazonaws.com/jrc_hela-2/jrc_hela-2.n5'
    sources = ['em/fibsem-uint16']
    add_open_organelle_dataset(address, root, sources)


if __name__ == '__main__':
    create_hela_project()
