# Integration of the ADASTRA database as a novel annotator module in the OpenCRAVAT pipeline

The ADASTRA database contains information about allele-specific transcription factor binding events. A Transcription Factor (TF) might prefer to bind one of two alternative alleles of homologous chromosomes and thus exhibit allele-specific binding (ASB). ASB highlights regulatory SNPs with high potential to affect gene expression.

## Integration of a novel ADASTRA annotator module in the OpenCRAVAT pipeline

![image](https://user-images.githubusercontent.com/70381751/169640530-d6e9a033-d517-4a49-bddf-1f6b4cbbefb5.png)

## Installation

Creating a new OpenCRAVAT directory called ./oc_test/ 

You can save this or choose any other name.

` ` `
mkdir oc_test
` ` `

Moving to a directory ./oc_test/

` ` `
cd oc_test/
` ` `

Creating a new virtual environment located at ./new_oc_env/

` ` `
python3 -m venv ./new_oc_env/
` ` `

Activating a new virtual environment

` ` `
source ./new_oc_env/bin/activate
` ` `

Installation of the OpenCRAVAT

` ` `
pip3 install open-cravat
` ` `

Installation of base OpenCRAVAT modules

` ` `
oc module install-base
` ` `

This command can help you find out exactly where OpenCRAVAT was installed

` ` `
which oc
` ` `

Cloning the OpenCravat-Adastra github repository

` ` `
git clone https://github.com/gottalottarock/OpenCravat-Adastra.git
` ` `

This command can help you find out exactly where python3 was installed and its version which you have to indicate in paths to modules below

` ` `
which python3
` ` `

Further commands are given for python3.9, if you are using a different version, then change it in the paths to the OpenCRAVAT modules below

OR

You can find the path to OpenCRAVAT modules with this command

` ` `
oc config md
` ` `

Integration of the ADASTRA module as a novel annotator module in the OpenCRAVAT

` ` `
cp -r ./OpenCravat-Adastra/adastra/ ./new_oc_env/lib/python3.9/site-packages/cravat/modules/annotators/
` ` `

Creating a new ADASTRA annotator module directory /data/

` ` `
mkdir ./new_oc_env/lib/python3.9/site-packages/cravat/modules/annotators/adastra/data/
` ` `

Integration of the ADASTRA module database as a novel database in the OpenCRAVAT

` ` `
cp ~/adastra_tf.sqlite ./new_oc_env/lib/python3.9/site-packages/cravat/modules/annotators/adastra/data/
` ` `

Changing the access permissions of an ADASTRA module database

` ` `
chmod 777 ./new_oc_env/lib/python3.9/site-packages/cravat/modules/annotators/adastra/data/adastra_tf.sqlite
` ` `

Integration of the ADASTRA module widget as a novel widget module in the OpenCRAVAT

` ` `
cp -r ./OpenCravat-Adastra/wgadastra/ ./new_oc_env/lib/python3.9/site-packages/cravat/modules/webviewerwidgets/
` ` `

## Usage

Run OpenCRAVAT pipeline with a novel ADASTRA annotator module

` ` `
oc run example_input_new.vcf -a adastra -l hg38
` ` `

Open the results from OpenCRAVAT pipeline with a novel ADASTRA annotator module in browser

` ` `
oc gui example_input_new.vcf.sqlite
` ` `

## Results

### Results of an annotation via a novel ADASTRA annotator module

![table_1](https://user-images.githubusercontent.com/70381751/169640611-248f4004-fa2b-4c57-b4e0-1ae3900717e5.png)

![table_2](https://user-images.githubusercontent.com/70381751/169640638-090e8738-8282-41ac-a330-7e4ce825db38.png)

### Background Allelic Dosage

Background Allelic Dosage (BAD) is the expected ratio of major to minor allelic frequencies in a particular genomic region. For example, if a copy number of two alternating alleles is the same (e.g. 1:1 (diploid), 2:2, or 3:3), then the respective region has BAD=1, i.e. the expected ratio of reads mapped to alternative alleles on heterozygous SNVs is 1. All triploid regions have BAD=2 and the expected allelic read ratio is either 2 or ½. In general, if BAD of a particular region is known, then the expected frequencies of allelic reads are 1/(BAD +1) and BAD/(BAD + 1).
ASB significance (FDR)

### ASB effect size

The Effect Size of an ASB event is calculated separately for Reference and Alternative alleles and is defined as the weighted mean of log-ratios of observed and expected allelic read counts, with weights being -log10 of the respective P-values.

### Motif Concordance

Motif Concordance indicates whether the allelic read imbalance is consistent with the transcription factor motif Fold Change (FC, predicted from sequence analysis). The following notation is used:

*  n/a: Motif is not available;
*  No hit: The best hit P-value is higher than 0.0005 threshold;
*  Weak concordant: The absolute value of FC is less than 2 but consistent with the allelic read imbalance;
*  Weak discordant: The absolute value of FC is less than 2 and not consistent with the allelic read imbalance;
*  Concordant: The absolute value of FC is greater or equal to 2 and consistent with allelic read imbalance;
*  Discordant: The absolute value of FC is greater or equal to 2 but not consistent with allelic read imbalance.

For more information please visit: [Link](https://adastra.autosome.org/zanthar/help)
