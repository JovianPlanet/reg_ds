import os
import numpy as np
import nibabel as nib
from pathlib import Path
from ants import image_read
from utils import plot_fcd, plot_rfx, plot_flipped

mode = 'flipped'

transforms = ['Translation', 
              'Rigid', 
              'Similarity', 
              'QuickRigid', 
              'DenseRigid', 
              'BOLDRigid', 
              'Affine', 
              'AffineFast', 
              'BOLDAffine', 
              'TRSAA', 
              'ElasticSyN'
             ]

if mode == 'reg':

    for transform in transforms:

        print(f'Transform: {transform}\n')

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
        unreg_mri = os.path.join('/media', 
                               'davidjm', 
                               'Disco_Compartido', 
                               'david', 
                               'datasets', 
                               'IATM-Dataset', 
                               'FCD020_MR1', 
                               '7', 
                               'DISPLASIA.nii.gz'
        )

        # Ruta de la imagen registrada
        reg_mri = os.path.join('/media', 
                               'davidjm', 
                               'Disco_Compartido', 
                               'david', 
                               'datasets', 
                               'IATM-Dataset', 
                               'Reg_ds', 
                               '7', 
                               'Reg-DISPLASIA.nii.gz'
        )

        # Cargar las imagenes
        ref = nib.load(ref_mri).get_fdata()#np.int16()
        #ref = image_read(ref_mri)
        unreg = nib.load(unreg_mri).get_fdata().squeeze(3)
        #unreg = image_read(unreg_mri)
        reg = nib.load(reg_mri).get_fdata()
        #reg = image_read(reg_mri)

        filename = transform+'-DISPLASIA_.nii.gz'

        syn_mri = os.path.join('/media', 
                               'davidjm', 
                               'Disco_Compartido', 
                               'david', 
                               'datasets', 
                               'IATM-Dataset', 
                               'Reg_ds', 
                               '7', 
                               filename
        )

        syn = nib.load(syn_mri).get_fdata()

        print(f'{ref.shape}, {unreg.shape}, {reg.shape}\n')

        unreg = np.transpose(unreg, (2, 0, 1))

        for slice_ in range(ref.shape[2]):
            if unreg[:, :, slice_].sum() > 0:

                #print(f'{slice_}')
                #plot_fcd(ref, unreg, reg, syn, slice_)
                pass

            elif reg[:, :, slice_].sum() > 0:

                #print(f'{slice_}')
                plot_fcd(ref, unreg, reg, syn, slice_, 'reg')
                #pass

            elif syn[:, :, slice_].sum() > 0:

                #print(f'{slice_}')
                #plot_fcd(ref, unreg, reg, syn, slice_, transform)
                pass

elif mode == 'reflex':

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
    unrfx_mri = os.path.join('/media', 
                           'davidjm', 
                           'Disco_Compartido', 
                           'david', 
                           'datasets', 
                           'IATM-Dataset', 
                           'FCD020_MR1', 
                           '7', 
                           'DISPLASIA.nii.gz'
    )

    # Ruta de la imagen registrada
    rfx_mri = os.path.join('/media', 
                           'davidjm', 
                           'Disco_Compartido', 
                           'david', 
                           'datasets', 
                           'IATM-Dataset', 
                           'Reg_ds', 
                           '7', 
                           'Reflex-DISPLASIA.nii.gz'
    )

    # Cargar las imagenes
    ref_ = nib.load(ref_mri)
    ref = ref_.get_fdata()
    unrfx = nib.load(unrfx_mri).get_fdata().squeeze(3)
    rfx = nib.load(rfx_mri).get_fdata()

    print(f'{ref.dtype}, {unrfx.dtype}, {rfx.dtype}\n')
    print(f'{ref.shape}, {unrfx.shape}, {rfx.shape}\n')

    unrfx = np.transpose(unrfx, (2, 0, 1))
    rfx = np.transpose(rfx, (2, 0, 1))

    print(f'{ref.shape}, {unrfx.shape}, {rfx.shape}\n')

    for slice_ in range(ref.shape[2]):

        if unrfx[:, :, slice_].sum() > 0:

            #print(f'{slice_}')
            plot_rfx(ref, unrfx, rfx, slice_, 'unrfx')
            #pass

        # if rfx[:, :, slice_].sum() > 0:

        #     #print(f'{slice_}')
        #     plot_rfx(ref, unrfx, rfx, slice_, 'rfx')
        #     plot_rfx(ref, rfx, rfx1, slice_, 'rfx')
        #     plot_rfx(ref, rfx, rfx2, slice_, 'rfx')
        #     plot_rfx(ref, rfx, rfx3, slice_, 'rfx')
            #pass

elif mode == 'flipped':

    # Ruta de la imagen de referencia
    ref_mri = os.path.join('/media', 
                           'davidjm', 
                           'Disco_Compartido', 
                           'david', 
                           'datasets', 
                           'IATM-Dataset', 
                           'Reg_ds', 
                           'FCD013_MR1', 
                           '100', 
                           'Reg-DICOM_t1_mprage_sag_p2_20220129173507_100.nii.gz'
    )

    # Ruta de la imagen registrada
    flip_mri = os.path.join('/media', 
                           'davidjm', 
                           'Disco_Compartido', 
                           'david', 
                           'datasets', 
                           'IATM-Dataset', 
                           'Reg_ds', 
                           'FCD013_MR1',
                           '100', 
                           'Reg-DISPLASIA.nii.gz'
    )

    # Cargar las imagenes
    ref_ = nib.load(ref_mri)
    ref = ref_.get_fdata()
    flip = np.flip(nib.load(flip_mri).get_fdata(), 2) #np.flip(nib.load(flip_mri).get_fdata().squeeze(3), (0, 1))

    print(f'{ref.shape}, {flip.shape}')

    for slice_ in range(ref.shape[2]):

        if flip[:, :, slice_].sum() > 0:

            plot_flipped(ref, flip, slice_, str(slice_))