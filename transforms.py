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

    # Modo (-Y,-Z,-X)
    if 'FCD020_MR1' in config['unmod_info']['patient'] and '7' in config['unmod_info']['study']: # Modo (-Y,-Z,-X)

        unflp  = np.transpose(unflp, (2, 0, 1))
        unflp1 = np.flip(unflp, (1, 0, 2))

    # Modo (-Y,-Z,-X)
    elif 'FCD012_MR1' in config['unmod_info']['patient'] and '9' in config['unmod_info']['study']:

        unflp  = np.transpose(unflp, (2, 0, 1))
        unflp1 = np.flip(unflp, (1, 0, 2))

    # Modo (-Y,-Z,-X)
    elif 'FCD018_MR1' in config['unmod_info']['patient'] and '29' in config['unmod_info']['study']:

        unflp  = np.transpose(unflp, (2, 0, 1))
        unflp1 = np.flip(unflp, (1, 0, 2))

    # Modo (-Y,-Z,-X)
    elif 'FCD024_MR1' in config['unmod_info']['patient'] and '601_VOL_T1_SAG' in config['unmod_info']['study']:

        unflp  = np.transpose(unflp, (2, 0, 1))
        unflp1 = np.flip(unflp, (1, 0, 2))

    # Modo (-Y,-Z,-X)
    elif 'FCD039_MR1' in config['unmod_info']['patient']:# and '601_VOL_T1_SAG' in config['unmod_info']['study']:

        unflp  = np.transpose(unflp, (2, 0, 1))
        unflp1 = np.flip(unflp, (1, 0, 2))

    # Modo (-Y,-Z,-X)
    elif 'FCD042_MR1' in config['unmod_info']['patient']:# and '601_VOL_T1_SAG' in config['unmod_info']['study']:

        unflp  = np.transpose(unflp, (2, 0, 1))
        unflp1 = np.flip(unflp, (1, 0, 2))

    # Modo (-Y,-Z,-X)
    elif 'FCD014_MR1' in config['unmod_info']['patient'] and '12' in config['unmod_info']['study']:# and '601_VOL_T1_SAG' in config['unmod_info']['study']:

        unflp  = np.transpose(unflp, (2, 0, 1))
        unflp1 = np.flip(unflp, (1, 0, 2))

    # Modo (-Y,-Z,-X)
    elif 'FCD015_MR1' in config['unmod_info']['patient'] and '502' in config['unmod_info']['study']:# and '601_VOL_T1_SAG' in config['unmod_info']['study']:

        unflp  = np.transpose(unflp, (2, 0, 1))
        unflp1 = np.flip(unflp, (1, 0, 2))

    # Modo (-Y,-Z,-X)
    elif 'FCD027_MR1' in config['unmod_info']['patient'] and '7' in config['unmod_info']['study']:# and '601_VOL_T1_SAG' in config['unmod_info']['study']:

        unflp  = np.transpose(unflp, (2, 0, 1))
        unflp1 = np.flip(unflp, (1, 0, 2))

    # Modo (-Y,-Z,-X)
    elif 'FCD030_MR1' in config['unmod_info']['patient'] and '802_eFL_VOL_SAG' in config['unmod_info']['study']:# and '601_VOL_T1_SAG' in config['unmod_info']['study']:

        unflp  = np.transpose(unflp, (2, 0, 1))
        unflp1 = np.flip(unflp, (1, 0, 2))

    # Modo (-Y,-Z,-X)
    elif 'FCD032_MR1' in config['unmod_info']['patient'] and '13_t2_space_dark-fluid_sag_cs5.6' in config['unmod_info']['study']:# and '601_VOL_T1_SAG' in config['unmod_info']['study']:

        unflp  = np.transpose(unflp, (2, 0, 1))
        unflp1 = np.flip(unflp, (1, 0, 2))

    # Modo (-Y,-Z,-X)
    elif 'FCD033_MR1' in config['unmod_info']['patient'] and '16_t2_space_dark-fluid_sag_cs5.6' in config['unmod_info']['study']:# and '601_VOL_T1_SAG' in config['unmod_info']['study']:

        unflp  = np.transpose(unflp, (2, 0, 1))
        unflp1 = np.flip(unflp, (1, 0, 2))

    # Modo (-Y,-Z,-X)
    elif 'FCD034_MR1' in config['unmod_info']['patient'] and '7' in config['unmod_info']['study']:# and '601_VOL_T1_SAG' in config['unmod_info']['study']:

        unflp  = np.transpose(unflp, (2, 0, 1))
        unflp1 = np.flip(unflp, (1, 0, 2))

    # Modo (-Y,-Z,-X)
    elif 'FCD037_MR1' in config['unmod_info']['patient'] and '14' in config['unmod_info']['study']:# and '601_VOL_T1_SAG' in config['unmod_info']['study']:

        unflp  = np.transpose(unflp, (2, 0, 1))
        unflp1 = np.flip(unflp, (1, 0, 2))

    # Modo (-Y,-Z,-X)
    elif 'FCD040_MR1' in config['unmod_info']['patient'] and '13' in config['unmod_info']['study']:# and '601_VOL_T1_SAG' in config['unmod_info']['study']:

        unflp  = np.transpose(unflp, (2, 0, 1))
        unflp1 = np.flip(unflp, (1, 0, 2))

    # Modo (-Y,-Z,-X)
    elif 'FCD041_MR1' in config['unmod_info']['patient'] and '4' in config['unmod_info']['study']:# and '601_VOL_T1_SAG' in config['unmod_info']['study']:

        unflp  = np.transpose(unflp, (2, 0, 1))
        unflp1 = np.flip(unflp, (1, 0, 2))

    ################

    # Modo:(-X,-Y,Z)
    elif 'FCD013_MR1' in config['unmod_info']['patient'] and '100' in config['unmod_info']['study']: 

        unflp1 = np.flip(unflp, (0, 1))

    # Modo:(-X,-Y,-Z)
    elif 'FCD012_MR1' in config['unmod_info']['patient'] and '11' in config['unmod_info']['study']: 

        unflp1 = np.flip(unflp, (0, 1))

    # Modo:(-X,-Y,Z)
    elif 'FCD036_MR1' in config['unmod_info']['patient'] and '401_VOL_AX_T1_CRANEO' in config['unmod_info']['study']: 

        unflp1 = np.flip(unflp, (0, 1))

    # Modo:(-X,-Y,Z) # Este estudio primero debe registrarse la T1 respecto de la flair, luego flippear la displasia
    elif 'FCD004_MR1' in config['unmod_info']['patient'] and '601' in config['unmod_info']['study']: 

        #unflp1 = np.flip(unflp, (0, 1))
        unflp  = np.flip(unflp, (0, 1))
        unflp1 = np.flipud(unflp)

    # Modo:(-X,-Y,-Z)
    elif 'FCD006_MR1' in config['unmod_info']['patient'] and '1002' in config['unmod_info']['study']: 

        unflp1 = np.fliplr(unflp)#np.flip(unflp, (0, 1))#
        #unflp1 = np.flipud(unflp)

    # Modo:(-X,-Y,Z) # Este estudio primero debe registrarse la T1 respecto de la flair, luego flippear la displasia
    elif 'FCD007_MR1' in config['unmod_info']['patient'] and '801' in config['unmod_info']['study']: 

        unflp1 = np.flip(unflp, (0, 1))
        #unflp  = np.flip(unflp, (0, 1))
        # unflp1 = np.flipud(unflp)

    # Modo:(-X,-Y,Z) # Este estudio primero debe registrarse la T1 respecto de la flair, luego flippear la displasia
    elif 'FCD021_MR1' in config['unmod_info']['patient'] and '6' in config['unmod_info']['study']: 

        #unflp1 = np.flip(unflp, (0, 1))
        unflp  = np.flip(unflp, (0, 1))
        unflp1 = np.flipud(unflp)

    Path(os.path.join(config['out_dir'])).mkdir(parents=True, exist_ok=True)
    
    try:
        img = nib.Nifti1Image(np.int16(unflp1), unflp_.affine)
    except:
        print(f'No se encontró ninguna imagen')
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


