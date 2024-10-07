from enum import Enum

class Assay(Enum):
    NMR_SPECTROSCOPY = 'NMR spectroscopy'
    MASS_SPECTROMETRY = 'Mass-spectrometry'
    WHOLE_GENOME_SEQUENCING = 'Whole genome sequencing'
    EXOME_SEQUENCING = 'Exome sequencing'
    GENOTYPING_BY_ARRAY = 'Genotyping by array'
    TRANSCRIPTOME_PROFILING_BY_HIGH_THROUGHPUT_SEQUENCING = 'Transcriptome profiling by high-throughput sequencing'
    TRANSCRIPTOME_PROFILING_BY_ARRAY = 'Transcriptome profiling by array'
    AMPLICON_SEQUENCING = 'Amplicon sequencing'
    METHYLATION_BINDING_DOMAIN_SEQUENCING = 'Methylation binding domain sequencing'
    METHYLATION_PROFILING_BY_HIGH_THROUGHPUT_SEQUENCING = 'Methylation profiling by high-throughput sequencing'
    GENOMIC_VARIANT_CALLING = 'Genomic variant calling'
    CHROMATIN_ACCESSIBILITY_PROFILING_BY_HIGH_THROUGHPUT_SEQUENCING = 'Chromatin accessibility profiling by high-throughput sequencing'
    HISTONE_MODIFICATION_PROFILING_BY_HIGH_THROUGHPUT_SEQUENCING = 'Histone modification profiling by high-throughput sequencing'
    CHROMATIN_IMMUNOPRECIPITATION_SEQUENCING = 'Chromatin immunoprecipitation sequencing'
    WHOLE_GENOME_SHOTGUN_SEQUENCING = 'Whole genome shotgun sequencing'
    WHOLE_TRANSCRIPTOME_SEQUENCING = 'Whole transcriptome sequencing'
    TARGETED_MUTATION_ANALYSIS = 'Targeted mutation analysis'

