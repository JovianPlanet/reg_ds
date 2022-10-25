import os
from pathlib import Path
import nibabel as nib
import numpy as np
from ants import image_read, image_write, registration, apply_transforms, reflect_image


def flip(config):

    # Cargar las imagenes
    unflp_ = nib.load(config['mod_msk'])
    try:
        unflp = unflp_.get_fdata().squeeze(3)
    except:
        unflp = unflp_.get_fdata()

    if 'FCD020_MR1' in config['mod_mri']:

        unflp  = np.transpose(unflp, (2, 0, 1))
        unflp1 = np.flip(unflp, (1, 0, 2))

    elif 'FCD013_MR1' or 'FCD012_MR1' in config['mod_mri']:

        unflp1 = np.flip(unflp, (0, 1))

    Path(os.path.join(config['out_dir'])).mkdir(parents=True, exist_ok=True)
    img = nib.Nifti1Image(np.int16(unflp1), unflp_.affine)
    nib.save(img, os.path.join(config['out_dir'], config['mod_msk_fn']))


def registrate(config):

    # Cargar las imagenes
    ref     = image_read(config['ref_mri'], pixeltype='unsigned int')
    reg_img = image_read(config['mod_mri'], pixeltype='unsigned int')
    reg_msk = image_read(config['mod_msk'], pixeltype='unsigned int')

    # Registrar imagen
    rs2_img = registration(fixed=ref, 
                           moving=reg_img, 
                           type_of_transform=config['transforms'][4]
    )

    rs = apply_transforms(fixed=ref, 
                          moving=reg_img, 
                          transformlist=rs2_img['fwdtransforms'], 
                          interpolator='linear' #'multiLabel'
    )

    # Registrar etiqueta
    rs2_msk = registration(fixed=ref, 
                           moving=reg_msk, 
                           type_of_transform=config['transforms'][4]
    )

    rs_ = apply_transforms(fixed=ref, 
                           moving=reg_msk, 
                           transformlist=rs2_msk['fwdtransforms'], 
                           interpolator='nearestNeighbor' #'multiLabel'
    )

    Path(os.path.join(config['out_dir'])).mkdir(parents=True, exist_ok=True)
    image_write(rs, os.path.join(config['out_dir'], config['mod_mri_fn']), ri=False)
    image_write(rs_, os.path.join(config['out_dir'], config['mod_msk_fn']), ri=False)

'''
kevin - aumentar datos
terraza = transfer
registrar
'''