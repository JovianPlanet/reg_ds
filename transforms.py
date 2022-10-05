import os
from pathlib import Path
import nibabel as nib
import numpy as np
from ants import image_read, image_write, registration, apply_transforms, reflect_image

def flip(config):

    filename = 'Flipped-DISPLASIA.nii.gz'

    # Cargar las imagenes
    unflp_ = nib.load(config['unflp_mri'])
    unflp = unflp_.get_fdata().squeeze(3)

    if 'FCD020_MR1' in config['unflp_mri']:

        unflp = np.transpose(unflp, (2, 0, 1))
        unflp1 = np.flip(unflp, (1, 0, 2))

    elif 'FCD013_MR1' in config['unflp_mri']:
        unflp1 = np.flip(unflp, (0, 1))

    Path(os.path.join(out_dir)).mkdir(parents=True, exist_ok=True)
    img = nib.Nifti1Image(np.int16(unflp1), unflp_.affine)
    nib.save(img, os.path.join(out_dir, filename))


def registrate(config):

    # Cargar las imagenes
    ref = image_read(config['ref_mri'], pixeltype='unsigned int')
    reg_img = image_read(config['unreg_mri'], pixeltype='unsigned int')
    reg_msk = image_read(config['unreg_msk'], pixeltype='unsigned int')

    for transform in config['transforms'][0]:

        filename_msk = 'Reg-DISPLASIA.nii.gz' #transform+'-DISPLASIA_.nii.gz'
        filename_img = 'Reg-DICOM_t1_mprage_sag_p2_20220129173507_100.nii.gz' #transform+'-DICOM_t1_mprage_sag_p2_20220129173507_100.nii.gz'

        # Registrar imagen
        rs2_img = registration(fixed=ref, 
                               moving=reg_img, 
                               type_of_transform = 'Affine'
        )

        rs = apply_transforms(fixed=ref, 
                               moving=reg_img, 
                               transformlist=rs2_img['fwdtransforms'], 
                               interpolator='linear' #'multiLabel'
        )

        # Registrar etiqueta
        rs2_msk = registration(fixed=ref, 
                               moving=reg_msk, 
                               type_of_transform = 'Affine'
        )

        rs_ = apply_transforms(fixed=ref, 
                               moving=reg_msk, 
                               transformlist=rs2_msk['fwdtransforms'], 
                               interpolator='nearestNeighbor' #'multiLabel'
        )

        Path(os.path.join(config['out_dir'])).mkdir(parents=True, exist_ok=True)
        image_write(rs, os.path.join(config['out_dir'], filename_img), ri=False)
        image_write(rs_, os.path.join(config['out_dir'], filename_msk), ri=False)

'''
kevin - aumentar datos
terraza = transfer
registrar
'''