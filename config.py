import os

def get_parameters(env):

    mode = 'flip' # available modes: 'reg', 'flip', 'plot'

    plot_mode = 'reg' # available modes: 'flipped', 'reflex', 'reg'

    ref_patient  = 'FCD020_MR1'
    ref_study    = '7'
    ref_filename = 'DICOM_t1_mprage_sag_p2_iso_20210902014629_7.nii.gz'

    mod_patient = 'FCD013_MR1'
    mod_study   = '100'
    mod_mri     = 'DICOM_t1_mprage_sag_p2_20220129173507_100'
    mod_msk     = 'DISPLASIA.nii.gz'

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
                           mod_patient,
                           mod_study,
                           mod_mri
    )

    # Ruta de la mascara sin modificar
    mod_msk = os.path.join(root_path,
                           mod_patient,
                           mod_study,
                           mod_msk
    )

    # Ruta de salida

    if mode == 'reg':
        
        out_dir = os.path.join(root_path,
                               'Reg_ds',
                               mod_patient,
                               mod_study,
        )

        mod_mri_fn = 'Reg-' + mod_mri
        mod_msk_fn = 'Reg-' + mod_msk

    elif mode == 'flip':

        out_dir = os.path.join(root_path,
                               mod_patient,
                               mod_study,
        )

        mod_mri_fn = 'Flipped-' + mod_mri
        mod_msk_fn = 'Flipped-' + mod_msk

    return {'mode'      : mode,
            'transforms': transforms, 
            'ref_mri'   : ref_mri, 
            'mod_mri'   : mod_mri, 
            'mod_msk'   : mod_msk, 
            'out_dir'   : out_dir
            'mod_mri_fn': mod_mri_fn,
            'mod_msk_fn': mod_msk_fn

           }