### Procedure to follow:

1. Run the setup script on a head-node (it involves downlaoding data)

    $ module load singularity
    $
    $ # Obviously, update paths as needed for your system
    $ cd /project/6049200/afq-pytracer/
    $
    $ singularity exec -B ${PWD} -B ${HOME} fuzzyafq.sif python3 gkiar-fuzzafq/code/afq.py --setup


2. Get a resource allocation (or script the rest and submit it to a queue)

    $ # Similarly, change resource request based on your affiliations, the system, etc..
    $ salloc --account rrg-glatard --mem=12000 --time=2:0:0


3. Enter singularity environment

    $ singularity exec -B ${PWD} -B ${HOME} fuzzyafq.sif /bin/bash


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
    $ python3 gkiar-fuzzafq/code/afq.py -p ${dpath} -i ${run_id}


