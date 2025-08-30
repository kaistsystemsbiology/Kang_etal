import os
from glob import glob
from copy import deepcopy
import logging

import yaml
import pandas as pd
from tqdm import tqdm
from cobra.io import read_sbml_model

from baebra.utils import argument_parser_pipeline
from baebra.ibridge import predict_ibridge_targets


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()]
                    )

logger = logging.getLogger('runiBridge')


if __name__ == '__main__':
    parser = argument_parser_pipeline()
    options = parser.parse_args()
    
    target_rxn = options.target_rxn
    input_model_dir = options.input_model
    output_dir = options.output_dir

    exclude_met_dir = './baebra/excluded_metabolites.txt'


    if output_dir[-1] == '/':
        output_dir = output_dir[:-1]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    model = read_sbml_model(input_model_dir)
    
    if target_rxn not in [rxn.id for rxn in model.reactions]:
        raise Exception("Target reaction not in the model")
        
        
    df = predict_ibridge_targets(
        model, target_rxn, exclude_met_dir, num_step=10,
    )

    if len(df) == 0:
        print('No target identified')
    else:
        df.to_csv(output_dir + '/result_ibridge.txt', sep='\t')