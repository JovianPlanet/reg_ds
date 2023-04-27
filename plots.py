import os
import numpy as np
import nibabel as nib
from ants import image_read
from utils import plot_fcd, plot_rfx, plot_flipped, plot_unreg, plot_reg


def plots(config):

    if config['plot_mode'] == 'reg':

        # Cargar las imagenes
        ref       = nib.load(config['ref_mri']).get_fdata()#np.int16()
        unreg     = nib.load(config['mod_mri']).get_fdata()#.squeeze(3)
        unreg_msk = nib.load(config['mod_msk']).get_fdata()
        reg       = nib.load(os.path.join(config['out_dir'], config['mod_mri_fn'])).get_fdata()
        reg_msk   = nib.load(os.path.join(config['out_dir'], config['mod_msk_fn'])).get_fdata()

        print(f'ref = {ref.shape}, unreg = {unreg.shape}, reg = {reg.shape}\n')

        #unreg = np.transpose(unreg, (2, 0, 1))

        for slice_ in range(unreg_msk.shape[2]):

            if unreg_msk[:, :, slice_].sum() > 0:

                print(f'{slice_}')
                plot_unreg(unreg, unreg_msk, slice_)

        for slice_ in range(reg_msk.shape[2]):

            if reg_msk[:, :, slice_].sum() >= 0:

                print(f'{slice_}')
                plot_reg(reg, reg_msk, slice_)

            # elif reg_msk[:, :, slice_].sum() > 0:

            #     print(f'{slice_}')
            #     plot_fcd(ref, unreg, reg, reg_msk, slice_, 'reg')

    elif config['plot_mode'] == 'reflex':

        # Cargar las imagenes
        ref_ = nib.load(config['mod_mri'])
        ref  = ref_.get_fdata()

        unrfx = nib.load(config['mod_msk']).get_fdata().squeeze(3)
        rfx   = nib.load(os.path.join(config['out_dir'], config['mod_msk_fn'])).get_fdata()

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

    elif config['plot_mode'] == 'flipped':

        # Cargar las imagenes
        ref_ = nib.load(config['mod_mri'])
        ref = ref_.get_fdata()
        flip = np.flip(nib.load(flip_mri).get_fdata(), 2) #np.flip(nib.load(flip_mri).get_fdata().squeeze(3), (0, 1))

        print(f'{ref.shape}, {flip.shape}')

        for slice_ in range(ref.shape[2]):

            if flip[:, :, slice_].sum() > 0:

                plot_flipped(ref, flip, slice_, str(slice_))


    elif config['plot_mode'] == 'originals':

        # Cargar las imagenes
        mri = nib.load(config['mri'])
        mri = mri.get_fdata()
        msk = nib.load(config['msk'])
        msk = msk.get_fdata()
        
        for s in range(mri.shape[2]):
            if np.any(msk[:,:,s]):
                plot_unreg(mri, msk, s, offset=False)