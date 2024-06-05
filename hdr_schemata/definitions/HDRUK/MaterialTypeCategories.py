from enum import Enum


class MaterialTypeCategories(Enum):
    BLOOD = "Blood"
    DNA = "DNA"
    FAECES = "Faeces"
    IMMORTALIZED_CELL_LINES = "Immortalized Cell Lines"
    ISOLATED_PATHOGEN = "Isolated Pathogen"
    OTHER = "Other"
    PLASMA = "Plasma"
    RNA = "RNA"
    SALIVA = "Saliva"
    SERUM = "Serum"
    TISSUE_FROZEN = "Tissue (Frozen)"
    TISSUE_FFPE = "Tissue (FFPE)"
    URINE = "Urine"

class MaterialTypeCategoriesV2(Enum):
    NOT_AVAILABLE = 'Not available'
    BONE_MARROW = 'Bone marrow'
    CANCER_CELL_LINES = 'Cancer cell lines'
    CDNA_MRNA = 'CDNA/MRNA'
    CORE_BIOPSY = 'Core biopsy'
    DNA = 'DNA'
    ENTIRE_BODY_ORGAN = 'Entire body organ'
    FAECES = 'Faeces'
    IMMORTALIZED_CELL_LINES = 'Immortalized cell lines'
    ISOLATED_PATHOGEN = 'Isolated pathogen'
    MICRORNA = 'MicroRNA'
    PERIPHERAL_BLOOD_CELLS = 'Peripheral blood cells'
    PLASMA = 'Plasma'
    PM_TISSUE = 'PM Tissue'
    PRIMARY_CELLS = 'Primary cells'
    RNA = 'RNA'
    SALIVA = 'Saliva'
    SERUM = 'Serum'
    SWABS = 'Swabs'
    TISSUE = 'Tissue'
    URINE = 'Urine'
    WHOLE_BLOOD = 'Whole blood'
    AVAILABILITY_TO_BE_CONFIRMED = 'Availability to be confirmed'
    OTHER = 'Other'
