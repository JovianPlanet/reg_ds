import os

def get_parameters(env):

    mode = 'flip' # available modes: 'reg', 'flip', 'plot'

    plot_mode = 'reg' # available modes: 'flipped', 'reflex', 'reg'

    ref_patient  = 'FCD004_MR1'
    ref_study    = '503'
    ref_filename = '503_MPR_AX_T1_20181102190723_503.nii.gz'

    # En modo 'reg' : Imagen y mascara que se va a registrar respecto a la referencia
    # En modo 'flip': Imagen respecto a la cual se va a orientar la mascara
    unmod_patient  = 'FCD012_MR1'
    unmod_study    = '11'
    unmod_mri      = 'DICOM_t1_mprage_sag_p2_iso_20220105171437_11.nii.gz'
    unmod_msk      = 'Displasia.nii.gz'

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

    if env == 'lab':

        root_path = '/media/davidjm/Disco_Compartido/david/datasets/IATM-Dataset/'

    elif env == 'home':

        root_path = '/media/david/Ubuntu-Datos/Maestria/datasets/IATM/DISPLASIAS/'

    # Ruta de la imagen de referencia
    ref_mri = os.path.join(root_path,
                           ref_patient, 
                           ref_study, 
                           ref_filename
    )

    # Ruta de la imagen a modificar
    mod_mri = os.path.join(root_path,
                           unmod_patient,
                           unmod_study,
                           unmod_mri
    )

    # Ruta de la mascara sin modificar
    mod_msk = os.path.join(root_path,
                           unmod_patient,
                           unmod_study,
                           unmod_msk
    )

    # Ruta de salida
    if mode == 'reg':
        
        out_dir = os.path.join(root_path,
                               'Reg_ds',
                               unmod_patient,
                               unmod_study,
        )

        mod_mri_fn = 'Reg-' + unmod_mri
        mod_msk_fn = 'Reg-' + unmod_msk

    elif mode == 'flip':

        out_dir = os.path.join(root_path,
                               unmod_patient,
                               unmod_study,
        )

        mod_mri_fn = 'Flipped-' + unmod_mri
        mod_msk_fn = 'Flipped-' + unmod_msk

    elif mode == 'plot':

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


    return {'mode'      : mode,
            'plot_mode' : plot_mode,
            'transforms': transforms, 
            'ref_mri'   : ref_mri, 
            'mod_mri'   : mod_mri, 
            'mod_msk'   : mod_msk, 
            'out_dir'   : out_dir,
            'mod_mri_fn': mod_mri_fn,
            'mod_msk_fn': mod_msk_fn,
           }