import os

def get_parameters(env):

    mode = 'reg'

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

        # Ruta de la imagen de referencia
        ref_mri = os.path.join(root_path, 
                               'FCD020_MR1', 
                               '7', 
                               'DICOM_t1_mprage_sag_p2_iso_20210902014629_7.nii.gz'
        )

        unreg_mri = os.path.join(root_path, 
                               'FCD013_MR1', 
                               '100', 
                               'DICOM_t1_mprage_sag_p2_20220129173507_100.nii.gz'
        )

        # Ruta de la mascara sin registrar
        unreg_msk = os.path.join(root_path, 
                               'FCD013_MR1', 
                               '100', 
                               'DISPLASIA.nii.gz'
        )

        # Ruta de la imagen sin orientar
        unflp_mri = os.path.join(root_path, 
                               'FCD013_MR1', 
                               '100', 
                               'DISPLASIA.nii.gz'
        )

        # Ruta de salida
        out_dir = os.path.join(root_path, 
                               'Reg_ds',
                               'FCD013_MR1', 
                               '100',  
        )

    if env == 'home':

        root_path = '/media/david/Ubuntu-Datos/Maestria/datasets/IATM/DISPLASIAS/'
        
        # Ruta de la imagen de referencia
        ref_mri = os.path.join(root_path,
                               'FCD020_MR1', 
                               '7', 
                               'DICOM_t1_mprage_sag_p2_iso_20210902014629_7.nii.gz'
        )

        unreg_mri = os.path.join(root_path,
                               'FCD013_MR1', 
                               '100', 
                               'DICOM_t1_mprage_sag_p2_20220129173507_100.nii.gz'
        )

        # Ruta de la mascara sin registrar
        unreg_msk = os.path.join(root_path,
                               'FCD013_MR1', 
                               '100', 
                               'DISPLASIA.nii.gz'
        )

        # Ruta de la imagen sin orientar
        unflp_mri = os.path.join(root_path, 
                               'FCD013_MR1', 
                               '100', 
                               'DISPLASIA.nii.gz'
        )

        # Ruta de salida
        out_dir = os.path.join(root_path,
                               'Reg_ds',
                               'FCD013_MR1', 
                               '100',  
        )

    return {'mode':       mode,
            'transforms': transforms, 
            'ref_mri':    ref_mri, 
            'unreg_mri':  unreg_mri, 
            'unreg_msk':  unreg_msk, 
            'unflp_mri':  unflp_mri,
            'out_dir':    out_dir
           }