"""
==========================
AFQ API
==========================

An example using the AFQ API


"""
import os.path as op
import os

from argparse import ArgumentParser
import matplotlib.pyplot as plt
import nibabel as nib
import plotly

from AFQ import api
import AFQ.data as afd



def main():
    parser = ArgumentParser()
    parser.add_argument("--run-id", "-i", default=None)
    parser.add_argument("--data-path", "-p", default=None)
    parser.add_argument("--dataset", "-d", default="stanford_hardi")
    results = parser.parse_args()

    orig_dp = op.join(afd.afq_home, results.dataset)
    bp = results.data_path if results.data_path else afd.afq_home

    dp = op.join(bp, results.dataset)
    if results.run_id:
        dp = op.join(dp, results.run_id)

    if dp != orig_dp:
        try:
            # Create the data directory
            os.makedirs(op.join(dp, 'derivatives'))

            # Make a symbolic link to the original
            os.symlink(op.join(orig_dp, 'derivatives', 'freesurfer'),
                       op.join(dp, 'derivatives', 'freesurfer'))
            os.symlink(op.join(orig_dp, 'derivatives', 'vistasoft'),
                       op.join(dp, 'derivatives', 'vistasoft'))
        except FileExistsError:
            pass

    #   ``AFQ_data/stanford_hardi/``
    # afd.organize_stanford_data(clear_previous_afq=True)

    return -1
    # Run AFQ
    myafq = api.AFQ(bids_path=dp,
                    reg_template="mni_T2",
                    reg_subject="b0",
                    dmriprep='vistasoft',
                    viz_backend='plotly_no_gif')

    # FA_fname = myafq.dti_fa[0]
    # FA_img = nib.load(FA_fname)
    # FA = FA_img.get_fdata()
    # fig, ax = plt.subplots(1)
    # ax.matshow(FA[:, :, FA.shape[-1] // 2], cmap='viridis')
    # ax.axis("off")


if __name__ == "__main__":
    main()

