import os
from pathlib import Path
import nibabel as nib
import numpy as np
#from ants import image_read, image_write, reflect_image, reorient_image

# Ruta de la imagen de referencia
ref_mri = os.path.join('/media', 
                       'davidjm', 
                       'Disco_Compartido', 
                       'david', 
                       'datasets', 
                       'IATM-Dataset', 
                       'FCD020_MR1', 
                       '7', 
                       'DICOM_t1_mprage_sag_p2_iso_20210902014629_7.nii.gz'
)

# Ruta de la imagen sin registrar
unflp_mri = os.path.join('/media', 
                       'davidjm', 
                       'Disco_Compartido', 
                       'david', 
                       'datasets', 
                       'IATM-Dataset', 
                       'FCD013_MR1', 
                       '100', 
                       'DISPLASIA.nii.gz'
)

# Ruta de la imagen flipeada
out_dir = os.path.join('/media', 
                       'davidjm', 
                       'Disco_Compartido', 
                       'david', 
                       'datasets', 
                       'IATM-Dataset', 
                       #'Reg_ds', 
                       'FCD013_MR1',
                       '100', 
)

filename = 'Flipped-DISPLASIA.nii.gz'

# Cargar las imagenes
ref_ = nib.load(ref_mri)
ref = ref_.get_fdata()
unflp_ = nib.load(unflp_mri)
unflp = unflp_.get_fdata().squeeze(3)

if 'FCD020_MR1' in unflp_mri:

    unflp = np.transpose(unflp, (2, 0, 1))
    unflp1 = np.flip(unflp, (1, 0, 2))

elif 'FCD013_MR1' in unflp_mri:
    unflp1 = np.flip(unflp, (0, 1))

Path(os.path.join(out_dir)).mkdir(parents=True, exist_ok=True)
img = nib.Nifti1Image(np.int16(unflp1), unflp_.affine)
nib.save(img, os.path.join(out_dir, filename))

'''
kevin - aumentar datos
terraza = transfer
registrar
'''