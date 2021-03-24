### Procedure to follow:

1. Run the setup script on a head-node (it involves downlaoding data)

    $ module load python
    $ python gkiar-fuzzafq/code/afq.py --setup


2. Get a resource allocation (or script the rest and submit it to a queue)

    $ salloc --account rrg-glatard --mem-per-cpu=6000 --cpus-per-task=1 --time=2:0:0


3. Enter singularity environment

    $ singularity exec -B /project/6049200/afq-pytracer/ fuzzyafq.sif /bin/bash


4. Configure the MCA backend as you wish

    $ export VFC_BACKENDS="libinterflop_ieee.so"  # OR
    $ export VFC_BACKENDS="libinterflop_mca.so -m rr"


5. Run the script with unique params to avoid overwriting results

    $ # In the case of IEEE backend use 'ref', or just a numeric ID for MCA
    $ run_id="ref"
    $
    $ # This will hold symlinks to the original dataset and the pipeline outputs
    $ dpath="/project/6049200/afq-pytracer/data/"
    $
    $ python3 /project/6049200/afq-pytracer/gkiar-fuzzyafq/code/afq.py -p ${dpath} -i ${run_id}


