from argparse import ArgumentParser


def argument_parser_pipeline(version=None):
    def boolean_string(s):
        if s not in {'False', 'True'}:
            raise ValueError('Not a valid boolean string')
        return s == 'True'
    
    parser = ArgumentParser()
    parser.add_argument('-i', '--input_model', 
                        required=False, help='Input model name', default=None)
    parser.add_argument('-t', '--target_rxn', required=False,
                        help='Target reaction ID', type=str, default=None)
    parser.add_argument('-o', '--output_dir', required=False,
                        help='Output directory', type=str, default=None)
    return parser