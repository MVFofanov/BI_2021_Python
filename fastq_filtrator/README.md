# Description:
## Usage
### This program can help you to filter your raw .fastq data obtained from Illumina sequencing.
### The following parameters are subject to change:
Feature | Default | Input format
------------ | ------------- | -------------
Input .fastq file name | | my_reads.fastq
Output .fastq file prefix | | my_result
GC content (%) | 0, 100 | 40, 60
Read length (bp) | 0, 2 ^ 32 | 100, 150
Read quality | 0 | 30

You can save reads failed after filtering by typing 'yes' or 'y' when you will be asked about it.

Type one number as upper boundary instead using interval for GC content and Read length.

Skip the output .fastq file prefix step and use input fastq name as output prefix.

Skip all steps except Input .fastq file name to use default settings.

### After filtering you can get:
Output file | Description
------------ | -------------
no output file | every single read was saved and nothing was filtered
passed.fastq | contains all reads saved after filtering
failed.fastq | contains all reads discarded after filtering

### WARNING!
Make sure available RAM have at least three times the size of the .fastq file before RUN,
This program is sensitive to it, dont use it to analyse whole human genome raw sequencing data.
This script was tested on the .fastq data which took up about 100 Mb disk space.
After RUN, this program demanded usage up to 300 Mb RAM and time up to 10 seconds
