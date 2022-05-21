The ADASTRA database contains information about allele-specific transcription factor binding events. A Transcription Factor (TF) might prefer to bind one of two alternative alleles of homologous chromosomes and thus exhibit allele-specific binding (ASB). ASB highlights regulatory SNPs with high potential to affect gene expression. 
Background Allelic Dosage
Background Allelic Dosage (BAD) is the expected ratio of major to minor allelic frequencies in a particular genomic region. For example, if a copy number of two alternating alleles is the same (e.g. 1:1 (diploid), 2:2, or 3:3), then the respective region has BAD=1, i.e. the expected ratio of reads mapped to alternative alleles on heterozygous SNVs is 1. All triploid regions have BAD=2 and the expected allelic read ratio is either 2 or ½. In general, if BAD of a particular region is known, then the expected frequencies of allelic reads are 1/(BAD +1) and BAD/(BAD + 1).
ASB significance (FDR)

ASB effect size
The Effect Size of an ASB event is calculated separately for Reference and Alternative alleles and is defined as the weighted mean of log-ratios of observed and expected allelic read counts, with weights being -log10 of the respective P-values.
Motif Concordance
Motif Concordance indicates whether the allelic read imbalance is consistent with the transcription factor motif Fold Change (FC, predicted from sequence analysis). The following notation is used:
o  n/a: Motif is not available;
o  No hit: The best hit P-value is higher than 0.0005 threshold;
o  Weak concordant: The absolute value of FC is less than 2 but consistent with the allelic read imbalance;
o  Weak discordant: The absolute value of FC is less than 2 and not consistent with the allelic read imbalance;
o  Concordant: The absolute value of FC is greater or equal to 2 and consistent with allelic read imbalance;
o  Discordant: The absolute value of FC is greater or equal to 2 but not consistent with allelic read imbalance.
For more information please visit: https://adastra.autosome.org/zanthar/help
