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
    parser.add_argument("--setup", "-s", action="store_true")

    results = parser.parse_args()

    if results.setup:
        afd.organize_stanford_data()
        afd.fetch_templates()
        afd.fetch_hcp_atlas_16_bundles()
        afd.fetch_hcp_atlas_80_bundles()
        return 0

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

    return -1
    # Run AFQ
    myafq = api.AFQ(bids_path=dp,
                    reg_template="mni_T2",
                    reg_subject="b0",
                    dmriprep='vistasoft',
                    viz_backend='plotly_no_gif')


if __name__ == "__main__":
    main()

