# Kang_etal

#Kang_etal #In this study, the in silico simulation tool iBridge was upgraded to systematically predict effective gene manipulation targets for enhancing metabolic flux toward two target molecules. This framework was employed to increase the production of novel aromatic PHA


##Example

1. Clone the repository

        git clone https://github.com/kaistsystemsbiology/Kang_etal.git

2. Change the directory

        cd Kang_etal

3. Create and activate virtual environment

        conda env create -f environment.yml
        conda activate baebra

4. Run iBrdige

        python run_ibrdige.py -i {input GEM directory} -o {output directory} -t {target reaction ID}
