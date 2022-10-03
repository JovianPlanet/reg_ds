import os
from pathlib import Path
from ants import image_read, image_write, registration, apply_transforms, reflect_image

transforms = ['Translation', 
              # 'Rigid', 
              # 'Similarity', 
              # 'QuickRigid', 
              # 'DenseRigid', 
              # 'BOLDRigid', 
              # 'Affine', 
              # 'AffineFast', 
              # 'BOLDAffine', 
              # 'TRSAA', 
              # 'ElasticSyN'
             ]

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

unreg_mri = os.path.join('/media', 
                       'davidjm', 
                       'Disco_Compartido', 
                       'david', 
                       'datasets', 
                       'IATM-Dataset', 
                       'FCD013_MR1', 
                       '100', 
                       'DICOM_t1_mprage_sag_p2_20220129173507_100.nii.gz'
)

# Ruta de la mascara sin registrar
unreg_msk = os.path.join('/media', 
                       'davidjm', 
                       'Disco_Compartido', 
                       'david', 
                       'datasets', 
                       'IATM-Dataset', 
                       'FCD013_MR1', 
                       '100', 
                       'DISPLASIA.nii.gz'
)

# Ruta de la imagen registrada
out_dir = os.path.join('/media', 
                       'davidjm', 
                       'Disco_Compartido', 
                       'david', 
                       'datasets', 
                       'IATM-Dataset', 
                       'Reg_ds',
                       'FCD013_MR1', 
                       '100',  
)

# Cargar las imagenes
ref = image_read(ref_mri, pixeltype='unsigned int')
reg_img = image_read(unreg_mri, pixeltype='unsigned int')
reg_msk = image_read(unreg_msk, pixeltype='unsigned int')

for transform in transforms:

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

    Path(os.path.join(out_dir)).mkdir(parents=True, exist_ok=True)
    image_write(rs, os.path.join(out_dir, filename_img), ri=False)
    image_write(rs_, os.path.join(out_dir, filename_msk), ri=False)
