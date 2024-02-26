from enum import Enum


class AccessService(Enum):
    TRE_SDE = "TRE/SDE"
    DIRECT_ACCESS = "Direct access"
    OPEN_ACCESS = "Open access"
    VARIED = "Varies based on project"