def reg_T1toT2FLAIR(config):

    # Cargar las imagenes
    ref     = image_read(config['ref_mri'], pixeltype='unsigned int')
    reg_img = image_read(config['mod_mri'], pixeltype='unsigned int')

    Path(os.path.join(config['out_dir'])).mkdir(parents=True, exist_ok=True)

    # Registrar imagen
    rs2_img = registration(fixed=ref, 
                           moving=reg_img, 
                           type_of_transform=config['transforms'][6]
    )

    rs = apply_transforms(fixed=ref, 
                          moving=reg_img, 
                          transformlist=rs2_img['fwdtransforms'], 
                          interpolator='linear' #'multiLabel'
    )

    image_write(rs, os.path.join(config['out_dir'], config['mod_mri_fn']), ri=False)

    # Registrar etiqueta
    if config['reg_mask']:

        reg_msk = image_read(config['mod_msk'], pixeltype='unsigned int')

        rs2_msk = registration(fixed=ref, 
                               moving=reg_msk, 
                               type_of_transform=config['transforms'][6]
        )

        rs_ = apply_transforms(fixed=ref, 
                               moving=reg_msk, 
                               transformlist=rs2_msk['fwdtransforms'], 
                               interpolator='nearestNeighbor' #'multiLabel'
        )

        image_write(rs_, os.path.join(config['out_dir'], config['mod_msk_fn']), ri=False)

    return