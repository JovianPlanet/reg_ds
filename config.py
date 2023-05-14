import os

def get_parameters(mode, env):

    #mode = 'reg' # available modes: 'reg', 'flip', 'plot'

    if env == 'lab':

        #root_path = '/media/davidjm/Disco_Compartido/david/datasets/IATM-Dataset/'
        root_path = '/media/davidjm/Disco_Compartido/david/torch-transfer_fcd_seg/data/train/'

    elif env == 'home':

        root_path = '/media/david/Ubuntu-Datos/Maestria/datasets/IATM/DISPLASIAS/'

    transforms = ['Translation', # 0
                  'Rigid',       # 1
                  'Similarity',  # 2
                  'QuickRigid',  # 3
                  'DenseRigid',  # 4
                  'BOLDRigid',   # 5
                  'Affine',      # 6
                  'AffineFast',  # 7
                  'BOLDAffine',  # 8
                  'TRSAA',       # 9
                  'ElasticSyN'   # 10
                 ]

    ref_patient  = 'FCD004_MR1'
    ref_study    = '503'
    ref_filename = 'DICOM_eFL_AX_20191116175403_1002.nii.gz'

    ref_info = {'patient':ref_patient, 'study':ref_study, 'mri':ref_filename}
    

    # Ruta de la imagen de referencia
    ref_mri = os.path.join(root_path,
                           ref_patient, 
                           ref_study, 
                           ref_filename
    )


    if mode == 'reg':

        reg_mask = False

        # En modo 'reg' : Imagen y mascara que se va a registrar respecto a la referencia
        unmod_patient  = 'FCD006_MR1'
        unmod_study    = '503'
        unmod_mri      = 'DICOM_MPR_AX_T1_20191116175403_503.nii.gz'#'Reg-503_MPR_AX_T1_20181102190723_503.nii.gz'#
        unmod_msk      = 'FCD040_roi.nii.gz' # Displasia FCD042_roi DISPLASIA

        # Ruta de la imagen a modificar
        mod_mri = os.path.join(root_path,
                               unmod_patient,
                               unmod_study,
                               unmod_mri
        )

        # Ruta de la mascara sin modificar
        mod_msk = os.path.join(root_path,
                               ref_patient, # unmod_patient
                               ref_study,   # unmod_study
                               unmod_msk
        )
        
        out_dir = os.path.join(root_path,
                               unmod_patient,
                               'Reg',
        )

        mod_mri_fn = 'Reg-' + unmod_mri
        mod_msk_fn = 'Reg-' + unmod_msk

        return {'mode'      : mode,
                'transforms': transforms, 
                'ref_mri'   : ref_mri, 
                'mod_mri'   : mod_mri, 
                'mod_msk'   : mod_msk, 
                'out_dir'   : out_dir,
                'mod_mri_fn': mod_mri_fn,
                'mod_msk_fn': mod_msk_fn,
                'reg_mask'  : reg_mask,
               }

    elif mode == 'flip':

        # En modo 'flip' : Imagen y mascara que se va a orientar respecto a la referencia
        unmod_patient  = 'FCD006_MR1'
        unmod_study    = '1002'
        unmod_msk      = 'DISPLASIA.nii.gz' # DISPLASIA # FCD042_roi

        unmod_info = {'patient':unmod_patient, 'study':unmod_study, 'msk':unmod_msk}

        # Ruta de la mascara sin modificar
        mod_msk = os.path.join(root_path,
                               unmod_patient, 
                               unmod_study,   
                               unmod_msk
        )

        out_dir = os.path.join(root_path,
                               unmod_patient,
                               unmod_study,
        )

        #mod_mri_fn = 'Flipped-' + unmod_mri
        mod_msk_fn = 'Flipped-' + unmod_msk

        return {'mode'      : mode,
                'mod_msk'   : mod_msk, 
                'unmod_info': unmod_info,
                'out_dir'   : out_dir,
                'mod_msk_fn': mod_msk_fn,
               }

    elif mode == 'plot':

        plot_mode = 'single' # available modes: 'flipped', 'reflex', 'reg', 'originals'

        # En modo 'plot' : Imagen y mascara que se va a registrar respecto a la referencia
        unmod_patient  = 'FCD011_MR1'
        unmod_study    = '1002'
        unmod_mri      = 't1.nii.gz'#'Reg-503_MPR_AX_T1_20181102190723_503.nii.gz'#
        unmod_msk      = 'mask.nii.gz' # Displasia # FCD042_roi # Flipped-DISPLASIA

        # Ruta de la imagen a modificar
        mod_mri = os.path.join(root_path,
                               unmod_patient,
                               #unmod_study,
                               unmod_mri
        )

        # Ruta de la mascara sin modificar
        mod_msk = os.path.join(root_path,
                               unmod_patient, # 
                               #unmod_study,   # 
                               unmod_msk
        )

        if plot_mode == 'reg':

            out_dir = os.path.join(root_path,
                                   'Reg_ds',
                                   unmod_patient,
                                   unmod_study,
            )

            mod_mri_fn = 'Reg-' + unmod_mri
            mod_msk_fn = 'Reg-' + unmod_msk

        elif plot_mode == 'flipped':

            out_dir = os.path.join(root_path,
                                   unmod_patient,
                                   unmod_study,
            )

            mod_mri_fn = 'Flipped-' + unmod_mri
            mod_msk_fn = 'Flipped-' + unmod_msk

        elif plot_mode == 'originals':

            out_dir = ''
            mod_mri_fn = ''
            mod_msk_fn = ''

        elif plot_mode == 'single':
            mod_mri_fn = ''
            mod_msk_fn = ''

            out_dir = os.path.join(root_path,
                                   unmod_patient,
                                   #unmod_study,
            )

        return {'mode'      : mode,
                'plot_mode' : plot_mode,
                'ref_mri'   : ref_mri, 
                'mod_mri'   : mod_mri, 
                'mod_msk'   : mod_msk, 
                'out_dir'   : out_dir,
                'mod_mri_fn': mod_mri_fn,
                'mod_msk_fn': mod_msk_fn,
               }