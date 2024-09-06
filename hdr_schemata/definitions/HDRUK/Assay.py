from enum import Enum

class Assay(Enum):
    NMR_SPECTROSCOPY = 'NMR spectroscopy'
    MASS_SPECTROMETRY = 'mass-spectrometry'
    WHOLE_GENOME_SEQUENCING = 'whole genome sequencing'
    EXOME_SEQUENCING = 'exome sequencing'
    GENOTYPING_BY_ARRAY = 'genotyping by array'
    TRANSCRIPTOME_PROFILING_BY_HIGH_THROUGHPUT_SEQUENCING = 'transcriptome profiling by high-throughput sequencing'
    TRANSCRIPTOME_PROFILING_BY_ARRAY = 'transcriptome profiling by array'
    AMPLICON_SEQUENCING = 'amplicon sequencing'
    METHYLATION_BINDING_DOMAIN_SEQUENCING = 'methylation binding domain sequencing'
    METHYLATION_PROFILING_BY_HIGH_THROUGHPUT_SEQUENCING = 'methylation profiling by high-throughput sequencing'
    GENOMIC_VARIANT_CALLING = 'genomic variant calling'
    CHROMATIN_ACCESSIBILITY_PROFILING_BY_HIGH_THROUGHPUT_SEQUENCING = 'chromatin accessibility profiling by high-throughput sequencing'
    HISTONE_MODIFICATION_PROFILING_BY_HIGH_THROUGHPUT_SEQUENCING = 'histone modification profiling by high-throughput sequencing'
    CHROMATIN_IMMUNOPRECIPITATION_SEQUENCING = 'chromatin immunoprecipitation sequencing'
    WHOLE_GENOME_SHOTGUN_SEQUENCING = 'whole genome shotgun sequencing'
    WHOLE_TRANSCRIPTOME_SEQUENCING = 'whole transcriptome sequencing'
    TARGETED_MUTATION_ANALYSIS = 'targeted mutation analysis'

